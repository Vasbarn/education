"""
Реализация связанного списка
"""
from typing import Any, Optional


class Node:
	"""
	Класс узла, умеет принимать значение, и отдвать\получить следующий узел
	"""
	def __init__(self, value: Optional[Any] = None, next_elem: Optional['Node'] = None) -> None:
		"""
		Создается узел с данными, и в процессе работы может быть задан следующий связанный узел.
		:param value: любая информация для сохранения.
		:param next_elem: следующий узел.
		"""
		self.__value = value
		self.__next_elem = next_elem

	def __str__(self) -> str:
		return "Node [{value}]".format(value=str(self.__value))

	@property
	def value(self) -> Any:
		return self.__value

	@value.setter
	def value(self, value: Any) -> None:
		self.__value = value

	@property
	def next_elem(self) -> 'Node':
		return self.__next_elem

	@next_elem.setter
	def next_elem(self, value: "Node"):
		self.__next_elem = value


class LinkedList:
	"""
	Класс реализации связей узлов
	"""
	def __init__(self) -> None:
		"""
		При объявлении класса ничего не происходит, кроме непосредственного создания экземпляра класса.
		"""
		self.__head: Optional[Node] = None
		self.__len = 0

	def __str__(self):
		result_str = "LinkedList [{values}"
		cur_node = self.__head
		values = ""
		while cur_node is not None:
			if values == "":
				values = str(cur_node.value)
			else:
				values += ", {cur_node}".format(cur_node=cur_node.value)
			cur_node = cur_node.next_elem
		return result_str.format(values=values + "]")

	def append(self, value: Any) -> None:
		"""
		Метод добавления новых узлов в конец связей.
		:param value: Любое значение, которое будет передано в созданный узел, и размещен в классе связей.
		:return: вызывается только, если в цепи связей задается первый узел.
		"""
		new_node = Node(value=value)
		self.__len += 1
		if self.__head is None:
			self.__head = new_node
			return
		last = self.__head
		while last.next_elem:
			last = last.next_elem
		last.next_elem = new_node

	def remove(self, index: int = 0) -> None:
		"""
		Метод для удаления узла по его индексу.
		Узел перед ним получит обновленную связь.
		:param index: номер узла по порядку, начиная с 0.
		:return:
		"""
		if not isinstance(index, int):
			return
		else:
			if index < 0 or index >= self.__len:
				return
		if index == 0:
			if self.__head.next_elem is None:
				self.__head = None
			else:
				self.__head = self.__head.next_elem
			self.__len -= 1
			return
		current_node = self.__head
		current_index = 0
		prev_node = None
		while current_node is not None:
			if current_index == index:
				break
			prev_node, current_node = current_node, current_node.next_elem
			current_index += 1
		prev_node.next_elem = current_node.next_elem
		self.__len -= 1

	def index(self, index: int) -> Any:
		"""
		Получение значение узла по его индексу в цепочки связи.
		:param index: целочисленное значение.
		:return: Значение узла под действительным индексом.
		"""
		if not isinstance(index, int):
			return
		else:
			if index < 0 or index >= self.__len:
				return
		current_node = self.__head
		for _ in range(index):
			current_node = current_node.next_elem
		return current_node.value


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
my_list.remove(2)
print(my_list)
print(my_list.index(1))

