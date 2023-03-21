import requests
import json

API_KEY = 'bd1dd0381d5dd72e2f2c2d50d7ddf8e4'


def get_city_data(city_name):
    """
    get_city_data 함수는 OpenWeather 에서부터 가져온 데이터를 json 형태로
    리턴해야 합니다.

    파라미터:
        - city_name: 조회할 도시 이름을 담은 문자열(str) 입니다.

    리턴:
        - 파이썬 딕셔너리: 조회한 API JSON 데이터를 파이썬 딕셔너리 형태로
        리턴합니다.
    """
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    raw_data = requests.get(link)


    current_weather = json.loads(raw_data.text)
    
    return current_weather




def get_weather_description(json_data):
    """
    get_weather_description 함수는 weather description, 날씨가 어떤지 알려주는 문자열을 리턴합니다.

    파라미터:
        - json_data: OpenWeather API 로부터 받아온 JSON 데이터입니다.

    리턴:
        - 날씨 정보: 주어진 데이터에서 날씨에 대해서 담고 있는 문자열(str) 을
        리턴합니다.
    """

    weather_description = json_data["weather"][0]["description"]

    return weather_description


def get_minimum_temp(json_data):
    """
    get_minimum_temp 함수는 최저 온도를 섭씨(℃) 단위로 리턴해야 합니다.

    파라미터:
        - json_data: OpenWeather API 로부터 받아온 JSON 데이터입니다.

    리턴:
        - 온도 정보: 주어진 JSON 데이터에서 숫자(int) 인 온도 정보를 리턴합니다.
    """

    temp_min = json_data["main"]["temp_min"]


    return temp_min
