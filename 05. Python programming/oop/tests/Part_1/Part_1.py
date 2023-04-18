import re
import pytest

@pytest.fixture(autouse=True)
def test_part1_import():
    try:
        from src.Part_1 import CarOwner, Car, SelfDrivingCar
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part1_CarOwner():
    from src.Part_1 import CarOwner

    owner = CarOwner('kimcoding')
    assert owner.name == 'kimcoding', \
        'CarOwner 클래스는 이름(name) 속성이 있어야합니다.'

    assert owner.concentrate() == 'kimcoding can not do anything else',\
        f'CarOwner 클래스는 concentrate 메소드를 가지고 있어야하며, 자동차 주인이름에 따라 "자동차주인이름" can not do anything else를 반환해야합니다.\n현재 name이 {owner.name}일 때 {owner.concentrate()}를 반환하고 있습니다.'


def test_part1_Car():
    from src.Part_1 import CarOwner, Car

    car = Car('kimcoding')
    assert isinstance(car.owner, CarOwner), \
        'Car 클래스는 자동차 주인(owner) 속성이 있어야하며, 자동차 주인은 CarOwner로 생성되어야합니다.'

    assert car.owner.name == 'kimcoding', \
            'Car 클래스는 자동차 주인(owner) 속성이 있어야하며, 자동차 주인은 CarOwner로 생성되어야합니다. CarOwner를 한 번 확인해주세요.'

    assert car.owner.concentrate() == 'kimcoding can not do anything else',\
        'Car의 owner는 CarOwner로 선언되었기에 owner.concentrate()를 실행 할 수 있어야합니다' 

    assert car.drive() == 'kimcoding can not do anything else\nkimcoding is driving now.',\
        f"""
        car.drive 메소드가 있어야합니다.
        AS IS 
        {car.drive()}

        TO BE
        {car.owner.name} can not do anything else
        {car.owner.name} is driving now.
        """


def test_part1_SelfDrivingCar():
    from src.Part_1 import CarOwner, Car, SelfDrivingCar

    scar = SelfDrivingCar('kimcoding')
    assert isinstance(scar, Car), \
        'SelfDrivingCar는 Car로부터 상속을 받아야합니다.'

    assert scar.drive() == 'Car is driving by itself', \
        'SelfDrivingCar의 drive 메소드는 "Car is driving by itself"를 반환해야합니다.'