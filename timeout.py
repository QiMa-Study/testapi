# testapi
import turtle
import time

def draw_clock(h, m, s):
    # 绘制表盘
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.circle(200)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    # 绘制时针
    turtle.seth(90)
    turtle.rt(h * 30 + m * 0.5)
    turtle.fd(100)

    # 绘制分针
    turtle.seth(90)
    turtle.rt(m * 6)
    turtle.fd(150)

    # 绘制秒针
    turtle.seth(90)
    turtle.rt(s * 6)
    turtle.fd(180)

while True:
    # 获取当前时间
    t = time.localtime()
    h = t.tm_hour % 12
    m = t.tm_min
    s = t.tm_sec

    # 清空画布，重新绘制时钟
    turtle.clear()
    draw_clock(h, m, s)

    # 显示当前时间
    current_time = time.strftime('%H:%M:%S')
    turtle.penup()
    turtle.goto(-100, 250)
    turtle.write(current_time, font=('Arial', 20, 'normal'))

    # 暂停一秒钟，然后重新绘制时钟
    time.sleep(1)
