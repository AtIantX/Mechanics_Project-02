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
        Simulation.Engine = ComputationEngine()

    @staticmethod
    def start_simulation():
        ComputationEngine.compute()
