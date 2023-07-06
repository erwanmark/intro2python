from peewee import *
from os import path

# creating our first database
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "genesis.db"))


# creating table inside db
class Student(Model):
    name = CharField()
    gender = CharField(unique=True)
    studentcode = CharField()
    phonenumber = CharField()
    age = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)