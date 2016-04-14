from random import randint
import math

def permQuest():
    a = []
    n = randint(6, 8)
    r = randint(2, n - 3)
    answer = (math.factorial(n))//(math.factorial(n-r))
    a.append("P")
    a.append(n)
    a.append(r)
    a.append(answer)
    a.append(randint(answer - 50, answer + 50))
    a.append(randint(answer - 10, answer + 10))
    a.append(randint(answer - 25, answer + 25))
    return a

def comboQuest():
    a = []
    n = randint(6, 10)
    r = randint(2, n - 3)
    answer = (math.factorial(n))//(math.factorial(r) * math.factorial(n-r))
    a.append("C")
    a.append(n)
    a.append(r)
    a.append(answer)
    a.append(randint(answer - 50, answer + 50))
    a.append(randint(answer - 10, answer + 10))
    a.append(randint(answer - 25, answer + 25))
    return a



def permAns(n, r):
    return (math.factorial(n))//(math.factorial(n-r))



def comboAns(n, r):
    return (math.factorial(n))//(math.factorial(r) * math.factorial(n-r))



def pickRandQuestion():
    a = randint(1, 10)
    if a % 2 == 0:
        return permQuest()
    elif a % 2 == 1:
        return comboQuest()
    else:
        return "ERRORS"

