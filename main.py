# Main Controller
from Computation_Controllers.Simulation_Controller import Simulation
from Computation_Controllers.CSV_controller import CSVController


class MainController:
    simulation = None
    csv_controller = None

    def __init__(self):
        MainController.simulation = Simulation()
        MainController.csv_controller = CSVController()

    @staticmethod
    def test_acceleration():
        result = MainController.simulation.start_acceleration_computation_simulation()
        print(result)

    @staticmethod
    def collect_acceleration_data(test_number):
        header = ["Mass_1", "Mass_2", "Mass_3", "Friction_1", "Friction_2", "Friction_3", "g", "External_Force",
                  "Acceleration of Object 1", "Acceleration of Object 2"]
        acceleration_data = []
        for _ in range(test_number):
            result = MainController.simulation.start_acceleration_computation_simulation()
            acceleration_data.append(result)
        MainController.csv_controller.write_csv("Simulation_results/force_acceleration.csv", acceleration_data, header)


if __name__ == "__main__":
    main_controller = MainController()
    main_controller.test_acceleration()
    main_controller.collect_acceleration_data(10000)
