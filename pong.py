import turtle


p1score = 0
p2score = 0
# Setup screen
wn = turtle.Screen()
wn.title('Pong by Arav')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('white')
paddle1.penup()
paddle1.goto(-350., 0)
paddle1.shapesize(stretch_wid=5, stretch_len=1)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.color('white')
paddle2.penup()
paddle2.goto(350, 0)
paddle2.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.clear()
pen.write('Player 1 : 0  Player 2 : 0'.format(p1score, p2score), align='center', font=('courier', 24, 'normal'))

# Move
def pad1up():
    y1 = paddle1.ycor()
    y1 += 20
    paddle1.sety(y1)

def pad1down():
    y1 = paddle1.ycor()
    y1 -= 20
    paddle1.sety(y1)

def pad2up():
    y2 = paddle2.ycor()
    y2 += 20
    paddle2.sety(y2)

def pad2down():
    y2 = paddle2.ycor()
    y2 -= 20
    paddle2.sety(y2)

# Keyboard input
wn.listen()
wn.onkey(pad1up, 'w')
wn.onkey(pad1down, 's')
wn.onkey(pad2up, 'Up')
wn.onkey(pad2down, 'Down')

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Check if the ball hit the border
    if ball.ycor() == 280:
        ball.dy *= -1

    if ball.ycor() == -280:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        p1score += 1
        pen.clear()
        pen.write('Player 1 : {}  Player 2 : {}'.format(p1score, p2score), align='center', font=('courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        p2score += 1
        pen.clear()
        pen.write('Player 1 : {}  Player 2 : {}'.format(p1score, p2score), align='center', font=('courier', 24, 'normal'))

    # Checking if the paddle touches the ball
    if ball.xcor() == paddle2.xcor() and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() -50):
        ball.dx *= -1

    if ball.xcor() == paddle1.xcor() and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() -50):
        ball.dx *= -1
