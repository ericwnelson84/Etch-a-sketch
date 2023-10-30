from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(10)

def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.penup()
    tim.setheading(0)
    tim.setpos(0,0)
    tim.clear()
    tim.pendown()


screen.listen()
# when a function is used as an argument into another function we don't add the parentheses. functions that take
# functions as inputs are called higher order functions
screen.onkey(key="w", fun=move_forwards)
screen.onkey(move_backwards, "s")
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()