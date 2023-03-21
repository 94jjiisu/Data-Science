import requests
from src.Part_1 import (API_KEY, get_city_data, get_weather_description,
                        get_minimum_temp)


def sample_data():
    city_name = 'Busan'
    BASE_API_URL = 'https://api.openweathermap.org/data/2.5/weather?'
    resp = requests.get(
        f"{BASE_API_URL}q={city_name}&units=metric&appid={API_KEY}")

    try:
        src_data = get_city_data(city_name)
    except Exception as e:
        print('get_city_data 함수가 정상으로 작동해야 합니다.')
        raise e

    return resp, src_data


resp, src_data = sample_data()


def test_api_key_is_valid():
    assert resp.status_code == 200


def test_get_city():
    assert resp.status_code == 200
    assert resp.json()['name'] == get_city_data('Busan')['name']


def test_get_weather_description():
    test_description = resp.json()['weather'][0]['description']

    assert test_description == get_weather_description(src_data)


def test_get_minimum_temp():
    test_temp = resp.json()['main']['temp_min']

    assert type(test_temp) == float
    assert test_temp == get_minimum_temp(src_data)
