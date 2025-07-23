# import random

# random_int = random.randint(1 , 10)
# print(random_int)

# random_float = random.random()
# print(random_float)


# random_side = random.randint(0, 1)

# if random_side == 0:
#     print('Heads')
# else:
#     print('Tails')


# us_states = [
#     "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
#     "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
#     "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
#     "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
#     "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
#     "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
#     "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
#     "Wisconsin", "Wyoming"
# ]

# us_states[0] = "obama"

# us_states.append("new state")
# us_states.extend(['angelaland' , 'jack bauer land'])

# print(us_states) 


# import random

# names_string = input("Give me everybody's names, seperated by comma. ")
# names = names_string.split(", ")

# # total_person = len(names)

# # select_random = random.randint(0 , total_person)

# # select_person = names[select_random]

# select_person = random.choice(names)

# print(select_person)



# us_states = [
#     "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
#     "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
#     "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
#     "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
#     "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
#     "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
#     "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
#     "Wisconsin", "Wyoming"
# ] 

# num_of_states = len(us_states)

# print(us_states[num_of_states - 1])


# fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple", "Strawberry"]
# vegetables = ["Carrot", "Broccoli", "Spinach", "Potato", "Tomato", "Cucumber", "Onion"]

# dirty_dozens = [fruits,vegetables]

# print(dirty_dozens)


# row1 = ['⬜', '⬜', '⬜']
# row2 = ['⬜', '⬜', '⬜']
# row3 = ['⬜', '⬜', '⬜']
# map = [row1, row2, row3]

# print("Treasure Map:")
# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? (columnrow, e.g., 23): ")

# horizontal = int(position[0]) 
# vertical = int(position[1])   

# map[vertical - 1][horizontal - 1] = '❌'

# print("\nUpdated Treasure Map:")
# print(f"{row1}\n{row2}\n{row3}")


import random

choices = ["Rock", "Paper", "Scissors"]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if user_input < 0 or user_input > 2:
    print("Invalid input. You lose!")
else:
    computer_choice = random.randint(0, 2)

    print(f"\nYou chose: {choices[user_input]}")
    print(f"Computer chose: {choices[computer_choice]}\n")

    if user_input == computer_choice:
        print("It's a draw! Play again.")
    elif (user_input == 0 and computer_choice == 2) or \
         (user_input == 1 and computer_choice == 0) or \
         (user_input == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
