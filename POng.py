import turtle

wn = turtle
wn.title("Pong game first try")
wn.bgcolor("red")
wn.setup(width=800  , height=600 )
wn.tracer(0)

#Score

score_a=0
score_b=0

#Paddle a

paddle_a = turtle.Turtle()
paddle_a.speed(1)
paddle_a.shape("square")
paddle_a.color("light blue")
paddle_a.shapesize(stretch_wid= 5,stretch_len= 1 )
paddle_a.penup()
paddle_a.goto(-550,0)

#paddle_b

paddle_b = turtle.Turtle()
paddle_b.speed(1)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid= 5 ,stretch_len= 1 )
paddle_b.penup()
paddle_b.goto(550, 0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0 , 100)
pen.write("Player A: 0  Player B:0", align="center", font=("Courier", 30, "normal"))

#Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keybinding

wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

def end_board(s):
   pen.clear()
   pen.write("Player"+s+"wins")

#Main game loop

while True:
    wn.update()

    #game end

    if score_a==10 :
        end_board("A")
        exit()
    if  score_b==10:
        end_board("B")
        exit()

    #Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border check

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 590:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 30, "normal"))

    if ball.xcor() < -590:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 30, "normal"))

    #Paddle and ball colllison

    if(ball.xcor() >540 and ball.xcor() < 550 and ball.ycor()< paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.dx *= -1

    if (ball.xcor() < -540 and ball.xcor() > -550 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.dx *= -1