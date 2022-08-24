# 4
x = []

# 3
# import math
# from typing import List, Union
#
#
# class Square:
# 	"""
# 	Абстрактный класс квадрат 2D
# 	задается две стороны
# 	"""
# 	def __init__(self, side_a: int, side_b: int) -> None:
# 		self._side_a = side_a
# 		self._side_b = side_b
# 		self._side_c = side_a
# 		self._side_d = side_b
#
# 	@property
# 	def a(self):
# 		return self._side_a
#
# 	@property
# 	def b(self):
# 		return self._side_b
#
# 	@property
# 	def c(self):
# 		return self._side_c
#
# 	@property
# 	def d(self):
# 		return self._side_d
#
# 	@a.setter
# 	def a(self, value: int):
# 		self._side_a = value
#
# 	@b.setter
# 	def b(self,  value: int):
# 		self._side_b = value
#
# 	@c.setter
# 	def c(self,  value: int):
# 		self._side_c = value
#
# 	@d.setter
# 	def d(self,  value: int):
# 		self._side_d = value
#
# 	def perimeter(self) -> int:
# 		"""Возвращает сумму длина всех сторон"""
# 		result = self._side_a + self._side_b + self._side_c + self._side_d
# 		return result
#
# 	def square(self) -> int:
# 		"""Возвращает площадь четырехугольника"""
# 		result = self._side_a * self._side_b
# 		return result
#
#
# class Triangle:
# 	"""
# 	Абстрактный класс треугольник 2D
# 	задается основание и высота
# 	"""
#
# 	def __init__(self, side_a: int, side_h: int) -> None:
# 		self._side_a = side_a
# 		self._side_h = side_h
#
# 	@property
# 	def a(self):
# 		return self._side_a
#
# 	@a.setter
# 	def a(self, value: int):
# 		self._side_a = value
#
# 	@property
# 	def h(self):
# 		return self._side_h
#
# 	@h.setter
# 	def h(self, value: int):
# 		self._side_h = value
#
# 	def perimeter(self):
# 		"""Возвращает сумму длин сторон треугольника"""
# 		side_b = math.sqrt(self._side_a ** 2 + self._side_h ** 2)
# 		result = self._side_a + side_b * 2
# 		return result
#
# 	def square(self):
# 		"""Возвращает площадь треугольника"""
# 		result = self._side_a * self._side_h / 2
# 		return result
#
#
# class MyCube(Square):
# 	"""3д куб из прямоугольников"""
# 	def __init__(self, side_a, side_b):
# 		super().__init__(side_a, side_b)
# 		self.__cube_data = []
# 		for _ in range(6):
# 			self.__cube_data.append(Square(side_a, side_b))
#
# 	@property
# 	def cube_data(self) -> List[Square]:
# 		"""Представление куба в виде списка"""
# 		return self.__cube_data
#
# 	def square(self) -> int:
# 		"""Площадь поверхности куба"""
# 		result = 0
# 		for elem in self.__cube_data:
# 			result += elem.a * elem.b
# 		return result
#
# 	def perimeter(self) -> int:
# 		"""Возвращает сумму длина всех сторон"""
# 		result = self._side_a * 6 + self._side_b * 6
# 		return result
#
#
# class MyPyramid(Square, Triangle):
# 	"""3д куб из прямоугольников"""
# 	def __init__(self, side_a, side_h):
# 		super().__init__(side_a, side_h)
# 		self.__pyramid_data = []
# 		for _ in range(3):
# 			self.__pyramid_data.append(Triangle(side_a, side_h))
# 		self.__pyramid_data.append(Square(side_a, side_a))
#
# 	@property
# 	def pyramid_data(self) -> List[Union[Square, Triangle]]:
# 		"""Представление пирамиды в виде списка"""
# 		return self.__pyramid_data
#
# 	def square(self) -> int:
# 		"""Площадь пирамиды"""
# 		result = 0
# 		for elem in self.__pyramid_data:
# 			if isinstance(elem, Triangle):
# 				result += elem.a * elem.h / 2
# 			else:
# 				result += elem.a * elem.b
# 		return result
#
# 	def perimeter(self) -> None:
# 		"""Возвращает сумму длина всех сторон"""
# 		pass
#
#
#
#
#
# my_cube = MyCube(2, 4)
# print(my_cube.square())
# print(my_cube.perimeter())
# print(my_cube.cube_data)
#
# my_tr = MyPyramid(2, 6)
# print(my_tr.square())

# 2
# from abc import ABC
#
#
# class MyMath(ABC):
# 	"""
# 		Абстрактный класс. Типа math только меньше.
# 		__pi атрибут класса
# 	"""
# 	__pi = 3.14
#
# 	@classmethod
# 	def square_circle(cls, r: float) -> float:
# 		"""
# 		:param r: радиус
# 		:return: площадь окружности
# 		"""
# 		return MyMath.__pi * r ** 2
#
# 	@classmethod
# 	def circumference(cls, r: float) -> float:
# 		"""
# 		:param r: радиус
# 		:return: длина окружности
# 		"""
# 		return 2 * MyMath.__pi * r
#
# 	@classmethod
# 	def square_cube(cls, le: float) -> float:
# 		"""
# 		:param le: длина стороны куба
# 		:return: площадь куба
# 		"""
# 		return le ** 3
#
# 	@classmethod
# 	def sphere_surface_area(cls, r: float) -> float:
# 		"""
# 		:param r: радиус
# 		:return: площадь поверхности шара
# 		"""
# 		return 4 * MyMath.__pi * r ** 2
#
#
# print(MyMath.square_circle(2))

# 1
# import time
#
#
# class timer:
# 	def __init__(self) -> None:
# 		print("Время работы когда")
# 		self.start = None
#
# 	def __enter__(self) -> 'Timer':
# 		self.start = time.time()
# 		return self
#
# 	def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
# 		print(time.time() - self.start)
# 		# if exc_type is TypeError:
# 		# 	return True
# 		return True
#
#
# with timer() as t1:
# 	print("первая часть")
# 	val_1 = 100 * 100 ** 1000000
# 	val_1 += 'abc'
# 	# код
#
#
# with timer() as t2:
# 	print("вторая часть")
# 	val_2 = 200 * 200 ** 1000000
# 	# код
# with timer() as t3:
# 	print("первая часть")
# 	val_3 = 200 * 200 ** 1000000
# 	# код
