import sqlite3
from string import Template

from sprint_challenge import Part_1 

"""
Part 1.1 - Schema Testing
"""

SQL_CHECK_COLUMNS = Template("SELECT name from PRAGMA_TABLE_INFO('$table')")
SQL_CHECK_TABLE = Template("SELECT sql FROM sqlite_master WHERE name='$table';")

def test_user_table(test_cursor):
    test_table = 'User'

    cur = test_cursor
    cur.execute(Part_1.CREATE_USER_TABLE)

    test_exists = cur.execute(SQL_CHECK_TABLE.substitute(table=test_table)).fetchall()
    test_columns = cur.execute(SQL_CHECK_COLUMNS.substitute(table=test_table)).fetchall()

    assert test_exists != []
    assert test_columns.__len__() == 3

def test_product_table(test_cursor):
    test_table = 'Product'

    cur = test_cursor
    cur.execute(Part_1.CREATE_PRODUCT_TABLE)

    test_exists = cur.execute(SQL_CHECK_TABLE.substitute(table=test_table)).fetchall()
    test_columns = cur.execute(SQL_CHECK_COLUMNS.substitute(table=test_table)).fetchall()

    assert test_exists != []
    assert test_columns.__len__() == 3

def test_join_table(test_cursor):
    test_table = 'User_Product'

    cur = test_cursor
    cur.execute(Part_1.CREATE_USER_PRODUCT_TABLE)

    test_exists = cur.execute(SQL_CHECK_TABLE.substitute(table=test_table)).fetchall()
    test_columns = cur.execute(SQL_CHECK_COLUMNS.substitute(table=test_table)).fetchall()

    assert test_exists != []
    assert test_columns.__len__() == 3

"""
Part 1.2 - Query Testing
"""

def test_question_1(get_answer):
    expected_answer = [
        ('Côte de Blaye',),
        ('Thüringer Rostbratwurst',),
        ('Mishi Kobe Niku',),
        ("Sir Rodney's Marmalade",),
        ('Carnarvon Tigers',),
        ('Raclette Courdavault',),
        ('Manjimup Dried Apples',),
        ('Tarte au sucre',),
        ('Ipoh Coffee',),
        ('Rössle Sauerkraut',)
    ]

    assert get_answer(Part_1.SQL_QUERY_1) == expected_answer

def test_question_2(get_answer):
    expected_answer = [(37.22222222222222,)]

    assert get_answer(Part_1.SQL_QUERY_2) == expected_answer

def test_question_3(get_answer):
    expected_answer = [
        (38, 'Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
        (29, 'Thüringer Rostbratwurst', 123.79,
         'Plutzer Lebensmittelgroßmärkte AG'),
        (9, 'Mishi Kobe Niku', 97, 'Tokyo Traders'),
        (20, "Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
        (18, 'Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
        (59, 'Raclette Courdavault', 55, 'Gai pâturage'),
        (51, 'Manjimup Dried Apples', 53, "G'day, Mate"),
        (62, 'Tarte au sucre', 49.3, "Forêts d'érables"),
        (43, 'Ipoh Coffee', 46, 'Leka Trading'),
        (28, 'Rössle Sauerkraut', 45.6,
         'Plutzer Lebensmittelgroßmärkte AG')
    ]

    assert get_answer(Part_1.SQL_QUERY_3) == expected_answer

def test_question_4(get_answer):
    expected_answer = [('Confections',)]

    assert get_answer(Part_1.SQL_QUERY_4) == expected_answer

def test_question_5(get_answer):
    expected_answer = [
        ('Kirkland', 29.0),
        ('London', 32.5),
        ('Redmond', 56.0),
        ('Seattle', 40.0),
        ('Tacoma', 40.0)
    ]

    assert get_answer(Part_1.SQL_QUERY_5) == expected_answer

def test_question_6(get_answer):
    expected_answer = [(7, 'King', 10)]

    assert get_answer(Part_1.SQL_QUERY_6) == expected_answer
