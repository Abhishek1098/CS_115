#Abhishek Yadav
#I pledge my honor to abide by the Stevens Honor Code.

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


def baseToBase(B1, B2, SinB1):
    '''Converts SinB1 a number in B1 to a number in B2'''
    N = baseBToNum(SinB1, B1)
    return numToBasesB(N, B2)


def add(S, T):
    '''Add two binary numbers by change of base'''
    return numToBasesB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)


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

    
