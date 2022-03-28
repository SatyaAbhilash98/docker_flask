from calculator.calculations import Summation, Difference, Product, Divide


class Calculations:
    """Calculations class manages the history of calculations"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear the history of calculations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """get number of items in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.calculate_res()

    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from history"""
        return Calculations.history.append(calculation)