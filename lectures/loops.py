def factorial(n):
    answer = 1
    for x in range(1,n+1):
        answer = answer * x
    return answer

#def fib(n):


def breakingLoop():
    password = ""
    while True:
        inpt = str(input("password? "))
        if inpt == password:
            break
    print("yay!")

    #dont use break


def z(n):
    if n == 0:
        return 0
    else:
        return sqrt(z(n-2)) + C
'''fractal?
z0= 0
zn+1=zn^2+C'''

'''
Good Design

design on paper, write functions, fill functiosn, use good names, dont repeat functionality,
use comments, no global vars, use recursion/map/reduce/filter/lambda when appropriate
'''
