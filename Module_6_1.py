class Animal:
    def __init__(self,name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self,food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не может съесть {food.name}")
            print(f"{self.name} умер голодной смертью")
            self.alive = False

class Predator (Animal):
    def eat(self,food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не может съесть {food.name}")
            print(f"{self.name} умер голодной смертью")
            self.alive = False

class Flower (Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit (Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

if __name__ == "__main__":
    dog = Predator(" Пёс")
    mouse = Mammal("Мышь")

    rose = Flower("Роза")
    orange = Fruit("Апельсин")

    print(dog.name)
    print(mouse.name)

    print(dog.alive)
    print(mouse.fed)

    dog.eat(rose)
    mouse.eat(orange)
    print(dog.alive)
    print(mouse.fed)