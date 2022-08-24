# 7
# class CanFly:
# 	def __init__(self):
# 		self.__height = 0
# 		self.__speed = 0
#
# 	def set_height(self, value):
# 		self.__height = value
#
# 	def set_speed(self, value):
# 		self.__speed = value
#
# 	def get_height(self):
# 		return self.__height
#
# 	def get_speed(self):
# 		return self.__speed
#
# 	def take_off(self, *args):
# 		pass
#
# 	def fly(self, **kwargs):
# 		pass
#
# 	def to_land(self):
# 		self.set_height(0)
# 		self.set_speed(0)
#
# 	def info(self):
# 		print("Высота = {}\nСкорость = {}".format(self.get_height(), self.get_speed()))
#
#
# class ButterFly(CanFly):
# 	def __init__(self):
# 		super().__init__()
#
# 	def take_off(self, height):
# 		self.set_height(height)
#
# 	def fly(self, speed):
# 		self.set_speed(speed)
#
#
# class Rocket(CanFly):
# 	def __init__(self):
# 		super().__init__()
#
# 	def take_off(self, height, speed):
# 		self.set_height(height)
# 		self.set_speed(speed)
#
# 	def to_land(self):
# 		self.set_height(0)
# 		self.explosion()
#
# 	def explosion(self):
# 		print("Бум")
#
#
# obj1 = CanFly()
# obj1.fly()
# obj1.info()
#
# obj2 = ButterFly()
# obj2.fly(speed=2)
# obj2.info()
#
# obj3 = Rocket()
# obj3.take_off(speed=1000, height=5)
# obj3.info()

# 6
# class Unit:
# 	def __init__(self, health):
# 		self.__health = health
#
# 	def get_health(self):
# 		print("Моё здоровье = {}".format(self.__health))
# 		return self.__health
#
# 	def take_damage(self, value=0):
# 		self.__health -= 0
#
# 	def set_health(self, value):
# 		self.__health -= value
#
#
# class Solder(Unit):
# 	def __init__(self, health):
# 		super().__init__(health)
#
# 	def take_damage(self, value=0):
# 		self.set_health(value)
#
#
# class Civil(Unit):
# 	def __init__(self, health):
# 		super().__init__(health)
#
# 	def take_damage(self, value=0):
# 		self.set_health(value * 2)
#
#
# men = Unit(100)
# men.take_damage(50)
# men.get_health()
#
# men = Solder(100)
# men.take_damage(50)
# men.get_health()
#
# men = Civil(100)
# men.take_damage(50)
# men.get_health()

# 5
# import os
#
#
# class MyException(Exception):
# 	pass
#
#
# name = "Numbers for error.txt"
# path = os.path.join(os.path.abspath(os.sep), "Users", "мвидео", "Desktop", "Папка для тестов", name)
#
# with open(path, 'r', encoding='utf-8') as file:
# 	for line in file:
# 		x, y = [int(num) for num in line.split()]
# 		try:
# 			if x > y:
# 				raise MyException("По выдуманному условию X должен быть меньше Y")
# 			else:
# 				value = x / y
# 				print(value)
# 		except MyException as er:
# 			print(er)
# 			continue






# 4
# class Robot:
# 	def __init__(self, number):
# 		self.__number = number
#
# 	def operate(self):
# 		print("Робот № {} что-то делает".format(self.__number))
#
# 	def get_number(self):
# 		return self.__number
#
#
# class Vacuum(Robot):
# 	def __init__(self, number):
# 		super().__init__(number)
# 		self.__rubbish_bag = 1
#
# 	def operate(self):
# 		print("Робот-пылесос № {} пылесосит".format(self.get_number()))
# 		self.__rubbish_bag += 1
# 		print("Текущий уровень заполняемость: {}".format(self.__rubbish_bag))
#
#
# class Warrior(Robot):
# 	def __init__(self, number):
# 		super().__init__(number)
# 		self.__gun = "Вилка на палке"
#
# 	def operate(self):
# 		print("Робот-воин № {} атакует с помощью оружия {}".format(self.get_number(), self.__gun))
#
# 	def get_gun(self):
# 		return self.__gun
#
#
# class Submarine(Warrior):
# 	def __init__(self, number):
# 		super().__init__(number)
# 		self.__depth = 10000
#
# 	def operate(self):
# 		print("Робот-воин № {} атакует с помощью оружия {} атлантов".format(self.get_number(), self.get_gun()))
#
#
# r1 = Robot("123")
# r2 = Vacuum("321")
# r3 = Warrior("312")
# r4 = Submarine("666")
#
# r1.operate()
# r2.operate()
# r3.operate()
# r4.operate()


# 3
# class Ship:
# 	def __init__(self, model):
# 		self.__model = None
# 		self.set_model(model)
#
# 	def set_model(self, value):
# 		self.__model = value
#
# 	def get_model(self):
# 		print("Корабль {}".format(self.__model))
# 		return self.__model
#
# 	def move(self):
# 		print("Иду по воде ведь я {}".format(self.get_model()))
#
#
# class WarShio(Ship):
# 	def __init__(self, model, gun):
# 		super().__init__(model)
# 		self.__gun = None
# 		self.set_gun(gun)
#
# 	def set_gun(self, value):
# 		self.__gun = value
#
# 	def get_gun(self):
# 		return self.__gun
#
# 	def	attack(self):
# 		print("{} атакует {}".format(self.get_model(), self.get_gun()))
#
#
# class TradeShip(Ship):
# 	def __init__(self, model):
# 		super().__init__(model)
# 		self.__workload = 0
#
# 	def load(self):
# 		self.__workload += 1
#
# 	def unload(self):
# 		self.__workload -= 1
#
# 	def get_workload(self):
# 		print("{} имеет загруженность {}".format(self.get_model(), self.__workload))
# 		return self.__workload
#
#
#
# ws = WarShio("Черная жемчужина", "Залпом зубочисток")
# ws.attack()
# th = TradeShip("Продажная шлюха")
# th.load()
# th.load()
# th.get_workload()
# th.unload()
# th.get_workload()
# th.move()

# 2
# class People:
# 	__count = 0
#
# 	def __init__(self, name=None, age=None):
# 		People.__count += 1
# 		self.__name = None
# 		self.__age = None
# 		self.set_name(name)
# 		self.set_age(age)
#
# 	def __str__(self):
# 		return "Челок по имени {} ему {} лет".format(self.get_name(), self.get_age())
#
# 	def set_name(self, value):
# 		if value.isalpha():
# 			self.__name = value
# 		else:
# 			raise TypeError("Name должно быть str")
#
# 	def set_age(self, value):
# 		if 0 <= value <= 100:
# 			self.__age = value
# 		else:
# 			raise ValueError("Age должно быть в диапазоне на 0 до 100")
#
# 	def get_name(self):
# 		return self.__name
#
# 	def get_age(self):
# 		return self.__age
#
# 	def get_count(self):
# 		return People.__count
#
#
# men = People("Саша", 25)
# print(men)
# print(men.get_count())

# # 1
# class Point:
# 	def __init__(self, x=0, y=0):
# 		self.set_x(x)
# 		self.set_y(y)
#
# 	def __str__(self):
# 		return "Координаты точки ({}, {})".format(self.get_x(), self.get_y())
#
# 	def set_x(self, value):
# 		if isinstance(value, int):
# 			self.__x = value
# 		else:
# 			raise Exception("X должен быть целым числом")
#
# 	def set_y(self, value):
# 		if isinstance(value, int):
# 			self.__y = value
# 		else:
# 			raise Exception("Y должен быть целым числом")
#
# 	def get_x(self):
# 		return self.__x
#
# 	def get_y(self):
# 		return self.__y
#
#
# point = Point(2, 17)
# print(point)
