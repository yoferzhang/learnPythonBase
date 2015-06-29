#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def power(x):
	return x * x

def power(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

power(x, n) # x和n都是位置参数

def power(x, n = 2): # 默认参数
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

>>> def power(x):
...     return x * x
...
>>> power(5)
25
>>> def power(x, n):
...     s = 1
...     while n > 0:
...             n = n - 1
...             s = s * x
...     return s
...
>>> power(5, 2)
25
>>> power(5) # 原来一个参数的函数失效了
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: power() missing 1 required positional argument: 'n'
>>> def power(x, n = 2): # 默认参数
...     s = 1
...     while n > 0:
...             n = n - 1
...             s = s * x
...     return s
...
>>> power(5)
25

def enroll(name, gender, age = 6, city = 'Beijing'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)

>>> def enroll(name, gender, age = 6, city = 'Beijing'):
...     print('name:', name)
...     print('gender:', gender)
...     print('age:', age)
...     print('city:', city)
...
>>> enroll('Sarah', 'F')
name: Sarah
gender: F
age: 6
city: Beijing
>>> enroll('Bob', 'M', 7
... )
name: Bob
gender: M
age: 7
city: Beijing
#当不按顺序提供部分默认参数时，需要把参数名写上
>>> enroll('Adam', 'M', city = 'Tianjin')
name: Adam
gender: M
age: 6
city: Tianjin

def addEnd(L = []):
	L.append('END')
	return L

>>> def addEnd(L = []):
...     L.append('END')
...     return L
...
>>> addEnd([1, 2, 3])
[1, 2, 3, 'END']
>>> addEnd(['x', 'y', 'z'])
['x', 'y', 'z', 'END']
>>> addEnd()
['END']
>>> addEnd() # 再调用，不对了
['END', 'END']
>>> addEnd()
['END', 'END', 'END']

def addEnd(L = None):
	if L is None:
		L = []
	L.append('END')
	return L

>>> def addEnd(L = None):
...     if L is None:
...             L = []
...     L.append('END')
...     return L
...
>>> addEnd()
['END']
>>> addEnd()
['END']

def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

>>> def calc(*numbers):
...     sum = 0
...     for n in numbers:
...             sum = sum + n * n
...     return sum
...
>>> calc(1, 3, 5, 7)
84
>>> nums = [1, 2, 3]
>>> calc(*nums)
14

def person(name, age, **kw):
	print('name', name, 'age:', age, 'other:', kw)

>>> def person(name, age, **kw):
...     print('name', name, 'age:', age, 'other:', kw)
...
>>> person('Michael', 30)
name Michael age: 30 other: {}
>>> person('Bob', 35, city = 'Beijing')
name Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender = 'M', job = 'Engineer')
name Adam age: 45 other: {'job': 'Engineer', 'gender': 'M'}
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, cith = extra['city'], job = extra['job'])
name Jack age: 24 other: {'cith': 'Beijing', 'job': 'Engineer'}
>>> person('jack', 24, **extra)
name jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

def person(name, age, *, city, job):
	print(name, age, city, job)
# 命名关键字参数需要一个特殊分割符*
# *后面的参数被视为命名关键字参数。

>>> def person(name, age, *, city, job):
...     print(name, age, city, job)
...
>>> person('Jack', 24, city = 'Beijing', job = 'Engineer')
Jack 24 Beijing Engineer
#命名关键字必须传入参数名，这和位置参数不同。如果没有传入
#参数名，调用报错
>>> person('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() takes 2 positional arguments but 4 were given

def person(name, age, *, city = 'Beijing', job):
	print(name, age, city, job)
>>> def person(name, age, *, city = 'Beijing', job):
...     print(name, age, city, job)
...
>>> person('Jack', 24, job = 'Engineer')
Jack 24 Beijing Engineer

def f1(a, b, c = 0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c = 0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

>>> def f1(a, b, c = 0, *args, **kw):
...     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
...
>>> def f2(a, b, c = 0, *, d, **kw):
...     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
...
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c = 3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x = 99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d = 99, ext = None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'x': '#', 'd': 99}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
