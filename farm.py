class Animal:
    hunger = 'hungry'
    voice = 'mute'
    collectable = 'None'
    ready = 'Full'

    def __init__(self, init_name, init_weight):
        self.name = init_name
        self.weight = init_weight

    def feed(self):
        self.hunger = 'sated'
        print(f'{self.name} looks happy')

    def listen(self):
        print(f'{self.name} voice sounds like {self.voice}')

    def collect(self):
        if self.ready == 'Full':
            print(f'you have collected {self.collectable} from {self.name}')
            self.ready = 'Empty'
        else:
            print(f'You have already collected {self.collectable} from {self.name}, you have to wait')


class Geese(Animal):
    voice = 'Honk'
    collectable = 'egg'


class Chicken(Animal):
    voice = 'Cluck'
    collectable = 'egg'


class Cows(Animal):
    voice = "Moo"
    collectable = 'milk'


class Sheep(Animal):
    voice = 'Baa'
    collectable = 'wool'


class Ducks(Animal):
    voice = 'Quack'
    collectable = 'egg'


class Goats(Animal):
    voice = 'Bleat'
    collectalbe = 'milk'


animalList = [Geese('Серый', 3.2), Geese('Белый', 3.1), Cows('Манька', 455), Sheep('Барашек', 107),
              Sheep('Кудрявый', 106), Chicken('Ко-ко', 1.2), Chicken('Кукареку', 1.3), Goats('Рога', 87),
              Goats('Копыта', 76), Ducks('Кряква', 1.7)]

print(animalList[0].__dict__)
scaling = {
}

for animals in animalList:
    scaling[animals.__dict__['name']] = animals.__dict__['weight']

print(f'Общей вес животных составлят {sum(scaling.values())} кг')

for name, weight in scaling.items():
    if weight == max(scaling.values()):
        print(f'Самое тяжелое животное зовут {name}')
