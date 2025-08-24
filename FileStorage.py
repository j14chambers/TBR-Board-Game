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

# Set defaults
in_jail = False
jail_turns = 0

if file_has_data(csv_file):
    current_position = get_last_position(csv_file)
    print(f'RESUMING GAME from position {current_position}')
    if current_position == 30:
        print("You are on 'Go to Jail'! Moving you to Jail (position 10).")
        current_position = 10
        in_jail = True
        jail_turns = 0
else:
    current_position = 0
    print('STARTING NEW GAME')

with open('game_output.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    if not file_has_data(csv_file):
        writer.writerow(['PromptPosition', 'Prompt', 'Title', 'Author'])  # write header if file is new

    while True:
        if in_jail:
            print("You're in Jail! Roll doubles to get out.")
            die1, die2 = BookMonopoly.roll_two_dice()
            print(f'You rolled: {die1} and {die2}')
            if die1 == die2:
                print("You rolled doubles! You're out of jail.")
                in_jail = False
                dice_roll = die1 + die2
                current_position = (current_position + dice_roll) % number_of_spaces
                book_data = BookMonopoly.get_book_data(current_position, dice_roll)
                writer.writerow([book_data['PromptPosition'], book_data['Prompt'], book_data['Title'], book_data['Author']])
            else:
                jail_turns += 1
                print("Not doubles. Stay in jail.")
                if jail_turns >= 3:
                    print("You've served your time. You're out of jail!")
                    in_jail = False
                    jail_turns = 0
            # Ask if they want to continue
            print('Roll Again? (t to continue, any other key to stop)')
            continue_choice = input().strip().lower()
            if continue_choice != 't':
                break
            continue  # This continue is now at the correct level
        else:
            prev_position = current_position
            current_position, dice_roll = BookMonopoly.roll_dice_and_get_position(current_position, number_of_spaces)
            # Check if landed on or passed 'Go to Jail'
            if (
                (prev_position < 30 <= current_position) or
                (prev_position > current_position and (prev_position < 30 or current_position >= 30)) or
                (current_position == 30)
            ):
                print("Oh no, you've landed on or passed 'Go to Jail'! Moving you to Jail (position 10).")
                current_position = 10
                in_jail = True
                jail_turns = 0
                continue
            book_data = BookMonopoly.get_book_data(current_position, dice_roll)
            writer.writerow([book_data['PromptPosition'], book_data['Prompt'], book_data['Title'], book_data['Author']])
            print('Roll Again? (t to continue, any other key to stop)')
            continue_choice = input().strip().lower()
            if continue_choice != 't':
                break
print('Data written to game_output.csv successfully!')
