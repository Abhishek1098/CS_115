'''
Created on 10/12/19
@author:   Abhishek Yadav
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


def compress(S):
    '''Takes a binary string S of length 64 and returns run-length
        representation in binary of bit size 5'''

    def binaryToRL(B, countingZero):
        '''Takes binary string and counts succesive ones or zeros based on bool value. Starts true so checks for 0s first.
            Returns list of 1s for each consecutive value
        '''
        if not B:
            return ""
        elif (B[0] == '0' and countingZero) or (B[0] == '1' and not countingZero):
            return "1" + binaryToRL(B[1:], countingZero)
        else:
            return "," + binaryToRL(B, not countingZero)

    def restraint(L):
        '''Takes list of numbers of repeating 0s or 1s. Because limit of 5 bits. We cannot represent anything bigger than 31 or 11111.
        So this method breaks up anything greater than 31.'''
        if L:
            if L[0]>31:
                if L[0] - 31 <= 31:
                    return [31, 0, L[0]-31] + restraint(L[1:])
                else:
                    return [31, 0, 31, 0, L[0]-62] + restraint(L[1:])
            else:
                return [L[0]] + restraint(L[1:])
        return []
        

    def RLToBinaryList(n):
        '''function takes single value and turns it into binary number'''
        if n == 0:
            return ''
        elif n % 2 != 0:
            return RLToBinaryList(n // 2) + str(1)
        else:
            return RLToBinaryList(n // 2) + str(0)

    def listToBinary(n):
        '''takes list of binary numbers and combines them into big string. Makes any binary numbers with less than 5 bits, 5 bits.'''
        if n:
            return (COMPRESSED_BLOCK_SIZE * '0' + n[0])[-1*COMPRESSED_BLOCK_SIZE:] + listToBinary(n[1:])
        else:
            return ''
 
    return listToBinary(list(map(RLToBinaryList, restraint(list(map(lambda x: len(x), binaryToRL(S, True).split(",")))))))


def uncompress(S):
    '''Inverse of compress function'''

    def split(L):
        '''Splits string by 5 and returns list'''
        return [] if not L else [L[0:5]] + split(L[5:])

    def binaryToNum(s):
        '''Precondition: s is a string of 0s and 1s.
        Returns the integer corresponding to the binary representation in s.
        Note: the empty string represents 0.'''
        return 0 if not s else binaryToNum(s[:-1]) * 2 + int(s[-1])

    def rToBin(L, addingZero):
        '''adds 0s and 1s according to list value and addingZero boolean'''
        if not L:
            return ''
        elif L[0] == 0:
            return rToBin(L[1:], not addingZero)
        else:
            L[0] = L[0] - 1
            return '0' + rToBin(L, addingZero) if addingZero else '1' + rToBin(L, addingZero)

    return rToBin(list(map(binaryToNum, split(S))), True)


def compression(S):
    '''returns ration of compressed to originial'''
    return len(compress(S))/len(S)

'''
The largest amount of bits the compress function could return for an input of 64 is 325. Because the runlength documents
each change. There can be a max of 65 changes in a 64 bit input. each change has a 5 bit binary representation.
64 * 5 = 325. By change i mean a change from 0s to 1s and vis versa.

It is not possible because if k = 5   the only way to have a compressed output shorter then the input would be
if there were less then 12 changes. Otherwise there is no way to represent more than 12 changes with less then
64 bits because each change has a 5 bit representation. 
'''


def test(T):
    print(T[0])
    print("T = ", T[1])
    print("compress(T) = ", compress(T[1]))
    print("uncompress(compress(T)) = ", uncompress(compress(T[1])))
    print("compression(T) = ", compression(T[1]))
    print("Pass?", T[1] == uncompress(compress(T[1])))
    print("="*100)
    


test(("Blank", "0"*64))
test(("Full", "1"*64))
test(("Checkerboard", "10101010"*8))
test(("Penguin", "00011000"+"00111100"*3+"01111110"+"11111111"+"00111100"+"00100100"))
test(("Five", "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01111110" + "0"*8))
        
    
