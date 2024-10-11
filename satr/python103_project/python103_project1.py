# function
def update_sale_price(bike, sale_price):
    if bike['sold'] == True:
        print('action not allowed, bike has already been sold')
    else:
        bike['sale_price'] = sale_price

def sell(bike):
    bike['sold'] = True

def create_bike(desc, cost, sale_price, condition):
    return {
        'desc':desc,
        'cost':cost,
        'sale_price':sale_price,
        'condition':condition,
        'sold':False
    }

# 
bike1 = create_bike('albine, orange',100,500,.5)

print(bike1)
update_sale_price(bike1,450)
sell(bike1)
print(bike1)

###################################################################
# class
class Bike:
    def __init__(self, desc, cost, sale_price, condition):
        self.desc = desc
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self.sold = False

    def update_sale_price(self, sale_price):
        if self.sold:
            print('action not allowed, bike has already been sold')
        else:
            self.sale_price = sale_price

    def sell(self):
        self.sold = True

#
bike_c1 = Bike('bike class 1',100,500,.5)

print(bike_c1.__dict__)
bike_c1.update_sale_price(450)
bike_c1.sell()
print(vars(bike_c1))
