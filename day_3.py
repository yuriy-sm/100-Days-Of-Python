# day3_theory

#if statements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#   print("You can ride rollercoaster")
# else:
#   print("You are to short to ride the rollercoaster")

#excercise
# print("Even number checker")
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# remainder = number % 2
# if remainder == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

#nested if statements
# height = int(input("What is your height in cm?\n "))
# age = int(input("What is your age?\n "))
# if height >= 120:
#   print("You can ride rollercoaster")
#   if age <= 12:
#     print("Please pay $5.")
#   elif age <= 18:
#     print("Please pay $7.")
#   else:
#     print("Please pay $12.")
# else:
#   print("You are to short to ride the rollercoaster")

#excercise
# print("BMI Calculator")
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# BMI = weight / height ** 2
# if BMI < 18.5:
#   print(f"Your BMI is {round(BMI)}, you are underweight.")
# elif BMI < 25:
#   print(f"Your BMI is {round(BMI)}, have a normal weight.")
# elif BMI < 30:
#   print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
# elif BMI < 35:
#   print(f"Your BMI is {round(BMI)}, you are obese.")
# else:
#   print(f"Your BMI is {round(BMI)}, you are clinically obese.")

#excercise
# print("Check if given year is a leap year.")
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# price = 0

# if size.upper() == "S":
#     price += 15
# elif size.upper() == "M":
#     price += 20
# elif size.upper() == "L":
#     price += 25

# if add_pepperoni.upper() == "Y":
#     if size.upper() == "S":
#         price += 1
#     else:
#         price += 3

# if extra_cheese.upper() == "Y":
#     price += 1

# print(f"Your final bill is: ${price}.")

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1_lower_case = name1.lower()
# true_name_1 = name1_lower_case.count("t") + name1_lower_case.count("r") + name1_lower_case.count("u") + name1_lower_case.count("e")
# love_name_1 = name1_lower_case.count("l") + name1_lower_case.count("o") + name1_lower_case.count("v") + name1_lower_case.count("e")

# name2_lower_case = name2.lower()
# true_name_2 = name2_lower_case.count("t") + name2_lower_case.count("r") + name2_lower_case.count("u") + name2_lower_case.count("e")
# love_name_2 = name2_lower_case.count("l") + name2_lower_case.count("o") + name2_lower_case.count("v") + name2_lower_case.count("e")

# love_score_str = str(true_name_1 + true_name_2) + str(love_name_1 + love_name_2)
# love_score = int(love_score_str)

# if love_score < 10 or love_score > 90:
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 or love_score <= 50:
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is  {love_score}.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
step_1 = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right?\n'
)

if step_1.lower() == 'left':
    step_2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
    )
    if step_2.lower() == 'wait':
        step_3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
        )
        if step_3.lower() == 'yellow':
            print("You found the treasure! You Win!")
        elif step_3.lower() == 'red':
            print("It's a room full of fire. Game Over.")
        elif step_3.lower() == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
