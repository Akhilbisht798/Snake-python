import turtle as t
import snakeClass
import time
import scoreboard
import snakefood
screen = t.Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = snakeClass.Snake()
food = snakefood.Food()
screen.listen()
score = scoreboard.Scoreboard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")



is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)< 15:
        food.refresh()
        score.increaseScore()
        snake.extend()
    
    if snake.segments[0].xcor()>= 300 or snake.segments[0].ycor()>= 300:
        score.resetScore()
        snake.reset_snake()
    if snake.segments[0].xcor()<= -300 or snake.segments[0].ycor()<= -300:
        score.resetScore()
        snake.reset_snake()
    
    #tail detection;
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            score.resetScore()
            snake.reset_snake()
        
    


screen.exitonclick()
