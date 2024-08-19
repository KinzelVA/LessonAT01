import unittest
from main import modulo


class TestModuloFunction(unittest.TestCase):

    def test_positive_division(self):
        """Тест: Остаток от деления положительных чисел."""
        self.assertEqual(modulo(10, 3), 1)

    def test_division_by_one(self):
        """Тест: Остаток от деления на 1."""
        self.assertEqual(modulo(10, 1), 0)

    def test_division_by_self(self):
        """Тест: Остаток от деления числа на себя."""
        self.assertEqual(modulo(7, 7), 0)

    def test_zero_dividend(self):
        """Тест: Остаток от деления нуля на любое число."""
        self.assertEqual(modulo(0, 5), 0)

    def test_negative_dividend(self):
        """Тест: Остаток от деления отрицательного числа на положительное."""
        self.assertEqual(modulo(-10, 3), 2)

    def test_negative_divisor(self):
        """Тест: Остаток от деления положительного числа на отрицательное."""
        self.assertEqual(modulo(10, -3), -2)

    def test_negative_dividend_and_divisor(self):
        """Тест: Остаток от деления отрицательного числа на отрицательное."""
        self.assertEqual(modulo(-10, -3), -1)

    def test_division_by_zero(self):
        """Тест: Проверка деления на ноль."""
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
