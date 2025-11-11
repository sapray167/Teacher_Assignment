""" 7th Nov"""
''' Use Recursion '''
''' Sum of digits for positive number '''
def sumdigits(num):
    if num==0:
        return 0
    remain=num%10
    num=num//10
    return remain+sumdigits(num)
print(sumdigits(12345))
''' or without recursion'''

def sumdigits(num):
    sumd=0
    while num!=0:
        remain=num%10
        num=num//10
        sumd+=remain
    return sumd
print(sumdigits(1234))

''' removal of occurences of a character '''

def removechar(string,target):
    if not string:
        return ''
    if string[0]==target:
        new_s=removechar(string[1:],target)
    else:
        new_s=string[0]+removechar(string[1:],target)
    return new_s
print(removechar('prayas','a'))


''' removal of occurences of a character '''
def uniqstr(string):
    if not string:
        return ''
    if string[0] in string[1:]:
        news=uniqstr(string[1:])
    else:
        news=string[0]+uniqstr(string[1:])
    return news
print(uniqstr('hemelata'))

''' without recursion '''

def uniqstr(string):
    nstr=''
    for i in range(len(string)):
        if string[i] not in nstr:
            nstr+=string[i]
    return nstr
print(uniqstr('Prayas'))

''' conversion of a number to binary'''

def conversion_binary(num,power=0):
    if num==0:
        return 0
    remain=num%2
    num=num//2
    return remain*(10**power)+conversion_binary(num,power+1)
print(conversion_binary(137))

''' reversing a string '''
def reversing(string):
    if not string:   # string==''
        return ''
    return reversing(string[1:])+string[0] # each time string reduces its first character and we also side by adds that character to a string
print(reversing('prayas'))     