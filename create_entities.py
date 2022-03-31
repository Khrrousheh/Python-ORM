from datetime import date, datetime
import os
from turtle import title

from Schema import db, Movie

os.remove('movies.db')

db.connect()
db.create_tables([Movie])

blade_runner = Movie.create(
    title = 'Blade Runner',
    release_date = date(1982,6,25),
    rating = 10
)


blade_runner.save()

movies = (
    ("Blade Runner 2049", 2018, 9),
    ("2001: a space odyssey", 1968, 10),
    ("Godzilla vs Hedorah", 1968, 6),
    ("Silnet Running", 1972,8)
) 

for movie in movies:
    Movie.create(title = movie[0], release_date = date(movie[1],1,1), rating = movie[2])

