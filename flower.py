

#import turtle
import turtle

my_screen = turtle.getscreen()
my_turtle = turtle.Turtle()
                #start by making the flower petals
for p in range(10):
                        my_turtle.speed(0)
                        my_turtle.pensize(3)
                        my_turtle.pencolor("pink")
                        my_turtle.penup()
                        my_turtle.goto(0,10)
                        my_turtle.pendown()
                        my_turtle.circle(100,100)
                        my_turtle.left(80)
                        my_turtle.circle(100,100)

                #then make the pistol, or the yellow/orange middle part, of the flowe
for c in range(1):
                        my_turtle.speed(0)
                        my_turtle.pensize(5)
                        my_turtle.pencolor("yellow")
                        my_turtle.penup()
                        my_turtle.goto(-15,7)
                        my_turtle.pendown()
                        my_turtle.color("yellow")
                        my_turtle.begin_fill()
                        my_turtle.circle(20)
                        my_turtle.end_fill()

                #make the stem
for s in range(1):
                        my_turtle.speed(0)
                        my_turtle.pensize(10)
                        my_turtle.pencolor("green")
                        my_turtle.penup()
                        my_turtle.goto(0,-100)
                        my_turtle.pendown()
                        my_turtle.setheading(-90)
                        my_turtle.forward(200)

                #finally make a leaf
for l in range(2):
                        my_turtle.speed(0)
                        my_turtle.pensize(5)
                        my_turtle.pencolor("green")
                        my_turtle.penup()
                        my_turtle.goto(0,-200)
                        my_turtle.pendown()
                        my_turtle.setheading(45)
                        my_turtle.forward(50)
        
        
        

        
        
        








    
