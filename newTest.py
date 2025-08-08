import csv
import TestFiles

number_of_spaces = len(TestFiles.spaces_on_board)
current_position = 0

with open('output_dict.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    while True:
        current_position = TestFiles.roll_dice_and_get_position(current_position, number_of_spaces)
        book_data = TestFiles.get_book_data(current_position)
        writer.writerow([book_data['Prompt'], book_data['Title'], book_data['Author']])
        print('Do you want to add another book? (t to continue, any other key to stop)')
        continue_choice = input().strip().lower()
        if continue_choice != 't':
            break
    print('Data written to output_dict.csv successfully!')

