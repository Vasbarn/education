# задача 9 не осилил 10 устно
# def my_func(var_list):
#     for item in var_list:
#         for key, item2 in item.items():
#             print(key)
#
#
#
# #count = int(input("Количество человек: "))
# # start_list = list()
#
# # for iterate in range(1, count):
# #     value = input("{} пара: ".format(iterate)).split()
# #     child = value[1]
# #     parent = value[0]
# #     start_list.append({parent: child})
#
# start_list = [{"Вова": "Таня"}, {"Вова": "Маша"}, {"Маша": "Саша"}]
# my_func(start_list)




# Задача 8
# import random
# n_num = int(input("Введите верхнюю границу значений: "))
# num_target = random.randint(0, n_num)
# print(num_target)
# answer = set()
# while len(answer) != 1:
#     print(answer)
#     text = input("Я загадал число, отгадай: (пиши несколько вариантов через пробел): ").lower()
#     if text == "помогите":
#         break
#     my_num = set([int(x) for x in text.split()])
#     if num_target in my_num:
#         answer.update(my_num)
#         print("Близко")
#     else:
#         answer.difference_update(my_num)
#         print("Мимо")
# print(" Твой ответ {}".format(answer))

# задача 7
# def create_data(client, good, count, var_dict):
#     if var_dict.get(client):
#         for item in var_dict.get(client):
#             if item.get(good):
#                 item[good] += int(count)
#             else:
#                 var_dict.get(client).append({good: int(count)})
#     else:
#         var_dict[client] = [{good: int(count)}]
#
#
# num = int(input("Количество заказов: "))
# my_dict = dict()
# for numer in range(1, num + 1):
#     value = input("Введите Клиента Заказ Количество: ").split()
#     create_data(value[0], value[1], value[2], my_dict)
#
# for key1 in my_dict.keys():
#     print(key1, ":")
#     for item in range(len(my_dict[key1])):
#         for key2 in my_dict[key1][item].keys():
#             print("\t {}:{}".format(key2, my_dict[key1][item][key2]))

# задача 6
# count_par = int(input("Количество пар: "))
# sin_dict = dict()
# for _ in range(count_par):
#     value = input("Введите слово и синоним к нему через пробел: ").lower().split()
#     sin_dict[value[0]] = value[1:]
#
# while True:
#     word = input("Введите слово: ")
#     if sin_dict.get(word):
#         print("Синоним: ", sin_dict[word][0])
#     else:
#         print("Такого слова не знаю")

# задача 5 снова словарь
# my_text = input("Введите текст: ").lower()
# dict1 = dict()
# dict2 = dict()
# for word in my_text:
#     if dict1.get(word):
#         dict1[word] += 1
#     else:
#         dict1[word] = 1
# print(dict1)
# for key, item in dict1.items():
#     if dict2.get(item):
#         var = dict2[item]
#         dict2[item].append(key)
#     else:
#         dict2[item] = [key]
# print(dict2)

# задача 4
# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
#
#
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
#
# for key, good in goods.items():
#     goods[key] = store.get(good)
# print(goods)
# print(goods.values())
# for key, elem in goods.items():
#     total_count = 0
#     total_sum = 0
#     for i_elem in range(len(elem)):
#         total_count += elem[i_elem]["quantity"]
#         total_sum += elem[i_elem]["quantity"] * elem[i_elem]["price"]
#     print("Товара {} на остатках {} на сумму {:,}".format(key, total_count, total_sum).replace(",", " "))


# задача 3
# data = {
#     "address": "0x544444444444",
#     "ETH": {
#         "balance": 444,
#         "totalIn": 444,
#         "totalOut": 4
#     },
#     "count_txs": 2,
#     "tokens": [
#         {
#             "fst_token_info": {
#                 "address": "0x44444",
#                 "name": "fdf",
#                 "decimals": 0,
#                 "symbol": "dsfdsf",
#                 "total_supply": "3228562189",
#                 "owner": "0x44444",
#                 "last_updated": 1519022607901,
#                 "issuances_count": 0,
#                 "holders_count": 137528,
#                 "price": False
#             },
#             "balance": 5000,
#             "totalIn": 0,
#             "total_out": 0
#         },
#         {
#             "sec_token_info": {
#                 "address": "0x44444",
#                 "name": "ggg",
#                 "decimals": "2",
#                 "symbol": "fff",
#                 "total_supply": "250000000000",
#                 "owner": "0x44444",
#                 "last_updated": 1520452201,
#                 "issuances_count": 0,
#                 "holders_count": 20707,
#                 "price": False
#             },
#             "balance": 500,
#             "totalIn": 0,
#             "total_out": 0
#         }
#     ]
# }
# data.get('ETH', {})["total_diff"] = 100
# data["tokens"][0]["fst_token_info"]["name"] = 'doge'
# for elem in data["tokens"]:
#     data['ETH']["totalOut"] += elem.pop('total_out')
# data["tokens"][1]["sec_token_info"]["Total_price"] = data["tokens"][1]["sec_token_info"].pop("price")
#
# for key, item in data.items():
#     print("Ключ: {}  - Значение: {}".format(key, item))



# задача 2 страны
# def check(vcity, vmy_dict):
#     for key, item in vmy_dict.items():
#         if vcity in item:
#             print("Город {} принадлежит стране {}".format(vcity, key))
#             return
#     print(city, "- Данны нет")
#
#
# count_country = int(input("Сколько стран будет: "))
# my_dict = dict()
# for _ in range(count_country):
#     country = input("Введите Страну и три города этой страны, все через пробел").split()
#     my_dict[country[0]] = country[1:]
# search_city = input("Введите названия городов(3 шт), а я угадаю его страну: ").split()
# for city in search_city:
#     check(city, my_dict)

# задача 1
# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
#
# count_music = int(input("Сколько песен выбрать?: "))
# my_playlist = dict()
# for _ in range(count_music):
#     name_song = input("Введите название песни для добавления: ")
#     if violator_songs.get(name_song):
#         my_playlist[name_song] = violator_songs.get(name_song)
#     else:
#         print("Такой песни не нашел.")
# print("Длительность плейлиста = {0:.2f}".format(sum(my_playlist.values())))
