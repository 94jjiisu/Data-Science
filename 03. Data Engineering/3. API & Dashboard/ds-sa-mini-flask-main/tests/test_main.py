import pytest
from flask import url_for
from bs4 import BeautifulSoup

class TestMain:
    def test_main_index(self, client):
        res = client.get(url_for('main.index'))

        soup = BeautifulSoup(res.data, 'html.parser')

        try:
            assert res.status_code == 200
        except:
            pytest.fail('서버에서 200 응답을 받지 못했습니다.')

        try:
            assert soup.find('html') is not None
        except:
            pytest.fail('받은 응답에서 \'html\' 을 찾지 못했습니다.')

    def test_index_html(self, client, csv_operator):
        # 유저를 데이터베이스에 추가 뒤 main.index 에서 렌더링이 되는지 확인
        test_user = {
            'username':'spongebob'
        }

        operator = csv_operator()

        # csv 파일에 test_user 추가
        operator.add_row(test_user)

        res = client.get(url_for('main.index'))
        html_text = BeautifulSoup(res.data, 'html.parser').text

        try:
            assert html_text.find('spongebob') != -1
        except AssertionError as e:
            print(e)
            pytest.fail('유저네임 값을 index.html 에서 찾을 수 없습니다')

        try:
            assert html_text.find('1') != -1
        except AssertionError as e:
            print(e)
            pytest.fail('유저 아이디 값을 index.html 에서 찾을 수 없습니다.')
