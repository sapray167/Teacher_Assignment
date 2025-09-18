import csv
names=[]
subj=[]
marks=[]
dict={}
with open('marks.csv') as m:
    r=csv.DictReader(m)
    for i in r:
        names.append(i['name'])
        subj.append(i['subject'])
        marks.append(i['marks'])
dict['Name']=names
dict['Subject']=subj
dict['Marks']=marks
subject_groups={}
for name,subject,mark in zip(names,subj,marks):
    mark=int(mark)
    if subject not in subject_groups:
        subject_groups[subject]=[]
    subject_groups[subject].append((name,mark))
# print(subject_groups)
for k in subject_groups.keys():
    student_list = subject_groups[k]
    print(student_list)
    max_mark = max(student_list, key=lambda x: x[1])[1]
    top_scorers = [name for name, mark in student_list if mark == max_mark]
    print(f"Subject: {k} → {', '.join(top_scorers)} ({max_mark})")