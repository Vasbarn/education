# 6


# 5
# class Potatoes:
# 	count = 0
#
# 	def __init__(self, status="Росток"):
# 		"""Status может иметь четыре состояния: Росток, Зеленый, Зеленый с цветками, Зеленый с плодами """
# 		Potatoes.count += 1
# 		self.status = status
# 		self.numer = Potatoes.count
#
# 	def info(self):
# 		print("Картошка № {} в стадии {}".format(self.numer, self.status))
#
# 	def lvl_up(self):
# 		if self.status == "Росток":
# 			self.status = "Зеленый"
# 		elif self.status == "Зеленый":
# 			self.status = "Зеленый с цветками"
# 		elif self.status == "Зеленый с цветками":
# 			self.status = "Зеленый с плодами"
#
#
# class GardenBed:
#
# 	def __init__(self):
# 		self.list_plants = []
#
# 	def add_plant(self, plant):
# 		self.list_plants.append(plant)
#
# 	def lvl_up_plants(self):
# 		for elem in self.list_plants:
# 			elem.lvl_up()
#
# 	def info(self):
# 		print("Данные по выбранному саду: ")
# 		flag = True
# 		for elem in self.list_plants:
# 			elem.info()
# 			if elem.status != "Зеленый с плодами":
# 				flag = False
# 		if flag:
# 			print("Вся картошка созрела!")
# 		else:
# 			print("Нужно подождать")
# 		print()
#
#
# plant1 = Potatoes()
# plant2 = Potatoes()
# plant3 = Potatoes()
# plant4 = Potatoes()
# plant5 = Potatoes()
# list_plants = [plant1, plant2, plant3, plant4, plant5]
# my_garden = GardenBed()
# for plant in list_plants:
# 	my_garden.add_plant(plant)
# my_garden.info()
# my_garden.lvl_up_plants()
# my_garden.lvl_up_plants()
# my_garden.lvl_up_plants()
# my_garden.info()

# 4
# class Point:
# 	count = 0
#
# 	def __init__(self, x=0, y=0):
# 		Point.count += 1
# 		self.x = x
# 		self.y = y
#
# 	def info(self):
# 		print("Координата x = {}\nКоордината y = {}".format(self.x, self.y))
#
#
# new_point1 = Point()
# new_point1.info()
# new_point2 = Point(2, 2)
# new_point2.info()
# print("Всего точек:", Point.count)
# 3
# class Family:
# 	name = None
# 	money = None
# 	house = False
#
# 	def info(self):
#
# 		print(
# 			"Семья {}\n\tБюджет {:,}\n\tСтатус дома: {}".format(self.name, self.money, self.house)
# 		)
#
# 	def earn_money(self, value):
# 		self.money += value

# 	def buy_house(self):
# 		if self.money >= 1000000:
# 			print("Дом куплен.")
# 			self.earn_money(-1000000)
# 			self.house = True
# 		else:
# 			print("Денег для покупки недостаточно.")
#

# first_family = Family()
# first_family.name = "Петровы"
# first_family.money = 15000
# first_family.info()
# first_family.earn_money(1000000)
# first_family.buy_house()
# first_family.info()


# 2
# class Monitor:
# 	brand_name = "Samsung"
# 	matrix = "VA"
# 	screen_resolution = "WQHD"
# 	update_frequency = 60
#
#
# class Headphones:
# 	brand_name = "Sony"
# 	sensitivity = 108
# 	micro = True
#
#
# monitor1 = Monitor()
# monitor2 = Monitor()
# monitor2.update_frequency = 144
# monitor3 = Monitor()
# monitor3.update_frequency = 70
# monitor4 = Monitor()
#
# headphone1 = Headphones()
# headphone1.micro = False
# headphone2 = Headphones()
# headphone3 = Headphones()

# 1
# import random
#
#
# class Toyota:
# 	color_car = 'red'
# 	price_car = 1000000
# 	max_speed = 200
# 	current_speed = 0
#
# 	def info(self):
# 		print(
# 			"\tЦвет машины: {}\n\tЦена машины: {}\n\tМаксимальная скорость машины: {}\n\tТекущая скорость машины {}"
# 			.format(self.color_car, self.price_car, self.max_speed, self.current_speed))
#
# 	def pull_speed(self, value):
# 		self.current_speed = value
#
#
# car1 = Toyota()
# car1.pull_speed(66)
# car2 = Toyota()
# car2.current_speed = random.randint(0, 200)
# car3 = Toyota()
# car3.current_speed = random.randint(0, 200)
# car1.info()
