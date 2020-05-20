from math import *
num=eval(input())
if num > 0:
    print("{0:+>30.3f}".format(pow(num,0.5)))
else:
    num=fabs(num)
    t=len(str(num)
    print("+" * (24-t)+"0.000"+"{0:+>30.3f}j".format(pow(num,0.5)))
