#this is the example JSON

import json as js 

ptr = []
"""
print('Welcome to Directories')
while True:
    dic = {}
    dic['name'] = input("Enter your Name ]:::[ ")
    dic['Father'] = input('Enter your Father\'s Name]:::[ ')
    dic['Mother'] = input('Enter your Mother\'s Name]:::[ ')
    ptr.append(dic)
    ch = input("Type \'n\' to stop execution ]:::[ ")
    if ch == 'n':
        break

js.dump(ptr,open('test.txt','w+'))
"""
store = [{1: {'name': 'Samsung Galaxy J7 Prime (Gold, 32 GB)', 'rate': '4.2 ★', 'price': '₹10,990', 'mrp': '₹15,300', 'off': '28% off', 'stock': 'Available'}},
             {2: {'name': 'Samsung Galaxy J7 Prime 2 (Gold, 32 GB)', 'rate': '4.3 ★', 'price': '₹10,990', 'mrp': '₹14,990', 'off': '26% off', 'stock': 'Available'}}, 
             {3: {'name': 'Samsung Galaxy J7 Prime (Black, 32GB)', 'rate': '4.2 ★', 'price': '₹10,990', 'mrp': '₹15,300', 'off': '28% off', 'stock': 'Available'}}, 
             {4: {'name': 'Samsung Galaxy J7 Prime 2 (Black, 32 GB)', 'rate': '4.3 ★','price': '₹11,990', 'mrp': 'Not Available', 'off': 'Not Available', 'stock': 'Available'}}, 
             {5: {'name': 'Samsung Galaxy J7 Prime (Gold, 16 GB)', 'rate': '4.2 ★', 'price': '₹10,890', 'mrp': 'Not Available', 'off': 'Not Available', 'stock': 'Available'}}, 
             {6: {'name': 'Samsung Galaxy J7 Prime (Black, 16 GB)', 'rate': '4.2 ★', 'price': '₹10,990', 'mrp':'Not Available', 'off': 'Not Available', 'stock': 'Available'}}]
    
name = []
rate = []
price = []
mrp = []
off = []
stock = []

def  rate_cutter(r):
    "this will slice the rate of the selected "
    no = [' ','★']
    temp = ""
    for i in r:
        if i not in no:
            temp += i
    print(temp)
    return float(temp)

def price_cutter(p):
    "this will slice the price of the selected" 
    no = ['₹',',']
    temp = ""
    for i in p:
        if i not in no:
            temp += i
    print(temp)
    return int(temp)

def mrp_cutter(m):
    "this will slice the price of the selected" 
    no = ['₹',',']
    temp = ""
    if m != "Not Available":
        for i in m:
            if i not in no:
                temp += i
    else:
        temp = "0"
    print(temp)
    return int(temp)

def off_cutter(o):
    "this will slice the off of the selected"
    no  = ['%',' ','o','f']
    temp = ""
    if o != "Not Available":
        for i in o:
            if i not in no:
                temp += i
    else:
        temp = '0'
    print(temp)
    return float(temp)

for i in store:
        for j in i.items():
            for k in j[1].items():
                if 'name' in k:
                    name.append(k[1])
                elif 'rate' in k:
                    rate.append(rate_cutter(k[1]))
                elif 'price' in k:
                    price.append(price_cutter(k[1]))
                elif 'mrp' in k:
                    mrp.append(mrp_cutter(k[1]))
                elif "off" in k:
                    off.append(off_cutter(k[1]))
                elif "stock" in k:
                    stock.append(k[1])

for i,j,k,l,m,n in zip(name,rate,price,mrp,off,stock):
    print(i,j,k,l,m,n)
