x = [1.0,1.6,3.4,4.0,5.2]
y = [1.2,2.0,2.4,3.5,3.5]

def suma(x):
    sum = 0
    for i in range(len(x)):
        sum = x[i] + sum
        return sum

print (suma(x))
print (suma(y))

import pandas as pd
x1 = pd.array(x)
