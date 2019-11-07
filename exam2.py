def fastLCS(S1, S2):
    memo = {}
    def helper(S1, S2):
        if (S1, S2) in memo:
            return memo [(S1, S2)]
        elif S1 == "" or S2 == "":
            answer = 0
        elif S1[0] == S2[0]:
            answer = 1 + helper(S1[1:], S2[1:])
        else:
            chopS1 = helper(S1[1:], S2)
            chopS2 = helper(S1, S2[1:])
            answer = max(chopS1, chopS2)
            
        memo[(S1, S2)] = answer
        return answer

    return helper(S1, S2)



def knapsack(capacity, itemList):
    if capacity < 0:
        return [-float('inf'), []]
    elif capacity == 0 or itemList == []:
        return [0, []]
    else:
        use = knapsack(capacity - itemList[0][0], itemList[1:])
        lose = knapsack(capacity, itemList[1:])
        useVal = itemList[0][1] + use[0]
        loseVal = lose[0]
        if useVal > loseVal:
            return [useVal, [itemList[0]] + use[1]]
        else:
            return lose


def numToBasesB(N,B):
    #Assumption N >= 0
    '''Converts number of base 10 to a base B'''
    def helper(N, B):
        if N == 0:
            return ''
        elif N % B == 0:
            return helper(N // B, B) + str(0)
        else:
            return helper(N // B, B) + str(N % B)


    output = helper(N, B)
    return '0' if output == '' else output


def baseBToNum(S, B):
    '''Number S in B to number in base 10'''
    if not S:
        return 0
    return baseBToNum(S[:-1], B) * B + int(S[-1])


def addB(B1, B2):
    '''Add two binary numbers'''
    def helper(B1, B2, carry):
        # Each row has (x,y,carry-in) : (sum,carry-out)
        FullAdder = {   ('0','0','0') : ('0','0'),
                        ('0','0','1') : ('1','0'),
                        ('0','1','0') : ('1','0'),
                        ('0','1','1') : ('0','1'),
                        ('1','0','0') : ('1','0'),
                        ('1','0','1') : ('0','1'),
                        ('1','1','0') : ('0','1'),
                        ('1','1','1') : ('1','1')   }

        if B1 != '' and B2 != '':
            outcome = FullAdder[(B1[-1], B2[-1], carry)]
            return helper(B1[:-1], B2[:-1], outcome[1]) + outcome[0]
        elif carry == '1':
            return '1'
        else:
            return '';

    
    return helper(B1, B2, '0')
