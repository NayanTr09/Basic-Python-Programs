'''
@Author: Nayan Tripathi
@Date: 2021-03-28 10:00:00
@Title : Powerof2
'''

terms = int(input("How many terms? "))
result = list(map(lambda x: 2 ** x, range(terms)))
for i in range(terms):
   print("2 raised to power",i,"is",result[i])