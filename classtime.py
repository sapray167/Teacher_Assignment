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
print(fact(0))

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

c={'He','is','my','son.'}
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
sn=sorted(n)
print(n)
print(sn) 

f=['apple','banana','kiwi','aomegranate']
sorted_by_len=sorted(f,key=len)
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
zipped=zip(grades,scores) # work once 
l=list(zipped)
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
result=map(double,numbers) # same as zip
print(tuple(result))
print(list(result))

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
n_sum=map(lambda x,y : x+y,a,b)
print(list(n_sum))

n=[1,2,3,4,5,6,7]
d_even=map(lambda x: x*2 if x%2==0 else x,n)
print(list(d_even))

