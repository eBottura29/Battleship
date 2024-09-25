class Square:
    def __init__(self):
        self.sea = 0
        self.shot = 1
        self.destroyer = 2
        self.submarine = 3
        self.cruiser = 4
        self.battleship = 5
        self.carrier = 6

        self.destroyer_size = 2
        self.submarine_size = 3
        self.cruiser_size = 3
        self.battleship_size = 4
        self.carrier_size = 5


class ClassifiedSquare:
    def __init__(self):
        self.not_shot = 0
        self.miss = 1
        self.hit = 2


squares = Square()
csquares = ClassifiedSquare()
