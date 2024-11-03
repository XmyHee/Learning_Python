import turtle

#设置画笔与画布
canvas = turtle.Screen()
canvas.bgcolor("black")
pen = turtle.Turtle()
pen.speed(10)


#设置玫瑰花的颜色和形状

colors =  ["red","blue","purple","yellow"]
petal_shape =[(0,0),(-10,-50),(0,-80),(10,-50)]

#绘制玫瑰花
for _ in range(36):
    pen.color(colors[_%4])
    pen.penup()
    pen.goto (0,0)
    pen.pendown()
    pen.seth(_*10)
    pen.begin_fill()
    pen.circle(100,steps=4)
    pen.end_fill()

#绘制花瓣
    pen.color("green")
    pen.penup()
    pen.goto(0,-100)
    pen.pendown()
    pen.seth(_*10)
    pen.begin_fill()
    for point in petal_shape:
         pen.goto(point[0],point[1] -100)
    pen.end_fill()

#绘制结束
pen.hideturtle()
canvas.exitonclick()

