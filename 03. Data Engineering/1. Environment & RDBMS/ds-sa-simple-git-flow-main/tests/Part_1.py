"""
Part 1
"""

from src import Part_1

def test_cli_where_you_are():
    assert Part_1.WHERE_YOU_ARE == 'pwd'

def test_cli_make_directory():
    assert Part_1.MAKE_DIRECTORY == 'mkdir Section3'

def test_cli_change_direcoty():
    assert Part_1.CHANGE_DIRECTORY == 'cd Section3'

def test_cli_clone_repo():
    assert len(Part_1.CLONE_REPOSITORY) > 10
    assert Part_1.CLONE_REPOSITORY.startswith('git clone ')

