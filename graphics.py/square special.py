import turtle

my_turtle = turtle.Turtle()

def square(length,angle):
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)    

for i in range(4):
    square(70,90)




   
