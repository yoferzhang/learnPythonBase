#Python的语法比较简单，采用缩进方式，比如：

a = 100
if a >= 0:
	print(a)
else:
	print(-a)
#当语句以冒号:结尾时，缩进的语句视为代码快
#Python程序也是大小写敏感的

print('I\'m \"OK\"!')
#I'm "OK"!

print('I\' ok.')
#I' ok.
print('I\'m learning\nPython.')
#I'm learning
#Python.
print('\\\n\\')
#\
#\

print('\\\t\\')
#\	\
print(r'\\\t\\')
#\\\t\\


#>>> print('''line1
#... line2
#... line3''')
#line1
#line2
#line3

print('''line1
line2
line3''')

print(3 > 2)
print(3 > 5)

#注意大小写
#or或运算
print(True or True)
print(True or False)
print(False or False)
print(5 > 3 or 1 > 3)
'''
True
True
False
True
'''

#not非运算
print(not True)
print(not False)
print(not 1 > 2)
'''
False
True
True
'''

age = 23
if age > 18:
	print('adult')
else:
	print('teenager')

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

PI = 3.14159265359

# 练习
n = 123
print('n =', n)
f = 456.789
print(f)
print('f =', f)
s1 = 'Hello, world'
print('s1 =', s1)
s2 = 'Hello, \'Adam\''
print('s2 =', s2)
s3 = r'Hello, "Bart"'
print('s3 =', s3)
s4 = r'''Hello,
Lisa!'''
print('s4 =', s4)
'''
n = 123
456.789
f = 456.789
s1 = Hello, world
s2 = Hello, 'Adam'
s3 = Hello, "Bart"
s4 = Hello,
Lisa!
'''