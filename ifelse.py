#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 20
if age >= 18:
	print('your age is', age)
	print('adult')

age = 3
if age >= 18:
	print('your age is', age)
	print('adult')
else: # 别忘了冒号
	print('your age is', age)
	print('teenager')

if age >= 18:
	print('adult')
elif age >= 6: # elif是else if的缩写
	print('teenager')
else:
	print('kid')

>>> birth = input('birth: ')
birth: 1992
>>> if birth < 2000:
...     print('00前')
... else:
...     print('00后')
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() < int()
>>> s = input('birth')
birth 1992
>>> birth = int(s)
>>> if birth < 2000:
...     print('00前')
... else:
...     print('00后')
...
00前

height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi <= 18.5:
	print('过轻')
elif bmi <= 25:
	print('正常')
elif bmi <= 28:
	print('过重')
elif bmi <= 32:
	print('肥胖')
else:
	print('严重肥胖')
