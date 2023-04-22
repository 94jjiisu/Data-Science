"""
Part_5

NoSQL 데이터 입력하기 (csv-titanic)

클러스터 및 데이터베이스를 생성한 뒤에 titanic.csv 에 있는 탑승객 데이터 하나마다 문서로 저장합니다.

필요에 따라 추가로 코드를 작성합니다.

각 값의 데이터 타입은 아래와 같습니다. (필드명은 자유입니다).
아래에는 각 필드에 해당하는 데이터 타입입니다.
- Survived: int
- Pclass: int
- Name: str
- Sex: str
- Age: float
- Siblings/Spouses Aboard: int
- Parents/Children Aboard: int
- Fare: float

다 옮긴 뒤에 'passengers' 데이터베이스 정보를 아래 입력합니다.
해당 파트를 진행할 때는 titanic.csv 는 과제 레포에 있는 파일을 사용해야 합니다.
- 코드에 적혀있는 대로 콜렉션 이름은 변경하지 말아주세요!
"""

import csv
import os
from pymongo import MongoClient

HOST = 'cluster0.nsgft.mongodb.net'
USER = 'jisuuser'
PASSWORD = 'jisu123'
DATABASE_NAME = 'TITANIC'
COLLECTION_NAME = 'passengers'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

"""
위 코드는 힌트입니다. 자신에 맞는 HOST,USER, PASSWORD, DATABASE_NAME 을 입력하세요
! COLLECTION_NAME = 'openweather'
아래 pass 를 지우고 코드를 작성하세요
"""

import certifi 
ca = certifi.where()
### MongoClient를 설정하실 때 아래와 같이 해주세요
client = MongoClient(MONGO_URI, tlsCAFile=ca)

db = client[DATABASE_NAME]

db.passengers.drop()

collection = db[COLLECTION_NAME]


with open('titanic.csv', 'r') as f:
    data = csv.DictReader(f)
    for line in data:
        line["Survived"] = int(line["Survived"])
        line["Pclass"] = int(line["Pclass"])
        line["Age"] = float(line["Age"])
        line["Siblings/Spouses Aboard"] = int(line["Siblings/Spouses Aboard"])
        line["Parents/Children Aboard"] = int(line["Parents/Children Aboard"])
        line["Fare"] = float(line["Fare"])
        collection.insert_one(document=line)
