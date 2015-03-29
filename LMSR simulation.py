user1= User();
user2= User();
user3= User();
user4= User();



    
print('current price of q1=' + str(currentPriceQ1(q1,q2)));
print('current price of q2=' + str(currentPriceQ1(q1,q2)));




"""  #Test payment function
executePaymentQ1(user1, 30);
print('user1 money= ' + str(user1.money)+'user1 shares(1)= ' + str(user1.x1) + "user1 worth= " +str(user1.value()));
print('q1='+ str(q1));
print('q2='+ str(q2));
print('current price of q1= ' + str(currentPriceQ1(q1,q2)));
print('current price of q2= ' + str(currentPriceQ2(q1,q2)));

executePaymentQ2(user1, 5);
print('user1 money=' + str(user1.money)+'user1 shares(1)=' + str(user1.x1) + "user1 worth= " +str(user1.value()));
print('q1='+ str(q1));
print('q2='+ str(q2));
print('current price of q1=' + str(currentPriceQ1(q1,q2)));
print('current price of q2=' + str(currentPriceQ2(q1,q2)));
"""


  #Run simulation
i=1
L=[]

while i<20:

    
        
    if currentPriceQ1(q1,q2)< .2:
        shares = random.randint(-20, -10)
        executePaymentQ2(user3, shares);
    elif currentPriceQ1(q1,q2)> .25:
        shares = random.randint(10, 20)
        executePaymentQ2(user3, shares);

    if currentPriceQ1(q1,q2)< .3:
        shares = random.randint(-20, -10)
        executePaymentQ1(user4, shares);
    elif currentPriceQ1(q1,q2)> .35:
        shares = random.randint(10, 20)
        executePaymentQ2(user4, shares);

    if currentPriceQ1(q1,q2)< .7:
        shares = random.randint(10, 20)
        executePaymentQ1(user1, shares);
    elif currentPriceQ1(q1,q2)> .75:
        shares = random.randint(-20, -10)
        executePaymentQ1(user1, shares);
        
    if currentPriceQ1(q1,q2)< .6:
        shares = random.randint(10, 20)
        executePaymentQ1(user2, shares);
    elif currentPriceQ1(q1,q2)> .65:
        shares = random.randint(-20, -10)
        executePaymentQ1(user2, shares);

    #make list for share count and current prices after each round
    row= [q1, q2, currentPriceQ1(q1,q2), currentPriceQ2(q1,q2)]
    L.append(row);

    print('user1 money= ' + str(user1.money)+'user1 shares(1)= ' + str(user1.x1)+ "user worth= "+ str(user1.value()));
    print('user2 money= ' + str(user2.money)+'user1 shares(1)= ' + str(user2.x1)+ "user worth= "+ str(user2.value()));
    print('user3 money= ' + str(user3.money)+'user1 shares(1)= ' + str(user3.x1)+ "user worth= "+ str(user3.value()));
    print('user4 money= ' + str(user4.money)+'user1 shares(1)= ' + str(user4.x1)+ "user worth= "+ str(user4.value()));
    
    print('q1='+ str(q1));
    print('q2='+ str(q2));
    print('current price of q1=' + str(currentPriceQ1(q1,q2)));
    print('current price of q2=' + str(currentPriceQ2(q1,q2)));
    i=i+1

