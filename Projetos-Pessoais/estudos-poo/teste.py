

class Player:
    def __init__(self, name: str, height: float, position: str):
        self.name = name
        self.height = height
        self.position = position

    def introduce(self):
        print(f'Hi, I am {self.name}, {self.height}cm and I play as {self.position}!')

    def points(self, p=18):
        print(f'{self.name} scored {p} points tonight!')


Tatum = Player(name='Jayson Tatum', height=2.03, position='SF')

Tatum.introduce()
Tatum.points(51)
