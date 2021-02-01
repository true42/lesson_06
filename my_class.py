import time


# задача №1
class TrafficLight:
    __color = {'color': ['red', 'yellow', 'green'],
               'time': [7, 2, 5]}

    def running(self):
        for i in range(len(self.__color['color'])):
            print(self.__color['color'][i])
            time.sleep(self.__color['time'][i])
        return


# задача №2
class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calculation(self, thickness=5, weight=25):
        """
        Возвращает массу асфальта необходимого для покрытия дороги
        при расчёте на толщину дороги в 5 см и массе асфальта на 1 кв. см. в 25 кг
        """

        return f'{(self._length * self._width * weight * thickness) / 1000} т.'


# задача №3
class Worker:
    name = None
    surname = None
    position = None
    _income = {"engineer": {'wage': 50000, 'bonus': 10000},
               "cleaner": {'wage': 25000, 'bonus': 5000},
               "manager": {'wage': 50000, 'bonus': 10000}
               }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def __str__(self):
        try:
            return f'{self.name} {self.surname}, {self.position} — с зарплтой {self._income[self.position]["wage"]+self._income[self.position]["bonus"]} рублей.'
        except KeyError:
            return f'Введите вакансию правильно'

    def chek_position(self):
        if self.position not in self._income:
            print(f'У нас нет вакансии {self.position}.')
        else:
            return


class Position(Worker):
    def get_full_name(self):
        return f'Полное имя работника: {self.name} {self.surname}'

    def get_total_income(self):
        try:
            self.chek_position()
            return f'Зарплата {self.name} {self.surname}: {self._income[self.position]["wage"]+self._income[self.position]["bonus"]} рублей.'
        except KeyError:
            return f'Выберите из представленных: {", ".join("{}".format(k) for k in Worker._income.keys())}'


# задача №4
class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police=None):
        self.speed = speed
        self.name = name
        self.color = color
        if self.is_police is None:
            self.is_police = Car.is_police
        else:

            self.is_police = is_police

    def __str__(self):
        if self.is_police is True:
            return f"Полицейская {self.color} {self.name}, разгоняется до {self.speed} км/ч"
        else:
            return f"{self.color.title()} {self.name}, разгоняется до {self.speed} км/ч"

    def go(self):
        print(f'{self.color.title()} {self.name} поехала!')

    def stop(self):
        print(f'{self.color.title()} {self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.color.title()} {self.name} повернула {direction}!')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость!')


class PoliceCar(Car):
    pass


# задача № 5
class Stationery:
    title = ['ручка', 'карандаш', 'маркер']

    def __init__(self):
        self.title = Stationery.title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки инструментом: {self.title[0]}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки инструментом: {self.title[1]}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки инструментом: {self.title[2]}')
