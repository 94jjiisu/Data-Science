import json 
from flask import url_for

class TestUser:
    def test_get_user(self, client, csv_operator):
        """
        User 를 가져오는 엔드포인트를 실험합니다.
        """

        test_user = {
            'username':'spongebob'
        }

        operator = csv_operator()

        # 확인할 유저를 추가합니다.
        operator.add_row(test_user)
        
        # 정상적으로 가져오는 경우
        res = client.get(url_for('user.get_user',\
                                 username=test_user['username']))

        test_user_data = operator.get_row('username', test_user['username'])

        assert res.status_code == 200
        assert res.data == test_user_data['id'].encode()

        # username 이 주어지지 않은 경우
        res = client.get(url_for('user.get_user'))

        assert res.status_code == 400
        assert res.data == 'No username given'.encode()

        operator.delete_row('username', test_user['username'])

        # username 이 주어졌으나 데이터베이스에 없는 경우
        res = client.get(url_for('user.get_user',
                                 username=test_user['username']))

        assert res.status_code == 404
        assert res.data == f"User '{test_user['username']}' doesn't exist".encode()


    def test_post_endpoint(self, client, csv_operator):
        """
        유저를 새로 추가하는 엔드포인트를 확인합니다.
        """

        test_user = {
            'username':'spongebob'
        }

        operator = csv_operator()

        # 정상적으로 유저가 만들어지는 경우
        res = client.post(url_for('user.create_user'), json=test_user)

        assert res.status_code == 200
        assert res.data == f"Created user '{test_user['username']}'".encode()
        
        # 유저가 CSV 파일에 생성되었는지 확인
        user = operator.get_row('username', test_user['username'])

        assert user != None
        assert user['username'] == test_user['username']

        # username 을 사용하는 유저가 존재하는 경우
        res = client.post(url_for('user.create_user'), json=test_user)

        assert res.status_code == 400
        assert res.data == f"User '{test_user['username']}' already exists".encode()

        # username 이 주어지지 않은 경우
        res = client.post(url_for('user.create_user'))

        assert res.status_code == 400
        assert res.data.decode('utf-8') == "No username given"


    def test_delete_endpoint(self, client, csv_operator):
        """
        유저를 삭제하는 엔드포인트를 확인합니다.
        """

        test_user = {
            'username':'patrick'
        }

        operator = csv_operator()

        # 없는 유저를 삭제하려는 경우
        res = client.delete(url_for('user.delete_user',
                                    username=test_user['username']))
        
        assert res.status_code == 404
        assert res.data == f"User '{test_user['username']}' doesn't exist".encode()

        # 정상적으로 삭제가 되는 경우
        operator.add_row(test_user)

        res = client.delete(url_for('user.delete_user',
                                    username=test_user['username']))

        assert res.status_code == 200
        assert res.data == b'OK'

        # CSV 파일에서 유저가 삭제되었는지 확인
        user = operator.get_row('username', test_user['username'])

        assert user is None


    def test_patch_endpoint(self, client, csv_operator):
        """
        유저를 업데이트하는 엔트포인트를 확인합니다.
        """

        test_user = {
            'username':'squidward'
        }

        test_new_user = {
            'username':'plankton'
        }

        operator = csv_operator()

        # 정상적으로 업데이트가 되는 경우
        operator.add_row(test_user)

        
        res = client.patch(url_for('user.update_user', 
                                   username=test_user['username'],
                                   new_username=test_new_user['username']))

        assert res.status_code == 200
        assert res.data == b'OK'

        # CSV 파일에서 유저 이름이 변경되었는지 확인
        user = operator.get_row('username', test_user['username'])
        new_user = operator.get_row('username', test_new_user['username'])

        assert user is None
        assert new_user is not None
        assert new_user['username'] == test_new_user['username']

        # 업데이트하는 유저가 없는 경우
        res = client.patch(url_for('user.update_user',
                                   username='No User',
                                   new_username='New No User'))

        assert res.status_code == 400
        assert res.data == f"User 'No User' doesn't exist".encode()

        # 변경할 username 이 이미 사용중인 경우
        second_test_user = {
            'username':'spongebob'
        }

        operator.add_row(second_test_user)

        res = client.patch(url_for('user.update_user',
                                  username=second_test_user['username'],
                                  new_username=test_new_user['username']))

        assert res.status_code == 400
        assert res.data == f"Username '{test_new_user['username']}' is in use".encode()

        # username, new_username 둘 다 안 주어진 경우
        res = client.patch(url_for('user.update_user'))

        assert res.status_code == 400
        assert res.data == b"No username/new_username given"
                        
        # username 만 주어진 경우
        res = client.patch(url_for('user.update_user', username='Only username'))

        assert res.status_code == 400
        assert res.data == b"No username/new_username given"

        # new_username 만 주어진 경우
        res = client.patch(url_for('user.update_user', new_username='Only new_username'))

        assert res.status_code == 400
        assert res.data == b"No username/new_username given"
