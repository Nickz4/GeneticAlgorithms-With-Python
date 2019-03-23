#!/usr/bin/env python3
# coding:utf-8
import random
from Questions.quadratic import *


ga = QuadraticSolotion(equation = lambda x: (x ** 2 - 10 * x + 5), boundary=(0,63),generations=30, population_size=4,)
ga.search()
solution = ga.get_result()
print('Solution :{}'.format(solution.decimal_number))






# c= [DataProcess(random.randint(0,63)) for _ in range(10)]
# print(c)
# print(type(c))
# for x in c:
#     print(x.decimal_number)
#     print(type(x))
