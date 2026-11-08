import unittest

import rectangle


class RectangleTestCase(unittest.TestCase):

    # --- площадь ---

    def test_area_2_3(self):
        # 2 * 3 = 6
        self.assertEqual(rectangle.area(2, 3), 6)

    def test_area_zero_mul(self):
        # одна сторона 0 -> площадь 0
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_square_mul(self):
        # прямоугольник 10x10 это квадрат, площадь 100
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_float(self):
        # 2.5 * 4 = 10
        self.assertAlmostEqual(rectangle.area(2.5, 4), 10)

    # --- периметр ---

    def test_perimeter_2_3(self):
        # 2 * (2 + 3) = 10
        self.assertEqual(rectangle.perimeter(2, 3), 10)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_swap(self):
        # от перестановки сторон периметр не меняется
        self.assertEqual(rectangle.perimeter(4, 7), rectangle.perimeter(7, 4))

    # --- некорректные данные ---

    def test_area_negative(self):
        # сторона не может быть отрицательной, ждём ошибку
        with self.assertRaises(ValueError):
            rectangle.area(-2, 3)

    def test_area_string(self):
        # строка вместо числа -> ошибка типа
        with self.assertRaises(TypeError):
            rectangle.area("2", 3)


if __name__ == "__main__":
    unittest.main()
