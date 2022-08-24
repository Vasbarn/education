# 9 Крестики нолики
# class Cells:
# 	def __init__(self):
# 		self.value = None
#
# 	def set_value(self, value):
# 		self.value = value
#
# 	def get_value(self):
# 		return self.value
#
#
# class Board:
# 	def __init__(self):
# 		self.table = None
# 		self.size_x = 3
# 		self.size_y = 3
# 		self.set_table()
#
# 	def set_table(self):
# 		self.table = []
# 		for x in range(self.size_x):
# 			col = []
# 			for y in range(self.size_y):
# 				col.append(Cells())
# 			self.table.append(col)
# 		return self.table
#
# 	def info(self):
# 		for x in self.table:
# 			for y in x:
# 				if isinstance(y, Cells):
# 					print(y.get_value(), end="\t")
# 				else:
# 					print(y, end="\t\t")
# 			print()
# 		print()
#
# 	def check(self):
# 		for num_x in range(len(self.table)):
# 			if self.table[num_x][0] == self.table[num_x][1] == self.table[num_x][2]:
# 				print("Победил {}".format(self.table[num_x][0]))
# 			if self.table[0][num_x] == self.table[1][num_x] == self.table[2][num_x]:
# 				print("Победил {}".format(self.table[0][num_x].get_value))
# 		if self.table[0][0] == self.table[1][1] == self.table[2][2]:
# 			print("Победил {}".format(self.table[1][1].get_value))
# 		if self.table[0][2] == self.table[1][1] == self.table[2][0]:
# 			print("Победил {}".format(self.table[1][1].get_value))
#
#
#
# class Player:
# 	def __init__(self, name, mark):
# 		self.name = name
# 		self.mark = mark
#
# 	def write(self, x, y, cls_board):
# 		cls_board.table[x-1][y-1] = self.mark
#
#
#
#
# b = Board()
# b.info()
# me = Player("Саша", "Х")
# you = Player("Эля", "O")
# me.write(2, 2, b)
# you.write(2, 1, b)
# b.info()
# b.check()
# me.write(3, 3, b)
# you.write(1, 1, b)
# b.info()
# b.check()
# me.write(3, 1, b)
# you.write(1, 3, b)
# b.info()
# b.check()
# me.write(3, 2, b)
# you.write(1, 2, b)
# b.info()
# b.check()
#



# 8 БлекДжек
# import random
#
#
# class Card:
# 	def __init__(self, value, suit):
# 		self.value = self.set_value(value)
# 		self.suit = self.set_suit(suit)
# 		self.set_score()
#
# 	def set_value(self, value):
# 		if isinstance(value, int):
# 			if 2 <= value <= 10:
# 				return value
# 		elif isinstance(value, str):
# 			if value in ["Король", "Дама", "Валет", "Туз"]:
# 				return value
# 		raise ValueError("Не корректное значение для Value")
#
# 	def set_suit(self, value):
# 		if isinstance(value, str):
# 			if value in ["Черви", "Пики", "Буби", "Крести"]:
# 				return value
# 		raise ValueError("Не корректное значение для Suit")
#
# 	def set_score(self, variant=None):
# 		if self.value == "Туз":
# 			if variant is None:
# 				self.score = 11
# 			else:
# 				self.score = variant
# 		elif isinstance(self.value, int):
# 			self.score = self.value
# 		elif self.value in ["Король", "Дама", "Валет"]:
# 			self.score = 10
#
#
#
# 	def get_score(self):
# 		return self.score
#
# 	def get_value(self):
# 		return self.value
#
# 	def get_info(self):
# 		print("\t{} {} очков: {}".format(self.value, self.suit, self.score))
#
#
#
# class Deck:
#
# 	def __init__(self):
# 		self.list_cards = self.set_list_cards()
#
# 	def set_list_cards(self):
# 		list_cards = []
# 		for suit in ["Черви", "Пики", "Буби", "Крести"]:
# 			for value in range(2, 11):
# 				list_cards.append(Card(value, suit))
# 			for value in ["Король", "Дама", "Валет", "Туз"]:
# 				list_cards.append(Card(value, suit))
# 		return list_cards
#
# 	def info(self):
# 		for item in self.list_cards:
# 			item.get_info()
#
# 	def give_card(self):
# 		return self.list_cards.pop(random.randint(0, len(self.list_cards)-1))
#
#
# class Player:
# 	def __init__(self, name):
# 		self.name = name
# 		self.hand = []
# 		self.total_score = 0
#
# 	def info(self):
# 		print("Игрок: {}\nРука:".format(self.name))
# 		if len(self.hand) == 0:
# 			print("Нету карт")
# 		else:
# 			print("Очков {}".format(self.total_score))
# 			print("Выши карты:")
# 			for card in self.hand:
# 				card.get_info()
# 			print()
# 		return self.total_score
#
# 	def add_card(self, cls_deck):
# 		card = cls_deck.give_card()
# 		if card.get_value() == "Туз":
# 			if self.total_score + card.get_score() > 21:
# 				self.total_score += 1
# 				card.set_score(1)
# 			else:
# 				self.total_score += card.get_score()
# 		else:
# 			self.total_score += card.get_score()
# 		self.hand.append(card)
#
#
#
# my_deck = Deck()
# my = Player("Саша")
# your = Player("Дилер")
#
#
# while True:
# 	my_score = my.info()
# 	if my_score > 21:
# 		print("Вы проиграли")
# 		break
# 	say = input("Еще или хватит?\n").lower()
# 	if say == "еще":
# 		my.add_card(my_deck)
# 		continue
# 	break
# if my_score <= 21:
# 	your.add_card(my_deck)
# 	your.add_card(my_deck)
# 	your_score = your.info()
#
# 	if my_score > your_score:
# 		print("Вы победили")
# 	elif my_score < your_score:
# 		print("Вы проиграли")
# 	else:
# 		print("Ничья")

# 7 совместное проживание
# import random
#
#
# class People:
# 	def __init__(self, name):
# 		self.name = name
# 		self.satiety = 50
# 		self.status = "Alive"
#
# 	def info(self, cls_house):
# 		print("{} сытность={} денег={} еды={}".format(
# 			self.name, self.satiety, cls_house.get_money(), cls_house.get_food()))
#
#
# 	def get_status(self):
# 		return self.status
#
# 	def get_satiety(self):
# 		return self.satiety
#
# 	def dead(self, msg):
# 		print("{}".format(msg))
# 		self.status = "Dead"
#
# 	def feed(self, cls_house):
# 		money, food = cls_house.info()
# 		if food >= 10:
# 			print("{} кушает".format(self.name))
# 			cls_house.add_food(-5)
# 			self.satiety += 10
# 		else:
# 			self.dead("{} не нашел дома еды и умер!".format(self.name))
#
# 	def work(self, cls_house):
# 		print("{} пошел на работу".format(self.name))
# 		self.satiety -= 10
# 		if self.satiety <= 0:
# 			self.dead("{} заработал себя до смерти!".format(self.name))
# 		else:
# 			cls_house.add_money(15)
#
# 	def play(self):
# 		print("{} играет".format(self.name))
# 		self.satiety -= 5
# 		if self.satiety <= 0:
# 			self.dead("{} заигрался до смерти!".format(self.name))
#
# 	def buy_food(self, cls_house):
# 		money, food = cls_house.info()
# 		if money >= 10:
# 			print("{} пошел за едой".format(self.name))
# 			cls_house.add_money(-10)
# 			cls_house.add_food(20)
# 		else:
# 			print("{} Хотел пойти за едой, но денег нет!".format(self.name))
#
#
# class House:
# 	def __init__(self):
# 		self.money = 0
# 		self.food = 50
#
# 	def add_food(self, value=10):
# 		self.food += value
#
# 	def add_money(self, value=10):
# 		self.money += value
#
# 	def get_money(self):
# 		return self.money
#
# 	def get_food(self):
# 		return self.food
#
# 	def info(self):
# 		return self.money, self.food
#
#
# class Cube:
#
# 	def __init__(self):
# 		self.value = random.randint(1, 6)
#
# 	def quit(self):
# 		self.value = random.randint(1, 6)
# 		return self.show()
#
# 	def show(self):
# 		print("На кубике выпало:", self.value)
# 		return self.value
#
#
# my_home = House()
# me = People("Саша")
# you = People("Таня")
# my_cube = Cube()
# max_day = 365
# day = 1
# while day <= max_day and me.get_status() == "Alive" and  you.get_status() == "Alive":
# 	print("День {}-ый".format(day))
# 	for men in [me, you]:
# 		men.info(my_home)
# 		value_cube = my_cube.quit()
#
# 		if men.get_satiety() < 20:
# 			men.feed(my_home)
# 		elif my_home.get_food() < 10:
# 			men.buy_food(my_home)
# 		elif my_home.get_money() < 50:
# 			men.work(my_home)
# 		elif value_cube == 1:
# 			men.work(my_home)
# 		elif value_cube == 2:
# 			men.feed(my_home)
# 		else:
# 			men.play()
# 			print()
#
# 	day += 1
# 	print()






# class Water:
# 	def __add__(self, other):
# 		if isinstance(other, Earth):
# 			return Dirt()
#
#
# class Earth:
# 	def __add__(self, other):
# 		if isinstance(other, Water):
# 			return Dirt()
# 		elif isinstance(other, Fire):
# 			return Clay()
#
#
# class Fire:
# 	def __add__(self, other):
# 		if isinstance(other, Earth):
# 			return Clay()
# 		elif isinstance(other, Air):
# 			return Steam()
#
#
# class Air:
# 	def __add__(self, other):
# 		if isinstance(other, Fire):
# 			return Steam()
#
#
# class Dirt:
# 	def __init__(self):
# 		print("Получена грязь")
#
#
# class Clay:
# 	def __init__(self):
# 		print("Получена глина ")
#
#
# class Steam:
# 	def	__init__(self):
# 		print("Получен пар")
#
#
# a = Fire()
# b = Air()
# c = a + b
# c = b + a


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
# 		self.status = "Ухоженная"
# 		self.readiness = False
#
# 	def add_plant(self, plant):
# 		self.list_plants.append(plant)
#
# 	def lvl_up_plants(self):
# 		if self.status == "Ухоженная":
# 			for elem in self.list_plants:
# 				elem.lvl_up()
# 			self.status = "Неухоженная"
# 		else:
# 			print("Нужно ухаживать за грядкой!")
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
# 			self.readiness = True
# 		else:
# 			print("Нужно подождать")
# 		print()
#
#
# class GardenMen:
#
# 	def __init__(self, name):
# 		self.name = name
# 		self.garden = None
# 		self.count_harvest = 0
#
# 	def select_garden(self, garden):
# 		self.garden = garden
#
# 	def look_after(self):
# 		self.garden.status = "Ухоженная"
#
# 	def harvest(self):
# 		if self.garden.readiness:
# 			print("{} собрал урожай".format(self.name))
# 			for plant in self.garden.list_plants:
# 				plant.status = "Росток"
# 				self.count_harvest += 1
# 		else:
# 			print("Урожай еще не готов")
#
#
#
#
#
# my_garden = GardenBed()
# garden_men = GardenMen("Семен")
# garden_men.select_garden(my_garden)
#
# for _ in range(5):
# 	pl = Potatoes()
# 	my_garden.add_plant(pl)
#
# my_garden.info()
# my_garden.lvl_up_plants()
# garden_men.look_after()
# my_garden.lvl_up_plants()
# garden_men.look_after()
# garden_men.harvest()
# my_garden.lvl_up_plants()
# my_garden.info()
# garden_men.harvest()
# my_garden.info()


# 4
# class Parent:
#
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		self.dict_child = dict()
#
# 	def info(self):
# 		print("Имя родителя: {}\nВозраст родителя {}".format(self.name, self.age))
# 		if len(self.dict_child) != 0:
# 			print("Список детей:")
# 			for num, item in enumerate(self.dict_child.items()):
# 				child = item[1]
# 				print("{}-ый ребенок\n\tИмя: {}\n\tВозраст: {}\n\tНастроение: {}\n\tГолоден: {}".format(
# 					num + 1, child.name, child.age, child.mood_status, child.hunger_status))
# 		else:
# 			print("Детей нет")
# 		print()
#
# 	def create_child(self, name):
# 		if self.age >= 16:
# 			new_child = Child(name)
# 			self.dict_child[name] = new_child
# 		else:
# 			print("{}, чтобы заводить детей нужно подрасти!".format(self.name))
#
# 	def calm_down(self, child):
# 		if self.dict_child.get(child):
# 			self.dict_child[child].mood_status = "Хорошие настроение"
# 		else:
# 			print("У {} нет детей с именем {}".format(self.name, child))
#
# 	def feed(self, child):
# 		if self.dict_child.get(child):
# 			self.dict_child[child].hunger_status = "Нет"
# 		else:
# 			print("У {} нет детей с именем {}".format(self.name, child))
#
#
# class Child:
#
# 	def __init__(self, name):
# 		self.name = name
# 		self.age = 0
# 		self.mood_status = "Плохое настроение"
# 		self.hunger_status = "Да"
#
#
#
# parent1 = Parent("Света",20)
# parent1.info()
# parent1.create_child("Тоня")
# parent1.info()
# parent1.calm_down("Тоня")
# parent1.info()

# 3
# import math
#
#
# class Circle:
#
# 	def __init__(self, x=0, y=0, radius=1):
# 		self.x = x
# 		self.y = y
# 		self.radius = radius
#
# 	def square(self):
# 		value = math.pi * self.radius ** 2
# 		print("Площадь круга =", round(value,3))
# 		return value
#
# 	def perimeter(self):
# 		value = 2 * math.pi * self.radius
# 		print("Периметр круга =", round(value, 3))
# 		return value
#
# 	def increase(self, value):
# 		self.radius *= value
#
# 	def intersection(self, other_x, other_y, other_radius):
# 		segment_length = math.sqrt((other_x - self.x) ** 2 + (other_y - self.y) ** 2)
# 		if segment_length <= self.radius + other_radius:
# 			print("Пересекаются")
# 		else:
# 			print("Не пересекаются")
#
#
# cir_1 = Circle()
# cir_2 = Circle(10, 10, 3)
# sq_1 = cir_1.square()
# sq_2 = cir_2.square()
# cir_1.intersection(cir_2.x, cir_2.y, cir_2.radius)


# 2 Студенты
# import random
#
#
# class Student:
#
# 	def __init__(self, name=None, num_group=None):
# 		self.name = name
# 		self.num_group = num_group
# 		self.dict_progress = dict()
# 		self.gpa_value = None
#
# 	def info(self):
# 		print("Студент {}\nСредний балл {}".format(self.name, self.gpa_value))
#
# 	def work_with_progress(self, name, score):
# 		self.dict_progress[name] = score
#
# 	def gpa(self):
# 		self.gpa_value = round(sum(self.dict_progress.values()) / len(self.dict_progress), 2)
#
#
# my_class = []
#
# name_list = ["Саша", "Паша", "Олег", "Таня", "Марго", "Оксана", "Эдуард", "Света", "Сергей", "Кристина"]
# list_lesson = ["История России", "История", "Политология", "Право", "Статистика"]
#
# for item in name_list:
# 	new_stud = Student(item)
# 	for lesson in list_lesson:
# 		new_stud.work_with_progress(lesson, random.randint(40, 100))
# 	new_stud.gpa()
# 	my_class.append([new_stud.gpa_value, new_stud.name, new_stud])
#
# for item in sorted(my_class, reverse=True):
# 	print(item)

# 1 Драка
# import random
#
#
# class Warrior:
# 	count = 0
#
# 	def __init__(self):
# 		Warrior.count += 1
# 		self.name = "Воин {}".format(Warrior.count)
# 		self.health = 100
# 		self.status = "ALive"
#
# 	def dead(self):
# 		self.status = "Dead"
# 		print("{} мертв".format(self.name))
#
# 	def info(self):
# 		print("Здоровье {} = {}".format(self.name, self.health))
#
# 	def minus_health(self):
# 		if self.health > 0:
# 			self.health -= 20
# 		if self.health <= 0:
# 			self.dead()
#
# 	def hit(self, target):
# 		print("{} ударил {}".format(self.name, target.name))
# 		target.minus_health()
#
#
# war1 = Warrior()
# war2 = Warrior()
# war1.info()
# war2.info()
# while war1.status == "ALive" == war2.status:
# 	if random.random() < 0.5:
# 		war1.hit(war2)
# 		if war2.status == "ALive":
# 			war2.info()
# 	else:
# 		war2.hit(war1)
# 		if war1.status == "ALive":
# 			war1.info()


