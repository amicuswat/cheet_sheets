from unittest import TestCase

from find_square_roots import find_square_roots


class SquareRootTest(TestCase):
    """
        ax^2 + bx + c = 0
        три коэф: a, b, c
        Решения:
            x1 <> x2
            x1 == x2
            корней нет

        def find_square_root(a: float, b: float, c: float) -> Tuple(Optional(flaot), Optional(float)):
            pass
    """

    def test_1(self):
        """
            x^2 - 4 = 0
            x1 = -2
            x2 = 2
        :return:
        """

        result = find_square_roots(1.0, 0.0, -4.0)

        self.assertEqual(
            (-2, 2),
            result
        )

    def test_2(self):
        """
            x^2 - 9 = 0
            x1 = -3
            x2 = 3
        :return:
        """

        result = find_square_roots(1.0, 0.0, -9.0)

        self.assertEqual(
            (-3, 3),
            result
        )

    def test_no_roots(self):
        result = find_square_roots(1.0, 1.0, 1.0)
        self.assertEqual(
            (None, None),
            result
        )

    def test_one_root(self):
        result = find_square_roots(1.0, -6.0, 9.0)
        self.assertEqual(
            (3, None),
            result
        )