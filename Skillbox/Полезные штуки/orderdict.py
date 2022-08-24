from collections import OrderedDict
""" суть в том, что словарь выдает ключ-значение в том порядке в каком мы их добавлял"""
my_dict = OrderedDict()

my_dict["11"] = "test"
my_dict[2] = "test"
my_dict[3] = "test"
my_dict[4] = "test"
my_dict[5] = "test"
my_dict[6] = "test"
my_dict[7] = "test"
my_dict[8] = "test"
for key, item in my_dict.items():
	print(key, item)

print()
my_dict = dict()

my_dict["11"] = "test"
my_dict[2] = "test"
my_dict[3] = "test"
my_dict["4"] = "test"
my_dict[5] = "test"
my_dict[6] = "test"
my_dict[7] = "test"
my_dict[8] = "test"
for key, item in my_dict.items():
	print(key, item)

