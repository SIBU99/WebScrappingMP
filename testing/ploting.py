import matplotlib.pyplot as plt 

x = ["kumar","baba","kumar"]
y = [10,30,10]
z = [i for i  in range(len(x))]
plt.bar(z,y)
plt.xticks(z,x)
plt.show()
