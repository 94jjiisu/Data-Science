from src.Part_2 import dont_touch

def test_octokit(collection):
    """
    주어진 github 의 octokit 데이터가 몽고디비에 들어가 있는지 확인합니다.
    - node_id 기반으로 데이터를 확인합니다.
    """

    for repo in dont_touch:
        your_repo = collection.find_one({"id":repo['id']})
        del your_repo['_id']
        assert your_repo['node_id'] == repo['node_id']