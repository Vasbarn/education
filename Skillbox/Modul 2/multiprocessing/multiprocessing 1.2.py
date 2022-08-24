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

	def run(self):
		catch = defaultdict(int)
		for worm in range(1, self.__warms + 1):
			print("{name} забросил червя {worm}".format(name=self.__name, worm=worm), flush=True)
			time.sleep(1)
			fish = random.choice(self.__FISH)
			if fish is None:
				print("У {} сорвалась рыбка, прощай червяк".format(self.__name), flush=True)
			else:
				print("{} поймал {}".format(self.__name, fish), flush=True)
				catch[fish] += 1
		print("Итого {} поймал целых:".format(self.__name), flush=True)
		for key, item in catch.items():
			print("\t{} - {} штук".format(key, item), flush=True)


vasya = Fisher(name="Вася", warms=10)
petya = Fisher(name="Петя", warms=10)

print("-"*20, "Пошли на рыбалку", "-"*20)
vasya.start()
petya.start()
print("-"*20, "ждем", "-"*20)
vasya.join()
petya.join()
print("-"*20, "Оба закончили", "-"*20)