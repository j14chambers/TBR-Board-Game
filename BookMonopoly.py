import random
import json

# A Simple list of genre. Program returns a random genre.

genres = [
    'Action & Adventure',
    'Crime & Mystery',
    'Fantasy',
    'Horror',
    'Literary Fiction',
    'Romance',  
    'Science Fiction',
    'Science Fiction',
    'Western',
    'Children',
    'Young Adult',
    'Thriller & Suspense',
    'Psychological',
    'Political',
    'Legal'
    'Biography & Memior',
    'History',
    'Self-Help',
    'Science & Technology',
    'Trime Crime',
    'Poetry',
    'Graphic Novel',
    'Manga',
    'Comic'
]


random_genre = random.choice(genres)

# User input & Return of genre & board position.



print("Your random genre is:")
print(random_genre)


