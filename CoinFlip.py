'''
@Author: Nayan Tripathi
@Date: 2021-03-28 10:00:00
@Title : CoinFlip
'''

import random

result = random.randint(0,1)
if result <= 0.5 :
  print(random.choice(['Heads', 'Tails']))
else :
  print("Not a valid coin toss")
