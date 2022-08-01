# '''function is represented by key word calld us def'''
# '''def function nane greet function name'''
# def greet(): function declaration
    # print('hello')
# greet()    # calling function          # hello
# def greet(n):     # n is called us argument
    # print('hello'+n)
# greet('HD')           #helloHD
# greet('PY')           #hellopy
# def greet(n):     # n is called us argument
    # print('hello'+n)
# greet()            #  IndentationError: expected an indented block after function definition on line 1
# def greet(n):
    # print('hello'+n)
# greet()               # TypeError: greet() missing 1 required positional argument: 'n'
# ''' int cannot possible to string but you can change to str  we use another method'''
# def greet(n):
    # print('hello'+str(n))
# greet(56)                 # hello56
# def greet(*names):
#     print('Hey',names)
#     greet('python','programming','core','functions')
# def details(n,a):
    # print('Hey'+n+'! your age is '+str(a))
# details('hd',25)          # Heyhd! your age is 25
# details(n='HD',a=26)        # HeyHD! your age is 26
# details(a=26,n='SD')         # HeySD! your age is 26
# def details(n,a):
    # print('Hey'+n+'! your age is'+str(a))
# n=input('Enter your name:')     # babu
# a=input('Enter your age:')      # 24
# details(n,a)                    #  Heybabu! your age is24 
# def r(x,y):
    # return print(x+y)
# r(4,5)
# print(r(5,6))            # 11
# def z(p,q):
#     return p*q,p+q;
# p=int(input())
# q=int(input())
# print(z(p,q))
# '''sorted()'''
# '''we can pass list also tuple akso'''
# a=[1,6,3,8,2]
# a.sort()
# print(a)
# print(sorted([12,3,120,9]))
# print(sorted((12,3,4,56)))
# '''all()'''
# print(all([True,1,2]))              # true
# print(all([True,'',1,2]))           # false
# print(all([True,' ',1,2]))          # true
# print(all([True,False,1,2]))        # false
# print(all([True,True,1,2,0]))       # false
# print(all([True,True,1,2,None]))    # false
# '''any()'''
# print(any([True,False,False,23]))     # True
# print([False,False,0])                # [False, False, 0]
# print(True,True,None,0)               # True True None 0
# # '''bool'''
# print(bool(False))             # False
# print(bool(True))              # True
# print(bool(1))                 # True
# print(bool(0))                 # False
# print(bool(None))              # False
# print(bool(bool))              # True
# '''eval()'''
# print('eval=',eval('5+6,8-1'))      # eval= (11, 7)
# a=eval('5+6-1')                     # 10 <class 'int'>
# b=eval('4+3.8-1')                   # 6.8 <class 'float'
# print(a,type(a))
# print(b,type(b))
# '''  sum() '''
# print('sum=',sum([1,2,3,4,5]))         # sum= 15
# print('sum=',sum([10,5,20,30]))        # sum= 65
# import math
# a=3,4,5
# print(math.prod(a))      # 60
# ''' reversed()-list'''
# for i in reversed([1,2,3,4]):
#    print(i)
# ''' reversed()-tuple'''
# for i in reversed([1,2,3,4]):
#     print(i)
# '''   enumerate  '''
# a=['bread','milk','python']
# b=enumerate(a)             # <class 'enumerate'>
# print(type(b))             # {0: 'bread', 1: 'milk', 2: 'python'}
# print(dict(b))             # 
# print(list(b))             # []
# print(tuple(b))            #  ()
# a=['bread','milk','python']  
# c=enumerate(a,6)
# print(list(c))                # # [(6, 'bread'), (7, 'milk'), (8, 'python')]
# def gm():                       # this is called us .doc strings
# ''' Author:Python 9am
# The time is now 9:22am
# we are doing functions topic'''
# print(gm.__doc__)