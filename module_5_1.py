class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        
    def go_to(self, new_floor):
        a = 0
        if new_floor < self.number_of_floors:
            while a < self.number_of_floors and a < new_floor:
                a += 1
                print(a)
        else:
            print(f'Такого этажа не существует')
        return a
        
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)   