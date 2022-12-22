# print the sin and cos values of 0 to 345 with 15 increments
import math
print("sin ---------- cos")
for i in range(0,360,15):
    print(round(math.sin(math.radians(i)),4), "---" ,round(math.cos(math.radians(i)),4))
    print("***************************")
    
