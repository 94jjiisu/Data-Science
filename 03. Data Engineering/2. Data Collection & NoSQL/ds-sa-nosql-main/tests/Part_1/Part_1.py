from src.Part_1 import dont_touch

def test_openweather(collection):
    """
    주어진 openweather 데이터가 몽고디비에 들어가 있는지 확인합니다.
    """
    one_weather = collection.find_one({"name":"Mountain View"})

    del one_weather['_id']
    
    assert one_weather == dont_touch
    