# Exercise of PYthon training
# Print 1 - 10
for i in range(1,11):
    print(i, end = ',')
    
# Print 1 - 10 except 5 and 8
# i=1
# while i < 11:
#     if(i == 5 or i ==8):
#         pass
#     else:
#         print(i, end = ',')
#     i+= 1
    
for i in range (1, 11):
    if (i !=5 and  i!=8 ):
        print(i, end= ',')
        
# Print if a number is even or odd        
try:
    user_input = int(input("enter the number"))
    if(user_input%2 ==0):
        print(f"{user_input} is EVEN ")
    else:
        print(f"{user_input} is ODD ")
except:
    print("the number is not INTEGER")
    raise
    
# Print all divisor of number    
try:
    user_input = int(input("enter the number"))
    for i in range(1, user_input):
        if user_input % i == 0:
            print(f"{user_input} is divisible by {i}")
        else:
            pass
except:
    print("the number is not INTEGER")
    raise 