/* [Script: orders 테이블 재설계 및 JOIN 조회]
- 테이블 초기화 및 Foreign Key(외래키)를 활용한 관계 형성
- ALTER TABLE을 이용한 스키마 구조 변경
- INNER JOIN을 활용한 관계 데이터 동시 조회
*/

-- 1. 기존 테이블 삭제 (DDL)
DROP TABLE IF EXISTS orders;

-- 2. orders 테이블 생성 및 customers와 관계 형성 (Foreign Key)
-- total_amount는 다음 단계에서 삭제할 예정이므로 임시로 생성합니다.
-- customer_id 필드가 customers 테이블의 customer_id를 참조하도록 외래키를 설정합니다.
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE NOT NULL,
    total_amount REAL, 
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 3. 테이블 필드 수정 (DDL - ALTER)
-- price 컬럼을 정수형(INTEGER)으로 추가합니다.
ALTER TABLE orders ADD COLUMN price INTEGER;

-- total_amount 컬럼을 삭제합니다. 
-- (주의: SQLite 3.35.0 이전 버전에서는 DROP COLUMN을 지원하지 않습니다. 에러가 난다면 버전 문제입니다.)
ALTER TABLE orders DROP COLUMN total_amount;

-- 4. 데이터 삽입 (DML - INSERT)
-- total_amount가 삭제되었으므로 price에 Integer 값을 넣습니다. 
-- 요구사항의 'Real 타입 10.11 형식'은 삭제된 total_amount를 의미하는 과제 설명의 잔재로 보입니다. 
-- customers 테이블에 1, 2, 3번 고객이 존재한다고 가정합니다.
INSERT INTO orders (order_date, price, customer_id) VALUES ('2026-04-28', 15000, 1);
INSERT INTO orders (order_date, price, customer_id) VALUES ('2026-04-29', 25000, 2);
INSERT INTO orders (order_date, price, customer_id) VALUES ('2026-04-30', 8500, 3);

-- 5. JOIN을 활용한 데이터 조회 (DML - SELECT)
-- orders 테이블의 모든 데이터(o.*)와 customers 테이블의 name 필드(c.name)를 연결하여 출력합니다.
SELECT 
    o.*, 
    c.name AS customer_name
FROM 
    orders o
JOIN 
    customers c ON o.customer_id = c.customer_id;