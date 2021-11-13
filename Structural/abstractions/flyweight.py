import json
from typing import Dict

from creational.pizzeria import pizzeria

`
class Flyweight:
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


def get_key(state: Dict) -> str:
    return "_".join(sorted(state))


class FlyweightPizzeria:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[get_key(state)] = Flyweight(state)

    def get_flyweight(self, shared_state: Dict) -> Flyweight:

        key = get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightPizzeria: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightPizzeria: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightPizzeria: This store has {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_pizza_to_database(
    factory: Pizzeria, owner: str,
    brand: str, type: str, price: str
) -> None:
    print("\n\nClient: Adding a pizza to database.")
    flyweight = factory.get_flyweight([brand, type, price])
    flyweight.operation([brand, owner])
