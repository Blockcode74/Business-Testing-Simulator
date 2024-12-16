start = False

timepass = 0
timeset = 0

speed = 0.5

import time

def clamp(value, min_value, max_value):
  return max(min(value, max_value), min_value)

difference = 0

taxes = 0
taxpercent = 0

maxmake = 0
maxsell = 0
money = 0
cost = 0
rawstock = 0
roundstock = 0
money = 0
price = 0
quality = 0

dynamicprice = False

availablesales = clamp(0, 0, maxsell)
availablestock = clamp(0, 0, maxmake)

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
    maxmake = input("Max Made? (Per Year)")
    maxsell = input("Max Sales? (Per Year)")
    taxpercent = int(input("Tax Percent?")) * 0.01
    speed = input("Speed? (Seconds)")

    print("Current Tax Percent: ", taxpercent)
    print("Current Max Made (Per Year): ", maxmake)
    print("Current Max Sales (Per Year): ", maxsell)
    print("Current quality: ", quality)
    print("Current price: $", price)
    print("Current stock: ", roundstock)
    print("Current money: $", money)
    print("Current cost: $", cost)
    print("Current will: $", will)
    print("Dynamicprice:", dynamicprice)
    print("Speed (Seconds): ", speed)

    ready = input("Ready? y/n")
    if ready == "y":
        start = True
    elif ready == "n":
        pass
    else:
        print("unknown answer")

while start == True:

    while int(money) > -100 and int(roundstock) > -5 and int(price) > 0:
        if int(price) < int(will):
            availablesales = availablesales + 1
        if int(cost) < int(money):
            availablestock = availablestock + 1
        difference = int(price) - int(will)
        taxes = int(money) * taxpercent
        print("Current stock: ", roundstock)
        print("Current money: $", money)
        print("Current will: $", will)
        print("Current price: $", price)
        print("Current year: ", timepass)
        if int(price) < int(will):
            roundstock = int(roundstock) - 1 * availablesales * int(quality)
            money = int(money) + int(price) * int(quality)
            int(will) - 5 * int(quality)
            availablesales = 0
        if dynamicprice == True:
            price = int(price) - int(difference)
        if int(cost) < int(money):
            money = int(money) - int(cost) * availablestock
            roundstock = int(roundstock) + 1 * availablestock
            availablestock = 0
        timepass = int(timepass) + 1
        timeset = int(timeset) + 1
        money = int(money) - int(taxes)
        will = int(will) - 5
        if int(timeset) > int(quality):
            will = int(will) + int(quality) * 2
            timeset = 0
        time.sleep(float(speed))
    start = False

print("FINAL STATS")
print("Final price: $", price)
print("Final stock: ", roundstock)
print("Final money: $", money)
print("Final cost: $", cost)
print("Final will: $", will)
print("Final years", timepass)

