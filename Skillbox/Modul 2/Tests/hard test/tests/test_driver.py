from some_module import Driver
from unittest import TestCase, main


class DriverTest(TestCase):
	def test_init(self):
		new_elem = Driver("Петя")
		self.assertEqual(isinstance(new_elem, Driver), True)
		self.assertEqual(new_elem.name, "Петя")
		self.assertEqual(new_elem.power, 100)

	def test_sleep(self):
		new_elem = Driver("Петя")
		new_elem.sleep()
		self.assertEqual(new_elem.power, 120)

	def test_work(self):
		new_elem = Driver("Петя")
		new_elem.work()
		self.assertEqual(new_elem.power, 87)

	def test_hi(self):
		new_elem = Driver("Петя")
		self.assertEqual(new_elem.hi(), "Привет")


if __name__ == "__main__":
	main()
