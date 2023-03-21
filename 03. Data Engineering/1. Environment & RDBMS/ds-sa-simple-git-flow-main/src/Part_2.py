"""
Part 2

Assignment Requirement

> 시작하기 전에 Part 1 이 먼저 진행되어야 합니다.
> 해당 과제 파일 안의 요구사항은 힌트가 될 수 있습니다.
> 최대한 Urclass 요구사항으로만 시도/완성 후 해당 파일을 열어주세요!


1 & 2. s1n1 이라는 이름을 가진 가상환경을 생성하고, 그 가상환경에서 작업을 진행합니다.

    1) s1n1 이라는 이름을 가진 가상환경을 생성합니다.
    2) s1n1 가상환경을 활성화합니다.
    3) 콘다 가상환경의 목록을 조회합니다.
        -> 출력된 결과를 'result.txt' 에 저장합니다. (setup.cfg 와 같은 위치에 저장합니다.)

3. 해당 가상환경에 pytest 제출 플러그인을 다운 받습니다.

4. pytest 를 제출합니다. 

    Hint! :
    -> 제출을 하기 위해서는 먼저 'requirements.txt' 파일에 있는 패키지들을 설치해야 합니다. 
    -> 파이썬에서는 requirements.txt 에 있는 패키지들을 다음과 같이 설치할 수 있습니다.

        $ pip install -r requirements.txt

** 대소문자를 정확히 구분해서 작성해 주세요. **
"""

MAKE_VIRTUAL_ENV = "conda create --name s1n1 python=3.8"

ACTIVATE_VIRTUAL_ENV = "conda activate s1n1"

VIRTUAL_ENV_LIST = "conda env list"
