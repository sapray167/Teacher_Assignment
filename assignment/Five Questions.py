def choc(n):
    for i in range(n,3*n,2):
        print(i)

choc(10)


def dist_values():
    list=input('Enter the numbers seperated by space: ').split()
    myset=set(list)
    for j in range(len(list)):
        if j<len(list)-1:
            if len(myset)==5 and list[j]!=list[j+1]:
                continue
            else:
             print(False)
            break
        print(True)

dist_values()


def indexes():
    list=input("Enter the numbers seperated by space: ").split()
    thr=input("Enter the threshold value: ")
    print(list)
    mylist=[]
    for i in range(len(list)):
        if list[i]<thr:
            mylist.append(i)
    print(mylist)

indexes()


def pal():
    print("Enter the Words in lowercase or uppercase.")
    list=input("Enter the words seperated by space: ").split()
    print(list)
    mylist=[]
    output=[]
    for i in list:
        for j in i:
            mylist.append(j)
        if mylist[0:len(mylist):1]==mylist[::-1]:
            output.append(True)
        else:
            output.append(False)
        mylist.clear()
    print(output)

pal()


def count():
    list=input("Enter the words seperated by space: ").split()
    print(list)
    mylist=[]
    for i in list:
        b=0
        for j in i:
            b+=1
        mylist.append(b)
    print(mylist)

count()