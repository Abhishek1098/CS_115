#lab 2
#Abhishek Yadav

def dot(L, K):
    if not L or not K:
        return 0
    if length(L) == 1 or length(K) == 1:
        return L[0] * K[0]
    return L[0] * K[0] + dot(L[1:], K[1:])



def length(ofList):
    if ofList:
        return 1 + length(ofList[1:])
    return 0


def explode(S):
    if length(S) == 0:
        return []
    if length(S) == 1:
        return [S[0]]
    return [S[0]] + explode(S[1:])


def ind(e, L):
    if not L or e == L[0]:
        return 0
    return 1 + ind(e, L[1:])


def removeAll(e, L):
    if not L:
        return []
    if length(L) == 1:
        if e != L[0]:
            return [L[0]]
        else:
            return []
    if e != L[0]:
        return [L[0]] + removeAll(e, L[1:])
    return removeAll(e, L[1:])


def myFilter(func, L):
    if not L:
        return []
    if length(L) == 1:
        if func(L[0]):
            return [L[0]]
        else:
            return []
    if func(L[0]):
        return [L[0]] + myFilter(func, L[1:])
    else:
        return myFilter(func, L[1:])


def deepReverse(L):
    def isList(L):
        return isinstance(L, list)
    if L:
        if isList(L[-1]):
            return [deepReverse(L[-1])] + deepReverse(L[:-1])
        return [L[-1]] + deepReverse(L[:-1])
    else:
        return []


print(deepReverse([1,[2,3]]))

        
        



    

