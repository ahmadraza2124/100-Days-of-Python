# fruits = ["Apple", "Peach", "Pear"]


# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")


# for number in range(0, 10):
#     print(number + 1)


# student_height = [180, 124, 165, 173, 189, 169, 146]
# total_value = 0
# count = 0

# for number in student_height:
#     total_value += number
#     count += 1
#     avg_value = total_value / count
#     round_value = round(avg_value)
# print(round_value)


# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# highest_number = 0 

# for number in student_scores:
#     if number > highest_number:
#         highest_number = number
# print(highest_number)

 
# total = 0
# for num in range(1, 101):
#     total += num
# print(total)


# total_sum = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         total_sum += i 
# print(total_sum)


# for i in range(1,  101):
#     if i % 3 == 0 and i % 5 == 0: 
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


import random

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to PyPassword Generator!")

num_letters = int(input("How many letters do you want in your password?\n"))
num_symbols = int(input("How many symbols do you want in your password?\n"))
num_numbers = int(input("How many numbers do you want in your password?\n"))

password = []

for _ in range(num_letters):
    password.append(random.choice(alphabet))

for _ in range(num_symbols):
    password.append(random.choice(symbols))

for _ in range(num_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

final_password = ''.join(password)
print(f"Your generated password is: {final_password}")
