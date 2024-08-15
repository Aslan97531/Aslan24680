class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Fruit(Plant):

    def food(self, food):
        self.edible = True
        self.name = food


class Flower(Plant):

    def food(self, food):
        self.edible = False
        self.name = food


class Mammal(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.food = True

    def eat(self, food):
        print(f'{self.name} съел {food.name}')
        self.fed = True

class Predator(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.food = False

    def eat(self, food):
        print(f'{self.name} не стал есть {food.name}')
        self.alive = False


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
