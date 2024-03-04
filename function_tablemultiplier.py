""""
def average(a,b): 
    avg=(a+b)/2
    print(avg)
a: int=8
b: int=9
average(a,b)
"""

""""
x=int(input("please enter the table multiplier: "))
y=int(input("please mention the no. of table multipliers: "))
i=1
while i<=y:
    val=(x*i)
    print(val)
    i+=1
"""

def table_multiplier(i,x,y):
    while i<=y: # while loop 
        val=(x*i)
        print(val)
        i+=1

x=int(input("please enter the table multiplier: "))
y=int(input("please mention the no. of times table multipliers will run: "))
i=1
table_multiplier(i,x,y)
    
