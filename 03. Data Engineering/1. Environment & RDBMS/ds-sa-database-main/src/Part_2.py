"""
Part 2

Chinook.db를 이용하여 각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다. 데이터베이스 엔진은 SQLite를 사용합니다.
"""

QUERY_1 = """SELECT Title
FROM albums
WHERE AlbumId = 31;"""

QUERY_2 = """SELECT AlbumId 
FROM albums join artists on albums.ArtistId = artists.ArtistId
WHERE Name like "%the%";"""

QUERY_3 = """SELECT invoices.InvoiceId
FROM invoices
WHERE invoices.BillingCity IN ('Stuttgart', 'Oslo', 'Redmond')
ORDER BY invoices.InvoiceId ASC;"""

QUERY_4 = """SELECT tracks.TrackId 
FROM tracks
WHERE tracks.Name LIKE 'The%';"""

QUERY_5 = """SELECT customers.CustomerId 
FROM customers
WHERE customers.Email LIKE '%gmail.com';"""

QUERY_6 = """SELECT invoices.InvoiceId 
FROM invoices
WHERE invoices.CustomerId IN (29,30,63)
AND invoices.Total BETWEEN 1 AND 3;"""

QUERY_7 = """SELECT tracks.TrackId 
FROM tracks Join genres on tracks.GenreId = genres.GenreId 
WHERE genres.Name = 'Soundtrack'
AND tracks.Milliseconds BETWEEN 300000 AND 400000"""

QUERY_8 = """
SELECT COUNT(*) AS The_Num_of_customers_X_Country
FROM customers
GROUP BY customers.Country"""

QUERY_9 = """SELECT invoices.CustomerId
FROM invoices
GROUP BY invoices.CustomerId
ORDER BY SUM(invoices.Total) DESC
LIMIT 5;"""

QUERY_10 = """SELECT g.Name as 'Genre_name', 
count(DISTINCT c.CustomerId) as 'The Number of customer_ID'
FROM customers c 
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId 
JOIN tracks t ON ii.TrackId =  t.TrackId 
JOIN genres g ON t.GenreId =  g.GenreId
GROUP BY g.Name;"""
