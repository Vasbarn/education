import random
from collections import defaultdict
import time
from threading import Thread

FISH = (None, "Окунь", "Щука", "Язь", "Карась", "Форель")


def fishing(name, worms, catch):

	for worm in range(1,  worms + 1):
		print("{name} забросил червя {worm}".format(name=name, worm=worm), flush=True)  # flush - вывести значение сразу
		time.sleep(1)
		fish = random.choice(FISH)
		if fish is None:
			print("У {} сорвалась рыбка, прощай червяк".format(name), flush=True)
		else:
			print("{} поймал {}".format(name, fish), flush=True)
			catch[fish] += 1
	print("Итого {} поймал целых:".format(name), flush=True)
	for key, item in catch.items():
		print("\t{} - {} штук".format(key, item), flush=True)


# fishing(name="Вася", worms=10)


# потоки
dict_1 = defaultdict(int)
thread = Thread(target=fishing, kwargs=dict(name="Петя", worms=10, catch=dict_1))
thread.start()
dict_2 = defaultdict(int)
fishing(name="Женя", worms=10, catch=dict_2)
thread.join()
print(dict_1)
