# Task 1  function that takes name of a user and returns Hello <Username>

def greet_user(username):
    return "Hello " + username

# Example usage:
user_name = input("Please enter your name: ")
greeting_message = greet_user(user_name)
print(greeting_message)

# Task 2: a function that takes the date of birth of a user and returns age
from datetime import datetime

def calculate_age(date_of_birth):
    current_date = datetime.now()
    age = current_date.year - date_of_birth.year - ((current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day))
    return age

# Example usage:
date_of_birth_input = input("Please enter your date of birth (YYYY-MM-DD): ")
date_of_birth = datetime.strptime(date_of_birth_input, "%Y-%m-%d")
age = calculate_age(date_of_birth)
print("Your age is:", age)

# Task 3: use the above functions to make the Command line app to simply take Name and Date of birth as input and print "Hello <Username>, your age is <calculated age> years"

