#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#dict
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
>>> d['Adam'] = 67
>>> d['Adam']
67
>>> d['Jack'] = 90
>>> d['Jack']
90
>>> d['Jack'] = 88
>>> d['Jack']
88
>>> d['Thomas']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Thomas'
>>> 'Thomas' in d
False
>>> d.get('Thomas') # 这里返回None，命令交互行不会显示
>>> d.get('Thomas', -1) #返回子集指定的value
-1

>>> d.pop('Bob') #pop(key)方法，对应的value都会删除
75
>>> d
{'Jack': 88, 'Tracy': 85, 'Michael': 95, 'Adam': 67}

'''
dict内部存放的顺序和key放入的顺序是没有关系的
和list相比较，dict有以下几个特点：
1.查找和插入的速度极快，不会顺着key的增加而增加
2.需要占用大量的内存，内存浪费多
而list相反：
1.查找和插入的时间随着元素的增加而增加；
2.占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方。
需要牢记的第一条就是dict的key必须是不可变对象。
这是因为dict根据key来计算value的存储位置，如果每次计算
相同的key得出结果不同，那dict内部就完全混乱了。这个通过key
计算位置的算法就是哈希算法(Hash)。
要保证hash的正确性，作为key的对象就不能变。
在Python中，字符串、整数等都是不可变的。
而list是可变的，就不能作为key。
'''

>>> key = [1, 2, 3]
>>> d[key] = 'a list'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
