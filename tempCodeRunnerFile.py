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
    if hasdigit and hasupper and haslower and hasspecial is True:
        return True
    else:
        return False
print(pasw())