# 9

# 8
# def open_list(my_list, answer=None):
# 	if answer is None:
# 		answer = []
# 	for item in my_list:
# 		if isinstance(item, list):
# 			open_list(item, answer=answer)
# 		else:
# 			answer.append(item)
# 	return answer
#
#
# value = [1, 2, [3], [[4, 5]]]
# print(open_list(value))
# 7
# def my_sum(my_list, sum_x=0):
# 	for item in my_list:
# 		if isinstance(item, list):
# 			sum_x = my_sum(item, sum_x)
# 		else:
# 			sum_x += item
# 	return sum_x
#
#
# x = [1, [1, 1, [1, 2]], 1, [1]]
# print(my_sum(x))

# 6
# def print_structure(var_dict):
# 	pass
#
#
# def create_site(name=None, my_list=None):
# 	if my_list is None:
# 		my_list = []
# 	site = {
# 		'html': {
# 			'head': {
# 				'title': 'Куплю/продам {} недорого'.format(name)
# 			},
# 			'body': {
# 				'h2': 'У нас самая низкая цена на {}'.format(name),
# 				'div': 'Купить',
# 				'p': 'Продать'
# 			}
# 		}
# 	}
# 	my_list.append(site)
# 	return my_list
#
# value = create_site()
# print(value)

# 5
# def calculating_math_func(data, new_dict=dict()):
# 	print(new_dict)
# 	if new_dict.get(data):
# 		result = new_dict.get(data)
# 	else:
#
# 		result = 1
# 		for index in range(1, data + 1):
# 			result *= index
# 	new_dict[data] = result
# 	result /= data ** 3
# 	result = result ** 10
# 	return result
#
# calculating_math_func(4)
# calculating_math_func(4)


# 4
# site = {
# 	'html': {
# 		'head': {
# 			'title': 'Мой сайт'
# 		},
# 		'body': {
# 			'h2': 'Здесь будет мой заголовок',
# 			'div': 'Тут, наверное, какой-то блок',
# 			'p': 'А вот здесь новый абзац'
# 		}
# 	}
# }
#
#
# def search_key(var_dict, value, level=None, my_try=-1):
# 	my_try += 1
# 	if level == my_try:
# 		return None
# 	if value in var_dict:
# 		return var_dict[value]
# 	for var in var_dict.values():
# 		if isinstance(var, dict):
# 			result = search_key(var, value,level=level,my_try=my_try)
# 			if result:
# 				break
# 	else:
# 		return None
# 	return result
#
#
# my_value = "title"
# data = search_key(site, my_value, level=3)
# print(data)

# 3
# def my_feb(num, num1=1, num2=1, my_try=2):
# 	my_try += 1
# 	if num == 1 or num == 2:
# 		return 1
# 	if num > my_try:
# 		return my_feb(num, num1=num2, num2=(num1 + num2), my_try=my_try)
# 	else:
# 		return num1 + num2
#
# x = my_feb(7)
# print(x)

# 2
# def func(value, num):
# 	new_value = tuple(x[num] for x in value)
# 	return new_value
#
#
# def my_zip(*args):
# 	min_len = min([len(arg) for arg in args])
# 	new_tuple = [func(args, x) for x in range(min_len)]
# 	print(new_tuple)
#
#
# my_zip([123, 321, 222, 111], "фыв")

# 1
# def my_func(num, s_num=1):
# 	print(s_num)
# 	if s_num < num:
# 		return my_func(num, s_num+1)
#
#
# my_num = 10
# my_func(my_num)
