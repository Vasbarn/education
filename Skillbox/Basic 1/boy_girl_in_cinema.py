boy = int(input("Мальчиков:"))
girl = int(input("Девочек: "))
string = ""
if girl <= 0 or girl <= 0:
	print("Невозможно!")
elif boy * 2 < girl or girl * 2 < boy:
	print("Невозможно!")
elif boy >= girl:
	difference = boy - girl
	for bgb in range(difference):
		string += "BGB"
	for bg in range(boy - difference):
		string += "BG"
else:
	difference = girl - boy
	for bgb in range(difference):
		string += "GBG"
	for gb in range(girl - difference):
		string += "GB"
print(string)


