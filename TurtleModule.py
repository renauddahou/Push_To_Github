import turtle #the turtule module is built in
t = turtle.Turtle() #initializes the module
turtle.title("My First Turtle")
turtle.bgcolor("#8FCEEB")
#draw a circle:
t.circle(100)
#draw a square:
for i in range (4):
    t.forward(100)
    t.right(90)
turtle.done() #keeps the window open