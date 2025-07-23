# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print('You got it')

# my_function()


# from random import randint
# dice_images = ['1️⃣', '2️⃣','3️⃣', '4️⃣', '5️⃣', '6️⃣']
# dice_number = randint(0 , 5)
# print(dice_images[dice_number])


# year = int(input("Whats your year of birth? "))
# if year > 1980 and year < 1994:
#     print('You are a millenial')
# elif year >= 1994:
#     print("You are a Gen-Z")


# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")


pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)