# Start Simulation
from .Environment_Controller import Environment
from .Computation_Controller import ComputationEngine


class Simulation:
    Environment = None
    Engine = None

    def __init__(self):
        self.force_time = [[100, 0], [100, 5]]

    @staticmethod
    def create_environment():
        Simulation.Environment = Environment

    @staticmethod
    def create_compute_engine():
        Simulation.Engine = ComputationEngine(Simulation.Environment.object1, Simulation.Environment.object2,
                                              Simulation.Environment.object3, Simulation.Environment.g,
                                              Simulation.Environment.external_force)

    @staticmethod
    def start_simulation():
        ComputationEngine.compute()
