# 3

# # 2r
from abc import ABC, abstractmethod


class Frame(ABC):
	def __init__(self, color: str, speed: int) -> None:
		self._color = None
		self._speed = None
		self._color = color
		self._speed = speed

	@property
	def color(self) -> str:
		return self._color

	@property
	def speed(self) -> int:
		return self._speed

	@color.setter
	def color(self, value: str) -> None:
		self._color = value

	@speed.setter
	def speed(self, value: int) -> None:
		self._speed = value



	@abstractmethod
	def say(self) -> None:
		print("Звуковой сигнал Би-Би")

	@abstractmethod
	def move(self):
		print("Началось движение")


class Car(Frame):
	def __init__(self, color: str, speed: int):
		super().__init__(color, speed)

	def say(self) -> None:
		print("Машинный гудок")

	def move(self):
		print("Поехали")


class Ship(Frame):
	def __init__(self, color: str, speed: int):
		super().__init__(color, speed)

	def say(self) -> None:
		print("Корабельный гудок")

	def move(self):
		print("ПоПлыли")


class Music:
	def listen_to_music(self):
		print("Слушаю музыку")


class Amphibian(Frame, Music):
	def __init__(self, color: str, speed: int):
		super().__init__(color, speed)

	def say(self) -> None:
		print("Сквирт")

	def move(self) -> None:
		print("Поскиритили")






x = Car("Красный", 5)
x.speed = 10
x.say()
print(x.speed)

x = Ship("Синий", 2)
x.color = "Бурый"
x.say()
print(x.speed)

x = Amphibian("Золотой", 69)
x.speed = 10
x.say()
print(x.speed)
x.listen_to_music()


# 1
# class Robot:
# 	def __init__(self, model):
# 		self._model = model
#
# 	def say(self):
# 		print("Я - работ")
#
#
# class CanFly:
# 	def __init__(self, model):
# 		self._model = model
# 		self._height = 0
# 		self._speed = 0
#
# 	def set_height(self, value):
# 		self._height = value
#
# 	def get_height(self):
# 		return self._height
#
# 	def set_speed(self, value):
# 		self._speed = value
#
# 	def get_speed(self):
# 		return self._speed
#
#
# class DroidRanger(Robot, CanFly):
# 	def __init__(self, model):
# 		super().__init__(model)
#
# 	def operate(self):
# 		self.set_speed(5)
# 		print("Введу разведку со скорость движения {} км/ч".format(self.get_speed()))
#
#
# class DroidWarrior(Robot, CanFly):
# 	def __init__(self, model, gun="ЖЛДД-2"):
# 		super().__init__(model)
# 		self._gun = gun
#
# 	def operate(self):
# 		self.set_height(50)
# 		print("Обороняюсь с помощью {} с высоты {}".format(self._gun, self.get_height()))
#
#
#
# dr1 = DroidRanger(model="R2D2")
# dr1.say()
# dr1.operate()
# print(dr1)
#
# dr2 = DroidWarrior(model="R2D2")
# dr2.say()
# dr2.operate()
# print(dr2)

