Flag = False
Student_Dictionary = {
    'Name1':'Anusha',
    'Age1':36,
    'Class1':"17th",
    'Course1':'Mtech'
}

Search = str(input("What do you want to search? "))
for values in Student_Dictionary:
    if (Student_Dictionary.get(Search)):
       Flag = True 
    else:
        Flag = False
if (Flag == True):
    print("The string is not found")
else:
    print("The string is found")