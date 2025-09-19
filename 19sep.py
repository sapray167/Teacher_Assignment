#1
list=['a','b','a','d','b','c','d']
unique=[]
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)

#2
from collections import Counter
list=['apple','he','apple','pyhton','apple','he','java']
word_count=Counter(list)
print(word_count)

                #or

list=['apple','he','apple','pyhton','apple','he','java']
freq={}
for word in list:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)
#3
num=[12,45,67,89,45,37,-100]
num.sort()
print(num[-1])

#4
with open('C:/Users/VikasTest/Documents/Coding_Space/Teacher_Assignment/script.txt') as s:
    while True:
        r=s.readline()
        if 'error' in r:
            print(r)

#5
list=['apple','apricot','banana','blueberry','cherry']
grouped={}
for word in list:
    firstletter=word[0]
    if firstletter not in grouped:
        grouped[firstletter]=[]
    grouped[firstletter].append(word)
print(grouped)
