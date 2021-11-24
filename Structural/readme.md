
# Topic: *Structural Design Patterns*
## Author: *Furdui Alexandru*
------
## Objectives:
&ensp; &ensp; __1. Structural design patterns study__

&ensp; &ensp; __2. As continuation of last lab, to implement some functionalities using design patterns__


&ensp; &ensp; __3. Implement some additional functionalities using structural design patterns.__


## Used Design Patterns:

* Decorator
* Flyweight
* Adapter


## Implementation

__1. Decorator__

-   Responsibilities should be added to (and removed from) an object dynamically at run-time.
-   A flexible alternative to subclassing for extending functionality should be provided.

```
class  HavingAccountant:
	def  __init__(self, accountant, restaurant):
		self.accountant = accountant
		self.restaurant = restaurant
		accountant.having_accountant = False
	def  get_money(self, profit):
		return  "good"  if  profit == "stable"  else  self.accountant.get_money(profit)

class  BusinessPlan:
	def  __init__(self, business):
		self.business = business
business.business_plan = True
	def  get(self):
		return  self.business.get().replace("Without business plan", "With business plan")
	def  get_money(self, profit):
		return  "great"  if  profit == "huge"  else  self.business.get_money(profit)
```

__2. Flyweight__ 

The performance is increased by creating a pool of common Strings and assigning multiple reference variables to the ones with the same content, and only creating new Strings when no match is found.

```
class  FlyweightPizzeria:
	_flyweights: Dict[str, Flyweight] = {}
	def  __init__(self, initial_flyweights: Dict) -> None:
		for  state  in  initial_flyweights:
		self._flyweights[get_key(state)] = Flyweight(state)
	def  get_flyweight(self, shared_state: Dict) -> 	Flyweight:
		key = get_key(shared_state)
		if  not  self._flyweights.get(key):
		print("FlyweightPizzeria: Can't find a flyweight, creating new one.")
		self._flyweights[key] = Flyweight(shared_state)
		else:
		print("FlyweightPizzeria: Reusing existing flyweight.")
		return  self._flyweights[key]

	def  list_flyweights(self) -> None:
		count = len(self._flyweights)
		print(f"FlyweightPizzeria: This store has {count} flyweights:")
		print("\n".join(map(str, self._flyweights.keys())), end="")
```

__3. Adapter__ 
   
**The adapter design pattern describes how to solve such problems:**

1.  Define a separate adapter class that converts the (incompatible) interface of a class ( adaptee ) into another interface ( target ) clients require.
2.  Work through an adapter to work with (reuse) classes that do not have the required interface.
```
class  ClassB(IB):
	def  method_b(self):
	print("The pizza restaurant that has a business plan, helping out to enhance the business")

class  ClassBAdapter(IA):
	def  __init__(self):
	self.class_b = ClassB()

	def  method_a(self):
	#calls the class b method_b instead
	self.class_b.method_b()
```
