from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
    tim.heading()


def move_backwards():
    tim.backward(10)
    tim.heading()


def move_right():
    tim.right(10)
    tim.heading()


def move_left():
    tim.left(10)
    tim.heading()


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
