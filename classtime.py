x='Python'
def my():
    x='C'
    print("I like "+x)
my()
print('I like '+x)

x='Python'
def my():
    global x
    x='C'
    print("I like "+x)
my()
print('I like '+x)
c=0
for i in range(3):
    for j in range(2):
        for k in range(10):
            # print(i,j,k)
            c+=1
print(c)

evens=[]
for i in range(1,21):
    if i%2==0:
        evens.append(i)
print(evens)

# using list comprehension
evens=[n for n in range(1,21) if n%2==0]
print(evens)

#using for loop
mylist=['any','am','ivy','airy','a']
newlist=[]
for i in mylist:
    if i.startswith('a') and i.endswith('y'):
        newlist.append(i)
print(newlist)

#list comprehension
mylist=['any','am','ivy','airy','a']
newlist=[x for x in mylist if x.startswith('a') and x.endswith('y')]
print(newlist) 
print(newlist)

mylist=['a','b','c','d']
print(mylist[-2:3:-1])  

with open('C:/Users/priya/Desktop/test_py_repo/Teacher_Assignment/script.txt') as s:
         for i in range(4):
            r=s.readline()
            print(r[::-1])

my_subs=[['this is prayas','age is 19+'],['this is amit','age is 20+'],['this is abhishek','age is 22+']]
for i in my_subs:
    for j in i:
        # print(len(j))
        print(j)

# 7 digit number divisible by 137
for n in range(0,10000000,137):
    if len(str(n))==7:
        print(n)
        break

tupule=('python','java','c++',)
tup=('scala')
tupule+=tup
print(tupule)

l=[1,2,3,4,5]
print(l[3:0:-1])
l+='prayas'
print(l)

myset={1,2,'u',3,4,65,5,'rp'}
yourset={65,45,1,2,'rp'}
theirset={1,2,'pr','rp','lko',65}
uheirset={1,2,'pr','rp','lko',65,67,89}
list=[1,2]
tupule=('python','java','c++',)
yourset.update(myset)
unewset=myset.union(yourset,theirset,uheirset)
inewset=myset.intersection(yourset,theirset,uheirset)
print(yourset)
print(unewset)
print(inewset)
for i in unewset:
    print(i)
def f(c='India'):
    print('I am from '+c)
f('sweden')
f()
a=[1,2,3,4,5,6]
a[2:4]=[9,8,7]
print(a)

def m(*id):
    print(id[2])
m('alpha','beta','gama','delta','zeta')


def fact(x):
    if x==1 or x==0:
        return 1
    else:
        return x*fact(x-1)
print(fact(4))

def prime():
    n=int(input('Enter the number: '))
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if n==2:
            return True
        elif n%i==0:
            return False
    return True
print(prime())

dict={'P':20,'C':30}
print(dict.keys())
print(dict.values())
print(dict.items())
for i in dict:
    print(i) #takes keys

def myf(ch1,ch2='Neil'):
    print('The eldest son is '+ch1)
myf('Nitin')

x='Global'
def glo():
    global x
    x='awesome'
    print(x)
glo()
print('Python is '+x)

v=[1,2,3,4,5,6]
print(v[1:5:2])

list=[1,2,3,4,5,6]
for i in range(1,6):
    list[i-1]=list[i]
for i in range(6):
    print(list[i],end='')


def f(value,values):
    values[value]=44 # list is muatable
    value=0 # interger can't be modified
t=3
v=[1,2,3,4]
f(t,v)
print(t,v[t])

def f(i,values=[]):
    values.append(i)
    print(values)
    return values
f(1)
f(2)
f(3)

name='python'
stars='*'.join(name)
print(stars)

c=['He','is','my','son.']
co=' '.join(c)
print(co)

def palin():
    str=input('Enter string:').lower().split()
    nstr=str.copy()
    str=nstr.reverse()
    if nstr==str:
        return True
    else:
        return False
print(palin())

def pasw():
    pas=input("enter your password: ")
    specials='!@#$%^&*'
    if len(pas)<8:
        return False
    hasdigit=hasspecial=hasupper=haslower=False
    for i in pas:
        if i.isdigit():
            hasdigit=True
        elif i.isupper():
            hasupper=True
        elif i.islower():
            haslower=True
        elif i in specials:
            hasspecial=True
    return hasdigit and hasupper and haslower and hasspecial
print(pasw())

''' Sorting of numbers and string'''
n=[5,1,5,3,4]
sn=set(sorted(n))
print(n)
print(sn) 

f=['apple','banana','kiwi','aomegranate']
sorted_by_len=sorted(f,key=len, reverse=True)
print(sorted_by_len)

f=['apple','banana','kiwi','aomegranate']
sorted_by_len=sorted(f,reverse=True)
print(sorted_by_len)

''' formating string'''
grade="A"
score=90
print(f"Above {score} is {grade} grade.")

pi=3.14149
print(f"pi is approximately {pi:.2f}") # .2f two decimal places

''' zip '''
scores=[90,80,70]
grades=['A','B','C'] # if we give extra value then it will stop at the matching index
zipped=list(zip(grades,scores)) # work once 
print(zipped)
print(dict(zipped)) # gives a dictionary
print(l)

scores=[90,80,70]
grades=['A','B','C']
for g,s in zip(grades,scores):
    print(f"Above {s} is Grade {g}.")

''' unzip use * '''
pairs=[('x',1),('y',2),('z',3)]
l,n=zip(*pairs)
print(l,n)

''' map '''
def double(n):
    return n*2
numbers=[2,3,4]
result=list(map(double,numbers)) # same as zip
print(result)
print(tuple(result))

''' lambda '''
add=lambda x,y:x+y # useful for short, one-line function for simple operations and you want to use it once and forget about it 
print(add(1,2))

n=[1,2,3,4,5,6]
e=filter(lambda x: x%2==0,n) # filtering the numbers which follow the condition of lambda
print(list(e))

data=[(1,5),(3,1),(2,4)]
sorted_data=sorted(data,key=lambda x: x[1])
print(sorted_data)

numbers=[1,2,3,4]
result=map(lambda x: x*2,numbers)
print(list(result))

list1=['prayas','anurag']
u_case=map(lambda x: x.upper(),list1)
print(list(u_case))

list1=['prayas','anurag']
c_len=map(lambda x: len(x),list1)
print(list(c_len))

a=[1,2,3]
b=[4,5,6]
ad=[x+y for x,y in zip(a,b)]
print(ad)
n_sum=map(lambda x,y : x+y,a,b)
print(list(n_sum))

n=[1,2,3,4,5,6,7]
d_even=map(lambda x: x*2 if x%2==0 else x,n)
print(list(d_even))

word=['prayas','anurag','amit','abhishek chintu']
rev=map(lambda x: x[::-1].title(),word)
print(list(rev))

word=['prayas','anurag','amit','abhishek chintu']
rev=map(lambda x: x[::-1].capitalize(),word)
print(list(rev))

''' map function returns iterator object '''

l1=[1,2,3,4,5,6]
l2=[3,4,5,6,7,8]
result=[x+y for x ,y in zip(l1,l2) if x%2==0 and y%2==0]
print(result)
output=map(lambda x,y: x+y if x%2==0 and y%2==0 else None,l1,l2) # needs refinement
print(list(output))

def fibonacci_number(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci_number(num-1) + fibonacci_number(num-2)
print(fibonacci_number(7))

l1=['prayas','anurag','sam','sap']
l2=[90,40,80,50]
result=filter(lambda x:x[1]>50,zip(l1,l2))
print(dict(result))

''' stroing the sum of the number'''
def sum_digit(num):
        if num==0:
            return 0
        remain=num%10
        num=num//10
        fi_num=remain+sum_digit(num)
        if fi_num%10==fi_num:   # numbes do not have length as they are integers so already considered as 1
            return fi_num
        f_remain=fi_num%10
        fi_num=fi_num//10
        return f_remain+sum_digit(fi_num)
print(sum_digit(124))

# or 

def sum_digit(num):
        if num<10:
            return num
        fi_num=num%10+sum_digit(num//10)
        return sum_digit(fi_num)
print(sum_digit(124))

''' character sum '''  #needs refinment
def char_sum(string,new_str='',pow=1):
    if not string:
        return ''
    if string[0] in string[1:]:
        pow+=1
        new_str=string[0]+str(pow)+char_sum(string[1:],new_str,pow=1)
    # else:
    #     new_str=string[0]+str(pow)+char_sum(string[1:],new_str,pow=1)
    return new_str+char_sum(string[1:],new_str,pow=1)
print(char_sum('aabbbcdd'))


''' Exception '''
try:
    print(5/0)
except ZeroDivisionError:
    print('Zero Division Error')
print("hello")
    
try:
    n=int('abc')
    print(10/0)
except ValueError:
    print('Invalid integer input!')
except ZeroDivisionError:
    print('Can not divide by zero')
print("Hello World!")

'''
else: runs only if no exception occurs
finally: runs always whether there is exception or not(used for cleanup: closing files, releasing resources)
'''
try:
    num=int('20')
except ValueError:
    print("Invalid number")
else:
    print("conversion succeeded",num)
print('done')

try:
    num=int('2e0')
except ValueError:
    print("Invalid number")
else:
    print("conversion succeeded",num)
print('done')

try:
    f=open('story.txt')
    r=f.read()
    print(r)
except FileNotFoundError:
    print("file not found")
finally:
    print("This will always run")

'''
we can create custom exceptions to handlespecific error conditions within our applications.
'''
class MyNegError(Exception):
    pass
def set_age(age):
    if age<0:
        raise MyNegError("Age cannot be negative")
    print("Age set to", age)
try:
    set_age(-5)
except MyNegError as e:
    print("Custom Error:", e)


''' About Garbage Collection '''
import gc 
c=gc.collect()
print(c)
def fun(i):
    x = {}
    x[i + 1] = x
    return x
for i in range(5):
    fun(i)
c=gc.collect()
print(c)

import gc
a = [1, 2, 3]
b = {"a": 1, "b": 2}
c = "Hello, world!"
del a,b,c
print(gc.collect())

# Semster 2
import csv
with open('S:/Repositories/Teacher_Assignment/students.csv','r') as file:
    reader= csv.reader(file)
    for row in reader:
        print(row)

import json
with open('S:/Repositories/Teacher_Assignment/data.json','r') as jfile:
    data=json.load(jfile)
    print(data)
for person in data:
    if person.get('isStudent'):
        print(f'{person['name']} is a student.')
    else:
        print(f'{person['name']} is not a student.')