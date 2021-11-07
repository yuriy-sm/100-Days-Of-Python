#day2_theory
# data types
#Strings
# print("Hello"[4])
# print("Hello " + "World")

#Integer
# print(123 + 123)
# print(123_456_789)

#Float
# print(3.14)

#Boolean
# True 
# False

#Excerice Data types 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# print(type(two_digit_number))
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

#mathematical operators
# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3 #result is always float
# 2 ** 3 #raise number to power 2 power of 3

# round
# print(8//3) #contert result into integer 2.6666 = 2
# print(round(8/3)) #rounds number 2.666 = 3

# Excercise BMI calculator 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
# BMI = float(weight) / float(height) **2
# print(int(round(BMI))
#Write your code below this line 👇

#fsting
# score = 0
# height = 0
# isWinning = True
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")



# day2_project
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

welcome_msg = "Welcome to the tip calculator.\n"
print(welcome_msg)
total_bill = float(input("What was the total bill? $\n"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
number_of_people = int(input("How many people to split the bill?\n"))
tips = total_bill * (percentage_tip / 100) 
result = (total_bill + tips) / number_of_people
round(result, 2)
print(f"Each person should pay: {round}")