/* [Script: tracks 테이블 고급 조회 및 집계]
- 문자열 패턴 매칭, 다중 조건 필터링, 그룹화 및 집계 함수 적용
- 작성자: 시니어 멘토
*/

-- 1. name의 값에 'love'가 포함된 모든 행 조회 (대소문자 구분 없음)
SELECT * FROM tracks 
WHERE Name LIKE '%love%';

-- 2. GenreId가 1이고 재생시간이 300,000ms 이상인 데이터를 단가 기준 내림차순 정렬
SELECT * FROM tracks 
WHERE GenreId = 1 
  AND Milliseconds >= 300000 
ORDER BY UnitPrice DESC;

-- 3. 장르별 트랙 수 집계 (별칭: TotalTracks)
SELECT GenreId, COUNT(*) AS TotalTracks
FROM tracks 
GROUP BY GenreId;

-- 4. 장르별 총 매출(UnitPrice 합계)이 100 이상인 그룹만 조회 (별칭: TotalPrice)
SELECT GenreId, SUM(UnitPrice) AS TotalPrice
FROM tracks 
GROUP BY GenreId 
HAVING TotalPrice >= 100;