from abc import ABCMeta


class IPizzeriaBuilder(metaclass=ABCMeta):
    """The Pizzeria Interface"""

    @staticmethod
    def set_wall_material(value):
        """Set the wall_material"""

    @staticmethod
    def set_building_type(value):
        """Set the building_type"""

    @staticmethod
    def set_number_employees(value):
        """Set the number of employees"""

    @staticmethod
    def set_number_departments(value):
        """Set the number of departments"""

    @staticmethod
    def get_result():
        """Return the restaurant"""


class PizzeriaBuilder(IPizzeriaBuilder):
    """The Concrete Builder."""

    def __init__(self):
        self.factory = Pizzeria()

    def set_wall_material(self, value):
        self.factory.wall_material = value
        return self

    def set_building_type(self, value):
        self.factory.building_type = value
        return self

    def set_number_employees(self, value):
        self.factory.employees = value
        return self

    def set_number_departments(self, value):
        self.factory.departments = value
        return self

    def get_result(self):
        return self.factory


class Pizzeria:
    """The Product"""

    def __init__(self, building_type="Pizzeria", employees=100, departments=50, wall_material="Brick"):
        self.wall_material = wall_material
        self.building_type = building_type
        self.employees = employees
        self.departments = departments

    def __str__(self):
        return "This is the {0} {1} with {2} employees(s) and {3} departments(s).".format(
            self.wall_material, self.building_type, self.employees, self.departments
        )


class PizzeriaDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return PizzeriaBuilder()\
            .set_building_type("Pizzeria")\
            .set_wall_material("Concrete")\
            .set_number_employees("7777")\
            .set_number_departments(99)\
            .get_result()


class CrustDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return PizzeriaBuilder()\
            .set_building_type("Crust")\
            .set_wall_material("Best Wall Material")\
            .set_number_employees(6666)\
            .set_number_departments(666).get_result()


class TomatoFactory:
    @staticmethod
    def construct():
        return PizzeriaBuilder()\
            .set_building_type("Tomato Pizzeria")\
            .set_number_employees(1111)\
            .set_number_departments(11)\
            .set_wall_material("Metal").get_result()


if __name__ == "__main__":
    PIZZERIA = PizzeriaDirector.construct()
    PIZZERIA2 = CrustDirector.construct()
    PIZZERIA3 = TomatoFactory.construct()
    print(PIZZERIA)
    print(PIZZERIA2)
    print(PIZZERIA3)
