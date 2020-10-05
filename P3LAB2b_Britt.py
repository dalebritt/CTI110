import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("light pink")      # Set the window background color
wn.title("Hello, Dale!")  # Set the window title
dale = turtle.Turtle()    # Create a turtle, assign to dale
dale.pensize(5)           # Tell Dale to set the pen width
dale.shape("turtle")

# Letter D
dale.circle(50, 180) 
dale.left(90)
dale.forward(100)
dale.left (90)

# Letter B
dale.pendown()
dale.forward(75)
dale.circle(26,180)
dale.forward(25)
dale.setheading(0)
dale.forward(25)
dale.circle(22,180)
dale.forward(26)
dale.setheading(270)
dale.forward(95)
dale.setheading(32)
dale.penup()
dale.forward(160)
