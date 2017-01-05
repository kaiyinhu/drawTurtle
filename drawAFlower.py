import turtle

def draw_flower():
  window = turtle.Screen()
  window.bgcolor("red")
  brad = turtle.Turtle()
  brad.shape("arrow")
  brad.color("blue")
  for x in range (0, 36):
      brad.right(170)
      brad.forward(100)
      brad.right(45)
      brad.forward(100)
      brad.right(135)
      brad.forward(100)
      brad.right(45)
      brad.forward(100)
    

  window.exitonclick()

draw_flower()
