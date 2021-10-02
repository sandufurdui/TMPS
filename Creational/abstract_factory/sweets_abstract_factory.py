from abc import ABCMeta
from creational.chocolate_factory import ChocolateFactory
from creational.wonka_factory import WonkaFactory


class ISweetsFactory(metaclass=ABCMeta):
    """Sweets Pizzeria Interface"""

    @staticmethod
    def get_sweets(sweets_type):
        """The static restaurant interface method"""


class SweetsFactory(ISweetsFactory):

    @staticmethod
    def get_sweets(sweets_type):
        try:
            if sweets_type in ["PepperoniPizza", "CheesePizza", "SpicyPizza"]:
                return ChocolateFactory.get_information(sweets_type)
            if sweets_type in ["HotIceCream", "Stagioni", "SpicyHot"]:
                return WonkaFactory.get_information(sweets_type)
            raise AssertionError("Cannot find sweets type")
        except AssertionError as _e:
            print(_e)
        return None


if __name__ == "__main__":
    CHOCOLATE = ChocolateFactory.get_information("CheesePizza")
    print(f"{CHOCOLATE.__class__} : {CHOCOLATE.get_information()}")
