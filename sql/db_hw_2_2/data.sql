/* [Project: Kiosk Order Management System]
- 목적: 주문 정보 및 고객 정보를 관리하는 DB 구축
- 테이블: orders, customers
- 작성일: 2026-04-28
*/

-- 1. 테이블 생성 (DDL)
-- orders 테이블: 주문의 고유 ID, 주문 날짜, 총 금액을 관리
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE NOT NULL,
    total_amount REAL NOT NULL
);

-- customers 테이블: 고객의 고유 ID, 이름, 이메일, 전화번호 관리
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL
);


-- 2. 데이터 삽입 (DML - INSERT)
-- orders 데이터 삽입: 최소 3개 이상
INSERT INTO orders (order_date, total_amount) VALUES ('2026-04-20', 15.50);
INSERT INTO orders (order_date, total_amount) VALUES ('2026-04-21', 25.00);
INSERT INTO orders (order_date, total_amount) VALUES ('2026-04-22', 10.99);

-- customers 데이터 삽입: 최소 3개 이상
INSERT INTO customers (name, email, phone) VALUES ('김철수', 'chul@example.com', '010-1234-5678');
INSERT INTO customers (name, email, phone) VALUES ('이영희', 'young@example.com', '010-2345-6789');
INSERT INTO customers (name, email, phone) VALUES ('박민수', 'min@example.com', '010-3456-7890');


-- 3. 데이터 수정 및 삭제 (DML - UPDATE/DELETE)
-- 요구사항: orders의 3번째 레코드를 삭제
-- 주의: 실무에서는 PK(order_id)를 기준으로 삭제하는 것이 가장 안전합니다.
DELETE FROM orders WHERE order_id = 3;

-- 요구사항: customers의 1번째 레코드의 name을 '홍길동'으로 수정
UPDATE customers SET name = '홍길동' WHERE customer_id = 1;


-- 4. 데이터 조회 (DML - SELECT)
-- 모든 데이터 조회
SELECT * FROM orders;
SELECT * FROM customers;