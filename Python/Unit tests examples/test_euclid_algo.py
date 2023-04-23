from unittest import TestCase

from euclid_algorithm import get_nod

class EuclidAlgorithmTest(TestCase):
    """
    Если а != b вычитаем из большего, меньшее
    a = 18, b = 24
    b = b - a = 6
    a = a - b = 12
    a = a - b = 6
    a = b - результат 6

    """

    def test_1(self):
        """
        a = 18, b = 24
        result = 6
        :return:
        """
        result = get_nod(18, 24)

        self.assertEqual(
            6,
            result
        )

    def test_equal_nums(self):
        """
        а = 6, b = 6
        result = 6
        :return:
        """

        result = get_nod(6, 6)

        self.assertEqual(
            6,
            result
        )
