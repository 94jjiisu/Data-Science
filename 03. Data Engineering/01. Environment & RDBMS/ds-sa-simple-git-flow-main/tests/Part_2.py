"""
Part 2
"""

import os
from src import Part_2

def test_conda_make_virtual_env():
    assert Part_2.MAKE_VIRTUAL_ENV in {"conda create -n s1n1 python=3.8", "conda create -n s1n1 python==3.8", 
                                    'conda create -n "s1n1" python=3.8', 'conda create -n "s1n1" python==3.8',
                                    "conda create --name 's1n1' python=3.8","conda create --name s1n1 python=3.8",
                                    "conda create --name 's1n1' python==3.8","conda create --name s1n1 python==3.8"
                                    }

def test_conda_activate_virtual_env():
    assert Part_2.ACTIVATE_VIRTUAL_ENV == "conda activate s1n1"

def test_conda_virtual_env_list():
    assert Part_2.VIRTUAL_ENV_LIST == "conda env list"


def test_conda_if_result_file_exist():
    '''
    1) 수강생의 과제 파일 안에 콘다 가상환경의 목록이 있는지 확인합니다.
    2) 해당 가상환경 명이 s1n1 인지 확인합니다.
    '''
    exist = False
    FILEPATH = os.getcwd()
    with open(FILEPATH+"/result.txt", 'r') as file:
        line = file.read()
        if "s1n1" not in line:
            assert exist
