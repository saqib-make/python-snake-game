import turtle
import time
import random

# Game Settings
delay = 0.15
score = 0
high_score = 0
step = 10

# Screen
wn = turtle.Screen()
wn.title("Classic Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Arial", 16, "normal"))

# Movement
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + step)
    elif head.direction == "down":
        head.sety(head.ycor() - step)
    elif head.direction == "left":
        head.setx(head.xcor() - step)
    elif head.direction == "right":
        head.setx(head.xcor() + step)

# Keyboard
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main Loop
try:
    while True:
        wn.update()

        # Wall collision
        if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            pen.clear()
            pen.write(f"Score: {score} High Score: {high_score}",
                      align="center", font=("Arial", 16, "normal"))

        # Food collision
        if head.distance(food) < 15:
            food.goto(random.randint(-280, 280), random.randint(-280, 280))

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("lightgreen")
            new_segment.penup()
            segments.append(new_segment)

            score += 10
            high_score = max(high_score, score)

            pen.clear()
            pen.write(f"Score: {score} High Score: {high_score}",
                      align="center", font=("Arial", 16, "normal"))

        # Move body
        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].pos())

        if segments:
            segments[0].goto(head.pos())

        move()

        # Body collision
        for segment in segments:
            if segment.distance(head) < 10:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                for seg in segments:
                    seg.goto(1000, 1000)
                segments.clear()

                score = 0
                pen.clear()
                pen.write(f"Score: {score} High Score: {high_score}",
                          align="center", font=("Arial", 16, "normal"))

        time.sleep(delay)

except turtle.Terminator:
    print("Game closed safely")
