# шаблоны это пиздец
# почти целый язык


more_text = '''
Привет как дела как здоровье как дела мне нравятся губы твои и глаза. Давай познакомимся давай познакомимся
122 @ mail.ru  123@mail.ru   1232@mail.ru 1232mail'''



my_pattern = r"\w{,3}[1-3]@\w{,7}"
import re


matced = re.match(my_pattern, more_text ) # только с начала строки
print(matced)
searched = re.search(my_pattern, more_text)
print(searched)
print(searched.group())
for i in re.finditer(my_pattern, more_text):
	print(i)

x = re.sub(r"к\w{2}",  "", more_text)
print(x)
x = re.sub(r"к\w{2}\s+",  "", more_text)
print(x)