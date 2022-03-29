import itertools
import pandas as pd

class Order :
    def __init__(self, type, quantity, price, id):
        self.type = type
        self.quantity = quantity
        self.price = price
        self.id = id

    def type(self):
        return self.type

    def quantity(self):
        return self.quantity

    def price(self):
        return self.price

    def id(self):
        return self.id

    def Execute(self,counterparty):
        if counterparty.quantity > self.quantity:
            counterparty.quantity -= self.quantity
            self.quantity = 0
        else:
            self.quantity -= counterparty.quantity
            counterparty.quantity = 0

class Book:
    def __init__(self, name):
        self.name = name
        self.buy_orders = []
        self.sell_orders = []
        self.id_iter = 1

    def name(self):
        return self.name


    def execute_order(self):
        for i in range(len(self.sell_orders)):
            for j in range(len(self.buy_orders)):
                if self.sell_orders[i].price <= self.buy_orders[j].price:
                    trade_quantity = min(self.sell_orders[i].quantity, self.buy_orders[j].quantity)
                    trade_price = self.buy_orders[j].price
                    sel
                        def execute_order(self):
                            for i in range(len(self.sell_orders)):
                                for j in range(len(self.buy_orders)):
                                    if self.sell_orders[i].price <= self.buy_orders[j].price:
                                        trade_quantity = min(self.sell_orders[i].quantity, self.buy_orders[j].quantity)
                                        trade_price = self.buy_orders[j].price
                                        self.sell_orders[i].Execute(self.buy_orders[j])
                                        self.remove_executed()
                                        print("EXECUTE " + trade_quantity + " @ " + trade_price + " ON " + self.__name )
       

       def insert_order(self, type, quantity, price):
           if type == "BUY":
               self.buy_orders.append(Order("BUY",quantity, price,self.id_iter))
            elif type == "SELL":
                self.sell_orders.append(Order("SELL",quantity, price,self.id_iter))
            else:
                print("ORDER NOT VALID")
                return
            print("--- Insert ", str(type)," ", str(quantity), "@", str(price), " id =", str(self.id_iter)," on ", str(self.name))
            self.execute_order()
            self.print_infos()
            self.id_iter += 1

        
       def remove_executed(self):
           for i in range(len(self.sell_orders)):
               if self.sell_orders[i] == 0:
                   self.sell_orders.remove(self.sell_orders[i])
           for j in range(len(self.buy_orders)):
               if self.buy_orders[j]==0:
                   self.buy_orders.remove(self.buy_orders[j])


        def print_infos(self):
            self.buy_orders.sort()
            self.buy_orders.reverse()
            self.sell_orders.sort()
            self.sell_orders.reverse()


            print("Book on ", str(self.name))

            for i in range(len(self.sell_orders)):
                print('\tSELL ',self.sell_orders[i].quantity(),'@',self.sell_orders[i].price(),' id = ',self.sell_orders[i].id())

            for j in range(len(self.buy_orders)):
                print('\tBUY ',self.buy_orders[j].quantity(),'@',self.buy_orders[j].price(),' id = ',self.buy_orders[j].id())

            print("--------------------")

if __name__ == '__main__':
      TEST = Book("TEST")
      TEST.insert_order("SELL",10, 10)
      