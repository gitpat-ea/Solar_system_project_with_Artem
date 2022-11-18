# coding: utf-8
# license: GPLv3

from source_code.solar_objects import Star, Planet
from source_code.solar_vis import DrawableObject
import numpy as np

def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселаx> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star.R = float(line[1])
    star.color = line[2]
    star.m = float(line[3])
    star.x = float(line[4])
    star.y = float(line[5])
    star.vx = float(line[6])
    star.vy = float(line[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.R = float(line[1])
    planet.color = line[2]
    planet.m = float(line[3])
    planet.x = float(line[4])
    planet.y = float(line[5])
    planet.vx = float(line[6])
    planet.vy = float(line[7])


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            line = line.split()
            object_type = line[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")
    return [DrawableObject(obj) for obj in objects]


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        a = np.array()
        for obj in space_objects:
            np.append(a, 1)
            print(a)
            a = str(a)
            out_file.write(a)

#def clear_a_file(output_filename):
#    '''
#
#    :param output_filename: name of a file which should be cleaned
#    :return: cleared file fith same name
#    '''
#    with open(output_filename, 'w') as out_file:
#        out_file.clear()




if __name__ == "__main__":
    print("This module is not for direct call!")
