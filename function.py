#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数调用
>>> abs(100)
100
>>> abs(-110)
110
>>> abs(12.34)
12.34
>>> abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abs() takes exactly one argument (2 given)
>>> abs('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
>>> max(1, 2)
2
>>> max(2, 3, 1, -5)
3
>>> int('123')
123
>>> int(12.34)
12
>>> str(1.23)
'1.23'
>>> str(100)
'100'
>>> bool(1)
True
>>> bool('')
False
>>> a = abs # 变量a指向abs函数，相当于引用
>>> a(-1) # 所以也可以通过a调用abs函数
1

>>> n1 = 255
>>> n2 = 1000
>>> print(hex(n1))
0xff
>>> print(hex(n2))
0x3e8

