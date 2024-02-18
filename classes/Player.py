class Player:
    def __init__(self):
        self.pos_x = 300
        self.pos_y = 300
        self.max_energy = 255
        self.energy = 255
        self.color = (255, 0, self.energy)
        self.is_dead = False

    def move(self, x_move, y_move):
        if not self.is_dead:
            self.pos_x += (x_move * 3)
            if self.pos_x > 585:
                # Jump from Right Side to Left Side
                self.pos_x = 15
            if self.pos_x < 15:
                # Jump from Left Side to Right Side
                self.pos_x = 585
            self.pos_y += (y_move * 3)
            if self.pos_y < 15:
                # Jump from Top to Bottom
                self.pos_y = 585
            if self.pos_y > 585:
                # Jump from Bottom to Top
                self.pos_y = 15
            self.color = (255, 0, self.energy)
            if self.energy <= 0:
                self.is_dead = True

    def alter_energy(self, value):
        self.energy += value

    def get_max_energy(self):
        return self.max_energy

    def get_energy(self):
        return self.energy

    def get_color(self):
        return self.color

    def get_pos(self):
        return self.pos_x, self.pos_y

