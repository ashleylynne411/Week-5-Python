# Base class: Entity
class Entity:
    def move(self):
        raise NotImplementedError("Subclass must implement the move() method")

# Animal class
class Animal(Entity):
    def move(self):
        return "Walking"

# Vehicle class
class Vehicle(Entity):
    def move(self):
        return "Generic vehicle movement"

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving"

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying"

# Subclass: Reptile
class Snake(Animal):
    def move(self):
        return "Slithering"

# Subclass: Fish
class Fish(Animal):
    def move(self):
        return "Swimming"

# Subclass: Ship
class Ship(Vehicle):
    def move(self):
        return "Sailing"
    
# Example usage:
entities = [
    Car(),
    Plane(),
    Snake(),
    Fish(),
    Ship()
]

# Displaying how each entity moves
for entity in entities:
    print(f"{type(entity).__name__}: {entity.move()}")
