with open('C:/Users/VikasTest/Documents/Coding_Space/Teacher_Assignment/script.txt') as s:
    while True:
        r=s.readline()
        if 'error' in r:
            print(r)