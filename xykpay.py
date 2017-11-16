def luluji(rate,money,scale,price):
    '''rate费率 money净利润 scale兑换比例 price 1w里程价格'''
    total = money/(1/scale/10000*price-rate/100)
    print(total)
luluji(0.38,2000,10,900)