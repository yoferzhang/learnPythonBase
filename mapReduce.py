#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
	return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# 结果r是一个Itertator，是惰性序列
# 通过list()函数让它把整个序列都计算出来并返回一个list
print(list(r))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

from functools import reduce
def add(x, y):
	return x + y
print(reduce(add, [1, 3, 5, 7, 9]))
# 25

from functools import reduce
def fn(x, y):
	return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))
# 13579

# str2int的函数
from functools import reduce
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))
print(str2int('13579'))
# 13579

from functools import reduce
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('12354'))
# 12354

# 练习
def normalize(name):
	return name[:1].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
# ['Adam', 'Lisa', 'Bart']

from functools import reduce
def prod(L):
	def fn(x, y):
		return x * y
	return reduce(fn, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# 3 * 5 * 7 * 9 = 945

from functools import reduce
def str2float(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	def add1(x, y):
		return x * 10 + y
	index = s.find('.')
	t = len(s) - index - 1
	return reduce(add1, map(char2num, s.replace('.', ''))) / pow(10, t)

print('str2float(\'123.456\') =', str2float('123.456'))
# str2float('123.456') = 123.456

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))