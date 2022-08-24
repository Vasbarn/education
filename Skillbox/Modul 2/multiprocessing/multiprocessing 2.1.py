import os
import random
from multiprocessing import Process, Pipe, Queue
from queue import Empty
from collections import defaultdict

FISH = (None, "Окунь", "Щука", "Язь", "Карась", "Форель")


def fishing(name, worms):
	print(f"{name} parent process: {os.getppid()}", flush=True)
	print(f"{name} parent id: {os.getppid()}", flush=True)
	catch = defaultdict(int)
	for worm in range(worms):
		print(f"{name}: Червяк №{worm} - Забросил. Жду.", flush=True)
		_ = worm ** random.randint(500000, 700000) * 100000
		fish = random.choice(FISH)
		if fish is None:
			print(f"{name} упустил рыбку с крючка", flush=True)
		else:
			print(f"{name} поймал рыбку {fish}", flush=True)
			catch[fish] += 1
	print(f"Итого рыбак {name} поймал:", flush=True)
	for fish, count in catch.items():
		print(f"{fish}: {count} штук", flush=True)


if __name__ == "__main__":
	proc = Process(target=fishing, kwargs=dict(name="Вася", worms=100))
	proc.start()
	fishing(name="Коля", worms=100)
	proc.join()
