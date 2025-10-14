# GCD using Euclid's algorthim

import math
num1=int(input("Enter the 1st no: "))
num2=int(input("Enter the 2nd no: "))
print("GCD is: ", math.gcd(num1,num2))

#factorial

print('Find Factorial of a positive number')
n=int(input("Enter the number: "))
mul=1
for i in range(1,n+1):
    mul*=i
print('The foctorial is:',mul)

# sum of the number a

a=input("Enter the number: ")
c=0
for i in a:
    c+=int(i)
print("The Sum is",c)

# leap year concept
print("For Leap year True will be printed and if not then False")
# yr=int(input("Enter the Year: "))
# if yr%4==0 and yr%100==0 and yr%400!=0:
#     print(yr,"is not a leap year")
# elif yr%4==0 and yr%100!=0:
#     print(yr,"is a leap year")
# elif yr%100==0 and yr%400==0:
#     print(yr,"is a leap year")
# elif yr%4!=0:
#     print(yr,"is not a leap year")

yr=int(input('Enter year: '))
if yr%4==0:
    if yr%400==0:
        print(True)
    else:
        print(False)
else:
    print(False)

# Greetings

print("12-Hour Clock")
print("12 pm to 5 pm is Afternoon.\n5 pm to 11:59 pm is Evening.\n12 am to 6 am and 6 am to 11:59 am is Morning.")
print("---"*10)
name=input("Enter your name: ")
hr=int(input("Enter the hour: "))
minu=int(input("Enter the minutes: "))
cl=input("Enter am or pm : ")
if 5<hr<12 and cl=='pm':
    print("Good Evening",name) 
elif hr<=12 and cl=='am':
    print("Good Morning",name)
elif 12==hr<=5 and minu <=59 and cl=='pm':
    print('Good Afternoon',name)
else:
    print("Enter valid data.")

# Rock, Paper, Scissors

import  random
print("Terms and Conditions")
print("---"*10)
print("Rock beats scissors\nScissors beats paper\nPaper beats rock\nFor continue the Game press 1 and to end the game press 0")
print("---"*10)
options=['rock','scissors','paper']
w=0
l=0
t=0
while True:
    choice=int(input("Enter 1 or 0 : "))
    if choice==1:
        rn=random.choice(options)
        rn=rn.lower()
        print(options)
        un=input("Pick one item: ")
        un=un.lower()
        rule={'rock':'scissors','scissors':'paper','paper':'rock'}
        if rule[un]==rn:
            print("Win")
            w+=1
        elif rn==un:
            print('Tie')
            t+=1
        elif rule[un]!=rn:
            print('Lose')
            l+=1
        else:
            print('Enter valid name')
    elif choice==0:
        print("Thank you for playing.")
        print("---"*10)
        break
    else:
        print("Enter valid choice")
print('Your results are:')
print("Win",w)
print("Lose",l)
print('Tie',t)