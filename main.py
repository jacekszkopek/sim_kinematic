import matplotlib.pyplot as plt
import numpy as np
import math as mh
import msvcrt as msv

from fingerv1 import *
from matrices import *




base = tranrot(0,0,5,radians(0),radians(0),radians(180))
#print(base)

f2 = Finger(base,3.5, 2.5, 1.5, radians(0), radians(0), radians(0), radians(0))
print("mcp",f2.mcp)

print("pos",f2.pos)
print(f2.rot)
f2.move(radians(0),radians(0),radians(45),radians(45))
f2.show_finger()
print(f2.pos)
print(f2.rot)
msv.getch()
f2.move(radians(45),radians(0),radians(0),radians(0))
f2.show_finger()

# arr = np.array([[1,2],[3,4]])
# print(arr)
# arr2 = np.reshape(arr[:,1],(2,1))
# print(arr2)
# arr = np.concatenate([arr,arr2],axis=1)
# print(arr)




#print(f2.mcp)
#print(f2.pip)
#print(f2.dip)



