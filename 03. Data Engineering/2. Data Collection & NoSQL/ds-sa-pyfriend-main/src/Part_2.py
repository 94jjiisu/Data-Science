"""
문제 목록

1. 파이썬 클래스
2. 파이썬 클래스 속성
3. 파이썬 상속
4. 파이썬 예외처리

- "빈칸을 채워주세요" 는 지우고 테스트가 통과할 수 있도록 알맞은 코드를 입력해야 합니다.
- "예외 클래스를 넣어주세요" 로 시작하는 경우에는 
    파이썬 Exception 클래스 중에서 알맞은 클래스를 입력해 채워주셔야 합니다.
"""

from unittest import TestCase

"""
1. 파이썬 클래스
"""


class PythonClasses(TestCase):
    """
    파이썬 클래스에 대해서 알아보겠습니다. 클래스와 인스턴스 등 다양한 용어들에
    대해서도 반드시 찾아보세요!

    클래스를 어떻게 정의하고, 정의된 클래스를 통해 어떻게 객체를 생성하고
    활용할 수 있는지 살펴보겠습니다.
    """
    class Car:
        "There are many different cars"

    def test_about_instance_creation(self):
        """
        `new_car` 는 클래스의 인스턴스입니다.

        이렇게 생성된 인스턴스에는 기본으로 몇가지 속성들이 생겨납니다.
        이 중에서 `__name__` 어떤 속성인지 알아보세요
        
        # NOTE: .__name__ 속성은 클래스를 문자열로 만듭니다.
        """
        new_car = self.Car()
        assert "Car" == new_car.__class__.__name__

    def test_about_class_docstrings(self):
        """
        `__doc__` 은 언제 사용이 되고 어떤 용도로 사용이 될까요?
        
        파이썬에서 사용되는 라이브러리들에서도 이런 속성이 어떻게 도움이
        될까요?

        예를 들어 pandas 라이브러리에서 생성하는 `Dataframe` 도 이러한 속성이
        있을까요?
        """
    
        assert self.Car.__doc__ == "There are many different cars"

    # ------------------------------------------------------------------

    class Car2:
        def __init__(self):
            self._name = 'BatCar'

        def set_name(self, new_name):
            self._name = new_name

    def test_about_init_constructor(self):
        """
        'underbar' 라고 불리는 밑줄 (_) 에 대해서 알아보겠습니다.

        파이썬에서는 이러한 밑줄의 의미가 어떻게 되나요?

        클래스에서는 이 밑줄을 사용하는 용도가 있습니다.
        물론 규칙처럼 정해지지는 않았지만 하나의 암묵적인 convention 입니다.
        """
        new_car = self.Car2()
        assert 'BatCar' == new_car._name

    def test_about_private_attributes(self):
        """
        _ 은 파이썬에서 private 을 뜻하지만 동작은 어떨까요?

        밑줄이 없는 코드와 다르게 작동할까요?
        """
        new_car = self.Car2()
        new_car.set_name("SuperCar")
        assert "SuperCar" == new_car._name

    def test_about_getattr_and_dict(self):
        """
        이번에는 `getattr()` 에 대해서 알아보겠습니다.

        get 과 attribute 의 줄인말인 attr 을 합친 것 같은 이 함수는 어떻게
        사용할 수 있을까요?

        또한 `setattr()`, `delattr()` 등 다른 함수들도 있습니다.

        `__dict__` 은 항상 원하는 대로 작동할까요?

        클래스에 `__dict__` 함수를 따로 만든다면 어떻게 될까요?

        이러한 특별 메소드들에 대해서도 알아봅니다.
        """
        new_car = self.Car2()
        new_car.set_name("SuperCar")

        assert "SuperCar" == getattr(new_car, "_name")
        assert "SuperCar" == new_car.__dict__["_name"]

    # ------------------------------------------------------------------

    class Car3:
        def __init__(self):
            self._name = None

        def set_name(self, a_name):
            self._name = a_name

        def get_name(self):
            return self._name

        name = property(get_name, set_name)

    def test_about_class_property(self):
        """
        클래스에 있는 속성을 접근하는 두가지 방법을 살펴보겠습니다.

        먼저 메소드로 접근해 보겠습니다. 
        "SuperCar" 속성을 접근하기 위해서는 `getattr()` 를 어떻게 활용해야 할까요?

        다음은 메소드가 아닌 속성으로 접근해보겠습니다.

        위 코드에서 Car3 클래스에서는 어떤 속성이 "SuperCar" 에 접근하게
        해주나요?

        추가로 `_name` 을 사용하지 않습니다. `_name` 은 외부에서 접근하지
        말라고 _ 이 있습니다.

        # NOTE: `property` 함수는 어떻게 동작하는 함수인가요?
        """

        new_car = self.Car3()
        new_car.set_name("SuperCar")

        assert getattr(new_car, "_name") == "SuperCar"
        assert new_car.get_name() == "SuperCar"

    # ------------------------------------------------------------------

    class Car4:
        def __init__(self):
            self._name = None

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, a_name):
            self._name = a_name

    def test_about_decorators(self):
        """
        클래스에서 `@property` 에 대해서 살펴보겠습니다.

        왜 `@property` 를 사용할까요? 그냥 변수를 직접 접근하지 않는 이유는
        외부에서 섣불리 접근했다가 내부적으로 예기치 못한 오류를 발생할 수도
        있습니다. 물론 이외에도 클래스에서만 접근해야 하는 코드를 외부에서
        접근하는 것 자체에 대한 부분도 조심해야 합니다.

        그렇다면 위 코드에서 `@name.setter` 에서 `@name` 은 어디에서
        나왔을까요?

        # NOTE: decorator 에 대해서 알아보세요. 파이썬에서는 decorator 가 '@'
        # 표시를 이용해 사용이 됩니다. 하지만 위 코드가 어떻게 작동하는지
        # 하나부터 열까지 지금 아실 필요는 없습니다. 지금은 파이썬에서
        # decorator 가 어떻게 동작하는지에만 집중을 해주세요
        """
        new_car = self.Car4()

        # 이 방법이 어떻게 작동하는 걸까요?
        new_car.name = "SuperCar"

        # new_car 의 이름을 어떻게 받아올 수 있을까요? `_name` 은 아닙니다!
        assert new_car.name == "SuperCar"

    # ------------------------------------------------------------------

    class Car5:
        def __init__(self, initial_name):
            self._name = initial_name

        @property
        def name(self):
            return self._name

    def test_about_init_and_instance(self):
        """
        파이썬의 생성자 함수와 인스턴스에 대해서 살펴보겠습니다.

        생성자 함수는 말 그대로 '생성' 해주는 함수입니다. 구체적으로는 해당
        함수를 통해 하나의 인스턴스를 생성할 수 있습니다.

        생성자 함수는 일반 함수처럼 파라미터를 받을 수 있습니다.
        `Car5` 와 같은 경우에는 `initial_name` 을 받도록 되어 있습니다.
        """
        new_car = self.Car5("SuperCar")

        # 이제는 익숙해지셨겠지만 `_name` 을 사용하지 않습니다!
        assert new_car.name == "SuperCar"

    def test_about_init_args(self):
        """
        오류에 대해서도 알아보겠습니다.

        Car5 의 생성자 함수에서 받아야 하는 값을 주지 않은 경우에는 어떤 에러가
        발생하나요?

        아래 코드에 해당 오류, 예외 클래스를 써주시면 됩니다.

        예를 들어 파이썬에서 보셨을만한 예외 클래스는 `TypeError`,
        `IndentationError` 등 다양합니다.

        아래 코드에서 `self.Car5()` 를 실행하면 어떤 에러가 발생할까요?
        """
        with self.assertRaises(TypeError):
            self.Car5()

    def test_about_instance_variables(self):
        """
        하나의 인스턴스마다 저마다의 값들을 저장해 사용할 수 있습니다.

        아래 코드에서는 두 개의 인스턴스를 생성합니다.

        서로가 영향을 줄까요?

        직접 인스턴스를 만들어보면서 실험해 보세요!
        """
        old_car = self.Car5("SuperCar")
        new_car = self.Car5("RobinCar")

        assert False is (old_car.name == new_car.name)

    # ------------------------------------------------------------------

    class Car6:
        def __init__(self, initial_name):
            self._name = initial_name

        def get_self(self):
            return self

        def __str__(self):
            #
            # 아래 테스트가 통과하도록 코드를 작성해주세요!
            #
            return "This car is " + self._name

        def __repr__(self):
            #
            # 아래 테스트가 통과하도록 코드를 작성해주세요!
            #
            return f"<Car '{self._name}'>"
    def test_about_self_reference(self):
        """
        클래스에서 `self` 라는 것에 대해서 알아보겠습니다.

        위 코드에서 `get_self()` 함수는 `self` 를 리턴합니다.

        여기에서 `self` 란 어떤 것일까요?
        """
        new_car = self.Car6("SuperCar")

        assert new_car == new_car.get_self() # string 이 아닙니다!

    def test_about_str_method(self):
        """
        `str()` 함수를 써보신 적이 있으신가요?

        문자열로 바꿔주기도 하지만 `__str__` 을 통해서 해당 함수를 덮어쓸 수
        있습니다.

        이렇게 함수를 사용하게 되면 문자열로 변경해주는 함수도 조작할 수
        있습니다.
        """
        new_car=self.Car6("SuperCar")

        # Car6 의 __str__ 를 완성해야 합니다.
        assert str(new_car) == "This car is SuperCar"
        assert new_car.__str__() == "This car is SuperCar"

    def test_about_repr_method(self):
        """
        이번에는 `__repr__` 함수에 대해서 알아보겠습니다.

        이 특별한 함수는 언제 사용이 될까요?
        또한 `__str__` 과 `__repr__` 의 차이는 뭔가요?
        """
        batcar = self.Car6("BatCar")
        supercar = self.Car6("SuperCar")

        # Car6 의 __repr__ 를 완성해야 합니다.
        assert repr(batcar) == "<Car 'BatCar'>"
        assert repr(supercar) == "<Car 'SuperCar'>"

    def test_about_objects_str_and_repr(self):
        """
        이번에는 다른 객체들의 `__str__` 과 `__repr__` 함수들에 대해서
        살펴보겠습니다.

        어떤 결과들이 등장하나요?
        """
        nums=[1, 2, 3]

        assert "[1, 2, 3]" == str(nums)
        assert "[1, 2, 3]" == repr(nums)

        assert "STRING" == str("STRING")
        assert "'STRING'" == repr("STRING")


"""
2. 파이썬 클래스 속성
"""


class PythonClassAttributes(TestCase):
    class Car:
        pass

    def test_about_objects(self):
        """
        클래스는 그렇다면 어디서부터 생성이 될까요?

        파이썬에서 object 는 어떤 클래스인가요?
        """
        new_car = self.Car()
        assert True is isinstance(new_car, object)

    def test_about_class_and_types(self):
        """
        `__class__` 는 파이썬에서 특정 객체의 클래스를 파악하기 위해 사용이
        됩니다.
        """
        assert True is (self.Car.__class__ == type)

    def test_about_class_and_objects(self):
        """
        `issubclass` 에서 subclass 란 무엇을 의미할까요?

        파이썬은 클래스에서 다른 클래스가 파생된 경우가 있을까요?
        """
        assert True is (issubclass(self.Car, object))

    def test_about_object_methods(self):
        """
        파이썬에서 `dir()` 함수는 특정 객체의 메소드들을 파악할 때 유용합니다.

        아래 코드처럼 해당 함수에 인수를 넘겨줘도 되지만 안 넘겨줘도 실행은
        됩니다.

        그냥 실행할 때에는 어떤 결과가 보이나요?
        """
        new_car=self.Car()
        assert len(new_car.__dir__()) == len(dir(new_car))

    def test_about_class_methods(self):
        assert len(self.Car().__dir__()) == len(dir(self.Car))

    def test_about_individual_object_attributes(self):
        new_car=self.Car()
        new_car.wheels=4

        assert new_car.__dict__['wheels'] == new_car.wheels

    def test_about_individual_object_functions_1(self):
        new_car=self.Car()
        new_car.drive=lambda: 'driving car'

        assert new_car.drive.__call__() == new_car.drive()

    def test_about_individual_object_functions_2(self):
        old_car = self.Car()
        new_car = self.Car()

        def drive():
            return 'driving car'
        old_car.drive = drive

        with self.assertRaises(AttributeError):
            new_car.drive()


"""
3. 파이썬 상속
"""


class PythonInheritance(TestCase):
    """
    클래스를 배우게 되면 해당 클래스에서부터 상속을 받는 클래스를 추가로 생성할
    수 있습니다.

    예를 들어 아래 코드에서는 Car 라는 클래스를 상속한 Truck 클래스가 있습니다.

    이렇게 하나의 클래스와 해당 클래스를 상속한 클래스를 두고 부모 클래스와
    자식 클래스라고 부릅니다.
    """
    class Car:
        def __init__(self, name):
            self._name = name

        @ property
        def name(self):
            return self._name

        def honk(self):
            return "beep"

    class Truck(Car):
        def honk(self):
            return "beep beep"

        def drive(self):
            return "vroom"

    def test_about_subclass_ancestors(self):
        """
        `issubclass` 함수에 대해서 더 살펴보겠습니다.

        자식 클래스는 subclass 라고도 합니다. 그리고 부모 클래스는 superclass
        라고도 하죠.
        
        이러한 관계가 있기 때문에 해당 함수로 클래스들 간에 관계를 파악할 수
        있습니다.
        """
        assert True is (issubclass(self.Truck, self.Car))

    def test_about_python3_object_class(self):
        assert True is (issubclass(self.Truck, object))

    def test_about_behavior_inheritance(self):
        new_truck = self.Truck("Optimoose")
        assert "Optimoose" == new_truck.name

    def test_about_subclass_new_behaviors(self):
        """
        subclass 에만 있는 메소드를 superclass 에서 실행하면 어떻게 될까요?

        어떤 오류가 발생하는지 확인하고 해당 예외 클래스를 적어주세요!
        """
        new_truck = self.Truck("Optimoose")
        assert getattr(new_truck, 'drive').__call__() == new_truck.drive()

        new_car = self.Car("BatCar")
        with self.assertRaises(AttributeError):
            new_car.drive()

    def test_about_subclass_behavior_modification(self):
        """
        기존에 superclass 에 정의된 메소드를 subclass 에서 다시 재정의를 하게
        되면 어떻게 될까요?

        어떤 결과가 있을지 직접 확인해보시고 테스트를 통과하세요!
        """
        new_truck = self.Truck("Optimoose")
        assert getattr(new_truck, 'honk').__call__() == new_truck.honk()

        new_car = self.Car("BatCar")
        assert getattr(new_car, 'honk').__call__() == new_car.honk()

    # ------------------------------------------------------------------

    class Racecar(Car):
        def honk(self):
            # super 는 어떻게 작동하나요?
            return super().honk() + ", BEEP!"

    def test_about_super(self):
        """
        때로는 superclass 에 있는 메소드를 사용하고 싶을 때가 있습니다.

        subclass 에서 해당 메소드를 덮어 썼더라도 불러오는 방법이 있습니다.
        """
        new_racecar = self.Racecar("F1")
        assert "beep, BEEP!" == new_racecar.honk()

    # ------------------------------------------------------------------

    class LoudCar(Car):
        def honk(self):
            return super().honk() + ", BEEP BEEP!"

    def test_super_works_across_methods(self):
        new_loudcar = self.LoudCar("TooLoud")
        assert "beep, BEEP BEEP!" == new_loudcar.honk()

    # ---------------------------------------------------------

    class CoolCar(Car):
        def __init__(self, name):
            pass

    class Coldwheels(Car):
        def __init__(self, name):
            super().__init__(name)

    def test_about_init_is_not_automatic(self):
        """
        클래스를 다룰 때 생성자 함수가 받는 파라미터 값들이 저절로 클래스
        속성으로 변하지 않습니다.

        직접 지정을 해줘야 합니다.

        위 코드에서는 `CoolCar` 이나 `Coldwheels` 클래스에서는 따로 `name` 이라는
        파라미터에 대한 조치를 하지 않고 있습니다. 이러한 상황에서 인스턴스를
        생성하게 되면 과연 `name` 에 접근할 수 있을까요?

        또한 없는 속성을 접근하게 되면 어떤 오류가 나는지 예외 클래스를
        적어주세요!
        """
        new_coolcar = self.CoolCar("Ice Car")
        with self.assertRaises(AttributeError):
            name = new_coolcar.name

    def test_about_explicit_init_call(self):
        """
        subclass 에서 `super` 함수를 호출한다고 하면 달라질까요?

        superclass 의 생성자 함수를 사용하면 문제가 사라지지 않습니다.
        """
        new_coldwheels = self.Coldwheels("Icecube")
        assert "Icecube" == new_coldwheels.name

"""
4. 파이썬 예외
"""


class PythonExceptions(TestCase):
    """
    파이썬으로 코딩을 할 때 피할 수는 있지만 피하기 어려운 것이 에러입니다.

    파이썬에서는 이들을 예외 (Exception) 이라고 부릅니다.

    이번에는 파이썬의 예외 처리는 어떻게 하고 어떤 예외들이 있는지 등
    보겠습니다.
    """

    class CustomError(RuntimeError):
        pass

    def test_about_exception_inheritance(self):
        """
        여기에서 나오는 `mro` 에 대해서는 자세히 아실 필요는 없습니다.

        다만 해당 테스트를 통과하면서 어떤 것들이 나오는지 살펴보시면 될 것
        같습니다.

        직접 파이썬으로 확인해 보시면서 테스트를 통과해주세요
        """
        mro = self.CustomError.mro()
        assert "RuntimeError" == mro[1].__name__
        assert "Exception" == mro[2].__name__
        assert "BaseException" == mro[3].__name__

    def test_about_try_clause(self):
        """
        try... except 는 파이썬에서 예외처리할 때 사용되는 매우 중요한 기능 중
        하나입니다.

        에러를 항상 피하고 은밀하는 것이 반드시 좋지는 않습니다.

        어떤 에러가 발생했는지에 따라 해결책이 달라지고 어떻게 코드를 진행해야
        하는지 알려줄 수 있기도 합니다.

        앞으로 여러분도 에러 핸들링을 하실 때 try... except 를 사용하려면
        충분히 다룰 수 있는 연습이 필요합니다.
        """
        result=None

        try:
            self.fail("Oops")
        except Exception as e:
            result='exception handled'

            e2=e

        assert "exception handled" == result

        assert True is isinstance(e2, Exception)
        assert False is isinstance(e2, RuntimeError)

        assert True is issubclass(RuntimeError, Exception)

    def test_about_raising_specific_error(self):
        """
        에러가 먼저 발생하는 경우도 있지만 어느 경우에는 코드에서 에러를
        발생시키는 경우도 존재합니다.

        그렇다면 이러한 에러, 예외를 발생하기 위한 `raise` 에 대해서
        살펴보겠습니다.
        """
        result=None

        try:
            raise self.CustomError("Custom Message")
        except self.CustomError as e:
            result='exception handling'
            msg=e.args[0]

        assert "exception handling" == result
        assert "Custom Message" == msg

    def test_about_else_clause(self):
        """
        try... except 는 사실 if 조건문처럼 else 라는 구문도 있습니다.

        즉, try... except... else 도 실행할 수가 있죠.

        마치 if... elif... else 와도 비슷합니다.
        """
        result=None
        try:
            pass
        except RuntimeError:
            result='exception clause'
            pass
        else:
            result='else clause'

        assert "else clause" == result

    def test_about_finally_clause(self):
        """
        finally 는 else 와는 또 다릅니다.
        
        최종적으로 실행이 되기 때문이죠. 즉, 어떠한 경우에도 실행이 되는 코드를
        담을 수 있는 곳입니다.
        """
        result=None
        try:
            result = 'new result'
            self.fail("Oops")
        except:
            result = 'other result'
            pass
        finally:
            result='always run'

        assert "always run" == result
