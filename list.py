"""
Python list:
 Heterogenious indexed data structure (ex. str,int, any data type)
 Which grows dynamically. 
 it can be mutated
"""
marks = [22,23,24]
marks.append(25)
marks.insert(0,21)
print(marks)

# loop counter
counter: int = 0                                               # variable counter with int datatype 
for counter in range(len(marks)):                              # for loop with range (0,1,2,3,4)
    print(f"index:{counter}, value:{marks[counter]}")          # print index(counter variable) and value(marks w.r.t counter variable) using f func

print("==========="*10)

for score in marks:
    print(score)

print("==========="*10)
print(marks[0])

print("==========="*10)
print(marks[len(marks)-1])
