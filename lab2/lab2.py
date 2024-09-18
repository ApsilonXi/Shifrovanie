from datetime import datetime

def checkNum(num):
    for i in range(100):
        d = 0
        if num % i == 0:
            d += 1
    return d


n = 24   
m = 2**n

now = datetime.now() 
a = now.strftime("%H%M%S") 
b = now.strftime("%M%H%S")
c0 = now.strftime("%S%H")

while True:
    if checkNum(a) == 2:
        pass
    






