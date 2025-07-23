# def return_plus(num1, num2):
#     result = num1 + num2
#     return result

# output = return_plus(5,5)

# print(output)


# def format_name(f_name, l_name):

#     if f_name == '' or l_name == '':
#         return 'Please enter a valid name'

#     title_case_f_name = f_name.title()
#     title_case_l_name = l_name.title()

#     return f'Result: {title_case_f_name} {title_case_l_name}'

# first_name = input('What is your first name? ')
# last_name = input('What is your last name? ')

# print(format_name(first_name, last_name))



# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True  
#     else:
#         return False

# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return 'Invalid month'
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1] 

# # User input
# check_year = int(input("Enter a year: "))
# check_month = int(input("Enter a month (1-12): "))

# days = days_in_month(check_year, check_month)
# print(f"Days in month {check_month} of year {check_year}: {days}")




def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': sub,
    '*': multi,
    '/': divide
}

def calculator():
    num1 = float(input("What's the first number? "))
    
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))

        calculation_function = operations[operator]
        result = calculation_function(num1, num2)
        print(f'{num1} {operator} {num2} = {result}')

        action = input(f'Type "y" to continue calculating with {result}, or "n" to start a new calculation: ').lower()
        
        if action == 'y':
            num1 = result  
        else:
            should_continue = False
            print("🔁 Starting a new calculation...")
            calculator() 

calculator()
