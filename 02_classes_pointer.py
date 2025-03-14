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
