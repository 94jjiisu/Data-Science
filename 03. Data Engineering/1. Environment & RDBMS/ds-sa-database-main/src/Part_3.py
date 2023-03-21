"""
Part 3

STORE.db를 이용하여 각 이미지로 전달된 결과가 출력될 수 있는 SQL 문을 작성합니다. 데이터베이스 엔진은 SQLite를 사용합니다.
"""

QUERY_1 = """SELECT c.id, c.name, i.invoice_amt
FROM Customers c LEFT JOIN Invoices i
	ON c.id = i.customer_id
WHERE i.invoice_amt IS NULL;
"""

QUERY_2 = """SELECT i.customer_id, c.name, i.invoice_amt
FROM Invoices i LEFT JOIN Customers c
    ON i.customer_id = c.id 
WHERE c.name IS NULL
"""

QUERY_3 = """SELECT id, customer_id, DATE(invoice_date) AS 날짜, invoice_amt
FROM Invoices
ORDER BY invoice_amt DESC"""

