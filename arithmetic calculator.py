first=input("Enter the first number : ") #Taking input from user
second=input("Enter the second number : ") #Taking input from user
operator=input("Please enter +,-,*,/,% : ") #Taking input from user
first=int(first) #Conversion from str to int
second=int(second) #Conversion from str to int

if operator =="+": # : has to be used for if with condition in the same line
    print(first+second)
elif operator =="-": # : has to be used for elif with condition in the same line
    print(first-second)
elif operator =="%": # : has to be used for elif with condition in the same line
    print(first%second)
elif operator =="*": # : has to be used for elif with condition in the same line
    print(first*second)
elif operator =="/": # : has to be used for elif with condition in the same line
    print(first/second)
else : print("Sorry Invalid Input")# : has to be used for else with condition in the same line
