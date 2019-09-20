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
    my_turtle.right(105)
    # (105), (110), (05),(10) are the magical number that will bring near perfect circle.....

    #my_turtle.forward(24) .....  just remove this line will give u something like...............
    '''just run it dude!'''

for i in range(20):
    square(80,90)

