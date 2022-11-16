# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""
from solar_vis import *

def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """
    body.Fx = body.Fy = 0
    global alive
    global max_distance
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        body.r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.cos_alpha = (obj.x - body.x)/body.r
        body.sin_alpha = (obj.y - body.y)/body.r
        #print(body.color, body.r, body.R)
        #max_distance = max([max(abs(obj.obj.x), abs(obj.obj.y)) for obj in space_objects])
        #calculate_scale_factor(max_distance)       при вызове этой функции принтуется нормальный scale factor
        #print(scale_factor)                        но при попытке принтануть его отдельно выводится 1 и я хз почему оно так

        if body.r <= body.R:
            alive = False
            print("Crash object!!!")
        else:
            body.extra_force_x = gravitational_constant*body.m*obj.m/(body.r**2)*body.cos_alpha
            body.extra_force_y = gravitational_constant*body.m*obj.m/(body.r**2)*body.sin_alpha
            body.Fx += body.extra_force_x
            body.Fy += body.extra_force_y



def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    # FIXME: Вывести формулы для ускорения, скоростей и координат
    # скорее всего косяк именно тут ибо закон движения хуевый на вид
    body.ax = body.Fx/body.m
    body.x += body.vx * dt
    body.ay = body.Fy/body.m
    body.y += body.vy * dt
    body.vy += body.ay*dt
    body.vx += body.ax*dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
