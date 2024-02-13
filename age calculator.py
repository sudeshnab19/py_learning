age=input("Please enter your age : ") # input age from user
name=input("Please enter your name : ")
age=int(age) # converting str to int
if age>=18: # checking condition whether age is above or equal to 18
    print(f"Hello {name} You are an adult") #fstring approach
elif age<18: # checking if age is not 18
    print(f"Sorry {name} you are not yet 18")