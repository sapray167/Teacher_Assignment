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