class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock


class RegularProduct(Product):
    pass


class DiscountProduct(Product):
    def __init__(self, name, price, stock, discount):
        super().__init__(name, price, stock)
        self.discount = discount


class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product, quantity):
        if product in self.items:
            if self.items[product] <= quantity:
                del self.items[product]
            else:
                self.items[product] -= quantity

    def view_items(self):
        for product, quantity in self.items.items():
            print(f"{product.get_name()} - 数量：{quantity}")

    def clear(self):
        self.items = {}


class Order:
    def __init__(self, cart):
        self.cart = cart
        self.__total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for product, quantity in self.cart.items.items():
            if isinstance(product, DiscountProduct):
                total_price += product.get_price() * quantity * product.discount
            else:
                total_price += product.get_price() * quantity
        return total_price

    def pay(self):
        # 实现支付逻辑
        print(f"支付成功！支付金额：{self.__total_price}")


class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product, quantity):
        # print("user add_to_cart start")
        self.cart.add_item(product, quantity)
        # print("user add_to_cart end")

    def view_cart(self):
        self.cart.view_items()

    def checkout(self):
        order = Order(self.cart)
        order.pay()
        self.cart.clear()


rp01 = RegularProduct("iphone15", 9999, 100)
dp01 = DiscountProduct("Mac", 19999, 100, 0.8)

user = User("yuan")

user.add_to_cart(rp01,5)
user.add_to_cart(dp01,10)
user.view_cart()
user.checkout()
