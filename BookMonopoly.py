import random
import json

# A Simple list of genre. Program returns a random a prompt based on a dice roll.

spaces_on_board = [
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

dice_roll = random.randint(1,12)
print(f"You rolled {dice_roll}")

random_space_picked = spaces_on_board[dice_roll]

# User input & Return of genre & board position.

print(f"Moving to: {random_space_picked} ")


