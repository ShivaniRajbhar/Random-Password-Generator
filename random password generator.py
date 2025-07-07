
import random
import string

def generate_password(length):
    characters = string.ascii_letters+string.digits+string.punctuation
    password="".join(random.choice(characters)  in range(length))
    return password

print("Random Password Generator")
try:
    length=int(input("Enter desired password length:"))
    if length < 4:
        print("Password should atleast 4 characters long.")
    else:
        print("Generated Password:",
              generate_password(length))
    except ValueError:
print("Please enter a valid number:")