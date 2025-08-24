import csv
import os
import BookMonopoly


def file_has_data(filepath):
    return os.path.exists(filepath) and sum(1 for _ in open(filepath)) > 1  # assumes header

def get_last_position(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        if len(lines) > 1:
            last_line = lines[-1].strip().split(',')
            try:
                return int(last_line[0])  # assumes PromptPosition is int
            except Exception:
                return 0
        else:
            return 0

number_of_spaces = len(BookMonopoly.spaces_on_board)
csv_file = 'game_output.csv'

if file_has_data(csv_file):
    current_position = get_last_position(csv_file)
else:
    current_position = 0

with open('game_output.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    while True:
        current_position, dice_roll = BookMonopoly.roll_dice_and_get_position(current_position, number_of_spaces)

        #Start of Rolls
        #print('Roll the DICE!!!  Type T or t ')
        #rolling_dice = input()
        #print(f'Dice roll: {dice_roll}')

        book_data = BookMonopoly.get_book_data(current_position, dice_roll)
        writer.writerow([book_data['PromptPosition'],book_data['Prompt'], book_data['Title'], book_data['Author']])
        print('Roll Again? (t to continue, any other key to stop)')
        continue_choice = input().strip().lower()
        if continue_choice != 't':
            break
    print('Data written to game_output.csv successfully!')

