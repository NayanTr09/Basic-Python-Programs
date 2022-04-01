'''
@Author: Nayan Tripathi
@Date: 2021-03-28 10:00:00
@Title : LeapYear
'''

year = input("Enter a year")
if(int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0):
    print("Leap Year")
else :
    print("Not a leap year")
