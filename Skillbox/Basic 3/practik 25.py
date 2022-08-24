# 6


# 5 - н
# class Car:
# 	def __init__(self, x=0, y=0, coal=90):
# 		self.x = None
# 		self.y = None
# 		self.coal = None
# 		self.set_x_and_y(x, y)
# 		self.set_coal(coal)
#
# 	def set_x_and_y(self, x, y):
# 		if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float):
# 			self.x = x
# 			self.y = y
# 		else:
# 			raise TypeError("x, y должны быть числовыми")
#
# 	def set_coal(self, coal):
# 		if isinstance(coal, int):
# 			if coal == 0 or coal == 90 or coal == 180 or coal == 270:
# 				self.coal = coal
# 			else:
# 				raise ValueError("Значение coal должно быть 0, 90, 180 или 270")
# 		else:
# 			raise TypeError("Некорректный тип данных для coal")
#
# 	def get_data(self):
# 		return self.x, self.y, self.coal
#
# 	def move(self, value):
# 		x, y, coal = self.get_data()
# 		if self.coal == 0:
# 			self.set_x_and_y(x + value, y)
# 		elif self.coal == 90:
# 			self.set_x_and_y(x, y + value)
# 		elif self.coal == 180:
# 			self.set_x_and_y(x - value, y)
# 		elif self.coal == 270:
# 			self.set_x_and_y(x, y - value)
#
#
# class Bus(Car):
# 	def __init__(self, x=0, y=0, coal=90):
# 		super().__init__(x, y, coal)
# 		self.count_passenger = 0
# 		self.money = 0
#
# 	def input(self, count=1):
# 		self.count_passenger += count
#
# 	def output(self, count=1):
# 		if count > self.count_passenger:
# 			raise ValueError("Пассажиров не может выйти больше, чем есть")
# 		else:
# 			self.count_passenger -= count
#
# 	def move(self, value):
# 		x, y, coal = self.get_data()
# 		self.money += self.count_passenger * 1 * value
# 		if self.coal == 0:
# 			self.set_x_and_y(x + value, y)
# 		elif self.coal == 90:
# 			self.set_x_and_y(x, y + value)
# 		elif self.coal == 180:
# 			self.set_x_and_y(x - value, y)
# 		elif self.coal == 270:
# 			self.set_x_and_y(x, y - value)
#
# 	def get_money(self):
# 		return self.money
#
#
#
#
# car = Car()
# print(car.get_data())
# car.move(10)
# print(car.get_data())
#
# car2 = Bus()
# print(car2.get_data())
#
# car2.input(1)
# car2.move(10)
# print(car2.get_data())
# print(car2.get_money())

# 4
# class Person:
# 	"""
# 	Главный класс родитель
# 	:param name, surname, age
# 	"""
# 	def __init__(self, name=None, surname=None, age=0):
# 		self.__name = None
# 		self.__surname = None
# 		self.__age = None
# 		self.set_name(name)
# 		self.set_surname(surname)
# 		self.set_age(age)
#
# 	def set_name(self, value):
# 		if value.isalpha():
# 			self.__name = value
# 		else:
# 			raise TypeError("Name должно состоять из букв")
#
# 	def set_surname(self, value):
# 		if value.isalpha():
# 			self.__surname = value
# 		else:
# 			raise TypeError("Surname должно состоять из букв")
#
# 	def set_age(self, value):
# 		if 0 <= value <= 100:
# 			self.__age = value
# 		else:
# 			raise ValueError("Age должно быть от 0 до 100")
#
# 	def get_name(self):
# 		return self.__name
#
# 	def get_surname(self):
# 		return self.__surname
#
# 	def get_age(self):
# 		return self.__age
#
#
# class Employee(Person):
# 	"""Инициализация работника ни чем не отличается от родителя"""
# 	def __init__(self, name, surname, age):
# 		super().__init__(name, surname, age)
# 		self.__salary = None
#
# 	def set_salary(self, value):
# 		if isinstance(value, int) or isinstance(value, float):
# 			if value >= 0:
# 				self.__salary = value
# 			else:
# 				raise TypeError("Значение salary должно быть положительным числом")
# 		else:
# 			raise TypeError("Значение salary должно быть положительным числом")
#
# 	def get_salary(self):
# 		return self.__salary
#
# 	def payroll_preparation(self):
# 		"""Метод будет определен для каждого потомка свой"""
# 		pass
#
#
# class Manager(Employee):
# 	def __init__(self, name, surname, age):
# 		super().__init__(name, surname, age)
#
# 	def payroll_preparation(self):
# 		self.set_salary(13000)
#
#
# class Agent(Employee):
# 	def __init__(self, name, surname, age, total_sales=0):
# 		super().__init__(name, surname, age)
# 		self.__total_sales = None
# 		self.set_total_sales(total_sales)
#
# 	def set_total_sales(self, value):
# 		if isinstance(value, int) or isinstance(value, float):
# 			if value >= 0:
# 				self.__total_sales = value
# 			else:
# 				raise TypeError("Значение total_sales должно быть положительным числом")
# 		else:
# 			raise TypeError("Значение total_sales должно быть положительным числом")
#
# 	def get_total_sales(self):
# 		return self.__total_sales
#
# 	def payroll_preparation(self):
# 		self.set_salary(5000 + 0.05 * self.get_total_sales())
#
#
# class Worker(Employee):
# 	def __init__(self, name, surname, age, total_hours=0):
# 		super().__init__(name, surname, age)
# 		self.__total_hours = None
# 		self.set_total_hours(total_hours)
#
# 	def set_total_hours(self, value):
# 		if isinstance(value, int) or isinstance(value, float):
# 			if value >= 0:
# 				self.__total_hours = value
# 			else:
# 				raise TypeError("Значение total_hours должно быть положительным числом")
# 		else:
# 			raise TypeError("Значение total_hours должно быть положительным числом")
#
# 	def get_total_hours(self):
# 		return self.__total_hours
#
# 	def payroll_preparation(self):
# 		self.set_salary(100 * self.get_total_hours())
#
#
# m1 = Manager("Саша", "Васильев", 27)
# m2 = Manager("Коля", "Попов", 35)
# m3 = Manager("Ваня", "Ковалевский", 76)
# a1 = Agent("Эля", "Васильева", 27, 100000)
# a2 = Agent("Оля", "Геращенко", 25, 200000)
# a3 = Agent("Яна", "Телух", 29, 50000)
# w1 = Worker("Олег", "Краснов", 45, 144)
# w2 = Worker("Мария", "Ворфаломеева", 36, 166)
# w3 = Worker("Игорь", "Завьялов", 56, 122)
#
# list_worker = [m1, m2, m3, a1, a2, a3, w1, w2, w3]
#
# for men in list_worker:
# 	men.payroll_preparation()
# 	print("Сотрудник {} {} заработал {} рублей".format(men.get_surname() ,men.get_name(), men.get_salary()))




# 3
# все уже продумано.
# my_dict = dict()
# value = my_dict.get("Тест", 0)
# print("Значение Value по умолчанию = {}".format(value))

# 2
# import random
# import os
#
#
# class KillError(Exception):
# 	pass
#
#
# class DrunkError(Exception):
# 	pass
#
#
# class CarCrashError(Exception):
# 	pass
#
#
# class GluttonyError(Exception):
# 	pass
#
#
# class DepressionError(Exception):
# 	pass
#
#
# def one_day(value):
# 	"""
# 	Прибавляем к значению случайное число от 1 до 7 или случается одна из ошибок
# 	:return увеличенное число
# 	"""
# 	ran1 = random.randint(1, 10)
# 	if ran1 == 10:
# 		list_errors = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
# 		random_num = random.randint(0,4)
# 		raise list_errors[random_num](list_errors[random_num])
# 	else:
# 		value += random.randint(1, 7)
# 		return value
#
#
# path = os.path.join(os.path.abspath(os.sep), "Users", "мвидео", "Desktop", "Папка для тестов", "new_log_err.log")
# win_score = 500
# my_score = 0
# day = 1
# while my_score < win_score:
# 	print("Начался {}-й день. Моя карма = {}".format(day, my_score))
# 	try:
# 		my_score = one_day(my_score)
# 	except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
# 		with open(path, 'a', encoding='utf-8') as file:
# 			file.write("В {}-ый день случилась ошибка: {}\n".format(day, error))
# 	finally:
# 		day += 1
#
# print("Просветились")

# 1
# class Property:
# 	"""
# 	Базовый класс для имущества
# 	:param
# 	__price - это стоимость имущества
# 	__money - количество денег у родителя
# 	"""
# 	def __init__(self, price):
# 		self.__price = None
# 		self.set_price(price)
#
# 	def set_price(self, value):
# 		"""Задаем значение стоимости для объекта подлежащего налогообложению"""
# 		self.__price = value
#
# 	def get_price(self):
# 		"""Получаем значение стоимости объекта налогообложения"""
# 		return self.__price
#
# 	def tax(self):
# 		""" Расчет суммы налога, у каждого потомка полиморфизм"""
# 		pass
#
#
# class Apartment(Property):
# 	""" Недвижимость """
# 	def __init__(self, price):
# 		super().__init__(price)
#
# 	def tax(self):
# 		""" Для недвижимости налоговая ставка 1/1000 от суммы объекта"""
# 		print("Сумма налога на недвижимость = {}".format(self.get_price() / 1000))
# 		return self.get_price() / 1000
#
#
# class Car(Property):
# 	""" Движимость """
# 	def __init__(self, price):
# 		super().__init__(price)
#
# 	def tax(self):
# 		""" Для недвижимости налоговая ставка 1/200 от суммы объекта"""
# 		print("Сумма налога на недвижимость = {}".format(self.get_price() / 200))
# 		return self.get_price() / 200
#
#
# class CountryHouse(Property):
# 	""" Недвижимость за чертой города """
# 	def __init__(self, price):
# 		super().__init__(price)
#
# 	def tax(self):
# 		""" Для недвижимости налоговая ставка 1/500 от суммы объекта"""
# 		print("Сумма налога на недвижимость = {}".format(self.get_price() / 500))
# 		return self.get_price() / 500
#
#
# class People:
# 	"""
# 	Класс налогоплательщик у него есть:
# 	__name - Имя
# 	__money - Деньги
# 	__list_property - Список имущества который не используется пока что
# 	"""
# 	def __init__(self, name, money):
# 		self.__name = None
# 		self.__money = None
# 		self.__list_property = dict()
# 		self.set_name(name)
# 		self.set_money(money)
#
# 	def set_name(self, value):
# 		""" Задает  __name только из букв"""
# 		if value.isalpha():
# 			self.__name = value
# 		else:
# 			raise TypeError("Некорректный Name")
#
# 	def set_money(self, value):
# 		""" Задает __money только из чисел"""
# 		if isinstance(value, int) or isinstance(value, float):
# 			self.__money = value
# 		else:
# 			raise TypeError("Некорректный Money")
#
# 	def get_name(self):
# 		"""Получаем __name"""
# 		return self.__name
#
# 	def get_money(self):
# 		"""Получаем количество __money"""
# 		return self.__money
#
# 	def add_money(self, value):
# 		""" Изменяем количество __money  на величину value"""
# 		if isinstance(value, int) or isinstance(value, float):
# 			self.__money += value
# 		else:
# 			raise TypeError("Некорректный Value")
#
# 	def add_property(self, type_property, price_property):
# 		"""
# 		Добавляем имущество
# 		:param type_property:  1 = недвижимость, 2 = движимость, 3 = недвижимость за пределами города
# 		:param price_property: цена в рублях
# 		:return:
# 		"""
# 		if isinstance(price_property, int) or isinstance(price_property, float):
# 			if price_property > 0:
# 				if type_property == 1:
# 					my_property = Apartment(price_property)
# 					amount_tax = my_property.tax()
# 				elif type_property == 2:
# 					my_property = Car(price_property)
# 					amount_tax = my_property.tax()
# 				elif type_property == 3:
# 					my_property = CountryHouse(price_property)
# 					amount_tax = my_property.tax()
# 				else:
# 					raise ValueError("type_property должен быть равен 1, 2 или 3")
#
# 				if amount_tax <= self.get_money():
# 					self.add_money(-amount_tax)
# 					print("После уплаты налога у вас осталось {} рублей".format(self.get_money()))
# 				else:
# 					print("Вам нехватает {} рублей для оплаты налога!".format(amount_tax - self.get_money()))
#
# 			else:
# 				raise TypeError("price_property не может быть отрицательным")
# 		else:
# 			raise TypeError("price_property должно быть положительным числом")
#
#
# me = People("Саша", 1000000)
# me.add_property(1, 500000)
# me.add_property(2, 500000)
# me.add_property(3, 500000)
