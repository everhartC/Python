#%%

class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def add_product(self, name, price, weight):
        new_product = Product(name, price, weight)
        self.products.append(new_product)
        #new_product.print_info()
        return self

    def sell_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase)
            #product.print_info()
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.price = product.price - (product.price * percent_discount)
            return self
            
    def display(self):
        for product in self.products:
            product.print_info()
        return self


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change):
        if (self.price * percent_change) > self.price:
            is_increased = True
            self.price = self.price + (self.price * percent_change)
        else:
            is_increased = False
            self.price = self.price - (self.price * percent_change)
        return self

    def print_info(self):
        print(f"Product Name: {self.name} \
            \nPrice: {self.price} \
            \nCategory: {self.category}\n")
        return self


if __name__ == '__main__':
    p = Store('pizza hut',[])
    p.add_product('pizza',10.0,'food').add_product('salad',2.0,'food').add_product('bread stick',5.0,'app')
    p.display()
    p.set_clearance('food',.25).display()
# %%
