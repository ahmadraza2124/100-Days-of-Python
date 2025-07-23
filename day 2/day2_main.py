# print("Hello"[4])


# num_char = len(input("What is your name?"))
# print("your name has " + str(num_char) + " characters")



# number = input("Enter the 2 digit number?")

# if len(number) == 2:
#     sum = int(number[0]) + int(number[1])
#     print("Your result is " + str(sum) )


# PEMDAS rule

# print(3 * 3 + 3 / 3 - 3)

#BMI calculator

# height = float(input('enter your height in m: '))
# weight = float(input('enter your weight in kg: '))

# calculated_bmi = weight / (height ** 2)

# print('your BMI is ' + str(int(calculated_bmi)))


# score = 10
# height = 1.8 
# isWinning = True

# print(f'your score is: {score}, your height is {height}, and you are winning {isWinning}')


# age = input('enter your age: ')

# age_as_int = int(age)

# years_remaining = 80 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remianing = years_remaining * 52
# months_remaining = years_remaining * 12

# total_time = f"you have {days_remaining} days remaining, {weeks_remianing} weeks, and {months_remaining} months"
# print(total_time)


print('welcome to the tip calculator')

total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What percent tip would you like to give? 10, 12, 15? '))
split_bill = int(input('How many people should split the bill? '))

tip_percentage = (total_bill * tip_percentage) / 100
bill_with_percentage = total_bill + tip_percentage
splited_bill = bill_with_percentage / split_bill

print(f'Each person should have to pay: {round(splited_bill , 2)}')