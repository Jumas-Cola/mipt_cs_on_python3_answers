import graphics as gr
import re


#Получение координат в текущий момент времени
def get_circle_coords(circle):
    coords = list(map(lambda x: float(x), re.findall(r'Point+.*\),+', str(circle))[0].rstrip('),').lstrip('Point(').split(',')))
    return gr.Point(coords[0], coords[1])

#Проверка выхода за границы поля
def check_coords(coords, velocity):
    if coords.x>= SIZE_X or coords.x<=0:
        velocity.x = -velocity.x
    if coords.y>= SIZE_Y or coords.y<=0:
        velocity.y = -velocity.y

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

#Координаты новой точки с учётом центральной силы тяжести
def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)
    G = 2000
    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)

def sun(x,y,d):
    sun = gr.Circle(gr.Point(x,y), d)
    sun.setFill('yellow')
    sun.draw(window)


SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

#Обьект Circle создается здесь лишь ОДИН раз
coords = gr.Point(400, 700)

#Параметры двигающегося объекта
circle = gr.Circle(gr.Point(coords.x, coords.y), 10)
circle.setFill('red')
circle.draw(window)

sun(400,400,20)

velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)

while True:
    # Метод move передвигает обьект circle на (1, 1) относительно его текущего положения
    circle.move(velocity.x, velocity.y)

    acceleration = update_acceleration(coords, gr.Point(400, 400))

    coords = get_circle_coords(circle)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.02)
