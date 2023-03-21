from src.Part_2 import dont_touch
from src.Part_3 import Part_3_answer


def test_octokit_names():
    """
    octokit 이란 소유자의 repo 목록을 데이터베이스에 입력했는지 확인합니다.
    """
    repo_names = {repo['name'] for repo in dont_touch}
    assert Part_3_answer() == repo_names