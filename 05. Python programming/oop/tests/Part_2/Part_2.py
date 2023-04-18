import re
import pytest

@pytest.fixture(autouse=True)
def test_part2_import():
    try:
        from src.Part_2 import Computer,Laptop,oop_explain
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part2_Laptop():
    from src.Part_2 import Computer,Laptop

    cpu = 'cpu_10'
    ram = 'ram_9'
    battery = 'battery_100'

    laptop = Laptop(cpu, ram, battery)
    assert laptop.CPU == 'cpu_10', \
        'Laptop 클래스는 cpu 속성이 있어야합니다.'

    assert laptop.RAM == 'ram_9', \
        'Laptop 클래스는 ram 속성이 있어야합니다.'

    assert laptop.battery == 'battery_100', \
        'Laptop 클래스는 battery 속성이 있어야합니다.'

    assert isinstance(laptop, Computer), \
        'Laptop은 Computer로부터 상속을 받아야합니다.'
    

def test_part2_oop_explain():
    from src.Part_2 import oop_explain

    assert len(oop_explain()) > 1, \
        'oop에 대해서 공부한 내용들을 작성해주세요'

    assert '캡슐화' in oop_explain(), \
        '캡슐화에 대해서 작성해주세요'

    assert '상속' in oop_explain(), \
        '상속에 대해서 작성해주세요'

    assert '추상화' in oop_explain(), \
        '추상화에 대해서 작성해주세요'

    assert '다형성' in oop_explain(), \
        '다형성에 대해서 작성해주세요'