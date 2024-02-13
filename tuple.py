"""
Tuple is inmutable.
Add/Append/Clear not allowed
"""
marks = [1,2,3,3,3,4]
student = len(marks)
print(student)
print(marks.count(3))   #Both list and tuple can count no. of repeatetive objects
print(marks.index(3))   #3 position is 2,3,4. It gives the 1st position of 3.