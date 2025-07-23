# print("Welcom to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride!")
# else:
#     print("Sorry, You can't ride!")


# number = int(input("Enter you number! "))

# if number % 2 == 0:
#     print("This number is even number")
# else:
#     print("This is an odd number")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride!")
#     age = int(input("Enter your age: "))
#     if age < 12:
#         print("You'll get 5 dollar ticket")
#     elif age <= 18:
#         print("You'll get 7 dollar ticket")
#     else:
#         print("You are above 18, you must buy 12 dollar ticket")
# else:
#     print("Sorry, You can't ride!")




#BMI calculator

# height = float(input('Enter your height in meters: '))
# weight = float(input('Enter your weight in kilograms: '))

# calculated_bmi = weight / (height ** 2)

# if calculated_bmi < 18.5:
#     print(f'You are underweight. Your BMI is {calculated_bmi:.2f}')
# elif 18.5 <= calculated_bmi < 25:
#     print(f'You are normal weight. Your BMI is {calculated_bmi:.2f}')
# elif 25 <= calculated_bmi < 30:
#     print(f'You are overweight. Your BMI is {calculated_bmi:.2f}')
# elif 30 <= calculated_bmi < 35:
#     print(f'You are obese. Your BMI is {calculated_bmi:.2f}')
# else:
#     print(f'You are clinically obese. Your BMI is {calculated_bmi:.2f}')


# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("leap year")  
# else:
#     print("Not a leap year")


# print("Welcome to the rollercoaster!")
# bill = 0
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride!")
#     age = int(input("Enter your age: "))
#     if age < 12:
#         bill = 5
#         print(f"Child tickets are for {bill} dollar ticket")
#     elif age <= 18:
#         bill = 7
#         print(f"Youth tickets are for {bill} dollar ticket")
#     elif age >= 45 and age <= 55:
#         print("Everything is ok. Have a ride")
#     else:
#         bill = 12
#         print(f"Adult tickets are for {bill} dollar ticket")

#     wants_photo = input("Do you want photo? Y or N ")
#     if wants_photo == "Y":
#         bill += 3
#         print(f'you have to pay $3 extra! Your total bill is {bill}')

# else:
#     print("Sorry, You can't ride!")



# print("Welcome to Python Pizza Delivery!")
# pizza_price = 0

# size = input('What size do you want? S, M, L: ')
# add_pepperoni = input("Do you want extra pepperoni? Y or N: ")
# extra_cheese = input('Do you want extra cheese? Y or N: ')


# if size == "S":
#     pizza_price = 15
# elif size == "M":
#     pizza_price = 20
# elif size == "L":
#     pizza_price = 25 


# if add_pepperoni == "Y":
#     if size == "S":
#         pizza_price += 2
#     else:
#         pizza_price += 3


# if extra_cheese == "Y":
#     pizza_price += 1

# print(f"Your total bill is ${pizza_price}")



# print("Welcome to the Treasure Island.")
# print("Your mission is to find the treasure.")

# direction = input("Where do you want to go? Left or Right: ").lower()

# if direction == "left":
#     movement = input("You arrived at a river. Do you want to swim or wait? ").lower()
#     if movement == "wait":
#         door = input("You see three doors. One red, one blue, and one yellow. Which door do you choose? ").lower()
#         if door == "yellow":
#             print("You found the treasure! You Win! 🎉")
#         elif door == "red":
#             print("It's a room full of fire. Game Over.")
#         elif door == "blue":
#             print("You were eaten by beasts. Game Over.")
#         else:
#             print("That door doesn't exist. Game Over.")
#     else:
#         print("You were attacked by a crocodile. Game Over.")
# else:
#     print("You fell into a hole. Game Over.")
