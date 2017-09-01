import turtle
import webbrowser

def draw_square():
    jack=turtle.Turtle()
    jack.shape("triangle")
    jack.color("yellow")
    jack.speed(1)
    cnt=1
    jack.forward(100)
    while(cnt<=3):
        jack.right(90)
        jack.forward(100)
        cnt = cnt + 1
 
    
def draw_circle():
    julie=turtle.Turtle()
    julie.shape("circle")
    
    julie.color("blue")
    julie.circle(100)

window=turtle.Screen()
window.bgcolor("red")
webbrowser.open("https://www.youtube.com/watch?v=YAOTCtW9v0M")
draw_square()
draw_circle()
window.exitonclick()

    
    
    
