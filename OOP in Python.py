"""
Абстракция (abstraction) -      метод решения задачи, при котором объекты разного
                                рода объединяются общим понятием (концепцией), а затем сгруппированные сущности
                                рассматриваются как элементы единой категории.
Инкапсуляция (encapsulation) -  техника, при которой несущественная с точки
                                зрения интерфейса объекта информация прячется внутри него.
Наследование (inheritance) -    свойство объектов, посредством которого экземпляры
                                класса получают доступ к данным и методам классов-предков без их повторного
                                определения.
Полиморфизм (polymorphism) -    свойство, позволяющее использовать один и тот же
                                интерфейс для различных действий; полиморфной переменной, например,
                                может соответствовать несколько различных методов.
"""

# По принципу Абстракции, есть некоторое транспортное средство (Vehicle)
# с методами движение (ускорение - accelerate) и остановки (тормозить - brake)
# а так же с методом текущего статуса

class Vehicle(object):
    def __init__(self, speed, max_speed):
        self.speed = speed
        self.max_speed = max_speed
        print('Было создано транспортное средство')

    def accelerate(self, x):
        self.speed = self.speed + x
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def brake(self, x):
        self.speed = self.speed - x
        if self.speed < 0:
            self.speed = 0

    def print_status(self):
        print(f'Скорость транспортного средства равна {self.speed} км/ч')

# Данный класс Motorcycle по принципу Наследования - наследует методы класса Vehicle
# и по принципу Инкапсуляции создаются дополнительные защищенные свойства
class Motorcycle(Vehicle):
    def __init__(self, speed, max_speed):
        Vehicle.__init__(self, speed, max_speed)
        # Дополнительные поля, по принципу Полиморфизма
        self._front_tire_width = 95
        self._rear_tire_width = 95

    def set_tires_width(self, front, rear):
        self._front_tire_width = front
        self._rear_tire_width = rear
        print('На мотоцикл были установлены новые шины')

    def print_tire_info(self):
        print(f'Ширина передней шины {self._front_tire_width} мм')
        print(f'Ширина задней шины {self._rear_tire_width} мм')

# По такому же принципу, что и прошлый класс
class Automobile(Vehicle):
    def __init__(self, speed, max_speed):
        Vehicle.__init__(self, speed, max_speed)
        # Дополнительные поля, по принципу Полиморфизма
        self._gear = 0
        self._color = 'белый'

    def set_gear(self, gear):
        self._gear = gear

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def print_status(self):
        Vehicle.print_status(self)
        print(f'Коробка передач автомобиля переключена № {self._gear}')
        print(f'Автомобиль покрашен в {self._color} цвет')



print('>>> moto = Motorcycle(40, 120)')
moto = Motorcycle(40, 120)
print('>>> moto.print_status()')
moto.print_status()
print('>>> moto.set_tires_width(90, 100)')
moto.set_tires_width(90, 100)
print('>>> moto.print_tire_info()')
moto.print_tire_info()

print('\n\n>>> auto = Automobile(0, 150)')
auto = Automobile(0, 150)
print('>>> auto.accelerate(40)')
auto.accelerate(40)
print('>>> auto.set_gear(2)')
auto.set_gear(2)
print('>>> auto.print_status()')
auto.print_status()
print(">>> auto.set_color('красный')")
auto.set_color('красный')
print('>>> color = auto.get_color()')
color = auto.get_color()
print(color)