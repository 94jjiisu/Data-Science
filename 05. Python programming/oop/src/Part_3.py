"""
Bare Minimum Requirements
OOP에서 중요한 것은 기능별로 정확한 설계입니다.

요구사항:
    아래 작성된 내용은 전체 설명이 아니기 때문에 소스코드를 보시면서 설계를 하시길 바랍니다.

    Person(사람)
        사서 또는 이용자에 대한 기본정보를 보여준다.

    Librarian(사서)
    사서는 Person으로부터 상속을 받야야한다.
    사서에 대한 정보(변수): 이름, 나이, 관리하는 책 리스트(private)

        주요 기능
            사서는 관리하는 책 리스트에 책을 추가하는 함수를 가지고 있다.
            사서는 서적을 대출해주는 함수를 가지고 있다.
            사서가 관리하는 책의 리스트는 외부에서 접근할 수 없다.
            사서는 관리하는 책의 리스트를 반환하는 함수를 가지고 있다.

    User(이용자)
        이용자는 Person으로부터 상속을 받야야한다.
        이용자에 대한 정보(변수): 이름, 나이, 빌린 책 리스트(private)

        주요 기능
            이용자는 책을 빌리는 함수를 가지고 있다.
            이용자는 빌린 책을 반환하는 함수를 가지고 있다.
            이용자가 빌린 책의 리스트는 외부에서 접근할 수 없다.
            이용자는 빌린 책의 리스트를 반환하는 함수를 가지고 있다.

"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('안녕하세요! 제 이름은 {}, {}살 입니다!'.format(self.name, self.age))
        
        
class Book:
    def __init__(self, name, librarian):
        self.name = name
        self.librarian = librarian


class Librarian(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__book_list = []

    def add_book(self, book):   #새책을 받거나, 반납받는 함수
        ##### 소스코드를 작성해주세요 #####
        check_add = 0

        for i in self.__book_list:
            if i == book:
                print(f'정상적으로 추가되지 않았습니다.')
                return check

        self.__book_list.append(book)
        check_add = 1
        print('책이 추가되었습니다.')
        return check_add


    def remove_book(self, book):    #책을 빌려주는 함수
        ##### 소스코드를 작성해주세요 #####
        check_remove = 0

        try:
            self.__book_list.remove(book)
            check_remove = 1
        except:
            print('책을 찾을 수 없습니다.')
            return check_remove

        print('책이 목록에서 제거되었습니다.')
        return check_remove

    def get_book_list(self):    #관리중인 책 목록을 반환하는 함수
        ##### 소스코드를 작성해주세요 #####
        return self.__book_list


class User(Person):
    def __init__(self, name, age):
        ##### 소스코드를 작성해주세요 #####
        super().__init__(name, age)
        self.__book_list = []

    def borrow_book(self, book): #책을 대출하는 함수
        ##### 소스코드를 작성해주세요 #####
        check_borrow = 0

        for i in self.__book_list:
            if i == book:
                print('책을 이미 빌렸습니다.')
                return check_borrow
        
        self.__book_list.append(book)
        check_borrow = 1

        print('책을 빌렸습니다.')
        return check_borrow


    def return_book(self, book): #책을 반납하는 함수
        ##### 소스코드를 작성해주세요 #####
        check_return = 0

        try:
            self.__book_list.remove(book)
            check_return = 1
        except:
            print('책을 빌리지 않았습니다.')
            return check_return

        print('책을 반납했습니다.')
        return check_return


    def get_borrowed_list(self):    #빌린 책 목록을 반환하는 함수
        ##### 소스코드를 작성해주세요 #####
        return self.__book_list
