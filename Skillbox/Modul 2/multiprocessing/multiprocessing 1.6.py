import queue
from threading import Thread, Lock
from collections import defaultdict
import time
import random


class Fisher(Thread):
	__FISH = (None, "Окунь", "Щука", "Язь", "Карась", "Форель")

	def __init__(self, name: str, warms: int, fish_tank: queue.Queue, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__name = name
		self.__warms = warms
		self.__catch = 0
		self.__fish_tank = fish_tank

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
			print("{name} забросил червя {worm}".format(name=self.__name, worm=worm), flush=True)
			fish = random.choice(self.__FISH)
			if fish is None:
				print("У {} сорвалась рыбка, прощай червяк".format(self.__name), flush=True)
			else:
				print("{} поймал {}".format(self.__name, fish), flush=True)
				if self.__fish_tank.full():
					print(f"{self.__name}, {worm}: садок полон", flush=True)
				self.__fish_tank.put(fish)
				print(f"{self.__name}, {worm}: положил {fish} в садок", flush=True)


class Board(Thread):
	def __init__(self, warms_per_fisher, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__fishers = []
		self.__warms_per_fisher = warms_per_fisher
		self.__fish_tank = queue.Queue(maxsize=2)
		self.__catch = defaultdict(int)

	def add_fisher(self, name: str):
		fisher = Fisher(name=name, warms=self.__warms_per_fisher, fish_tank=self.__fish_tank)
		self.__fishers.append(fisher)

	def run(self):
		print("Лодка вышла в море...", flush=True)
		for fisher in self.__fishers:
			fisher.start()
		while True:
			try:
				fish = self.__fish_tank.get(timeout=1)
				print(f"Садок принял {fish}", flush=True)
				self.__catch[fish] += 1
			except queue.Empty:
				print("В садке пусто в течении 1 секунды", flush=True)
				if not any(fisher.is_alive() for fisher in self.__fishers):
					break
		for fisher in self.__fishers:
			fisher.join()
		print("Лодка плывет домой", flush=True)


board = Board(warms_per_fisher=10)
humans = ["Петя", "Женя", "Виталя", "Антон", "Глеб"]
for name in humans:
	board.add_fisher(name=name)

board.start()
board.join()

