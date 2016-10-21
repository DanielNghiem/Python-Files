from math import exp, log, floor
from collections import defaultdict


sensitivity=30
NO = 0
YES = 1


# addDicts: {key: value}, {key:value} -> {key:value}
# output a new dictionary which contains all the keys in both
# input dictionaries, and adds together the values when a key
# is in both input dictionaries
#
# WARNING: this does a shallow copy of the values
# of the two dictionaries
# d1 = {1:2, 2:5}, d2 = {1:7, 4:6} should output {1:9, 2:5, 4:6}
def addDicts(d1, d2):
    d = d1.copy()

    for key, value in d2.items():
        if key in d1:
            d[key] += value
        else:
            d[key] = value

    return d


#helper function used by all stocks
def cost(u, v):
    return sensitivity*log(exp(u/sensitivity) + exp(v/sensitivity))


class Stock(object):
    def __init__(self, name, counts={NO:0, YES:0}):
        self.counts = counts.copy()
        self.name = name


    def price(self, option):
        numerator = exp(self.counts[option]/sensitivity)
        denominator = exp(self.counts[NO]/sensitivity) + exp(self.counts[YES]/sensitivity)

        return numerator / denominator

    #list -> float
    #input: a list [n,m]  output: payment required to make proposed changes
    #where n is number of YES shares to buy/sell
    #and m is the number of NO shares to buy/sell
    def quotePayment(self, changes):
        newCost = cost(self.counts[NO] + changes[NO], self.counts[YES] + changes[YES])
        currentCost = cost(self.counts[NO], self.counts[YES])

        return newCost - currentCost


    def __repr__(self):
        return "%s(YES=%d,NO=%d)" % (self.name, self.counts[YES], self.counts[NO])


    def __hash__(self):
        return hash(self.name)



class User(object):
    def __init__(self, name='', money=1000):
        self.name=name
        self.money=money

        self.portfolio = defaultdict(lambda: [0,0])


    def printPortfolio(self):
        for stockname,holdings in self.portfolio.items():
            print (stockname, holdings)


    def getWorth(self):
        worth = self.money

        for stock, holdings in self.portfolio.items():
           worth += holdings[NO] * stock.price(NO) + holdings[YES] * stock.price(YES)

        return worth


    def __repr__(self):
        return "Name: %s; Money: %d; Net Worth: %d" % (self.name, self.money, self.getWorth())



# buy: User, Stock, int, int -> None
# stocktype is either the variable NO=0 or YES=1
def buy(user, stock, stocktype, quantity):
    changes = {0:0, 0:0}
    changes[stocktype] = quantity
    payment = stock.quotePayment(changes)

    if -quantity > user.portfolio[stock][stocktype]:
        print("You can't sell what you don't have! Transaction not executed.")
    elif user.money < payment:
        print("Not enough money! Transaction not executed.")
    else:
        user.portfolio[stock][stocktype] = user.portfolio[stock][stocktype] + quantity
        user.money = user.money - payment
        stock.counts = addDicts(stock.counts, {stocktype: quantity})

#User, Stock, int, float -> None
#limitbuy makes a transaction for User to buy a Stock
#until it's price reaches priceLimit
def limitbuy(user, stock, stocktype, priceLimit):

    if stocktype == 'Yes':
        changeInQuantity = floor(sensitivity*log( priceLimit/ (1-priceLimit)) + stock.noCount - stock.yesCount)

        user.getHoldings(stock.name)[0] =  user.getHoldings(stock.name)[0] + changeInQuantity
        user.money = user.money - stock.quotePayment(changeInQuantity,0)
        stock.yesCount = stock.yesCount + changeInQuantity

    #TODO: complete this!
    return None

