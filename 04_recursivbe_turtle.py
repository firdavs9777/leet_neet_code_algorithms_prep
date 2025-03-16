import turtle 

def drawSpiral(t, length, color, colorBase):
    if length == 0:
        return 
    
    # Convert color hex string to an integer
    newColor = (int(color[1:], 16) + 2 ** 10) % (2 ** 24)
    base = int(colorBase[1:], 16)

    if newColor < base: 
        newColor = (newColor + base) % (2**24)

    # Convert back to hex and ensure 6-digit formatting
    newColor = f"#{newColor:06x}"  # Format hex properly
    
    t.color(newColor)
    t.forward(length)
    t.left(90)
    
    drawSpiral(t, length - 1, newColor, colorBase)

def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(100)  # Use 0 for the fastest speed
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    drawSpiral(t, 200, "#000000", "#ff00ff")
    screen.exitonclick()  # Corrected function name

if __name__ == "__main__":
    main()
