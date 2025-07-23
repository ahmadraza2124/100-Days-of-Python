# def greet():
#  print("Hello")
#  print("how do you do?")
#  print("isn't the weather nice today?")

# greet()


# def great_with_name(name):
#  print(f"hello {name}")
#  print(f"How do you do? {name}")

# great_with_name("Ahmad")


# Function more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?") 

# greet_with("Ahmad", "Lahore")


# # Keyword arguments

# def my_fundtion(a, b, c):
#     print(f"This is {a}")
#     print(f"This is {b}")
#     print(f"This is {c}")

# my_fundtion(c=3, a=1, b=2)

# import math

# def paint_cal(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"Number of cans required for the wall are {number_of_cans}")


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# paint_cal(height=test_h, width=test_w, cover=coverage)


# def prime_checker(number): 
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime =  False
#     if is_prime:
#         print("Its a prime number")
#     else:
#         print("Its not a prime number")


# n = int(input("Check this number: "))
# prime_checker(number=n)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == 'decode':
            shift_amount *= -1

    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
             end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")



should_countinue = True

while should_countinue:
    direction =  input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, cipher_direction=direction, shift_amount=shift)

    result = input("Type Yes if you want to do this again or type No to shutdown: ").lower()

    if result == 'no':
        should_countinue = False
        print("Good Bye")