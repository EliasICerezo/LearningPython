import turtle



def draw_square():
    

    
    
    n=0
    
    while (n<4):
        brad.forward(100)
        brad.right(90)
        n=n+1

    
    

def draw_circle():
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    

def draw_triangle():
    chad=turtle.Turtle()
    chad.color("purple")
    n=0

    
    while (n<3):
        chad.forward(175)
        chad.right(120)
        n=n+1
    
def draw_circle_with_squares():
    n=0
    while(n<72):
        draw_square()
        brad.right(5)
        n=n+1

def draw_flower():
    draw_circle_with_squares()

    brad.right(90)
    brad.forward(200)


#Main


window= turtle.Screen()
window.bgcolor("red")

#Brad definition
brad=turtle.Turtle()
brad.shape("turtle")
brad.color("yellow")
brad.speed(100)

draw_flower()



#draw_square()
#draw_circle()
#draw_triangle()

window.exitonclick()


