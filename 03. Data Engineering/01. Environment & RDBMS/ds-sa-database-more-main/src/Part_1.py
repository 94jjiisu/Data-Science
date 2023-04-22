"""
Part 1

Chinook 데이터베이스를 이용하여 각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다.
"""

QUERY_1 = """SELECT c.CustomerId, UPPER(c.City || ' ' || c.Country) AS NewCol
FROM customers c"""

QUERY_2 = """SELECT LOWER(SUBSTRING(c.FirstName,1, 4) || SUBSTRING(c.LastName,1,2)) AS NewName
FROM customers c """

QUERY_3 = """SELECT e.EmployeeId
FROM employees e 
WHERE DATE(HireDate) < DATETIME('2013-01-01')
ORDER BY LastName """

QUERY_4 = """SELECT c.FirstName || c.LastName || i.InvoiceId
FROM invoices i 
JOIN customers c ON i.CustomerId = c.CustomerId 
ORDER BY c.FirstName , c.LastName , i.InvoiceId """

QUERY_5 = """SELECT t.NAME
FROM tracks t
JOIN albums a ON t.AlbumId = a.AlbumId 
WHERE a.Title IN (
	SELECT a.Title
	FROM albums a
	WHERE a.Title = 'Unplugged' OR a.Title = 'Outbreak')"""
