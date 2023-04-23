import unittest

from bubble_sort import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def test_integer(self):

        result = bubble_sort([7, 3, 5, 9])

        self.assertEqual(
            [3, 5, 7, 9],
            result
        )

    def test_float(self):

        result = bubble_sort([1.2, 3.8, 6.7, -3.9])

        self.assertEqual(
            [-3.9, 1.2, 3.8, 6.7],
            result
        )

    def test_chars(self):

        result = bubble_sort(['c', 'd', 'a', 'b'])

        self.assertEqual(
            ['a', 'b', 'c', 'd'],
            result
        )

    def test_incompatible_types(self):
        with self.assertRaises(TypeError):
            bubble_sort([1, 'fd', None])
