import math
import unittest

import circle


class CircleTestCase(unittest.TestCase):

    # --- площадь ---

    def test_area_radius_1(self):
        # площадь круга радиуса 1 = pi
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_radius_2(self):
        # pi * 2 * 2 = 4pi = 12.566...
        self.assertAlmostEqual(circle.area(2), 12.566370614359172)

    def test_area_zero(self):
        # радиус 0 -> площадь 0
        self.assertEqual(circle.area(0), 0)

    def test_area_float(self):
        # pi * 0.5 * 0.5 = 0.785...
        self.assertAlmostEqual(circle.area(0.5), 0.7853981633974483)

    # --- длина окружности ---

    def test_perimeter_radius_1(self):
        # 2 * pi * 1 = 6.283...
        self.assertAlmostEqual(circle.perimeter(1), 6.283185307179586)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_big(self):
        # 2 * pi * 1000
        self.assertAlmostEqual(circle.perimeter(1000), 2000 * math.pi)

    # --- некорректные данные ---

    def test_area_negative_radius(self):
        # радиус не может быть отрицательным, ждём ошибку
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_area_string(self):
        # строка вместо числа -> ошибка типа
        with self.assertRaises(TypeError):
            circle.area("abc")


if __name__ == "__main__":
    unittest.main()
