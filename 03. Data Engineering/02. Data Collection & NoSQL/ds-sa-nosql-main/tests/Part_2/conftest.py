import pytest
from pymongo import MongoClient
from src.Part_2 import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

import certifi 
ca = certifi.where()
### MongoClient를 설정하실 때 아래와 같이 해주세요
client = MongoClient(MONGO_URI, tlsCAFile=ca)

@pytest.fixture(scope='module')
def connection():
    conn = MongoClient(MONGO_URI, tlsCAFile=ca)
    yield conn
    conn.close()

@pytest.fixture
def database_conn(connection):
    database = connection[f"{DATABASE_NAME}"]
    yield database

@pytest.fixture
def collection(database_conn):
    collection = database_conn[f"{COLLECTION_NAME}"]
    yield collection
