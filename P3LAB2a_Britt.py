import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("purple")      # Set the window background color
wn.title("Hello, Alex!")  # Set the window title
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.pensize(5)           # Tell Alex to set the pen width
alex.shape("turtle")

# Draw a square
for i in range(3):
    alex.forward(75)          # Tell alex to move forward by 75 units
    alex.left(90)             # Tell alex to turn by 90 degrees

# Draw a triangle
for i in range(2):
    alex.forward(80)          # Tell alex to move forward by 80 units          
    alex.left(120)            # Tell alex to turn by 120 degrees
    alex.forward(80)          # Complete the second side of the triangle
    alex.left(120)            # Tell alex to turn by 120 degrees



# end commands
wn.mainloop()             # Wait for user to close window
