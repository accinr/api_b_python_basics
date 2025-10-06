class Car():
    
    @staticmethod
    def start_engine():
        print("Normal Engine Started")

    def stop_engine(self):
        print("Normal Engine Started")
        

print(Car.start_engine())
# print(Car.stop_engine())

car = Car()
car.stop_engine()