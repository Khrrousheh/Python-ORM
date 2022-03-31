from datetime import date
from Schema import db, Movie


db.connect()

template = '{movie.title} ({movie.release_date}) {movie.rating}/10'

print("Get All Titles ...\n")

for movie in Movie.select():
    print(template.format(movie=movie))

print('-'*40)
print("Starts With Blade \n")

for movie in Movie.select().where(Movie.title.startswith("Blade")):
    print(template.format(movie=movie))

print('-'*40)
print("Released After 1971\n")

for movie in Movie.select().where(Movie.release_date > date(1971,1,1)):
    print(template.format(movie=movie))

print('-'*40)
print("Sorted by Name\n")

for movie in Movie.select().order_by(Movie.title.asc()):
    print(template.format(movie=movie))

print('-'*40)
print("Sorted by Rating\n")

for movie in Movie.select().order_by(Movie.rating.desc()):
    print(template.format(movie=movie))
