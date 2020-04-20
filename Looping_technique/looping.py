"""
Print below pattern using nested loop:
 * 
  * * 
  * * * 
  * * * * 
  * * * * * 
"""
for i in range(1,6,1):
    print(i * '*')

"""
Print below pattern:
  1
  22
  333
  4444
  55555
  666666
  7777777
  88888888
  999999999
"""
for i in range(1, 10, 1):
    print(i * str(i))

"""
Print below pattern using nested loop:
  * 
  * * 
  * * * 
  * * * * 
  * * * * * 
  * * * * 
  * * * 
  * * 
  *
"""
star = 5
for i in range(1, star+1, 1):
    print(i * '*')
for i in range(star -1, 0, -1):
    print(i * '*')

"""
Print below pattern using loop:
   *                                                                      
   *                                                                      
   *                                                                      
   *                                                                      
   *                                                                      
   *                                                                      
   *****
"""
star = 6
for i in range(1, star, 1):
    print('*')
    if i == star-1:
        print(i * '*')

"""Calculate the individual expense by an individual, total expense and payable amount for each member from below data structures using loop:
"""
expenses = {
      'Eliza': {
          'Dahi': 280,
          'PaniPuri': 120,
          'Bara': 160,
          'Kulfi': 200,
          'Pau': 50,
      },
      'Binay': {
          'Water': 30,
      },
      'Kshitiz': {
          'Chocolate': 90,
      },
      'Sajal': {
          'Coffee':500,
      },
    }
individual_expeneses={}
for i in expenses:
    individual_expeneses[i] = sum(expenses[i].values())
print ("Individual expenses is: " + str(individual_expeneses))
print ("Total expenses is " + str(sum(individual_expeneses.values())))
individual_pay = sum(individual_expeneses.values()) / len(individual_expeneses)   
print('Payable Amount : ')
for item in individual_expeneses:
    print(item + '->' + str(individual_expeneses[item]-individual_pay))  

# Convert the above expenses dictionary keys to list using loop
list_keys=[]
for item in expenses:
    list_keys.append(item)
print(list_keys)

# Create a dictionary of cubes upto number 10 using loop.
{i:i**3 for i in range(1,11, 1)}

cube_dict = dict()
for i in range(1,11):
    cube_dict[i] = i**3
print(cube_dict)