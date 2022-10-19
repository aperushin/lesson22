# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, field, flying: bool, speed=1):
        self.field = field
        if flying:
            self.speed = speed * 1.2
        else:
            self.speed = speed * 0.5
        self.x_coord = 0
        self.y_coord = 0

    def move(self, direction):
        new_x, new_y = self.calculate_coord(direction)
        self.field.set_unit(x=new_x, y=new_y, unit=self)

    def calculate_coord(self, direction):
        if direction == 'UP':
            new_y = self.y_coord + self.speed
            new_x = self.x_coord
        elif direction == 'DOWN':
            new_y = self.y_coord - self.speed
            new_x = self.x_coord
        elif direction == 'LEFT':
            new_y = self.y_coord
            new_x = self.x_coord - self.speed
        elif direction == 'RIGTH':
            new_y = self.y_coord
            new_x = self.x_coord + self.speed
        return (new_x, new_y)
