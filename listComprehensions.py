#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list(range(1, 11))

# 生成1乘1，2乘2...10乘10
L = []
for x in range(1, 11):
	L.append(x * x)

# 上面太麻烦，看下面
[x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 加上if，就可以筛选出仅偶数的平方
[x * x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]

# 两层循环，可以生成全排列
[m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出当前目录下的所有文件和目录名
import os
[d for d in os.listdir('.')] # on.listdir可以列出文件和目录

# 列表生成式也可以使用两个变量来生成list:
d = {'x': 'A', 'y': 'B', 'z': 'C'}
[k + '=' + v for k, v in d.items()]
# ['x=A', 'z=C', 'y=B']

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
# ['hello', 'world', 'ibm', 'apple']

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
# ['hello', 'world', 'apple']
# isinstance函数可以判断一个变量是不是字符串