# def main_controller:


class ComputationEngine:
    object1, object2, object3 = None, None, None
    acceleration_2, acceleration_1 = 0, 0
    g, external_force = 0, 0

    def __init__(self, object1, object2, object3, g, external_force):
        ComputationEngine.object1 = object1
        ComputationEngine.object2 = object2
        ComputationEngine.object3 = object3
        ComputationEngine.g = g
        ComputationEngine.external_force = external_force

    @staticmethod
    def compute():
        obj1 = ComputationEngine.object1
        obj2 = ComputationEngine.object2
        obj3 = ComputationEngine.object3
        # First of all compute acceleration2
        ComputationEngine.acceleration_2 = ComputationEngine.compute_acceleration_2(obj1.weight, obj2.weight, obj3.weight, obj1.friction, obj2.friction, obj3.friction, ComputationEngine.g, ComputationEngine.external_force)
        ComputationEngine.acceleration_1 = ComputationEngine.compute_acceleration_1(ComputationEngine.acceleration_2, obj1.weight, obj2.weight, obj1.friction, obj2.friction, ComputationEngine.g)
        return [ComputationEngine.acceleration_2, ComputationEngine.acceleration_1]

    @staticmethod
    def compute_acceleration_2(m1, m2, m3, f1, f2, f3, g, external_force):
        acc = (-1*(m1+m3)*(f2*m2*g - m3*g + 2*f3*external_force) + m3*(f2*m2*g - f1*m1*g + f1*f2*m2*g))/(m2*(m1+m3) - m3*(-1*m2 + f1*m2 - m1 - m3))
        return acc

    @staticmethod
    def compute_acceleration_1(a2, m1, m2, f1, f2, g):
        acc = (-1*m2*a2 + f2*m2*g - f1*m1*g + f1*m2*a2 + f1*f2*m2*g)/(m1+m2)
        return acc
