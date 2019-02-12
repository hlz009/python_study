class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #指定默认值属性
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()
    
    #读取属性
    def read_odometer():
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    #修改属性
    def update_odometer(self, mileage):
        '''
        里程只允许上调，不允许下调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cannot roll back an odometer")
    
    def increment_odometer(self, miles):
        if miles < 0:
            print("you cannot set an negative miles")
            return
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("This car is filled with oil in it's tank")
    
# my_new_car = Car('Audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())