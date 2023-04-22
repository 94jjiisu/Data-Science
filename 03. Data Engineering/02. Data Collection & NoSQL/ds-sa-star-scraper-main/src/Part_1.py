import re
import requests
from bs4 import BeautifulSoup

"""
Part 1

영화 리뷰 스크레이핑을 위한 함수들을 구현해봅니다.

사용할 사이트는 네이버의 영화 리뷰입니다.

> 해당 BASE_URL 은 아래 설정이 되어 있습니다. 코드를 작성하면서 `BASE_URL` 에 문자열을 추가로 붙여서 사용해보세요!
> 추가로 BASE_URL 은 접속이 되지 않습니다.
"""

BASE_URL = "https://movie.naver.com/movie"


def get_page(page_url):
    """
    get_page 함수는 페이지 URL 을 받아 해당 페이지를 가져오고 파싱한 두
    결과들을 리턴합니다.

    예를 들어 `page_url` 이 `https://github.com` 으로 주어진다면
        1. 해당 페이지를 requests 라이브러리를 통해서 가져오고 해당 response 객체를 page 변수로 저장
        2. 1번의 response 의 html 을 BeautifulSoup 으로 파싱한 soup 객체를 soup 변수로 저장
        3. 저장한 soup, page 들을 리턴하고 함수 종료

    파라미터:
        - page_url: 받아올 페이지 url 정보입니다.

    리턴:
        - soup: BeautifulSoup 으로 파싱한 객체
        - page: requests 을 통해 받은 페이지 (requests 에서 사용하는 response
        객체입니다).
    """

    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")

    return soup, page


def get_avg_stars(reviews):
    """
    get_avg_stars 함수는 리뷰 리스트를 받아 평균 별점을 구해 리턴하는
    함수입니다.

    파라미터:
        - reviews: 리뷰 객체가 항목으로 이루어진 리스트. 각 리뷰 객체는 다음과
        같은 property 가 있어야 합니다:
            - 'review_text': 리뷰 내용이 담긴 문자열 (str)
            - 'review_star': 리뷰 별점이 담긴 숫자 (float)

    리턴:
        - 별점 평균: 주어진 리뷰들의 별점들을 평균을 낸 숫자(float) 입니다.

    ------------------------------------------------
    예시:

    reviews =
        [
            {
                'review_text': 'Wow...!',
                'review_star': 7
            },
            {
                'review_text': 'Okay movie',
                'review_star': 6
            }
        ]

    get_avg_stars(reviews) #=> 6.5
    ------------------------------------------------
    """
    #avg = None

    sum = 0
    for review in reviews:
        sum += review['review_star']
    
    avg = sum/len(reviews)

    return avg


def get_movie_code(movie_title):
    """
    get_movie_code 함수는 영화 제목을 받으면 해당 영화 제목으로 검색했을 때
    가장 먼저 나오는 영화의 아이디를 리턴합니다.

    해당 영화의 아이디는 네이버에서 지정한대로 사용합니다. 
    여기에서 네이버에서 지정한 아이디란 예를 들어 다음과 같습니다:
        - `https://movie.naver.com/` 에 접속
        - 검색란에 영화 제목 (예: Soul) 입력 뒤 검색
        - 해당 영화 페이지의 URL (예: `https://movie.naver.com/movie/bi/mi/basic.nhn?code=184517`) 의 'code=' 뒤에 나오는 숫자

    파라미터:
        - movie_title: 리뷰를 스크레이핑할 영화 제목이 담긴 문자열(str) 입니다.

    리턴:
        - 영화 아이디 번호: 네이버에서 지정한 영화의 아이디 번호가 담긴
        숫자(int) 입니다.
    """
    search_url = f"{BASE_URL}/search/result.naver?query={movie_title}&section=all&ie=utf8"
    #movie_code = None

    soup, page = get_page(search_url)

    movie_code = soup.find('dt').find('a')['href'].split('=')[-1]

    return int(movie_code)


def get_reviews(movie_code, page_num=1):
    """
    get_reviews 함수는 리뷰들이 담긴 리뷰 리스트를 리턴해주는 함수입니다.

    각 리뷰는 다음과 같은 파이썬 딕셔너리 형태입니다:
        {
            'review_text': 리뷰 글이 담긴 문자열(str) 입니다,
            'review_star': 리뷰 별점이 담긴 숫자(int) 입니다
        }

    파라미터:
        - movie_code: 네이버에서 지정한 영화 아이디 번호가 담긴 숫자(int)
        입니다.
        - page_num: 리뷰를 몇 번째 리뷰 페이지에서 가져와야 하는지 담긴
        숫자(int) 입니다. 아무것도 주어지지 않은 경우 기본값은 1 입니다.

    리턴:
        - 리뷰 리스트: 스크레이핑한 리뷰들이 각각 파이썬 딕셔너리로 위에 명시된
        형태로 저장된 리스트입니다.
    """
    review_url = f"{BASE_URL}/point/af/list.naver?st=mcode&sword={movie_code}&target=after&page={page_num}"
    review_list = []

    soup, page = get_page(review_url)

    review_text = soup.find_all('td', class_='title')
    review_star = soup.find_all('div', class_='list_netizen_score')

    for text, star in zip(review_text, review_star):
        review_list.append({
            'review_text': text.find_next('br').next_element,
            'review_star': int(star.find('em').text)
        })

    return review_list


def scrape_by_review_num(movie_title, review_num):
    """
    scrape_by_review_num 함수는 총 스크레이핑할 리뷰 개수를 받아 해당 개수만큼
    리뷰 항목이 담긴 리뷰 리스트를 리턴합니다.

    파라미터:
        - movie_title: 리뷰를 스크레이핑할 영화 제목이 담긴 문자열(str) 입니다.
        - review_num: 총 몇 개의 리뷰를 가져올지 정해주는 숫자(int) 입니다.

    리턴:
        - 리뷰 리스트: 주어진 review_num 만큼의 리뷰 항목을 담은 파이썬
        리스트입니다. (각 리뷰 항목은 get_reviews 에서 명시된 파이썬 딕셔너리
        형태여야 합니다.)
    """
    reviews = []

    movie_code = get_movie_code(movie_title)
    page_num = 1

    loading = get_reviews(movie_code, page_num)
    while len(loading) < review_num:
        page_num += 1
        loading.extend(get_reviews(movie_code, page_num))
    
    for i in range(review_num):
        reviews.append(loading[i])

    return reviews


def scrape_by_page_num(movie_title, page_num=10):
    """
    scrape_by_page_num 함수는 페이지 수를 기준으로 리뷰를 스크레이핑하는
    함수입니다.

    파라미터:
        - movie_title: 리뷰를 스크레이핑할 영화 제목이 담긴 문자열(str) 입니다.
        - page_num: 첫 번째 페이지에서부터 스크레이핑할 페이지 개수가 담긴
        숫자(int) 입니다.

    리턴:
        - 리뷰 리스트: 주어진 page_num 만큼의 페이지에서부터 스크레이핑한
        리뷰를 담은 파이썬 리스트입니다. (각 리뷰 항목은 get_reviews 에서
        명시된 파이썬 딕셔너리 형태여야 합니다.)
    """
    reviews = []

    movie_code = get_movie_code(movie_title)

    for n in range(page_num):
        reviews.extend(get_reviews(movie_code, n))

    return reviews
