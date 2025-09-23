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

