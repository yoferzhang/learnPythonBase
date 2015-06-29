#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}
for key in d: # 默认迭代是key
	print(key)
'''
a
c
b
'''
# 迭代value
for value in d.values(): 
	print(value)
'''
3
1
2
'''

for k, v in d.items():
	print(k, v)
'''
c 3
a 1
b 2
'''

#判断一个对象是否是可迭代对象
from collections import Iterable
isinstance('abd', Iterable) # str是否可迭代
# True
isinstance([1, 2, 3], Iterable) # list是否可迭代
# True
isinstance(123, Iterable) # 整数是否可迭代
# False

# 同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
'''
0 A
1 B
2 C
'''

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)
'''
1 1
2 4
3 9
'''
