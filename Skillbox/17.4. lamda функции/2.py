

class Person:
	"""
	Класс для учета сотрудников
	"""
	def __init__(self, name: str, age: int) -> None:
		"""Имеет имя и возраст"""
		self.__name = name
		self.__age = age

	def __repr__(self):
		return "Экземпляр класс Person. Имя: {}. Возраст {}".format(self.name, self.age)

	def __str__(self):
		return "Экземпляр класс Person. Имя: {}. Возраст {}".format(self.name, self.age)

	@property
	def name(self) -> str:
		return self.__name

	@property
	def age(self) -> int:
		return self.__age


list_person = list()
list_person.append(Person("Саша", 28))
list_person.append(Person("Алексей", 26))
list_person.append(Person("Семен", 30))

print(list_person)
print(sorted(list_person, key=lambda elem: elem.age))