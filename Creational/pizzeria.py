from abc import ABCMeta


class Pizza(metaclass=ABCMeta):
    @staticmethod
    def get_information():
        """"The Pizza Interface"""


class PepperoniPizza(Pizza):

    def __init__(self):
        self.cheese = 70
        self.carbs = 45
        self.fat = 38
        self.protein = 8

    def get_information(self):
        return {"cheese": self.cheese, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class CheesePizza(Pizza):

    def __init__(self):
        self.cheese = 30
        self.carbs = 59
        self.fat = 29
        self.protein = 6.3

    def get_information(self):
        return {"cheese": self.cheese, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class SpicyPizza(Pizza):

    def __init__(self):
        self.cheese = 0
        self.carbs = 65
        self.fat = 28
        self.protein = 4.3

    def get_information(self):
        return {"cheese": self.cheese, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class Pizzeria:

    @staticmethod
    def get_pizza(pizzatype):
        try:
            if pizzatype == "Pepperoni":
                return PepperoniPizza()
            if pizzatype == "Cheese":
                return CheesePizza()
            if pizzatype == "Spicy":
                return SpicyPizza()
            raise AssertionError("Pizza is lost")
        except AssertionError as _e:
            print(_e)

    def get_flyweight(self, param):
        pass


if __name__ == "__main__":
    pizza = Pizzeria.get_pizza("Pepperoni")
    print("Pepperoni Pizza Contains", pizza.get_information())
    pizza = Pizzeria.get_pizza("Cheese")
    print("Cheese Pizza Contains", pizza.get_information())
    pizza = Pizzeria.get_pizza("Spicy")
    print("Spicy contains", pizza.get_information())
