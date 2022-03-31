from operator import index
from turtle import title
from peewee import SqliteDatabase, Model, TextField, DateField, IntegerField

db = SqliteDatabase('movies.db')

class BasedTable(Model):
    class Meta:
        database = db

class Movie(BasedTable):
    title = TextField(null=False, index= True)
    release_date = DateField (null= False, index = True)
    rating = IntegerField()

