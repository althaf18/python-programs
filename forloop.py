digits=[0,1,5]
for i in digits:
    print(i)
else:
    print("No items left.")

student_name='Dora'
marks={'Dora':90,'Cake':89,'Nobita':77}

for student in marks:
    if student ==student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')