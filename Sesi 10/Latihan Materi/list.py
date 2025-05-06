import numpy as np

value = np.array([2,0,5,10],dtype= str)
print(value)

newvalue = [x*3 for x in value]
print(newvalue)

res = [2,6,5,10]
print(res*3)