#!/usr/bin/env python3
# -*- coding: utf-8 -*-

>>> classmates = ['Michael', 'Bob', 'Tracy'] # 
>>> classmates
['Michael', 'Bob', 'Tracy']
>>> len(classmates)
3
>>> classmates[0]
'Michael'
>>> classmates[1]
'Bob'
>>> classmates[2]
'Tracy'
>>> classmates[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> classmates[-1] #直接获取最后一个位置的元素
'Tracy'

>>> classmates[-1]
'Tracy'
>>> classmates[-2]
'Bob'
>>> classmates[-3]
'Michael'
>>> classmates[-4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> classmates.append('Adam') # 插入到尾部
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']
>>> classmates.insert(1, 'Jack') # 插入到指定位置，1
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']

>>> classmates.pop() # 删除list末尾的元素
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']
>>> classmates.pop(1) # 删除指定位置的元素
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
>>> classmates[1] = 'Sarach' # 替换
>>> classmates
['Michael', 'Sarach', 'Tracy']

>>> L = ['Apple', 123, True] # list元素的数据类型可以不同
>>> L
['Apple', 123, True]
>>> s = ['python', 'java', ['asp', 'php'], 'scheme'] # list可以包含list
>>> s
['python', 'java', ['asp', 'php'], 'scheme']
>>> len(s) # 可以将s看成二维数组
4
>>> L = [] #空list
>>> len(L)
0

>>> classmates = ('Michael', 'Bob', 'Tracy')
>>> classmates
('Michael', 'Bob', 'Tracy')
>>> classmates[0]  = 'Se'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

>>> t = (1, 2)
>>> t
(1, 2)
>>> t = ()
>>> t
()
>>> t = (1)
>>> t
1
>>> t = (1,)
>>> t
(1,)
>>>

>>> t = ('a', 'b', ['A', 'B'])
>>> t
('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])

>>> L = [
... ['Apple', 'Google', 'Microsoft'],
... ['Java', 'Python', 'Ruby', 'Php'],
... ['Adam', 'Bart', 'Lisa']
... ]
>>> L
[['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'Php'], ['Adam', 'Bart', 'Lisa']]
>>> print(L[0][0])
Apple
>>> print(L[1][1])
Python
>>> print(L[2][2])
Lisa