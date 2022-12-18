import random
import string

def generate_password(strength, num_chars):
  if strength == "weak":
    chars = string.ascii_lowercase
  elif strength == "medium":
    chars = string.ascii_letters + string.digits
  elif strength == "strong":
    chars = string.ascii_letters + string.digits + string.punctuation
  else:
    return "Invalid password strength"

  password = ''.join(random.choice(chars) for i in range(num_chars))
  return password

num_passwords = int(input("How many passwords do you want to generate? "))
strength = input("Enter the password strength (weak, medium, strong): ")
num_chars = int(input("Enter the number of characters for the password: "))

for i in range(num_passwords):
  print(generate_password(strength, num_chars))