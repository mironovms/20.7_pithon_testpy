import pytest

from calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding_seccess(self):
        assert self.calc.adding(1, 1) == 2, 'super'

    def test_division(self):
        assert self.calc.division(4, 2) == 2


    def test_zerodivision(self):
        with pytest.raises(ZeroDivisionError):
           self.calc.division(2, 0)

    # def calc_adding(self):
    #     return self.calc.adding(2, 2)
    #     print(self.calc_adding(2, 2))




    def teardown(self):
        print("Выполнение TearDovn")



