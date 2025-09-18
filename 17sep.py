#problem 4
num=input("Enter the numbers saprated by Space: ").split()
myset=set(num)
count=0
sum_=0
for i in myset:
    count+=1
    sum_+=int(i)
avg=sum_/count
print(count)
print(sum_)
print(avg)
print(max(myset))
print(min(myset))

#problem 5
roll_list=[2501,2502,2503,2504,2505,2506,2507,2508,2509,2510]
present=[]
with open('C:/Users/VikasTest/Documents/Coding_Space/Teacher_Assignment/attendance.txt') as f:
    for line in f:
        present.append(int(line.strip()))
        if int(line.strip()) in roll_list:
            print('Present',line.strip())
    print('---'*10)
    for x in roll_list:
        if x not in present:
            print("Absent",x)
            with open('C:/Users/VikasTest/Documents/Coding_Space/Teacher_Assignment/absent.txt','a') as ab:
                ab.write(str(x)+'\n')

#problem 3
books_ava={'The Conch Bearer':10,'The Hidden Hindu Trio':5,'Alchmist':1,'Forever is True':2,'Roses Are Blood Red':0}
a=input("Enter the Title of Book: ")
for i in books_ava.keys():
    if i==a and books_ava[i]==0:
        print('Out of stock')
        break
    elif i==a:
        print('Issued')
        books_ava[i]-=1
        break
    elif a not in books_ava.keys():
        print('Not Found')
        break
with open('library.txt','x') as l:
    l.write(str(books_ava.items()))

#problem 2
from collections import Counter
with open('C:/Users/VikasTest/Documents/Coding_Space/Teacher_Assignment/story.txt') as s:
    r=s.read()
    list=r.split()
mylist=[]
for i in list:
    if ',' in i:
        mylist.append(i.strip(',').lower())
    elif ';' in i:
        mylist.append(i.strip(';').lower())
    elif '-' in i:
        mylist.append(i.strip('-').lower())
    elif '.' in i:
        mylist.append(i.strip('.').lower())
    else:
        mylist.append(i.lower())
u=int(input("Enter the Word Frequency: "))
word_count=Counter(mylist)
for w in word_count.keys():
    if word_count[w]>u:
        print(w+':',word_count[w])

#problem 1
