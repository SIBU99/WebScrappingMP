import matplotlib.pyplot as plt 
import numpy as np 

threshold = int(input("enter the threshold of the garph:"))
price =np.array([50,70,90,120,150])
x = [i for i  in range(len(price))]

above_bar = np.maximum(price - threshold,0)
below_bar = np.minimum(price,threshold)
print("below:",below_bar)
print("above:",above_bar)

p1=plt.bar(x, below_bar, 0.35, color = 'g', label = "buy it")
p2=plt.bar(x, above_bar, 0.35, color = 'r',bottom = below_bar, label = "wait it")
p3 =plt.plot([-1.,4.5],[threshold,threshold],'k--', color = 'b', label = "saving")
plt.xticks(x,('kumar','baba','mama','gudu','sai'))
plt.legend((p1,p2),('buy it','wait it'))

plt.show()
