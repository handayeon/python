from time import sleep
from random import randrange
averagePrice = 185
targetPrice = 189
stopLossPrice = 101

def getRightTiming():

    while True:
        currentPrice = randrange(100, 110)
        if currentPrice >= targetPrice:
            print(f"현재 가격 : {currentPrice} - 목표가")
        elif currentPrice <= stopLossPrice:
            print(f"현재 가격 : {currentPrice} - 손절가")
        else :
            print(f"현재 가격 : {currentPrice}")
        sleep(2)

getRightTiming()