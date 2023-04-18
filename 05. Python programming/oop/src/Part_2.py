"""
Bare Minimum Requirements

요구사항:
    아래 문제들을 확인하며 하나씩 문제를 풀어주세요.    
"""

class Computer:
    """
    ## Computer 클래스의 코드는 수정하지 마세요 ##
    이미 완성된 코드입니다.
    아래 코드를 활용하여 문제를 해결해주세요.
    """
    def __init__(self, cpu, ram):
        self.CPU = cpu
        self.RAM = ram
        
    def browse(self):
        return('browse')

    def work(self):
        return('work')
        

class Laptop(Computer):
    """
    위에 작성된 Computer 클래스를 상속받는 Laptop 클래스를 완성해주세요. 
    """
    def __init__(self, cpu, ram, battery):
        """
        문제 1.
            Laptop 클래스의 생성자 함수를 완성해주세요.
            Laptop은 컴퓨터에 기본적으로 들어가는 부품 이외에 배터리도 추가됩니다.
            Computer 클래스에서 사용하는 변수에 battery를 추가해주세요.

            super키워드를 사용하여 상속받는 클래스에서 부모 클래스의 생성자를 사용하는 방법에 대해 익혀주세요.
        """
        super().__init__(cpu, ram)

        self.battery = battery



def oop_explain():
    """
    문제 2. OOP에 대해서 공부하신 내용들을 최대한 많이 작성해주세요.
    OOP의 구성에 대해서도 설명을 작성해주세요
    """

    answer = """

    OOP: 세상에 있는 실체가 있는 모든 물체, 개념을 클래스와 인스턴스, 함수, 변수라는 오브젝트로 변환시켜서 프로그램을 작성하는 것
         재사용이 가능하며 효율적으로 프로그래밍을 할 수 있도록 설계한다.
    캡슐화: 내부 속성과 함수를 하나로 묶어서 클래스로 선언하는 일반적인 개념
    상속: 하위 클래스는 상위 클래스의 모든 기능을 재사용할 수 있다.
    포함: 다른 클래스의 일부 기능만을 재사용한다.
    추상화: 복잡한 내용을 핵심적인 개념 및 기능을 요약하는 것. 일단 이름만 선언해놓고 구현은 하위 클래스에서 한다.
    다형성: 계층 구조의 상속 관계에서 상속받은 기능 외 다른 기능을 추가적으로 제공하고자 할 때 사용하는 방법.
    
    """

    return answer