
class Driver:
	def __init__(self, name):
		self.name = name
		self.power = 100



	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		if isinstance(value, str):
			self.__name = value
		else:
			raise TypeError("Имя должно быть стройкой")

	@property
	def power(self):
		return self.__power

	@power.setter
	def power(self, value):
		self.__power = value

	def sleep(self):
		self.power += 20

	def work(self):
		self.power -= 13

	def hi(self):
		return "Привет"


class Car:
	def __init__(self, model, max_weight, driver):
		self.model = model
		self.max_weight = max_weight
		self.weight_goods = 0
		self.driver = driver

	@property
	def model(self):
		return self.__model

	@model.setter
	def model(self, value):
		self.__model = value

	@property
	def max_weight(self):
		return self.__max_weight

	@max_weight.setter
	def max_weight(self, value):
		self.__max_weight = value

	@property
	def driver(self):
		return self.__driver

	@driver.setter
	def driver(self, value):
		self.__driver = value

	@property
	def weight_goods(self):
		return self.__weight_goods

	@weight_goods.setter
	def weight_goods(self, value):
		self.__weight_goods = value

	def take_goods(self, value=5):
		if value + self.weight_goods > self.max_weight:
			print("Я не могу взять этот груз")
			return self.weight_goods
		else:
			self.weight_goods += value
			return self.weight_goods

	def unload(self):
		self.weight_goods = 0

