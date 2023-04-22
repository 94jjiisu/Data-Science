import pytest
from src.Part_3 import (os, sqlite3, DB_FILEPATH)

@pytest.fixture
def test_connection():
    connection = None
    database_exist = os.path.isfile(DB_FILEPATH)

    if database_exist == True:
        connection = sqlite3.connect(DB_FILEPATH)
    
    yield connection
    connection.close()

@pytest.fixture
def test_cursor(test_connection):
    cursor = test_connection.cursor()
    yield cursor
    cursor.close()