"""
Simple Flask App 입니다.

간단한 플래스크 어플리케이션을 만들어 보면서
어떻게 동작을 하는지 살펴보세요!
"""
import os
from flask import Flask, render_template, request
import csv, json

# 추가로 필요한 패키지들이 있는 경우 가져와 사용합니다.

# 'app' 은 플래스크 어플리케이션 객체입니다.
app = Flask(__name__)

# CSV 파일이 어디에 있는지 알려주는 설정입니다.
# CSV 파일은 수정하지 않습니다!
app.config['USERS_CSV_FILE'] = os.path.join(os.path.dirname(__file__), 'users.csv')

# 플래스크 어플리케이션의 라우팅 설정입니다.
# 서버 주소 + '/' 로 들어가면 아래 함수가 실행이 됩니다.
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    index 함수에서는 'simple_flask_app/templates' 폴더에 있는 'index.html'
    파일을 렌더링해줘야 합니다!
    """
    if request.method == 'GET':
        return render_template('index.html'), 200

@app.route('/users', methods=['GET', 'POST'])
def users(): # ex) 127.0.0.1:5000/user/<item>/room
    """
    users 함수에서는 사용자가 '서버 주소 + /users' 로 접속하게 되면
    'users.csv' 파일을 읽은 뒤에 파일에 있는 유저들을 리스트에 담아 JSON 형태로 
    넘겨줘야 합니다.

    넘겨줄 때에는 다음과 같은 JSON 형태여야 합니다:

        {
            "users": ["spongebob", "patrick", "squidward"]
        }

    NOTE: CSV 파일을 읽어온 뒤에 가장 첫 줄인 'username' 은 리스트에 담지 않습니다!  """
    data = []
    if request.method == 'GET':
        csv_file = csv.reader(open(app.config['USERS_CSV_FILE']))
        for row in csv_file:
            data.extend(row)
        dict = {}
        dict['users'] = data[1:]

        return dict, 200

@app.route('/users/', defaults={'user_order':1})
@app.route('/users/<user_order>', methods=['GET', 'POST'])
def display_user(user_order):
    """
    display_user 함수에서는 사용자가 '서버 주소 + /users/{ 유저 아이디 }' 로
    접속하게 되면 'users.csv' 파일의 { 유저 아이디 } 번째 유저를 문자열로 
    돌려줘야 합니다.

    만약에 사용자가 { 유저 아이디 } 를 명시하지 않은 경우에는 유저 아이디는 '1'
    이라고 가정합니다.

    예시)

    ('users.csv' 파일에 'spongebob', 'patrick', 'squidward' 순으로 적혀있다고
    가정합니다.)

    -   예를 들어 사용자가 '/users/' 에 접속하면 { 유저 아이디 } 가 주어지지 않았기
        때문에 '1' 번째, 즉 첫 번째 유저인 'spongebob' 문자열을 돌려줍니다.

    -   예를 들어 사용자가 '/users/1' 에 접속하면 '1' 번째, 즉 첫 번째 유저인
        'spongebob' 문자열을 돌려줍니다.

    -   예를 들어 사용자가 '/users/2' 에 접속하면 '2' 번째, 즉 두 번째 유저인
        'patrick' 문자열을 돌려줍니다.
    """
    data = []
    if request.method == 'GET':
        csv_file = csv.reader(open(app.config['USERS_CSV_FILE']))
        for row in csv_file:
            data.extend(row)

    return data[int(user_order)], 200
    

if __name__ == "__main__":
    app.run(debug=True)
