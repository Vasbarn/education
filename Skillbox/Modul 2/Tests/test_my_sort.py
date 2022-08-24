from my_sort import my_sort
from unittest import TestCase, main


class MySortTest(TestCase):

	def test_normal(self):
		result = my_sort([6, 8, 1, 4, 3, 9, 2, 5, 7])
		self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])

	def test_equal(self):
		result = my_sort([5, 5, 1, 2, 4])
		self.assertEqual(result, [1, 2, 4, 5])

	def test_easy(self):
		result = my_sort([1, 2, 3])
		self.assertEqual(result, [1, 2, 3])

	def test_reserved(self):
		result = my_sort([3, 2, 1])
		self.assertEqual(result, [1, 2, 3])

	def test_empty(self):
		result = my_sort([])
		self.assertEqual(result, [])

	def test_negative(self):
		result = my_sort([1, 2, -3, 4, -5, 0])
		self.assertEqual(result, [-5, -3, 0, 1, 2, 4])

	def test_only_negative(self):
		result = my_sort([-1, -2, -3])
		self.assertEqual(result, [-3, -2, -1])


if __name__ == "__main__":
	main()