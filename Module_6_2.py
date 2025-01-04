class Vehicle:
    __COLOR_VARIANTS = ['черный', 'красный', 'синий', 'белый', 'желтый', 'зеленый']
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
    def valid_color(self,color):
        if color in (c.lower() for c in Vehicle.__COLOR_VARIANTS):
            print('Цвет выбран!')
        elif color not in (c.lower() for c in Vehicle.__COLOR_VARIANTS):
            print(f'{color} не допустим! Выберите другой цвет из предложенных')

    def get_model(self):
        print(f'Модель : {self.__model}')
    def get_horsepower(self):
        print(f'Мощность : {self.__engine_power}')
    def get_color(self):
        print(f'Цвет : {self.__color}')
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец : {self.owner}')
    def set_color(self,new_color):
        new_color_lower = new_color.lower()
        if new_color_lower in (c.lower() for c in Vehicle.__COLOR_VARIANTS):
            self.valid_color(new_color)
            self.__color = new_color_lower
            print(f'Цвет поменялся на {new_color_lower}')
        elif new_color_lower not in (c.lower() for c in Vehicle.__COLOR_VARIANTS):
            raise ValueError(f'Нельзя сменить цвет на {new_color}, выберите другой')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)
        self.current_passengers = 0
    def add_passengers(self, number_passengers):
        if self.current_passengers + number_passengers > self.__PASSENGERS_LIMIT:
           raise ValueError('Превышен лимит мест')
        self.current_passengers +=number_passengers
    def print_info(self):
        super().print_info()
        print(f'Пассажиров : {self.current_passengers}')

car = Sedan('Дима', 'Audi Q7', 200, 'черный')
car.add_passengers(5)
car.print_info()
car.set_color('красный')
car.print_info()
car.set_color('фиолетовый')
car.add_passengers(6)
car.print_info()