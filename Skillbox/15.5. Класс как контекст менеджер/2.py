from contextlib import contextmanager
from collections.abc import Iterator
import time


@contextmanager
def timer() -> Iterator:
	time_start = time.time()
	try:
		yield
	finally:
		print(time.time() - time_start, " время выполнения")


with timer() as t1:
	print(100000 * 100000 ** 10000)
