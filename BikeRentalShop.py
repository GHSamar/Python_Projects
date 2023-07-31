class bikeShop:
    def init(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Bikes in stocks: ",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Minimum 1 bike should be choosen")
        elif q>self.stock:
            print("Not enough stocks")
        else:
            self.stock=self.stock-q
            print("Total Price: ",(q*200))
            print("Stock left: ",self.stock)
while True:
    obj=bikeShop(150)
    uc=int(input('''
    1 Display The Stocks
    2 Rent Bike
    3 Exit
    '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter The Quantity: "))
        obj.rentForBike(n)
    else:
        break