
import random
import json

# This is the more complicated list. It works

dice_roll = random.randint(1,6)

print(f'You Rolled: {dice_roll}')

genres = [
    {
        'name': 'Action & Adventure',
        'subgenre':[]
    },
    {
        'name': 'Crime & Mystery',
        'subgenre': []
    },
    {
        'name': 'Fantasy',
        'subgenre': [
            'Dark',
            'Magical',
            'Dark',
            'Sword & Socrery'
        ]
    },
    {
        'name': 'Horror',
        'subgenre':[]
    },
    {
        'name': 'Literary Fiction',
        'subgenre':[]
    },
    {
        'name': 'Romance',
        'subgenre':[
            'Contemporary',
            'Historical',
            'Paranormal'
        ]
    },
    {
        'name': 'Science Fiction',
        'subgenre':[
            'Dystopian',
            'Cyberpunk'
        ]
    },
    {
        'name': 'Science Fiction',
        'subgenre':[
            'Dystopian',
            'Cyberpunk'
        ]
    },
    {
        'name': 'Western',
        'subgenre':[]
    },
    {
        'name': 'Children',
        'subgenre':[]
    },
    {
        'name': 'Young Adult',
        'subgenre':[]
    },
    {
        'name': 'Thriller & Suspense',
        'subgenre':[
            'Psychological',
            'Political',
            'Legal'
        ]
    },
    {
        'name': 'Biography & Memior',
        'subgenre':[]
    },
    {
        'name': 'History',
        'subgenre':[]
    },
    {
        'name': 'Self-Help',
        'subgenre':[]
    },
    {
        'name': 'Science & Technology',
        'subgenre':[]
    },
    {
        'name': 'Trime Crime',
        'subgenre':[]
    },
    {
        'name': 'Poetry',
        'subgenre':[]
    },
    {
        'name': 'Graphic Novel',
        'subgenre':[
            'Manga',
            'Comic'
        ]
    }
]


genre_dump = json.dumps(genres)
genre_load = json.loads(genre_dump)

random_genre = random.choice(genres)

print("Your random genre is:")
print(f"Name: {random_genre['name']}")

print(genre_load[dice_roll])




