import unittest

import triangle


class TriangleTestCase(unittest.TestCase):

    # --- площадь (основание и высота) ---

    def test_area_4_3(self):
        # 4 * 3 / 2 = 6
        self.assertEqual(triangle.area(4, 3), 6)

    def test_area_zero_height(self):
        # высота 0 -> площадь 0
        self.assertEqual(triangle.area(5, 0), 0)

    def test_area_float(self):
        # 3 * 3 / 2 = 4.5
        self.assertAlmostEqual(triangle.area(3, 3), 4.5)

    # --- периметр (три стороны) ---

    def test_perimeter_3_4_5(self):
        # 3 + 4 + 5 = 12
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        # равносторонний: 2 + 2 + 2 = 6
        self.assertEqual(triangle.perimeter(2, 2, 2), 6)

    def test_perimeter_float(self):
        # 1.5 + 2.5 + 3 = 7
        self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3), 7)

    # --- некорректные данные ---

    def test_area_negative(self):
        # основание не может быть отрицательным, ждём ошибку
        with self.assertRaises(ValueError):
            triangle.area(-4, 3)

    def test_perimeter_impossible_triangle(self):
        # треугольника 1, 2, 10 не существует (1 + 2 < 10), ждём ошибку
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 2, 10)


if __name__ == "__main__":
    unittest.main()
