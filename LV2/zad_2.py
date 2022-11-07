
import matplotlib.pyplot as plt
import numpy as np
random=[]
random=np.random.randint(1,7,100,int)
rangeOfnumbers=[1,2,3,4,5,6]
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
for x in random:
    if x==1:
        n1+=1
    elif x==2:
        n2+=1
    elif x==3:
        n3+=1
    elif x==4:
        n4+=1
    elif x==5:
        n5+=1
    else:
        n6+=1
countedRandomNums=[n1,n2,n3,n4,n5,n6]
plt.bar(rangeOfnumbers, countedRandomNums)
plt.show()