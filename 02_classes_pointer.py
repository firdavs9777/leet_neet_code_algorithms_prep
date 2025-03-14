import copy

class Cookie:
    def __init__(self, color):
        self.color = color  # Initialize the cookie color
    
    def get_color(self):
        return self.color  # Return the current color
    
    def set_color(self, color):
        self.color = color  # Update the color


# Creating two Cookie objects
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

# Printing the initial color of cookie_one
print("Cookie One Color:", cookie_one.get_color())  # Output: green

# Changing the color of cookie_one
cookie_one.set_color('red')

# Printing the updated color of cookie_one
print("Updated Cookie One Color:", cookie_one.get_color())  # Output: red

# Printing the color of cookie_two
print("Cookie Two Color:", cookie_two.get_color())  # Output: blue


## Pointers 

a = [1,2,3]
b = a
b.append(4)
print("A: ",a)
print("B: ",b)
# A:  [1, 2, 3, 4]
# B:  [1, 2, 3, 4]


# Mutable vs immutable objects 


# Avoiding Unintended Changes with copy.deepcopy()
a = 5
b  = a
b = 10 
print(a)
print(b)
# Integers are not mutable 
a = [1, 2, 3]
b = copy.deepcopy(a)  # Creates a new list in memory
b.append(4)
print(a)  # Output: [1, 2, 3]  (a remains unchanged)
print(b)  # Output: [1, 2, 3, 4]  (only b is modified)