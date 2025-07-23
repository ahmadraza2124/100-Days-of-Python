# Dictornaries
# Syntax

# {"key": "value"}


# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }

# print(person["name"])


# person["height"] = 5.9

# print([person])

# person["name"] = "Ahmad"

# print(person)


# #LOOP through dictionary

# for i in person:
#     print(i)



# students = {
#     "Alice": 85,
#     "Bob": 94,
#     "Charlie": 78,
#     "David": 92,
#     "Eva": 88
# }


# student_grades = {}


# for student in students:
#     score = students[student]

#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Failed"


# print(student_grades)



#####################################################################################

# Nesting with list

# travel_log = {
#     'France' : {'cities_visitied' : ['Paris', 'lille', 'dijon'], 'total_visited' : 12},
#     'Germany': ['Berlin', 'hamburg', 'stuttgart']
# }


# travel_log = [
#     {
#         'France' : {'cities_visitied' : ['Paris', 'lille', 'dijon'], 'total_visited' : 12},
#     },
#     {
#         'Germany': ['Berlin', 'hamburg', 'stuttgart']
#     }
# ]
    


travel_log =  [
    {
        'country' : 'France',
        'visits' : 12,
        'cities' : ['Paris', 'Lille', 'Dijon']
    },
    {
        'country' : 'Germany',
        'visits' : 5,
        'cities' : ['Berlin', 'Hamburg', 'Stuttgart']
    }
]



# def add_mew_country(country, visits, cities):
#     new_country = {}
#     new_country['country'] = country
#     new_country['visits'] = visits
#     new_country['cities'] = cities
#     travel_log.append(new_country)

# add_mew_country('russia', 2, ['moscow', 'saint petersburg'])

# print(travel_log)

import os

bid_over = False
bid_detials = []


while not bid_over:
    name = input('Enter your name: ')

    bid_price = int(input('Enter your bid price: $'))

    next_bidder = input('Is there any bidder enter Y for Yes and N for No: ').upper()

    new_details = {}
    new_details['name'] = name
    new_details['bid'] = bid_price
    bid_detials.append(new_details)

    if next_bidder == 'N':
        bid_over = True
    else:
        os.system('cls')


highest_bid = 0
winner = ''

for bidder in bid_detials:
    if bidder['bid'] > highest_bid:
        highest_bid = bidder['bid']
        winner = bidder['name']


print(f'The winner is {winner} with the higest bid {highest_bid}')

