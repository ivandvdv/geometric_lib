import unittest

import square


class SquareTestCase(unittest.TestCase):

    # --- площадь ---

    def test_area_3(self):
        # 3 * 3 = 9
        self.assertEqual(square.area(3), 9)

    def test_area_1(self):
        self.assertEqual(square.area(1), 1)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_float(self):
        # 1.5 * 1.5 = 2.25
        self.assertAlmostEqual(square.area(1.5), 2.25)

    # --- периметр ---

    def test_perimeter_3(self):
        # 4 * 3 = 12
        self.assertEqual(square.perimeter(3), 12)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_float(self):
        # 4 * 2.5 = 10
        self.assertAlmostEqual(square.perimeter(2.5), 10)

    # --- некорректные данные ---

    def test_perimeter_negative(self):
        # сторона не может быть отрицательной, ждём ошибку
        with self.assertRaises(ValueError):
            square.perimeter(-3)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            square.area("abc")


if __name__ == "__main__":
    unittest.main()
