def comp_q_res(base, comparison):
    for t in comparison:
        if t not in base:
            return False
    return True


class TestCustomerTable:
    """
    Customer 테이블에 대해서 테스트합니다.
    """
    __tablename__ = 'Customer'

    __fields__ = [
        ('customer_id', 'INTEGER', 1, 1),
        ('customer_name', 'VARCHAR(32)', 1, 0),
        ('customer_age', 'INTEGER', 0, 0)
    ]

    def test_table_exists(self, table_checker):
        assert len(table_checker(self.__tablename__)) == 1

    def test_fields(self, field_checker):
        assert len(field_checker(self.__tablename__)) == 3
        assert comp_q_res(self.__fields__, field_checker(
            self.__tablename__)) is True


class TestPackageTable:
    """
    Package 테이블에 대해서 테스트합니다.
    """
    __tablename__ = 'Package'

    __fields__ = [
        ('package_id', 'INTEGER', 1, 1),
        ('package_name', 'VARCHAR(32)', 1, 0),
        ('package_date', 'DATE', 0, 0)
    ]

    def test_table_exists(self, table_checker):
        assert len(table_checker('Package')) == 1

    def test_fields(self, field_checker):
        assert len(field_checker(self.__tablename__)) == 3
        assert comp_q_res(self.__fields__, field_checker(
            self.__tablename__)) is True


class TestJoinTable:
    """
    Customer 와 Package 조인 테이블에 대해서 테스트합니다.
    """

    __tablename__ = 'Customer_Package'

    __fields__ = [
        ('cp_id', 'INTEGER', 1, 1),
        ('customer_id', 'INTEGER', 0, 0),
        ('package_id', 'INTEGER', 0, 0),
    ]

    def test_table_exists(self, table_checker):
        assert len(table_checker(self.__tablename__)) == 1

    def test_fields(self, field_checker):
        assert len(field_checker(self.__tablename__)) == 3
        assert comp_q_res(self.__fields__, field_checker(
            self.__tablename__)) is True
