import math
from collections import defaultdict

#3/25/15

#To DO: define __repr__ for User class
#To Do: define Expected Worth function

#3/27:  Added user.printPortfolio() function
#       Added user.getWorth() function
#       Added limitBuy() function (not complete)
#       What is User.portfolio when portfolio is empty?
#       Where should I define the variable b and cost function?
#       Need to simplify limitBuy() code


b=30




def cost(u, v):         #global cost function used by all Stocks
        c = b*math.log(math.exp(u/b)+ math.exp(v/b))
        return c


    

class Stock(object):
   
    stockList=[]    #maintain list of stock 
    
    def __init__(self, name, yesCount=0, noCount=0): #yesCount and noCount is a count of number of shares sold
                                                     #Later: initialize Stock object with initial price
        self.yesCount=yesCount
        self.noCount=noCount
        self.name=name

        Stock.stockList.append(self)

    
    def yes_price(self): #returns current price of 'yes' Stock
        
            return math.exp(self.yesCount/b)/(math.exp(self.yesCount/b)+math.exp(self.noCount/b))
              
            
    def no_price(self): #returns currect price of 'no' Stock

            return math.exp(self.noCount/b)/(math.exp(self.yesCount/b)+math.exp(self.noCount/b))
        

    def quotePayment(self, yesChange=0, noChange=0):    #returns the cost buying/selling Yes or No stock
                                                        
            return cost(self.yesCount+yesChange, self.noCount+noChange)-cost(self.yesCount, self.noCount)
            

    def __repr__(self):
            return "%s: yesCount : %d, noCount : %d" % (self.name, self.yesCount, self.noCount)






        
class User(object):       
    def __init__(self, name='Unnamed', money=1000):

        self.name=name
        self.money=money

        self.portfolio = defaultdict(lambda: [0,0]) #create a dictionary of stock holdings for user
                                                    #key= 'stock name'; value = [number of yes stock, number of no stock]
    
    def getHoldings(self, stockname):
        return self.portfolio[stockname]

    def printPortfolio(self):                   #prints user's tuple of stockname, [yesStock, noStock]
        for stockname,holdings in self.portfolio.items():
            print (stockname, holdings)

    def getWorth(self):                         #returns "expected value" of user worth
    
        worth = self.money
        
        for stock in Stock.stockList:
           worth = worth + stock.yes_price() * self.portfolio[stock.name][0] + stock.no_price()*self.portfolio[stock.name][1]    
        return worth   
            
    
        

    def __repr__(self):
        return "Name: %s; Money: %d; Net Worth: %d" % (self.name, self.money, self.getWorth())






def buy(user, stock , stocktype , quantity):                        #'stocktype' either 'Yes' or 'No'

    if stocktype == 'Yes':  #if buy/selling "Yes"
        if  -quantity > user.portfolio[stock.name][0]:              # trying to sell more shares than owned
            print("You can't sell what you don't have! Transaction not executed.")

        
        elif user.money < stock.quotePayment(quantity, 0):          #check if user has enough money
            print("Not enough money! Transaction not executed.")

        else:                           
            (user.getHoldings(stock.name))[0]= (user.getHoldings(stock.name))[0]+ quantity
                                                                    #update User stock holdings
            user.money = user.money - stock.quotePayment(quantity, 0) #update User money
            stock.yesCount= stock.yesCount+quantity                 #update Stock's total "yes" count
            
    if stocktype == 'No':   #if buy/selling "No" stock
        if  -quantity > user.portfolio[stock.name][1]:              #if trying to sell more shares than owned
            print("You can't sell what you don't have! Transaction not executed.")

        
        elif user.money < stock.quotePayment(0,quantity):           #check if user has enough money
            print("Not enough money! Transaction not executed.")

        else:                           
            (user.getHoldings(stock.name))[1]= (user.getHoldings(stock.name))[1]+ quantity
                                                                    #update User stock holdings
            user.money = user.money - stock.quotePayment(0, quantity) #update User money
            stock.noCount= stock.noCount+quantity                   #update Stock's total "no" count



def limitBuy(user, stock, stocktype, priceLimit):  #buys a certain Stock until its price reaches pricelimit

    if stocktype== 'Yes':
                           #NEED to check pricelimit is between 0 and 1
        changeInQuantity = math.floor( b*math.log( priceLimit/ (1-priceLimit)) + stock.noCount - stock.yesCount )

        #if priceLimit is greater than current price:check if user can afford the transaction
        
        #if priceLimit is less than current price: check if user owns enough shares to sell

        #update User stock holdings
        user.getHoldings(stock.name)[0] =  user.getHoldings(stock.name)[0] + changeInQuantity
        #update User money
        user.money = user.money - stock.quotePayment(changeInQuantity,0)
        #update Stock's share count
        stock.yesCount = stock.yesCount + changeInQuantity


    



