import json

import random

nested_list = [
    [
        1, 2, 3
    ], 
    [
        4, 5
    ], 
    [
        6, 7, 8, 9
    ]
    ]

# Flatten the nested list
flattened_list = [item for sublist in nested_list for item in sublist]

# Pick a random item
random_item = random.choice(flattened_list)
print(f"Random item from flattened list: {random_item}")

nested_list = [
    ["apple", "banana"],
    ["cherry", "date", "fig"],
    ["grape"]
]

# Flatten the nested list
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

# Select a random item from the flattened list
random_item = random.choice(flat_list)

print(f"The random item is: {random_item}")