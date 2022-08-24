import os
import random
from multiprocessing import Process, Pipe, Queue
from queue import Empty
from collections import defaultdict

FISH = (None, "Окунь", "Щука", "Язь", "Карась", "Форель")


class Fishers(Process):
	def __init__(self, name, worms, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__name = name
		self.__worms = worms

	def run(self):
		catch = defaultdict(int)
		for worm in range(self.__worms):
			print(f"{self.__name}: Червяк №{worm} - Забросил. Жду.", flush=True)
			_ = worm ** random.randint(500000, 700000) * 100000
			fish = random.choice(FISH)
			if fish is None:
				print(f"{self.__name} упустил рыбку с крючка", flush=True)
			else:
				print(f"{self.__name} поймал рыбку {fish}", flush=True)
				catch[fish] += 1
		print(f"Итого рыбак {self.__name} поймал:", flush=True)
		for fish, count in catch.items():
			print(f"{fish}: {count} штук", flush=True)


if __name__ == "__main__":
	kolya = Fishers(name="Коля", worms=10)
	vasya = Fishers(name="Вася", worms=10)
	kolya.start()
	vasya.start()
	print("Рыбалка началась\n", "." * 20, )
	kolya.join()
	vasya.join()
	print("Рыбалка кончилась\n", "." * 20, )