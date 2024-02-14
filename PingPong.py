import turtle
import winsound
import time

wn = turtle.Screen()
wn.title("PingPong")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)
score_1 = 0
score_2 = 0
pressed_keys = set()
ticks_per_second = 60
delay = int(1000 / ticks_per_second)
tick_timer = 0
tick_timer_clock = 0



#paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("red")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)
#paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))

wn.listen()
wn.onkeypress(lambda: pressed_keys.add("w"), "w")
wn.onkeyrelease(lambda: pressed_keys.remove("w"), "w")

wn.onkeypress(lambda: pressed_keys.add("s"), "s")
wn.onkeyrelease(lambda: pressed_keys.remove("s"), "s")

# 2
wn.onkeypress(lambda: pressed_keys.add("Up"), "Up")
wn.onkeyrelease(lambda: pressed_keys.remove("Up"), "Up")

wn.onkeypress(lambda: pressed_keys.add("Down"), "Down")
wn.onkeyrelease(lambda: pressed_keys.remove("Down"), "Down")

timer = turtle.Turtle()
timer.speed(0)
timer.color("red")
timer.penup()
timer.hideturtle()
timer.goto(0, 220)

xcor_old = ball.xcor()
ycor_old = ball.ycor()

def game_loop():
    wn.update()
    global score_1, score_2
    global tick_timer
    global tick_timer_clock
    global xcor_old, ycor_old
    if tick_timer == 600:
        if ball.dy > 0:
            ball.dy = ball.dy + 0.5
        if ball.dy < 0:
            ball.dy = ball.dy - 0.5
        if ball.dx > 0:
            ball.dx = ball.dx + 0.5
        if ball.dx < 0:
            ball.dx = ball.dx - 0.5

        tick_timer = 0
    tick_timer += 1 

    tick_timer_clock += 1
    timer.clear()
    timer.write(f"Timer: {tick_timer_clock //60}", align="center", font=("Courier", 24, "normal"))

    if "w" in pressed_keys and paddle_1.ycor() < 290:
        paddle_1.sety(paddle_1.ycor() + 20)
    if "s" in pressed_keys and paddle_1.ycor() > -290:
        paddle_1.sety(paddle_1.ycor() - 20)


    if "Up" in pressed_keys and paddle_2.ycor() < 290:
        paddle_2.sety(paddle_2.ycor() + 20)
    if "Down" in pressed_keys and paddle_2.ycor() > -290:
        paddle_2.sety(paddle_2.ycor() - 20)

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bruh.wav", winsound.SND_ASYNC)
        time.sleep(3)
        



    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bruh.wav", winsound.SND_ASYNC)
        time.sleep(3)

    

    collision_radius = 60

    #math
    xcor_old = (xcor_old + ball.xcor()) / 2


    ycor_old = (ycor_old + ball.ycor()) / 2



#ball old collision check
    if (xcor_old > 340 and xcor_old < 350) and (ycor_old < paddle_2.ycor() + collision_radius and ycor_old > paddle_2.ycor() - collision_radius):
        ball.setx(340)
        ball.dx *= -1
    if (xcor_old > -350 and xcor_old < -340) and (ycor_old < paddle_1.ycor() + collision_radius and ycor_old > paddle_1.ycor() - collision_radius):
        ball.setx(-340)
        ball.dx *= -1
#current ball collision check
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + collision_radius and ball.ycor() > paddle_2.ycor() - collision_radius):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() > -350 and ball.xcor() < -340) and (ball.ycor() < paddle_1.ycor() + collision_radius and ball.ycor() > paddle_1.ycor() - collision_radius):
        ball.setx(-340)
        ball.dx *= -1
    
    xcor_old = ball.xcor()
    ycor_old = ball.ycor()



    wn.ontimer(game_loop, delay)
game_loop()
wn.mainloop()
