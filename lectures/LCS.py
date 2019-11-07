def fastLCS(S1, S2):
    memo = {}
    def helper(S1, S2):
        if (S1, S2) in memo:
            return memo [(S1, S2)]
        elif S1 == "" or S2 == "":
            memo[(S1, S2)] = 0
            return 0
        elif S1[0] == S2[0]:
            answer = 1 + helper(S1[1:], S2[1:])
            memo[(S1, S2)] = answer
            return answer
        else:
            chopS1 = helper(S1[1:], S2)
            chopS2 = helper(S1, S2[1:])
            answer = max(chopS1, chopS2)
            memo[(S1, S2)] = answer
            return answer
    return helper(S1, S2)
    
