import sys
import pygame
from random import randint

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

x = 30
y = 30
vx = 50
vy = 50
a = 5

x2 = 200
y2 = 200
vx2 = 0
vy2 = 0

sticks = 0
circles = []
while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
            circles.append({'color': (randint(0, 255),
                                      randint(0, 255),
                                      randint(0, 255)),
                            'pos': pygame.mouse.get_pos(),
                            'r': 20})

    x += vx * dt
    y += vy * dt

    if not (20 < x < width - 20):
        vx = -vx

    if not (20 < y < height - 20):
        vy = -vy

    if pygame.key.get_pressed()[pygame.K_UP]:
        vy -= a

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        vy += a

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        vx -= a

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        vx += a

    fx = -vx * abs(vx) * 0.00005
    fy = -vy * abs(vy) * 0.00005
    vx += fx
    vy += fy

    if not (20 < x2 < width - 20):
        vx2 = -vx2

    if not (20 < y2 < height - 20):
        vy2 = -vy2

    x2 += vx2 * dt
    y2 += vy2 * dt

    if ((x - x2)**2 + (y - y2)**2)**0.5 <= 40:
        # Код соударения
        if not sticks:
            sticks = 1
            c = (x2 - x, y2 - y)
            cos_cx = abs(c[0]) / (c[0]**2 + c[1]**2)**0.5
            cos_cy = abs(c[1]) / (c[0]**2 + c[1]**2)**0.5
            vx, vy, vx2, vy2 = \
                vx - vx * cos_cx + vx2 * cos_cx, \
                vy - vy * cos_cy + vy2 * cos_cy, \
                vx2 - vx2 * cos_cx + vx * cos_cx, \
                vy2 - vy2 * cos_cy + vy * cos_cy
    else:
        sticks = 0

    screen.fill((0, 0, 0))

    for circle in circles:
        pygame.draw.circle(screen, circle['color'], circle['pos'], circle['r'])

    v = (vx**2 + vy**2)**0.5
    pygame.draw.circle(screen, (v**2 / 255 if v**2 / 255 < 255 else 255,
                                100 - v / 5 if 100 - v / 5 > 0 else 0,
                                50), (int(x), int(y)), 20)

    pygame.draw.circle(screen, (173,
                                100,
                                50), (int(x2), int(y2)), 20)

    pygame.display.flip()
