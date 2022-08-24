from some_module import Car, Driver
from unittest import TestCase, main


class CarTest(TestCase):
	def setUp(self) -> None:
		self.new_car = Car("r2d2", 500, Driver("Андройд"))

	def test_init(self):
		self.assertEqual(isinstance(self.new_car, Car), True)
		self.assertEqual(self.new_car.model, "r2d2")
		self.assertEqual(self.new_car.max_weight, 500)
		self.assertEqual(self.new_car.driver.name, "Андройд")
		self.assertEqual(self.new_car.weight_goods, 0)

	def test_take_goods(self):
		self.new_car.take_goods()
		self.assertEqual(self.new_car.weight_goods, 5)
		self.new_car.take_goods(10)
		self.assertEqual(self.new_car.weight_goods, 15)

	def test_unload(self):

		self.new_car.take_goods(self.new_car.max_weight)
		self.assertEqual(self.new_car.weight_goods, 500)
		self.new_car.unload()
		self.assertEqual(self.new_car.weight_goods, 0)

if __name__ == "__maim__":
	main()
