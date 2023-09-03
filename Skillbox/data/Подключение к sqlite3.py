import peewee
import datetime
import sqlite3

# создание бд
database = peewee.SqliteDatabase("my_base.db")


# что бы создать таблицу надо создать класс от
class BaseTable(peewee.Model):
	#  в подклассе Мета подключение к базе
	class Meta:
		database = database


class Artist(BaseTable):
	name = peewee.CharField()  # тип поля


class Album(BaseTable):
	artist = peewee.ForeignKeyField(Artist)
	title = peewee.CharField()
	release_date = peewee.DateTimeField()
	publisher = peewee.CharField()
	media_type = peewee.CharField()


# Создание таблицы
database.create_tables([Artist, Album])

conn = sqlite3.connect("my_base.db",)
conn.text_factory = bytes
cursor = conn.cursor()


# Первый способ: явный save()
new_artist = Artist(name="Данил")
new_artist.save()
# Второй способ:
album_one = Album.create(
	artist="Данил",
	title="Утро Доброе",
	release_date=datetime.date(day=12, month=11, year=2022),
	publisher="РусРекорд",
	media_type="String"
)


cursor.execute("SELECT * FROM 'Artist'")
result = cursor.fetchall()
print(result)