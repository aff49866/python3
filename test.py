# from zhangmaode.zhangmao import print_lol
# movies = ["the holy grail", 1975, "terry jones &terry gilliam", 91, ["graham chapman", ["michael palin", "john cleese", "terry gilliam", "eric idle", "terry jones"]]]
# for x in movies:
#     if not isinstance(x, list):
#         print(x)
#     else:
#         for i in x:
#             if not isinstance(i, list):
#                 print(i)
#             else:
#                 for xthree in i:
#                     print(xthree)
# isinstance(movies, list)
# num_num = len(movies)
# print(isinstance(num_num, list))
# print_lol(movies)
# if 1 == 0 and 2 == 1 or 2 == 3:
#     print("true")
# else:
#     print("false")
# num = 0
# for i in range(100,1000):
#     if i % 17 == 0:
#         num += 1
# print(num)
# s = 'Hello World'
# s.replace('o', 'b')
# print(s)

# from
# def get_reponse(url):
#     respons = requests.get(url).text
#     return respons
# def get_content(html):


# -*- coding: UTF-8 -*-

import re
r = re.findall("1{:1}2","11120")
print(r)
# 廖学峰老师教程学习
# classmates = ['michael','bob','tracy']
# classmates.append('adam')
# classmates.insert(1,'b2')
# classmates.pop(1)
# print(classmates)
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# height = 1.75
# weight = 80.5
# bmi = weight / height
# if bmi < 18.5:
#     print('过轻')
# elif 18.5 < bmi <25:
#     print('正常')
# elif 25 < bmi <28:
#     print('过重')
# elif 28 < bmi <32:
#     print('肥胖')
# elif bmi > 32:
#     print('严重肥胖')

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum += n
#     n = n-2
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for i in L:
#     print('Hello,' + i)

# d = {'michael' : 95 , 'bob' : 75 , 'tracy' : 85}
# print(d['michael'])

# def myabs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('参数错误')
#     if x>=0:
#         return x
#     else:
#         return -x
# print(myabs('oi'))
# import string
#
# def triangles(x):
#     L = [1]
#     n = 0
#     while n<x :
#         yield L
#         L.append(0)
#         L = [L[i-1]+L[i] for i in range(len(L))]
#         n = n+1
# for t in triangles(10):
#     print(t)

# 把用户输入的不规范的英文名字，变为首字母大写
# def normalize(name):
#     name = name[0:1].upper()+name[1:].lower()
#     return name
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

from functools import reduce
# 接受一个list并求积
# def prod(L):
#     return reduce(lambda x, y: x *  y, L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 把字符串'123.456'转换成浮点数123.456
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# def str2float(s):
#     s=s.split('.')
#     s1 = reduce(lambda x,y:x*10+y,map(char2num,s[0]))
#     s2 = reduce(lambda x,y:x*10+y,map(char2num,s[1]))/10**len(s[1])
#     return s1+s2
# print('str2float(\'123.456\') =', str2float('123.456'))

# def is_palindrome(n):
#     return str(n)[::-1]==str(n)
# out=filter(is_palindrome,list(range(1,1000)))
# print(list(out))

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return str.lower(t[0])
# L1 = sorted(L, key=by_name)
# print(L1)
#
# def by_score(t):
#     return t[1]
# L2 = sorted(L,key=by_score,reverse=True)
# print(L2)