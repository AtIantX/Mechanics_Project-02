from random import randrange


class Environment:

    def __init__(self):
        self.mass_range = (0, 10)
        self.friction_range = (0, 0.5)
        self.external_force_range = (-300, 300)
        self.g = 10

    def get_variables_defined_random(self):
        mass_1 = randrange(*self.mass_range)
        friction_1 = randrange(*self.friction_range)
        mass_2 = randrange(*self.mass_range)
        friction_2 = randrange(*self.friction_range)
        mass_3 = randrange(*self.mass_range)
        friction_3 = randrange(*self.friction_range)
        external_force = randrange(*self.external_force_range)
        return {(mass_1, friction_1), (mass_2, friction_2), (mass_3, friction_3), external_force, self.g}

