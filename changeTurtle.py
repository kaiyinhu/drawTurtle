import turtle
def draw_shape():
     window = turtle.Screen()
     window.bgcolor("red")
     draw_square()
     draw_circle()
     draw_triangle()

     window.exitonclick() 

def draw_square():
     brad = turtle.Turtle()
     brad.shape("arrow")

     for x in range(0, 4):
          brad.forward(100)
          brad.right(90)
     
def draw_circle():
     angie = turtle.Turtle()
     angie.shape("arrow")
     angie.color("blue")
     angie.circle(100)

def draw_triangle():
     jack = turtle.Turtle()
     jack.shape("arrow")
     jack.color("green")

     for x in (0, 2):
          jack.forward(100)
          jack.right(120)

     jack.forward(100) 
     jack.right(60)   


draw_shape()
