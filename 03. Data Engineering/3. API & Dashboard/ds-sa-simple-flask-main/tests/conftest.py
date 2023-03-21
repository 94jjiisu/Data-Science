import os
import csv
import pytest
from flask import Response

@pytest.fixture
def app():
    from simple_flask_app.app import app
    return app

@pytest.fixture
def get_csv_data(app):
    try:
        with open(app.config['USERS_CSV_FILE'], 'r') as csv_file:
            content = csv.reader(csv_file)
            users = [_[0] for _ in content][1:]
    except Exception as err:
        print(err)
        print('CSV 파일을 읽어올 수가 없습니다.')

    return users
