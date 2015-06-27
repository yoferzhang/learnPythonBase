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

print(not True)
print(not False)
print(not 1 > 2)
'''

'''