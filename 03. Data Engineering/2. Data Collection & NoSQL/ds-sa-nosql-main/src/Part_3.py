"""
Part_3

NoSQL 데이터 가져오기 (Github API - User octokit repos)

Part_2 에서 입력한 데이터에서 중복되지 않는 repo 의 name 을 가져와서 set 형태로 저장합니다.
- User octokit repos 데이터가 저장될 리스트의 변수명은 names 로 지정해주세요
- 여러분의 행동에 따라 repo 의 중복된 이름이 MongoDB 에 있을 수도 있고, 유일한 이름만 있을 수도 있습니다.
- 코드에 적혀있는 대로 콜렉션 이름은 변경하지 말아주세요!

# 클라우드 데이터베이스는 테스트에 시간이 걸릴 수 있습니다. 기다려주세요.
"""
from pymongo import MongoClient

HOST = 'cluster0.nsgft.mongodb.net'
USER = 'jisuuser'
PASSWORD = 'jisu123'
DATABASE_NAME = 'git_data'
COLLECTION_NAME = 'octokit_repos'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

"""
아래 pass 와 주석을 지우고, 코드를 작성하세요
set 자료형인 names 변수에 octokit의 repo 이름이 저장되도록 작성해주세요
"""
import certifi 
ca = certifi.where()
### MongoClient를 설정하실 때 아래와 같이 해주세요
client = MongoClient(MONGO_URI, tlsCAFile=ca)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def Part_3_answer():

    names = []
    names = set(collection.distinct('name'))

    return names
