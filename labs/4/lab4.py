#[weight, value]
def knapsack(capacity, itemList):
    if capacity < 0:
        return [-float('inf'), []]
    elif capacity == 0 or itemList == []:
        return [0, []]
    else:
        use = knapsack(capacity-itemList[0][0], itemList[1:])
        lose = knapsack(capacity, itemList[1:])
        useVal = itemList[0][1] + use[0]
        loseVal = lose[0]
        print("use", use)
        print("lose", lose)
        print("useVal", useVal)
        print("loseVal", loseVal)
        if useVal > loseVal:
            return [useVal, [itemList[0]] + use[1]]
        else:
            return lose



print(knapsack(6, [[1, 4], [5, 150], [4, 180]]))

