#Creating an user list with values
x=input("Please enter the values of the list: ")
y=x.split(",") # delimiter specified
print(y)
to_search=input("Please enter the value for search:")

a=False
for l in y:
    if l==to_search:
        a=True
        break
if a==True:
    print("Found")
else:
    print("Not Found")
    

    

