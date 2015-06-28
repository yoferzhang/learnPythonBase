#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)
'''
Michael
Bob
Tracy
'''

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + x
print(sum)
'''
>>> list(range(5))
[0, 1, 2, 3, 4]
'''

sum = 0
for x in range(101):
	sum = sum + x
print(sum) # 5050

#计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum) # 2500

#练习
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('Hello,', name)
'''
Hello, Bart
Hello, Lisa
Hello, Adam
'''