import graphics as gr
import math as m


#Функция сложения координат двух точек
def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point

#Координаты новой точки с учётом заданной скорости
def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)

#Функция вычитания координат двух точек
def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point


SIZE_X = 700
SIZE_Y = 700

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

#  Начальное положение шарика
center_x = window.width//2
center_y = window.height//2
coords = gr.Point(center_x, center_y)

# Параметры двигающегося объекта
R = 10
circle = gr.Circle(gr.Point(coords.x, coords.y), R)
circle.setFill('red')
circle.draw(window)

velocity = gr.Point(6, 0)
acceleration = gr.Point(-0.1, 0)
flag = 1

while True:
    circle.move(velocity.x, velocity.y)
    velocity = update_velocity(velocity, acceleration)
    if (circle.getCenter().x <= center_x) and flag:
        acceleration.x = -acceleration.x
        velocity = gr.Point(-6, 0)
        flag = not flag
    elif (circle.getCenter().x >= center_x) and not flag:
        acceleration.x = -acceleration.x
        velocity = gr.Point(6, 0)
        flag = not flag
    x = circle.getCenter().x
    while circle.getCenter().y < int((400**2 - (x-center_x)**2)**.5):
        circle.move(0, 1)
    while circle.getCenter().y > int((400**2 - (x-center_x)**2)**.5):
        circle.move(0, -1)
    gr.time.sleep(0.04)
