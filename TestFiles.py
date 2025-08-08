import json
import random

spaces_on_board = [
    'Start Reading',
    'Read a book that has less than 250 pages',
    'Read a book that has been recommended online',
    'Read a book that has more than 400 pages',
    'Read a book chosen with your eyes closed',
    'Start a new book series',  
    'Read a book with a blue cover',
    'Reader Choice',
    'Read a book with a red cover',
    'Read a book with a white cover',
    'Read a book you have benn avoiding'
    'Read a book that you bought because of the cover',
    'Listen to an audiobook',
    'Read a book that has a person on the cover',
    'Rad a book that has an animal or natue on the cover',
    'Read a book in the Top 100 on Goodreads',
    'Read a book that has one word in the title',
    'Read a book recommended by a friend or faimly',
    'Read a book that has 4 or more words in the title',
    'Read a book whose title begines with the first letter of your name',
    'Rest Stop: Read a book that is easy going or a comfort read',
    'Read a book that you were gifted by someone else',
    'Reader Choice',
    'Read a book tha was written before 2010',
    'Read a book that has been on your bookshelf/TBR the longest',
    'Read a book by an author writing aunder a psuedonym',
    'Read a book from your favorite genre',
    'Read a non-fiction book or a book based on a true story',
    'Read a boo that has been turned into a movie or tv show',
    'Read a book outside of your comfort genre(s)',
    'Go to Jail',
    'Read a book setin a country you would like to visit',
    'Read a book set more than 50 years ago',
    'Read a book recommended by someone who is not your generation',
    'Read a book set in the current season',
    'Re-read your favorite book',
    'Read a book that won an award',
    'Read a book by a female author',
    'Reader Choice',
    'Read a book by your favorite author'
]


dice_roll = 0

random_space_picked = spaces_on_board[dice_roll]
number_of_spaces = len(spaces_on_board)

print(f'Total number of spaces : {number_of_spaces}')
current_position = 0
current_position = current_position + dice_roll
left = number_of_spaces - current_position

print(f'dice Roll : {dice_roll}')
print(f'current Space :    {current_position}')
print(f'number of spaces left:  {left}')


print('Roll the DICE!!!  Type T or t ')
rolling_dice = input()




def get_book_data(current_position):
    random_space_picked = spaces_on_board[current_position]
    print(f'Picking :  {current_position} --> {random_space_picked}')
    print('Enter the title of the book you read: ')
    book_title = input()
    print('Enter the author of the book you read: ')
    book_author = input()
    return {
        'Prompt': random_space_picked,
        'Title': book_title,
        'Author': book_author
    }


def roll_dice_and_get_position(current_position, number_of_spaces):
    dice_roll = random.randint(2,12)
    current_position = (current_position + dice_roll) % number_of_spaces
    return current_position