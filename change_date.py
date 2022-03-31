from datetime import date
from Schema import Movie

template = '{movie.title} ({movie.release_date}) {movie.rating}/10'

Movie.create(title='The Matrix', release_date = date(1999,3,31), rating=5)

bad_movies = Movie.create(title= "Mortel Kombat: Annihilation", release_date = date(1997,11,21), rating= 9)

print('-'*40)
print("Sorted by the rating (Why is The Matrix so Low and MK:A so high?)\n")

for movie in Movie.select().order_by(Movie.rating.desc()):
    print(template.format(movie=movie))

# Use an Update Query
Movie.update(rating=10).where(Movie.title=="The Matrix").execute()

bad_movies.rating = 5
bad_movies.save()

print("-"*40)
print("Sorted By Rating (Better!)\n")

for movie in Movie.select().order_by(Movie.rating.desc()):
    print(template.format(movie=movie))