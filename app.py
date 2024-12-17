import random

start = False

timepass = 0
timeset = 0

customers = 0.35

buy = 0

speed = 0.5

import time

def clamp(value, min_value, max_value):
  return max(min(value, max_value), min_value)

difference = 0

totalsales = 0

taxes = 0
taxpercent = 0

maxmake = 5
made = 0
maxsell = 5
sell = 0
money = 0
cost = 0
rawstock = 0
roundstock = 0
money = 0
price = 0
quality = 0

dynamicprice = False

availablesales = 5
availablestock = 5

stopyear = 0

will = 0

while start == False:
    money = input("Investment?")
    cost = input("Cost?")
    rawstock = int(money)/int(cost)
    roundstock = round(rawstock, 0)
    money = int(money) - int(roundstock)*int(cost)
    price = input("Price?")
    will = input("Will?")
    if input("Dynamic Price? y/n") == ("y"):
        dynamicprice = True
    else:
        dynamicprice = False
    quality = input("Quality?")
    maxsell = input("Max sellable?")
    maxmake = input("Max makeable?")
    taxpercent = int(input("Tax Percent?")) * 0.01
    speed = input("Speed? (Seconds)")
    stopyear = input("Stop Year?")

    print("Current Tax Percent: ", taxpercent)
    print("Current Maxsell: ", maxsell)
    print("Current Maxmake: ", maxmake)
    print("Current quality: ", quality)
    print("Current price: $", price)
    print("Current stock: ", roundstock)
    print("Current money: $", money)
    print("Current cost: $", cost)
    print("Current will: $", will)
    print("Dynamicprice:", dynamicprice)
    print("Speed (Seconds): ", speed)
    print("Stopyear: ", stopyear)

    ready = input("Ready? y/n")
    if ready == "y":
        start = True
    elif ready == "n":
        pass
    else:
        print("unknown answer")

while start == True:
    if int(money) > -100 and int(roundstock) > -5 and int(price) > 0 and int(will) > 0:
        while int(money) > int(cost) and made < int(maxmake):
            made = made + 1
            roundstock = roundstock + 1
            money = money - int(cost)
        buy = random.random()
        while int(roundstock) > 0 and int(will) > int(price) - 15 and sell < int(maxsell) and buy >= customers:
            buy = random.random()
            sell = sell + 1
            roundstock = roundstock - 1
            money = money + int(price)
            totalsales = totalsales + 1
        difference = int(price) - int(will)
        taxes = int(money) * taxpercent
        print("Possible Customers", customers)
        print("Current stock: ", roundstock)
        print("Current money: $", money)
        print("Current will: $", will)
        print("Current price: $", price)
        print("Current year: ", timepass)
        print("Total Sales", totalsales)
        if dynamicprice == True:
            price = int(price) - int(difference)
        timepass = int(timepass) + 1
        timeset = int(timeset) + 1
        money = int(money) - int(taxes)
        will = int(will) - customers * 0.75
        if int(stopyear) <= timepass:
            start = False
        if int(timeset) > int(quality):
            will = int(will) - customers * 2
            timeset = 0
        time.sleep(float(speed))
        made = 0
        sell = 0
        customers = customers - 0.009

    else:
        start = False

print("FINAL STATS")
print("Possible Customers", customers)
print("Final price: $", price)
print("Final stock: ", roundstock)
print("Final money: $", money)
print("Final cost: $", cost)
print("Final will: $", will)
print("Final years", timepass)
print("Total Sales", totalsales)