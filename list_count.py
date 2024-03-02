number_items= input("Please enter the no. of items in the list: ")
print(number_items)


user_data = [] #It represents empty list
item=1
while item<=int(number_items): # checking condition
    val = input("please enter the item: ") #stores the items
    user_data.append(val) #adding the items in the list

    item+=1 #iterative step

print(user_data) # print the list
to_search=input("Search the item: ")

is_found = False #flag
for data in user_data:
    if data==to_search:
        is_found = True
        break  #it breaks the nearest loop and will execute the next step

if is_found == True:
        print("Data found")
else:
        print("Data not found")

