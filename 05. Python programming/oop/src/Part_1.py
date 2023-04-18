"""
Bare Minimum Requirements

요구사항:
    아래 문제들을 확인하며 하나씩 문제를 풀어주세요.    
"""

class CarOwner:
    """
    자동차 주인을 나타내는 클래스입니다. 
    자동차 주인은 이름(name)을 가지고 있으며
    자동차 주인은 concentrate 메소드를 통해 이름 + ' can not do anything else'를 반환해야합니다. 
    """
    def __init__(self, name):
        """
        문제 1. 
            CarOwner 클래스의 생성자 메소드를 작성해주세요.
            매개변수를 수정하거나 추가하지 말아주세요.
        """
        self.name = name


    def concentrate(self):
        """
        문제 2. 
            자동차 주인 이름에 따라 
            '{자동차주인이름} can not do anything else'문구를 반환해주는 메소드를 작성해주세요.
        """
        return f'{self.name} can not do anything else'


class Car:
    """
    자동차를 나타내는 클래스입니다. 
    자동차는 주인(owner)을 가지고 있으며, 주인은 CarOwner를 통해서 생성됩니다.
    자동차는 drive 메소드를 통해 
    자동차 주인이 집중하고 있으며(concentrate), 누가 운전하고 있는지 반환해야합니다. 
    '{자동차주인이름} is driving now.'
    """
    def __init__(self, owner_name):
        """
        문제 3. 
            Car 클래스의 생성자 메소드를 작성해주세요.
            매개변수를 수정하거나 추가하지 말아주세요
        """
        self.owner = CarOwner(owner_name)


    def drive(self):
        """
        문제 4.
            자동차 주인이 집중하고 있으며, 자동차 주인이 자동차를 운전하고 있다는 내용을 반환해야합니다. 
            '{자동차주인이름} can not do anything else
            {자동차주인이름} is driving now.'

            자동차 주인이 집중하고 있다는 사실을 어떻게 하면 편하게 나타낼 수 있을까요?
            문자열에서 줄바꿈을 하고싶은 경우 '\n'을 사용해주세요.
            '\n'에 대해서 더 공부하고 싶으신 분은 '이스케이프 문자' 라고 검색해보세요
        """
        return f'{self.owner.concentrate()}\n{self.owner.name} is driving now.'


class SelfDrivingCar(Car):
    """
    문제 5. 
        이 자동차는 자율주행 자동차입니다! 
        자동차를 상속받아주세요!
    """
    def drive(self):
        """
        문제 5.
            이 자동차는 자동차 주인이 있지만... 자동차 주인이 운전하지 않고 스스로 운전하네요! 
            drive 메소드를 통해
            'Car is driving by itself'를 반환해야합니다. 
            상속을 받았는데.. drive메소드를 다시 선언해도 괜찮을까요?
            메소드 오버라이딩 개념을 다시 생각해보며 코드를 작성해주세요.
        """
        return 'Car is driving by itself'

