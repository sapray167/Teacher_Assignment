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