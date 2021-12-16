
# Topic:  _Behavioral Design Patterns__

## Author:  _Furdui Alexandru_

----------

## Objectives:

     **1. Study and understand the Behavioral Design Patterns.**

     **2. As a continuation of the previous laboratory work, think about what communication between software entities might be involved in your system.**

     **3. Implement some additional functionalities using behavioral design patterns.**

## Used Design Patterns:

-   Observer

## Implementation

**1. Observer**

The **observer pattern** is a software design pattern in which an object, named the **subject**:

```
class  Owner(Publisher):
	factory: object

	def  __init__(self) -> object:
		self.factory = CrustDirector

	def  update(self, subscriber):
		print("The " + self.factory + " was notified. " + subscriber)
```

that maintains a list of its dependents, called **observers**
```
class  FactoryAccountant(Publisher):
	def  __init__(self):
		self.factory = CrustDirector
	def  update(self, subscriber):
		print("Pizzeria Accountant " + self.factory + " was notified about coming of the Revenue Service. " + subscriber)
```

and notifies them automatically of any state changes, usually by calling one of their methods.
```
def  update(self, subscriber):
		print("The " + self.factory + " was notified. " + subscriber)
```