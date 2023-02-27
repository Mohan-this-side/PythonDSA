"""
1. A method calls itself
2. Exit from infinite loop
"""


a=1
def factorialofn(n):
    global a
    assert n >=0 and int(n) == n, 'No -ve numbers allowed'
    if n==1:
        print("factorinal of n is : ", a)
        a=1

    else:
        a = n * a
        factorialofn(n-1)




factorialofn(3)

factorialofn(-4)

factorialofn(10)


