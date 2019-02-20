from car import Car

'''
电池类
'''
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    
    def get_range(self, car_model="this car"):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(car_model + " can go approximately " + str(range) + 
             " miles on a full charge.")
    
    def update_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        print("This car doesnot need a gas tank!")