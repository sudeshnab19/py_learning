students=["Ram", "Shyam", "Lakshman"] #list

for student in students:            # for loop where variable= student holds the list
    if student == "Lakshman":       
        break;                      # After Lakshman nothing else will be shown from the list
    print(student)



for student in students:            # for loop where variable= student holds the list
    if student == "Shyam":       
        continue;                      # Ignore Shyam and continue showing others from the list
    print(student)