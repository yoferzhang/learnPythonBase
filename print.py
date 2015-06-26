#输出
print('hello, python')

print('The quick brown fox', 'jumps over', 'the lazy dog')
#多个字符串，用逗号隔开，就可以连成一串输出
#print()会依次打印每个字符串，遇到逗号会输出一个空格

print(300) # 300
print(100 + 200) # 300

print('100 + 200 =', 100 + 200) # 100 + 200 = 300

#输入
#name = input() #这行必须在命令行执行

#打印变量 print(name)
name = input()
print('hello', name)
'''
>>> name = input()
zhangyaoqi
>>> print('hello', name)
hello zhangyaoqi
'''

name  = input('Please input your name: ')
print('hello', name)
'''
>>> name  = input('Please input your name: ')
Please input your name: zhangyaoqi
>>> print('hello', name)
hello zhangyaoqi
>>>
'''

print('1024 * 768 =', 1024 * 768)
#1024 * 768 = 786432