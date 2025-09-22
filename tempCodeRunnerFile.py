list=['apple','apricot','banana','blueberry','cherry']
grouped={}
for word in list:
    firstletter=word[0]
    if firstletter not in grouped:
        grouped[firstletter]=[]
    grouped[firstletter].append(word)
print(grouped)