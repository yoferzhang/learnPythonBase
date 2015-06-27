#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，
#这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，
#否则，你在源代码中写的中文输出可能会有乱码。

'''
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
>>> '\u4e2d\u6587'
'中文'
>>> print('包含中文的str')
包含中文的str
'''

'''
>>> x = b'ABC'
>>> print(x)
b'ABC'
>>>
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
'''

'''
>>> len(b'ABC')
3
>>> len('ABC')
3
>>> len('中文')
2
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
可见1个中文字符经过UTF-8编码后通常会占用3个字节
而1个英文字符只占用1个字节
'''

'''
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
'''

# 练习
name = '小明'
score1 = 72
score2 = 85
p = (score2 - score1) / score1 * 100
print('%s的成绩提高了%.2f%%' % (name, p))