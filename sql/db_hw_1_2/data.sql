/* [Database: Chinook (Sample)]
tracks 테이블을 대상으로 하는 데이터 조회 쿼리 목록
*/

-- 1. tracks 테이블의 모든 데이터를 조회하시오.
SELECT * FROM tracks;

-- 2. Name, Milliseconds, UnitPrice 열의 모든 데이터를 조회하시오.
SELECT Name, Milliseconds, UnitPrice FROM tracks;

-- 3. GenreId 행의 값이 1인 모든 데이터를 조회하시오. (필터링)
SELECT * FROM tracks WHERE GenreId = 1;

-- 4. 모든 데이터를 Name을 기준으로 오름차순 정렬하여 조회하시오.
-- ASC는 오름차순(기본값)을 의미합니다.
SELECT * FROM tracks ORDER BY Name ASC;

-- 5. tracks 테이블의 모든 데이터를 조회하되, 10개만 출력하시오. (개수 제한)
SELECT * FROM tracks LIMIT 10;