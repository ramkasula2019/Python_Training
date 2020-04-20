#Sum all the items in the list [1, 2, 3, 4, 5, 6, 7] without built-in methods.
sum_list = [1, 2, 3, 4, 5, 6, 7]
result = 0
for i in sum_list:
    result = result + i
print(result)

# Remove odd number from [1, 2, 3, 4, 5, 6, 7] list
all_list = [1, 2, 3, 4, 5, 6, 7]
for i in all_list:
    if (i%2 ==0):
        continue
    else:
        all_list.remove(i)
all_list 

# Find the index of 4 in list [1, 2, 3, 4, 5, 6, 7]
index_list = [1, 2, 3, 4, 5, 6, 7]
index_list.index(4)

# Find the longest item in the list ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
long_list = [ 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana' ]
sorted(long_list, key = len, reverse=True)[0]

# Concatinate 'A ' to all the items in the list ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
['A'+i for i in long_list]


# Check if list is empty
b=[]
# empty list evalutate to false
if not b:
    print ("list is empty")

# Insert 7 to second last element of [1, 2, 3, 4, 5, 6, 8] list.
numeric_list = [1, 2, 3, 4, 5, 6, 8]
numeric_list.insert(len(numeric_list)-1,7)
numeric_list

# Extend ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'] list with ['pineapple', 'litchi'] without append.
fruit_list = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
next_fruit_list = ['pineapple', 'litchi']
fruit_list.extend(next_fruit_list)
fruit_list      


# Unpack a tuple into multiple variables
pack_tuple = ('apple', 'boy', 'cat')
type(pack_tuple)
a, b, c = pack_tuple
print(a, b, c)

# Check if an element exist in a tuple
'apple' in (pack_tuple) # return True
'zebra' in (pack_tuple)

# Find a repeacted item 2 in a tuple 2, 4, 5, 6, 2, 3, 4, 4, 7 Hint: use count()  
numeric_tuple = (2, 4, 5, 6, 2, 3, 4, 4, 2,2,3,7)
#converting tuple into list
len([i  for i in numeric_tuple if i==2])

"""For two set {'apple', 'orange', 'pear', 'pineapple'} and {'kiwi', 'orange', 'apple', 'guwava'}, find:
Intersection
Union
Difference
Symmetric Difference
"""

a = {'apple', 'orange', 'pear', 'pineapple'}
b = {'kiwi', 'orange', 'apple', 'guwava'}
a & b
a | b
a - b
a ^ b

# Find the length of the above sets
len(a)


contact = {'Ram Kasula':9999999999, 'Anu Pau':88888888, 'Kade Hade':777777777}

#Check if Anu Pau exists ing contact
'Anu Pau' in contact

"""
Concatenate below dictionary to contact:
new_contact = {
  'Suraj Shakya': 98546625,
  'Rashmni Maharjan': 98751478556,
  'Sanjeev KC': 984656221546,
  'Ram Kasula': 9840298755,
}
"""
new_contact = {
  'Suraj Shakya': 98546625,
  'Rashmni Maharjan': 98751478556,
  'Sanjeev KC': 984656221546,
  'Ram Kasula': 9840298755,
}
# following will merge in new dict
merge_contact = {**contact, **new_contact}
merge_contact

contact.update(new_contact)
contact

# Remove Sanjeev KC from the above dict.
del contact['Sanjeev KC']
contact

# Sort the above dict by Keys
sorted_contact = {}
sorted_contact = {i: contact[i] for i in sorted(contact.keys())}
sorted_contact

# Check if dict is empty
t = {}
type(t)
if not t:
    print('the dict is empty')
    
# Find common keys between above two dict.
contact.keys() & new_contact.keys()
   
# Count the number of items in the dict.
print(contact)
len(contact)



# Using list comprehension, print a table of 2
p = [i*2 for i in range (1,11,1 )]
p

# Using dictionary comprehension, print a table of 5
q={"5 * " + str(i): 5*i for i in range(1,11,1)}
q

# Remove vowel from string 
sentence = 'A dictionary is data strucuture similar to contacts. You can find an address or contact of a person by his/her/its name'
# def remove(sentence):
#     sentence_wo_vowel = []
#     for i in sentence:
#         vowel='aeiou'
#         if i not in vowel:
#             sentence_wo_vowel.append(i)
#     return "".join(sentence_wo_vowel)

# print(remove(sentence))

def remove(sentence):
    return "".join(i for i in sentence if i not in ('aeiou'))

print(remove(sentence))




# Find unique vowel from string "It is a good day to Practice Python"
sentence = 'It is a good day to Practice Python'
vowels = 'aeiou'
e = [i for i in sentence if i in vowels]
len(set(e))

# Find length of each word in "Today is my lucky day" using dictonary comprehension
sentence = 'Today is my lucky day'
q = {i:len(i) for i in sentence.split(' ')}
print(q)

# Find numbers which is divisible by 2 but not by 5 using list comprehension upto 100
s=[i for i in range(1,101,1) if (i%2==0 and i%5!=0)]
print(s)



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
        
    },
}

individual_expense = {person: sum(expenses[person].values()) for person in expenses.keys()}
print(individual_expense.values())
total_expense = sum(individual_expense.values())

print('Individual Expense', individual_expense)
print('Total Expense', total_expense)

for person, expense in individual_expense.items():
    print('Expense for %s is %d' % (person, ((total_expense/len(expenses)) - individual_expense[person])))