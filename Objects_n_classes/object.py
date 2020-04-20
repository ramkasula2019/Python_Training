#Implement pow(x, n) using class
class pow:
    # initialization
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent
        
    # instance method to calculate power
    def calculate_power(self):
        return self.base ** self.exponent
    
p = pow(2, 6)
p.calculate_power()
g = pow(3, 8)
g.calculate_power()

# Reverse a string word by word: Input: hello world Output: world hello
class reverse_string:
    
    def __init__(self, input_text):
        self.input_text = input_text
        
    def perform_reverse_by_word(self):
        split_in_list_of_word = self.input_text.split(' ')
        reverse_unlist_word = ' '.join(reversed(split_in_list_of_word))
        return reverse_unlist_word

    # Reverse a string in word by word. Example: Input: hello world Output: dlrow olleh
    #https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
    def perform_reverse_by_letter(self):
        p = self.perform_reverse_by_word()
        q = []
        for i in  list(p.split(' ')):            
            i = i[::-1] 
            q.append(i)
        return ' '.join(q) 
 
input_text='hello world program'
rev = reverse_string(input_text)
print(rev.perform_reverse_by_word())
print(rev.perform_reverse_by_letter())


# class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius **2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c = Circle (5)    
print(c.area())
print(c.perimeter())    
        
# A class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case
class StringManipulator():
    input_string = ''
    
#     def __init__(self):
#         pass

    def get_String(self, user_input):
        self.input_string = user_input
        #return self.input_string
    
    def print_String(self):
        return self.input_string.upper()
    
    
sm =  StringManipulator()  
sm.get_String('parasite')
sm.print_String()

# Create class named Shape which has attributes length and breath and a method area,
# which returns the area of the shape [Assuming area to be length * breath]

class Shape:
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return "The aread of given dimesion is %d" %(self.length * self.breadth)
    
s = Shape(5, 6)    
s.area()

# Create a class named Dog which has instance attributes name, breed, life_expectancy, origin_place and class attribute species.
# Add instance method bark(), eat(), description() methods.

class Dog:
    # class attribute
    species = 'German Shepard'
    
    # instance attribute
    def __init__(self, name, breed, life_expectancy, origin_place):
        self.name = name
        self.breed = breed
        self.life_expectancy = life_expectancy
        self.origin_place = origin_place
        
    def bark(self):
        return "%s with %s breed has life expectancy %d which is born on %s. it is simply species %s" %(self.name, self.breed, self.life_expectancy, self.origin_place, self.species) 
        
d1 = Dog('tiger', 'small', 12, 'Nepal')        
d1.bark()
d1.species = 'labroider'
d1.bark()