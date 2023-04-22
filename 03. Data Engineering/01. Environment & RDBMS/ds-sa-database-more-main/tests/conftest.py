import os
import pytest
import pickle
import shutil
import sqlite3
from string import Template

pytest.RESOURCE_PATH = os.path.join(os.getcwd(), 'tests', 'resources')


@pytest.fixture(autouse=True, scope="module")
def setup_teardown_msg():
    template = Template("""
        -------------------------------------
        $msg...
        -------------------------------------
        """)
    yield print(template.substitute(msg="Setting up"))
    print(template.substitute(msg="Tearing down"))


@pytest.fixture(autouse=True, scope="session")
def pkl_opener():
    def returner(file_path):
        with open(file_path, 'rb') as f:
            content = pickle.load(f)
        return content
    pytest.pkl_opener = returner
