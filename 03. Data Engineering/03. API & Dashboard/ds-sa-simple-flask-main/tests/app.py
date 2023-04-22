import csv
import pytest
from flask import url_for
from bs4 import BeautifulSoup

def test_index_html(client):
    res = client.get(url_for('index'))

    soup = BeautifulSoup(res.data, 'html.parser')

    try:
        assert res.status_code == 200
    except:
        pytest.fail('서버에서 200 응답을 받지 못했습니다.')

    try:
        assert soup.find('html') is not None
    except:
        pytest.fail('받은 응답에서 \'html\' 페이지를 찾지 못했습니다.')


def test_users_endpoint(client, get_csv_data):
    users = get_csv_data

    res = client.get(url_for('users'))
    client_users = res.json['users']

    try:
        assert client_users == users
    except AssertionError as e:
        print(e)
        pytest.fail("\'/users\' 에서 조회된 유저 목록이 CSV 파일과 일치하지 않습니다.")

def test_user_with_id(client, get_csv_data):
    csv_users = get_csv_data
    test_id = 1
    test_user = csv_users[test_id - 1]

    res = client.get(f"{url_for('display_user')}{ test_id }")
    client_user = res.get_data().decode('utf-8')

    try:
        assert client_user == test_user
    except AssertionError as err:
        print(err)
        pytest.fail(f"조회한 유저 아이디 {test_id} 의 유저 {test_user} 가 받은 응답의 유저 {client_user} 와 일치하지 않습니다.")

