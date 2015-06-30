#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# generator 生成器
L = [x * x for x in range(10)]
print(L)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(10))
print(g)
# <generator object <genexpr> at 0x00000000028F0120>

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
0
1
4
9
16
25
36
49
64
81
'''
# print(next(g))
'''
Traceback (most recent call last):
  File "E:\Code\python\learn\generator.py", line 23, in <module>
    print(next(g))
StopIteration
'''
# 上面这种调用方法太变态了
# 正确的使用for循环
g = (x * x for x in range(10))
for n in g:
	print(n)
'''
0
1
4
9
16
25
36
49
64
81
'''

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b # 注意这里
		n = n + 1
	return 'done'

fib(6)
'''
1
1
2
3
5
8
'done'
'''

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b 
		a, b = b, a + b
		n = n + 1
	return 'done'
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数
# 而是一个generator

f = fib(6)
f
# <generator object fib at 0x00000000022011F8>

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)
'''
>>> o = odd()
>>> next(o)
step 1
1
>>> next(o)
step 2
3
>>> next(o)
step 3
5
'''

for n in fib(6):
	print(n)

# 练习 - 杨辉三角
def triangles():
	a = [1];
	while True:
		yield a
		a = [sum(i) for i in zip([0] + a, a + [0])]

n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break
'''
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
'''