import math
import random
from collections import defaultdict

#To DO: define __repr__ for User class

b=30 #fixed parameter for the market maker

def cost(u, v):   #global cost function used by all Stocks
        c = b*math.log(math.exp(u/b)+ math.exp(v/b))
        return c
    

class Stock(object):
    
    def __init__(self, name, yesCount=0, noCount=0): #yesCount and noCount is a count of number of shares sold
                                                     #Later: initialize Stock object with initial price
        self.yesCount=yesCount
        self.noCount=noCount
        self.name=name

    
    def yes_price(self): #returns current price of 'yes' Stock
        
            return math.exp(self.yesCount/b)/(math.exp(self.yesCount/b)+math.exp(self.noCount/b))
              
            
    def no_price(self): #returns currect price of 'no' Stock

            return math.exp(self.noCount/b)/(math.exp(self.yesCount/b)+math.exp(self.noCount/b))
        

    def quotePayment(self, yesChange=0, noChange=0):    #returns the cost buying/selling Yes or No stock
                                                        
            return cost(self.yesCount+yesChange, self.noCount+noChange)-cost(self.yesCount, self.noCount)
            

    def __repr__(self):
            return "%s: yesCount : %d, noCount : %d" % (self.name, self.yesCount, self.noCount)

    def __str__(self):
            return self.__repr__()  




        
class User(object):       
    def __init__(self, money=1000):
        
        self.money=money

        self.portfolio = defaultdict(lambda: [0,0]) #create a dictionary of stock holdings for user
                                                    #key= 'stock name' value = [number of yes stock, number of no stock]
    

    def getHoldings(self, stockname):
        return self.portfolio[stockname]

''' def __repr__(self):
        return [[a, self.portfolio[a]] for a in self.portfolio.keys()]

    def __str__(self):
        return str(self.__repr__())
'''

    # To Do: define function for user's current expected value



def executePayment(user, stock , stocktype , quantity):             #'stocktype' either 'Yes' or 'No'

    if stocktype == 'Yes':                                           #to buy/sell "Yes"
        if  -quantity > user.portfolio[stock.name][0]:              # trying to sell more shares than owned
            print("You can't sell what you don't have! Transaction not executed.")

        
        elif user.money < stock.quotePayment(quantity, 0):           #check if user has enough money
            print("Not enough money! Transaction not executed.")

        else:                           
            (user.getHoldings(stock.name))[0]= quantity              #update User stock holdings
            user.money = user.money+ stock.quotePayment(quantity, 0) #update User money
            stock.yesCount= stock.yesCount+quantity                  #update Stock's total "yes" count
            
    if stocktype == 'No':                                           #to buy/sell "No" stock
        if  -quantity > user.portfolio[stock.name][1]:              #if trying to sell more shares than owned
            print("You can't sell what you don't have! Transaction not executed.")

        
        elif user.money < stock.quotePayment(0,quantity):           #check if user has enough money
            print("Not enough money! Transaction not executed.")

        else:                           
            (user.getHoldings(stock.name))[1]= quantity              #update User stock holdings
            user.money = user.money+ stock.quotePayment(0, quantity) #update User money
            stock.noCount= stock.noCount+quantity                    #update Stock's total "no" count
            
