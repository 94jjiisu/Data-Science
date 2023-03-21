"""
Part 3
"""

from src import Part_3

def test_git_add_to_staging_area():
    assert Part_3.ADD_TO_STAGING_AREA in {"git add .", "git add ./", "git add -A", "git add --all"}

def test_git_staging_area_statement():
    assert Part_3.CHECK_AREA_STATEMENT == "git status"

def test_git_commit_to_repo():
    commit_list = ["git commit", "-m", "Part3 commit"]
    for comment in commit_list:
        assert comment in Part_3.COMMIT_TO_REPO

def test_git_push_to_remote():
    assert Part_3.PUSH_TO_REMOTE == "git push origin main"
