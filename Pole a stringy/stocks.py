def highest_profit(stocks):
    
    lind,lowest=0,stocks[0]
    buy_ind,buy_price=0,lowest
    sell_ind,sell_price=0,stocks[0]
    profit=0
    for i,stock in enumerate(stocks):
        if stock<lowest:
            lind,lowest=i,stock
        if (nprofit:=(stock-lowest))>profit:
            buy_ind,buy_price=lind,lowest
            sell_ind,sell_price,profit=i,stock,nprofit
        
    return buy_price,sell_price
def highest_profit_twice(stocks):
    lowest=stocks[0]
    highest=0
    profit=0
    p1s=[]
    for i,stock in enumerate(stocks):
        lowest=min(lowest,stock)
        profit=max(stock-lowest,profit)
        p1s.append(profit)
    profit=0
    for i,stock in reversed(list(enumerate(stocks))):
        stock=stocks[i]
        highest=max(highest,stock)
        profit=max(highest-stock+p1s[i],profit)
        #vyřeš pro 0<=i a >i
        #sečti a vem maximum
    return profit
print(highest_profit((310,315,105,205,260,270,290,230,105,250)))
print(highest_profit_twice((10,150,20,150,290,100)))