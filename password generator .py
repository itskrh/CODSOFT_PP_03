# Python Password Generator

import random
import string

def password_generator(length):
   all_characters = string.ascii_letters + string.digits + string.punctuation
   if length < 8:
      print("Password length should be at least 8 characters.")
      return None
   password = ''.join(random.choice(all_characters) for i in range(length))
   return password

print("Welcome to Password Generator!")

while True:
   length = int(input("Enter the length of the password (at least 8 characters): "))
   password = password_generator(length)
   if password:
      print("Generated Password : ", password)
      break