# =============================================================================
# toss_app/services/crawler.py
# 역할: 토스증권 커뮤니티 댓글 자동 수집 (F103, F104)
# 원리: Selenium WebDriver로 실제 브라우저를 제어한다.
#       webdriver-manager가 ChromeDriver를 자동 설치·버전 매칭해 주므로
#       별도 드라이버 설치가 불필요하다.
#       명시적 대기(WebDriverWait + expected_conditions)를 사용하여
#       동적 SPA 렌더링이 완료된 후 요소를 안전하게 선택한다.
# =============================================================================

import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger(__name__)

# 토스증권 URL
TOSS_BASE_URL = "https://tossinvest.com"
TOSS_SEARCH_URL = f"{TOSS_BASE_URL}/search"

# 대기 타임아웃 (초)
WAIT_TIMEOUT = 15
# 수집 목표 댓글 수
TARGET_COMMENT_COUNT = 20


class TossCrawler:
    """
    토스증권 커뮤니티 댓글 크롤러.
    사용 방법:
        crawler = TossCrawler()
        stock_name, comments = crawler.crawl("삼성전자")
    """

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.driver = None

    # ------------------------------------------------------------------
    # 공개 API
    # ------------------------------------------------------------------

    def crawl(self, company_name: str) -> tuple[str, list[str]]:
        """
        company_name으로 토스증권을 검색하고 커뮤니티 댓글을 반환한다.

        Returns:
            (실제 종목명, 원본 댓글 리스트)

        Raises:
            ValueError: 검색 결과 없음 / 커뮤니티 탭 없음 등
        """
        try:
            self._init_driver()
            stock_name = self._search_and_navigate(company_name)
            comments = self._collect_comments()
            return stock_name, comments
        finally:
            self._quit_driver()

    # ------------------------------------------------------------------
    # 내부 메서드: 드라이버 초기화/종료
    # ------------------------------------------------------------------

    def _init_driver(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280,900")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(5)

    def _quit_driver(self):
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
            self.driver = None

    # ------------------------------------------------------------------
    # 내부 메서드: 검색 및 종목 페이지 이동 (F103)
    # ------------------------------------------------------------------

    def _search_and_navigate(self, company_name: str) -> str:
        """
        검색창에 company_name 입력 → 최상단 결과 클릭 → 종목명 반환.
        """
        wait = WebDriverWait(self.driver, WAIT_TIMEOUT)

        # 1) 검색 페이지 열기
        self.driver.get(TOSS_SEARCH_URL)
        logger.info("Opened search page: %s", TOSS_SEARCH_URL)

        # 2) 검색 input 찾아서 입력
        try:
            search_input = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[type='search'], input[placeholder*='검색']")
                )
            )
        except TimeoutException:
            raise ValueError("토스증권 검색창을 찾을 수 없습니다.")

        search_input.clear()
        search_input.send_keys(company_name)
        time.sleep(1)  # 자동완성 목록 렌더링 대기
        search_input.send_keys(Keys.RETURN)
        logger.info("Searched for: %s", company_name)

        # 3) 검색 결과 목록 대기 및 최상단 결과 클릭
        try:
            first_result = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-testid='search-result-item']:first-child, "
                                      ".search-result-item:first-child, "
                                      "li.stock-item:first-child, "
                                      "a[href*='/stock/']:first-of-type")
                )
            )
            stock_name = first_result.text.strip().split("\n")[0] or company_name
            first_result.click()
            logger.info("Clicked first result: %s", stock_name)
        except TimeoutException:
            raise ValueError(
                f"'{company_name}'에 대한 검색 결과가 없습니다. "
                "종목명을 정확히 입력해 주세요."
            )
        except ElementClickInterceptedException:
            # JS 클릭으로 재시도
            self.driver.execute_script("arguments[0].click();", first_result)

        time.sleep(2)  # 종목 상세 페이지 로딩 대기

        # 실제 종목명 재확인 (페이지 h1 or title)
        try:
            stock_name_el = self.driver.find_element(
                By.CSS_SELECTOR, "h1, [data-testid='stock-name'], .stock-name"
            )
            stock_name = stock_name_el.text.strip().split("\n")[0] or company_name
        except NoSuchElementException:
            stock_name = company_name

        return stock_name

    # ------------------------------------------------------------------
    # 내부 메서드: 커뮤니티 탭 이동 및 댓글 수집 (F104)
    # ------------------------------------------------------------------

    def _collect_comments(self) -> list[str]:
        """
        현재 종목 페이지에서 '커뮤니티' 탭으로 이동 후 댓글 텍스트를 수집한다.
        """
        wait = WebDriverWait(self.driver, WAIT_TIMEOUT)

        # 1) 커뮤니티 탭 클릭
        try:
            community_tab = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(),'커뮤니티')] | "
                               "//a[contains(text(),'커뮤니티')] | "
                               "//*[@role='tab' and contains(text(),'커뮤니티')]")
                )
            )
            community_tab.click()
            logger.info("Clicked 커뮤니티 tab")
        except TimeoutException:
            raise ValueError("커뮤니티 탭을 찾을 수 없습니다. 해당 종목이 지원되지 않을 수 있습니다.")

        time.sleep(2)

        # 2) 댓글 컨테이너 대기
        try:
            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     "[data-testid='community-post'], .community-post, "
                     ".comment-item, article, [class*='Post'], [class*='Comment']")
                )
            )
        except TimeoutException:
            logger.warning("댓글 컨테이너 대기 시간 초과 – 빈 목록 반환")
            return []

        # 3) 스크롤로 댓글 추가 로드
        comments = []
        scroll_attempts = 0
        max_scroll = 8

        while len(comments) < TARGET_COMMENT_COUNT and scroll_attempts < max_scroll:
            # 현재 화면의 댓글 요소 수집
            elements = self.driver.find_elements(
                By.CSS_SELECTOR,
                "[data-testid='community-post'] p, "
                ".community-post p, "
                ".comment-body, "
                "[class*='PostContent'], "
                "[class*='commentText'], "
                "article p",
            )

            for el in elements:
                text = el.text.strip()
                if text and text not in comments:
                    comments.append(text)

            if len(comments) >= TARGET_COMMENT_COUNT:
                break

            # 페이지 끝까지 스크롤
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)
            scroll_attempts += 1

        result = comments[:TARGET_COMMENT_COUNT]
        logger.info("Collected %d comments (target=%d)", len(result), TARGET_COMMENT_COUNT)
        return result
