#Unbeatable Pong


import turtle
import winsound

# Environment
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_a.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .22
ball.dy = .22

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1: 0, Player2: 0", align="center", font=("Courier", 24, "normal"))

#Functions

def paddle_a_up():
	y = paddle_a.ycor()
	y += 50
	paddle_a.sety(y)



def paddle_a_down():

	y = paddle_a.ycor()
	y -= 50
	paddle_a.sety(y)



def paddle_b_up():

	y = paddle_b.ycor()
	y += 33
	paddle_b.sety(y)



def paddle_b_down():

	y = paddle_b.ycor()
	y -= 33
	paddle_b.sety(y)



#Keyboard Binding

#Listen to key inputs
wn.listen()

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#Main game loop

while True:

	wn.update()

	#Move the Ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# This will cause paddle b to always be aligned with the ball
	# Remove this line of code for game to be two players (locally)
	paddle_b.sety(ball.ycor())

	#Borders
	if ball.ycor() > 290:
	    ball.sety(290)
	    ball.dy *= -1	#  <--- this equation reverses direction

	
	if ball.ycor() < -290:
	    ball.sety(-290)
	    ball.dy *= -1





	if ball.xcor() > 390:
	    ball.setx(390)
	    ball.dx *= -1
	    score_a += 1
	    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
	    pen.clear()
	    pen.write("Player1: {}, Player2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


	if ball.xcor() < -390:

	    ball.setx(-390)
	    ball.dx *= -1
	    score_b += 1
	    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
	    pen.clear()
	    pen.write("Player1: {}, Player2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	#Paddle & Ball collisions

	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
		ball.setx(340)
		ball.dx *= -1



	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
		ball.setx(-340)
		ball.dx *= -1





	



	


