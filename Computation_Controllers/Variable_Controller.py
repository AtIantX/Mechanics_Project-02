from random import randrange


class VariableController:

    g = 10

    def __init__(self):
        self.mass_range = (0, 10)
        # ToDo Change to (0, 0.5)
        self.friction_range = (0, 1)
        self.external_force_range = (-300, 300)

    def get_random_mass(self):
        mass = randrange(*self.mass_range)
        return mass

    def get_random_friction(self):
        friction = randrange(*self.friction_range)
        return friction

    def get_random_external_force(self):
        external_force = randrange(*self.external_force_range)
        return external_force
