from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car Engine Started")

car = Car()
car.start_engine()
