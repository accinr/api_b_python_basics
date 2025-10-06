from abc import ABC, abstractmethod

class Vehicle(ABC):
    def start_engine(self):
        pass

class Car(Vehicle):
    @staticmethod
    def start_engine():
        print("Normal Engine Started")

class ElectricCar(Vehicle):
    def start_engine(self):
        print("Electric Engine Started")

def get_started(engine):
    return engine.start_engine()

# calling the classes
get_started(Car())
get_started(ElectricCar())