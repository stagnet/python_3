import turtle

my_turtle = turtle.Turtle()

def square(length,angle):
    #1
    my_turtle.forward(length)
    my_turtle.right(angle)
   #2 
    my_turtle.forward(length)
    my_turtle.right(angle)
    #3
    my_turtle.forward(length)
    my_turtle.right(angle)
    #4
    my_turtle.forward(length)
    my_turtle.right(110)
    #gives extra distance to bring another circle outside previous one.
    my_turtle.forward(54)

for i in range(20):
    square(50,90)






  
