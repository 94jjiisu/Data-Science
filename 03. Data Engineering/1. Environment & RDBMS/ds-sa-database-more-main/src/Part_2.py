"""
Part 2

각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다.
"""

QUERY_1 = """CREATE TABLE Teacher(
	id INTEGER PRIMARY KEY,
	name VARCHAR(30),
	subject VARCHAR(10) NOT NULL,
	salary INTEGER
);"""
  
QUERY_2 = """CREATE TABLE Student(
	teacher_id INTEGER NOT NULL,
	student_id CHAR(4) NOT NULL,
	age INTEGER NOT NULL,
	PRIMARY KEY(teacher_id, student_id)
	FOREIGN KEY(teacher_id) REFERENCES Teacher(id)
	ON DELETE CASCADE ON UPDATE CASCADE	
);"""
 
BLANK = "INSERT INTO Teacher(name, subject, salary)"

#밑의 코드는 변경하지 않습니다.
QUERY_3_1 = f"{BLANK} VALUES ('Spongebob', 'Math', 3500)"
QUERY_3_2 = f"{BLANK} VALUES ('Patrick', 'Science', 3200)"
QUERY_3_3 = f"{BLANK} VALUES ('Squidward', 'Math', 3800)"
QUERY_3_4 = f"{BLANK} VALUES ('Sandy', 'English', 3300)"
QUERY_3_5 = f"{BLANK} VALUES ('Nimo', 'English', 3150)"
QUERY_3_6 = f"{BLANK} VALUES ('Dory', 'Math', 2800)"
QUERY_3_7 = f"{BLANK} VALUES ('Marlin', 'Science', 4000)"

#Student에 데이터를 넣는 쿼리입니다. 변경하지 마세요 (Part_3에서 사용)
QUERY_4_1 = "INSERT INTO Student VALUES(1, 'C100', 50);"
QUERY_4_2 = "INSERT INTO Student VALUES(1, 'C101', 55);"
QUERY_4_3 = "INSERT INTO Student VALUES(1, 'C102', 56);"
QUERY_4_4 = "INSERT INTO Student VALUES(2, 'D100', 60);"
QUERY_4_5 = "INSERT INTO Student VALUES(2, 'D101', 72);"
QUERY_4_6 = "INSERT INTO Student VALUES(2, 'D102', 73);"
QUERY_4_7 = "INSERT INTO Student VALUES(2, 'D103', 73);"

#Teaher 테이블에 Insert가 잘 되어있지 않다면, 해당 쿼리도 틀릴 수 있습니다
QUERY_4 = """SELECT name, subject, salary,
	CASE WHEN salary < 3000 THEN 'Low'
	WHEN salary BETWEEN 3000 AND 3999 THEN 'Mid'
	ELSE 'High'
	END AS '월급 그룹'
FROM Teacher;"""

#Teacher 테이블에 Insert 가 잘 되어있지 않다면, 해당 쿼리도 틀릴 수 있습니다
QUERY_6 = "DROP TABLE Teacher;"
