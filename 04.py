class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name}  поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текуща скорость  {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущую скорость в городе  {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенного для городского автомобиля'
        else:
            return f'Скорость {self.name} нормальная для городского автомобиля'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для рабочей машины {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенного для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полицейского департамента'
        else:
            return f'{self.name} не из плицейского департаменти'


audi = SportCar(100, 'Красная', 'Ауди', False)
oka = TownCar(30, 'Белая', 'Ока', False)
lada = WorkCar(70, 'Синяя', 'Лада', True)
volga = PoliceCar(110, 'Черная',  'Волга', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, тогда {audi.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name} это {lada.color} машина')
print(f'Это {audi.name} полицейская машина? {audi.is_police}')
print(f'Это {lada.name}  полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(volga.police())
print(volga.show_speed())