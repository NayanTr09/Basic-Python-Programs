'''
@Author: Nayan Tripathi
@Date: 2021-03-28 10:00:00
@Title : Username
'''

Username = input(" What is your username? ")
UsernameLength = len(Username)
if UsernameLength >= 3:
  print(f"Your Username is {Username}")
else:
  print("Username is too short! (Minimum is 3 characters)")

