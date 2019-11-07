def fastLCS(S1, S2):
    memo = {}
    def LCS(S1, S2):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        elif not S1 or not S2:
            value = 0
        elif S1[0] == S2[0]:
            value = 1 + LCS(S1[1:], S2[1:])
        else:
            branch_one = LCS(S1[1:], S2)
            branch_two = LCS(S1, S2[1:])
            value = max(branch_one, branch_two)

        memo[(S1, S2)] = value
        return value

    return LCS(S1, S2)

#input value: capacity, [[item1weight, item1val], ...]
#return value: [maxval, [[item1weight, item1val], ...] 
def knapsack(capacity, itemList):
    if capacity < 0:
        return [-float('inf'), []]
    elif capacity == 0 or itemList == []:
        return [0, []]
    else:
        branch1 = knapsack(capacity - itemList[0][0], itemList[1:]) #use
        branch2 = knapsack(capacity, itemList[1:]) #lose
        val1 = branch1[0] + itemList[0][1]
        val2 = branch2[0]
        return [val1, [itemList[0]] + branch1[1]] if val1 > val2 else branch2


print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))


def numToBasesB(N, B):
    if not N:
        return '';
    elif N % B == 0:
        return numToBasesB(N // B, B) + '0'
    else:
        return numToBasesB(N // B, B) + str(N % B)


def baseBToNum(S, B):
    if not S:
        return 0
    return baseBToNum(S[:-1], B) * B + int(S[-1])


add
                
                


