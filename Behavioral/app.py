from behavioral.implementation.owner import Owner
from behavioral.implementation.revenue_service import FactoryAccountant
from behavioral.implementation.factory_check import FactoryOwner


def if_subscribe(factory_accountant, person):
    val = input("Just go with the flow of notifications").lower()
    if val == "success" or val == "s": factory_accountant.attach(person)


if __name__ == "__main__":
    factory_check = FactoryOwner()
    while True:
        print("Print success if a revenue service came this quarter")
        print("Print failure to assign an accountant for this deal")

        val = int(input())
        factory = input("Your restaurant name: ")

        if val == 1:
            owner = Owner()
            factory_check.new_manager(owner)
            if_subscribe(factory_check, owner)
        elif val == 2:
            manager = FactoryAccountant()
            factory_check.new_manager(manager)
            factory_check.attach(manager)
