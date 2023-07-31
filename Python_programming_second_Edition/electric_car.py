class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + str(self.model)
        return long_name

    def read_odometer(self):
        print('This car has %s miles on it.' % self.odometer_reading)

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# class Battery:
#     def __init__(self, battery_size=75):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print('This car has a %s-kWh battery' % self.battery_size)
#
#     def get_range(self):
#         # global battery_range
#         if self.battery_size == 75:
#             battery_range = 260
#         elif self.battery_size == 100:
#             battery_range = 315
#         print('This car can go about %s miles on a full charge.' % battery_range)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.battery = Battery()
#
#     def describe_battery(self):
#         print(f'This car has a {self.battery_size}-kWh battery.')


# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

# my_new_cat = Car('audi', 'a4', 2019)
# print(my_new_cat.get_descriptive_name())
# my_new_cat.update_odometer(23)
# my_new_cat.update_odometer(21)
# my_new_cat.read_odometer()
