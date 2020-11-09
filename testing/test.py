import matplotlib.pyplot as plt 

price = [10,50,30,70,80,120]
item = ['2018-01-24','2018-02-13','2018-03-01','2018-05-17','2018-07-06','2018-12-09']

p1 = plt.bar(item,price,0.35,color = 'r')
plt.title("Deposite Vs Time")
plt.xticks(rotation=15)
plt.show()