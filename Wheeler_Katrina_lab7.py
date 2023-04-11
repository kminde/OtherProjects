from time import time


def DACcoins(coins, amount):
    if amount == 0: #base case
        return 0
    else:
        minCoins = float('inf')
        for currentCoin in coins: #check all coins
            #If we can give change
            if (amount - currentCoin) >= 0:
                #calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) +1
                #keep the best
                minCoins = min(minCoins, currentMin)
        return minCoins


def DPcoins(coins, amount):
    #create initial tables
    values = [float('inf') for i in range(0, amount+1)]
    minCoins = [float('inf') for i in range(0, amount+1)]
    traceback = [float('inf') for i in range(0, amount+1)]

    values[0] = 0
    minCoins[0] = 0
    traceback[0] = 0

    #base case
    if amount <= 0:
        print("Select a valid amount")

    for value in range(0, amount + 1):
        values[value] = value
        for coin in coins:
            if value - coin >= 0:
                currentMin = minCoins[value - coin] + 1
                newMin = minCoins[value]
                if currentMin < newMin:
                    minCoins[value] = currentMin
                    traceback[value] = coin

    print(f'DP Optimal: {minCoins[amount]} coins')
    currentValue = amount
    for i in range(0, minCoins[amount]):
        print(f'{traceback[currentValue]}')
        currentValue = currentValue - traceback[currentValue]

amount = int(input(("Enter amount: ")))

t1 = time()
print(DACcoins([1,5,10,12,25], amount))
t2 = time()
totTime = round(((t2 - t1) * 1000), 2)
print("DAC", totTime, "ms")

t3 = time()
DPcoins([1,5,10,12,25], amount)
t4 = time()
totTime2 = round(((t4 - t3) * 1000), 2)
print("DP", totTime2, "ms")