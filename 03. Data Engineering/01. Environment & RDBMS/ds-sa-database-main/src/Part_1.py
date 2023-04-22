"""
Part 1

아래에 코드에 요구사항에 알맞은 SQL 쿼리문을 작성합니다.
"""

CUSTOMER_TABLE = """CREATE TABLE Customer (
	customer_id INTEGER NOT NULL PRIMARY KEY,
	customer_name VARCHAR(32) NOT NULL,
	customer_age INTEGER
);"""

PACKAGE_TABLE = """CREATE TABLE Package (
	package_id INTEGER NOT NULL PRIMARY KEY,
	package_name VARCHAR(32) NOT NULL,
	package_date DATE
);
"""

CUSTOMER_PACKAGE_TABLE = """CREATE TABLE Customer_Package (
	cp_id INTEGER NOT NULL PRIMARY KEY,
	customer_id INTEGER,
	package_id INTEGER,
	FOREIGN KEY(customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(package_id) REFERENCES Package(package_id) ON DELETE CASCADE ON UPDATE CASCADE
);
"""
