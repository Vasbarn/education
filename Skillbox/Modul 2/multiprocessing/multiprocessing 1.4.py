from threading import Thread
from collections import defaultdict
import time
import random


class Fisher(Thread):
	__FISH = (None, "Окунь", "Щука", "Язь", "Карась", "Форель")

	def __init__(self, name: str, warms: int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__name = name
		self.__warms = warms
		self.__catch = defaultdict(int)

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
			time.sleep(0.01)
			fish = random.choice(self.__FISH)
			if fish is not None:
				self.__catch[fish] += 1


def timer(func):
	def into_def(*args, **kwargs):
		time_start = time.time()
		result = func(*args, **kwargs)
		print("{} выполнялась {} секунда".format(func.__name__, round((time.time() - time_start), 4)))
		return result
	return into_def


@timer
def run_in_one_thread(fishers):
	for fisher in fishers:
		fisher.run()


@timer
def run_in_thread(fishers):
	for fisher in fishers:
		fisher.start()
	for fisher in fishers:
		fisher.join()


humans = ["Петя", "Женя", "Виталя", "Антон", "Глеб"]
fishers = [Fisher(name=name, warms=100) for name in humans]

run_in_one_thread(fishers)
run_in_thread(fishers)
