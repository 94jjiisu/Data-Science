import re
import pytest

@pytest.fixture(autouse=True)
def test_part3_import():
    try:
        from src.Part_3 import Person, Book, Librarian,User
    except :
        pytest.fail('코드에서 에러가 발생했습니다. 다시 한번 확인해주세요')


def test_part3_inheritance():
    from src.Part_3 import Person, Librarian, User

    assert Person in Librarian.mro(), 'Librarian이 Person으로부터 상속을 받아야합니다'
    assert Person in User.mro(), 'User는 Person으로부터 상속을 받아야합니다'


def test_part3_introduce():
    from src.Part_3 import Librarian,User

    lisa = Librarian('lisa', 25)
    mark = User('mark', 14)

    assert 'introduce' in dir(lisa), 'Librarian이 Person으로부터 상속을 받았으면 introduce 함수를 실행할 수 있어야합니댜'
    assert 'introduce' in dir(mark), 'User가 Person으로부터 상속을 받았으면 introduce 함수를 실행할 수 있어야합니댜'


def test_part3_librarian():
    from src.Part_3 import Librarian

    lisa = Librarian('lisa', 25)

    assert lisa.name == 'lisa', 'lisa에게는 이름이 있어야합니다.'
    assert lisa.age == 25, 'lisa는 25살 입니다.'
    try:
        print(lisa.__book_list)
    except:
        assert True
    else:
        assert False, 'lisa의 책 리스트는 외부에서 접근할 수 없습니다'


def test_part3_user():
    from src.Part_3 import User

    mark = User('mark', 14)

    assert mark.name == 'mark', 'mark에게는 이름이 있어야합니다.'
    assert mark.age == 14, 'mark는 14살 입니다.'
    try:
        print(mark.__borrowed_list)
    except:
        assert True
    else:
        assert False, 'mark의 책 리스트는 외부에서 접근할 수 없습니다'


def test_part3_book():
    from src.Part_3 import Book, Librarian
    try:
        lisa = Librarian('lisa', 25)
        bible = Book('bible', lisa)
    except:
        assert False, '책이 정상적으로 생성되지 않습니다'

    assert bible.name == 'bible', '책에는 책 이름이 있어야합니다'
    assert bible.librarian == lisa, '책에는 책 주인의 이름이 있어야합니다'


def test_part3_book_react():
    from src.Part_3 import Book, Librarian,User

    lisa = Librarian('lisa', 25)
    mark = User('mark', 14)

    bible = Book('bible', lisa)
    python = Book('python', lisa)
    cpp = Book('cpp', lisa)
    java = Book('java', lisa)
    typescript = Book('typescript', lisa)

    lisa.add_book(bible)
    lisa.add_book(python)
    lisa.add_book(cpp)
    lisa.add_book(java)
    lisa.add_book(typescript)

    if lisa.remove_book(cpp):
        mark.borrow_book(cpp)
        assert True
    else:
        assert False, '대출 기능이 정상적으로 작동해야합니다'
    
    assert cpp not in lisa.get_book_list(), 'lisa가 빌려준 책은 lisa한테 있으면 안됩니다'
    assert cpp in mark.get_borrowed_list(), 'mark가 빌려온 책은 mark한테 있어야합니다'

    if mark.return_book(cpp):
        lisa.add_book(cpp)
        print(cpp in lisa.get_book_list())
    else:
        assert False, '반납 기능이 정상적으로 작동해야합니다'

    assert cpp in lisa.get_book_list(), '반납된 책은 lisa에게 있어야합니다'
    assert cpp not in mark.get_borrowed_list(), 'mark가 반납하면 그 책은 mark에게 있어서는 안됩니다'