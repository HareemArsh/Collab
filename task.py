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


#from datetime import datetime

def greet_user(username):
    return "Hello " + username

def calculate_age(date_of_birth):
    current_date = datetime.now()
    age = current_date.year - date_of_birth.year - ((current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day))
    return age

def main():
    # Input name
    username = input("Please enter your name: ")

    # Input date of birth
    date_of_birth_input = input("Please enter your date of birth (YYYY-MM-DD): ")
    date_of_birth = datetime.strptime(date_of_birth_input, "%Y-%m-%d")

    # Calculate age
    age = calculate_age(date_of_birth)

    # Greet user and print age
    greeting_message = greet_user(username)
    print(f"{greeting_message}, your age is {age} years")

if __name__ == "__main__":
    main()

