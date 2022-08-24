from threading import Thread, Lock
from collections import defaultdict
import time
import random


class Fisher(Thread):
	__FISH = (None, "Окунь", "Щука", "Язь", "Карась", "Форель")

	def __init__(self, name: str, warms: int, total_fish_: defaultdict, lock_, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__name = name
		self.__warms = warms
		self.__catch = 0
		self.__total_fish = total_fish_
		self.__lock: Lock = lock_

	@property
	def catch(self):
		return self.__catch

	def run(self):
		try:
			self._fish()
		except ValueError as ex:
			print(ex)

	def _fish(self):

		for worm in range(1, self.__warms + 1):
			_ = worm ** 100
			fish = random.choice(self.__FISH)
			if fish is not None:
				self.__lock.acquire()
				self.__total_fish[fish] += 1
				self.__catch += 1
				self.__lock.release()





total_fish = defaultdict(int)
humans = ["Петя", "Женя", "Виталя", "Антон", "Глеб"]
lock = Lock()
fishers = [Fisher(name=name, warms=100000, total_fish_=total_fish, lock_=lock) for name in humans]


for fisher in fishers:
	fisher.start()
for fisher in fishers:
	fisher.join()
print("Всего рыбы в общей копилке {}".format(sum([x for x in total_fish.values()])))
print("Всего рыбы у рыбаков {}".format(sum([fisher.catch for fisher in fishers])))
