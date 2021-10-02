from abc import ABCMeta


class IConcrete(metaclass=ABCMeta):
    @staticmethod
    def get_information():
        """"The Pizzeria Interface"""


class PipperoniHam(IConcrete):

    def __init__(self):
        self.cheese = 70
        self.carbs = 45
        self.fat = 38
        self.protein = 8

    def get_information(self):
        return {"cheese": self.cheese, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class Stagioni(IConcrete):

    def __init__(self):
        self.cheese = 30
        self.carbs = 59
        self.fat = 29
        self.protein = 6.3

    def get_information(self):
        return {"cheese": self.cheese, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class SpicyHot(IConcrete):

    def __init__(self):
        self.flavour = "hot"
        self.first = "tomato"
        self.second = "ham"
        self.stage = "oliva"

    def get_information(self):
        return {"Number of flavour": self.flavour, "first dish": self.first, "second dish": self.second, "stage": self.stage}


class ConcreteFactory:

    @staticmethod
    def get_information(pizzatype):
        try:
            if pizzatype == "PippetoniHam":
                return PipperoniHam()
            if pizzatype == "Stagioni":
                return Stagioni()
            if pizzatype == "SpicyHot":
                return SpicyHot()
            raise AssertionError("Pizza is lost")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    PIZZA = ConcreteFactory.get_information("PipperoniHam")
    print("PipperoniHam contains", PIZZA.get_information())
    PIZZA = ConcreteFactory.get_information("Stagioni")
    print("Stagioni Piza contains", PIZZA.get_information())
    PIZZA = ConcreteFactory.get_information("SpicyHot")
    print("Three Course Dinner Gum contains", PIZZA.get_information())
