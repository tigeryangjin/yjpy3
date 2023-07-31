class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print('店名：' + self.restaurant_name + ' 品类：' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + '餐馆正在营业')

    def increment_number_served(self, number_served):
        self.number_served = self.number_served + number_served


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = ['草莓', '牛奶', '薄荷']

    def read_flavors(self):
        print('售卖以下口味：')
        for i in self.flavors:
            print(i)


dq = IceCreamStand('冰雪皇后', '冰激凌', 65)
dq.describe_restaurant()
dq.read_flavors()
