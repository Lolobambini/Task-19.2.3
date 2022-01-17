# Задание 19.2.3
# Создайте новый проект с необходимыми директориями и файлами.
# Напишите по одному позитивному тесту для каждого метода
# калькулятора. Папку проекта загрузите на GitHub.
# В названии репозитория добавьте номер задания — 19.2.3.
# Ссылку на репозиторий опубликуйте в задании юнита 19.7.2.


import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiplu_calculatioon_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_pozitive(self):
        assert self.calc.division(self, 6, 3) == 2

    def test_subtraction_calculate_pozitive(self):
        assert self.calc.subtraction(self, 10, 3) == 7

    def test_adding_calculate_pozitive(self):
        assert self.calc.adding(self, 10, 3) == 13

