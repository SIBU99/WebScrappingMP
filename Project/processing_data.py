import matplotlib.pyplot as plt 
import numpy as np 
from flipkarttest import flipkart
from sys import exit
from time import sleep
from json import dump, load 
from time import time
from datetime import datetime as dt 
 
class processing:
    "this class is  responsible for the processing the data"

    def __init__(self,data):
        "this is the constructor of the processing class"
        for i in data:
            print(i)
        else:
            print("      ")
        self.data = data
        self.name = [] #this will store the name of product
        self.rate = [] #this will store the rate of product
        self.price = [] #this will store the flipkart product
        self.mrp = [] #this will store the MRP price
        self.off = [] # this will store the off price from mrp to get price of flipkart
        self._stock_checking()
    
    def _stock_checking(self):
        "this will check the stock of the items and return stock available items"
        for i in self.data:
            for j in i.items():
                for k in j[1].items():
                    if 'name' in k:
                        self.name.append(k[1])
                    elif 'rate' in k:
                        self.rate.append(self.rate_cutter(k[1]))
                    elif 'price' in k:
                        self.price.append(self.price_cutter(k[1]))
                    elif 'mrp' in k:
                        self.mrp.append(self.mrp_cutter(k[1]))
                    elif 'off' in k:
                        self.off.append(self.off_cutter(k[1]))
                    elif 'stock' in k:
                        if 'Out Of Stock' == k[1]:
                            self.name.pop()
                            self.rate.pop()
                            self.price.pop()
                            self.mrp.pop()
                            self.off.pop()

    def price_cutter(self,p):
        "this will slice the price of the selected" 
        no = ['₹',',']
        temp = ""
        for i in p:
            if i not in no:
                temp += i
        return int(temp)

    def mrp_cutter(self,m):
        "this will slice the price of the selected" 
        no = ['₹',',']
        temp = ""
        if m != "Not Available":
            for i in m:
                if i not in no:
                    temp += i
        else:
            temp = "0"
        return int(temp)

    def off_cutter(self,o):
        "this will slice the off of the selected"
        no  = ['%',' ','o','f']
        temp = ""
        if o != "Not Available":
            for i in o:
                if i not in no:
                    temp += i
        else:
            temp = '0'
        return float(temp)

    def rate_cutter(self,r):
        "this will slice the rate of the selected"
        no = [' ','★']
        temp = ""
        if r != "Not Available":
            for i in r:
                if i not in no:
                    temp += i
        else:
            temp = "0"
        return float(temp)

class person(processing):
    "this  class is the acounting section for tracking"
     
    def __init__(self,data):
        """this is the constructor for the person class and it is 
        child of processing class"""
        super().__init__(data)
        while True:
            self.work()
            ch = input("Press Y to contine and N to stop ]:::[ ")
            if ch == 'N' or ch == 'n':
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<(:  Thank you for using  :)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                break
        

    def work(self):
        "this method will perform the work of the customer"
        print("]:::::::::::::::::::::Information:::::::::::::::::::::[")
        print("]  1. Sign Up for the new user                        [")
        print("]  2. Log In                                          [")
        print("]:::::::::::::::::::::::::::::::::::::::::::::::::::::[")
        print("\n"*3)
        try:
            c = int(input("  ENTER YOUR CHOICE]:::::[ "))
            if c not in [1,2]:
                raise ValueError
        except ValueError:
            exit("ERROR: Press 1 and 2  or program terminated.")
        if c is 1:
            print("Welcome to Registation Form")
            dic = {}
            flag = 0
            while flag < 4:
                dic['name'] = input('Enter your NAME ]:::[ ')
                dic['uname'] = input('Enter a new USERNMAE ]:::[ ')
                st = "pass"
                st = self.search_username(dic['uname'])
                print(st)
                if st == 'fail':
                    print('%s is already used, so select any other username' % (dic['uname']))
                    flag += 1
                    print("you have only %d , Attempts" %(4 - flag) )
                else:
                    break
            else:
                exit('Sorry you program is terminated')
            try:
                dic['saving'] = int(input('Enter your Base Saving ]:::[ '))
            except ValueError:
                print('Enter the Base Saving in integer like :- 34000 and so on')
                try:
                    dic['saving'] = int(input("Enter your Base Saving ]:::[ "))
                except ValueError:
                    exit("Sorry Program terminated and Please follow Instruction")
            
            print("]::::::::::::::::::::::[  Your Registration is sucessful completed  ]::::::::::::::::::::::[")
            check = load(open("user_data.txt"))
            if type(check) != list:
                exit("Sorry your program is coruptted please check user_data.txt")
            check.append(dic)
            dump(check,open("user_data.txt",'w+'))
            del check
            check = load(open('user_name.txt'))
            check.append(dic['uname'])
            dump(check,open('user_name.txt','w+'))
            del check
            del dic
        elif c is 2:
            print("]:::::::::::::::::::::::::::::::::::::::::::::::[")
            print("]::::::::::Welcome to the Log In portal:::::::::[")
            print("]::::::::::::::::::Instruction::::::::::::::::::[")
            print("]:::Just Enter the choice you want to perform   [")
            print("]:::::::::::::::::::::::::::::::::::::::::::::::[")
            print("\n"*3)
            #this is the username loop
            controller = 0
            loader = load(open('user_name.txt'))
            while controller < 4:
                try:
                    ch = input("]::: Enter your Username ]:::[ ")
                    if type(loader) != list:
                        raise TypeError
                    if ch in loader:
                        print("\n"*2)
                        print("]:::::::::::Account Found:::::::::::[")
                        break
                    else:
                        raise TypeError
                except TypeError:
                    controller += 1
                    print("\n"*2)
                    print("]::: You have only more %d attempts :::[" %(4-controller))
            else:
                exit("Program terminated please remeber your Username")
            del loader
            
            #this is the loop for the data access for the specific user
            loader = load(open('user_data.txt'))
            front = []
            end = []
            try:
                if type(loader) != list:
                    raise TypeError
                dic = {}
                for i in loader:
                    if ch == i['uname']:
                        dic = i
                        front = loader[:loader.index(i)]
                        end = loader[loader.index(i)+1:] 
                        break 
                else:
                    raise NotADirectoryError# a msg that state that directory not fond ,data is courupted
            except TypeError:
                exit("ERROR: Data may be coruppted please check the file user_data.txt")
            except NotADirectoryError:
                exit("ERROR: Data may be corupted please chck the file user_data.txt")
            
            #this the user display content
            print("]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::[")
            print("]:::::::::::::::::::::::::   Instruction  :::::::::::::::::::::::::::::::::[")
            print("]::: 1. To add money to Account                                            [")
            print("]::: 2.To check the account status                                         [")
            print(']::: 3.To check the saving status for the product                          [')
            print(']::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::[')
            try:
                ch1 = int(input(']:::Just Enter the choice you want to perform  ]::::[ '))
                if ch1 not in [1, 2, 3]:
                    raise ValueError
            except ValueError:
                print("Note: Please enter the given Serial Number other wise program will terminate ")
                print("]:::::::::::::::           It is last chance            ::::::::::::::::[")
                try:
                    ch1 = int(input(']::: Enter the amount you want to enter ]::::[ '))
                    if ch1 not in [1, 2, 3]:
                        raise ValueError
                except ValueError:
                    exit("]:::Program Terminate and Please follow the Instruction           :::[")
            
            try:
                if ch1 is 1:
                    #add a function for the work with the selcted dictionary for the work name = [func1]
                    dic = self.func1(dic)
                    front.append(dic)
                    loader = front + end
                    dump(loader,open('user_data.txt','w+'))
                    del loader,dic
                elif ch1 is 2:
                    #add a function for the work with the selected dictionary for the work name = [func2]
                    self.func2(dic)
                elif ch1 is 3:
                    #add a funtion for the work with the selcted dictionary for the work name = [func3]
                    self.func3(dic)
                else:
                    print("Enter the right option and you have last chance otherwise the program will terminate ")
                    raise AttributeError
            except AttributeError:
                try:
                    if ch1 is 1:
                        #add a function for the work with the selcted dictionary for the work name = [func1]
                        self.func1(dic)
                    elif ch1 is 2:
                        #add a function for the work with the selected dictionary for the work name = [func2]
                        self.func2(dic)
                    elif ch1 is 3:
                        #add a funtion for the work with the selcted dictionary for the work name = [func3]
                        self.func3(dic)
                    else:
                        print("Enter the right option and you have last chance otherwise the program will terminate ")
                        raise ValueError
                except ValueError:
                    exit("]::: Program Terminate and Please follow the Instruction :::::::::::::[")
            
    def func1(self,dic):
        "this function will add money to account"
        try:
            if type(dic) != dict:
                raise NotADirectoryError
        except NotADirectoryError:
            exit("]::::::  Sorry there is a technical issue :::::::[")
        
        #add the time and the time
        put = {}
        s = str(dt.now()).split()
        put['time'] = s[1]
        put['date'] = s[0]
        try:
            put['add_on'] = int(input("Enter the amount the you want to add ]:::[ "))
        except ValueError:
            print('Note ]:::[ Please Enter the amount to be add in integer like :- 45000 and so on ')
            print("Note ]:::[ You have Last Chance then program will terminate......")
            try:
                put['add on'] = int(input("Enter the amount the you want to add ]:::[ "))
            except ValueError:
                exit('ERROR: Please Follow Intruction or the program  will terminate')

        l = [0]
        for i in dic:
            try:
                _ = int(i)
                l.append(int(i))
            except ValueError:
                pass

        dic[int(max(l) + 1)] = put

        return dic

    def func2(self,dic):
        "this method will check the account status and gives us a  graph of the deposit"
        try:
            if type(dic) != dict:
                raise NotADirectoryError
        except NotADirectoryError:
            exit('ERROR]::[Please check the file user_data.text it may be corrupted')
        
        total = 0
        x_axis = []
        y_axis = []
        for i in dic:
            if i == 'saving':
                x_axis.append('saving')
                y_axis.append(dic[i])
                total += dic[i]
            else:
                try: 
                    coke = int(i)
                    st = dic[i] 
                    x_axis.append(st['date'])
                    y_axis.append(st['add_on'])
                    total += st['add_on']
                    del st,coke
                except ValueError:
                    pass
        
        for i,j in zip(x_axis,y_axis):
            if i == 'saving':
                print("Your Initial Saving is Rs.%d" %(j))
            else:
                print("You have deposited Rs.%d on %s date" %(j,i))
        else:
            print("You have a TOTAL SAVING of Rs.%d" %(total))
        
        self.ploting(x_axis,y_axis)
        
    def func3(self,dic):
        "this function will show the status of the product wrt total "
        try:
            if type(dic) == int:
                raise NotADirectoryError
        except NotADirectoryError:
            exit("ERROR ]:::[ Please check the file user_data.txt so file is corrupted ")

        total = 0
        for i in dic:
            if i == "saving":
                total += dic[i]
            else:
                try:
                    _ = int(i)
                    st = dic[i]
                    total += st['add_on']
                except ValueError:
                    pass
        else:
            print("\n")
        print("]:::Total Saving Rs.%d::::["%(total))
        self.ploting(self.name,self.price,total)

    def ploting(self,x_axis,y_axis,thresold=None):
        "this will print the bar as per x and y axis it is passed"
        if thresold is None:
            #this will print the bargraph without any thrersold
            z_keep = [i for i in range(len(x_axis))]
            plt.title("Date - Saving")
            plt.bar(z_keep,y_axis)
            plt.xticks(z_keep,x_axis)
            plt.xticks(rotation=15)
            plt.show()

        else:
            y = np.array(y_axis)
            x =[i for i in range(len(x_axis))]

            above_bar = np.maximum(y - thresold,0)
            below_bar = np.minimum(y,thresold)

            p1=plt.bar(x, below_bar, 0.35, color = 'g', label = "buy it")
            p2=plt.bar(x, above_bar, 0.35, color = 'r',bottom = below_bar, label = "wait it")
            _ =plt.plot([-1.,max(x)+0.5],[thresold,thresold],'k--', color = 'b', label = "saving")
            plt.xticks(x,x_axis)
            plt.xticks(rotation=15)
            plt.legend((p1,p2),('buy it','wait it'))
            plt.show()

    def search_username(self,user_name):
        "this function will return the availability of the user_name"
        loader = load(open("user_name.txt"))
        try:
            if type(loader) != list:
                raise AttributeError
            else:
                for i in loader:
                    if user_name == i:
                        return 'fail'
                else:
                    return 'pass'
        except AttributeError:
            exit(']::: Note : Data is coruppted plesae check the file user_name.txt  :::[')




if __name__ == "__main__":
    store = [{1: {'name': 'Samsung Galaxy J7 Prime (Gold, 32 GB)', 'rate': '4.2 ★', 'price': '₹10,990', 'mrp': '₹15,300', 'off': '28% off', 'stock': 'Available'}},
             {2: {'name': 'Samsung Galaxy J7 Prime 2 (Gold, 32 GB)', 'rate': '4.3 ★', 'price': '₹10,990', 'mrp': '₹14,990', 'off': '26% off', 'stock': 'Available'}}, 
             {3: {'name': 'Samsung Galaxy J7 Prime (Black, 32GB)', 'rate': '4.2 ★', 'price': '₹10,990', 'mrp': '₹15,300', 'off': '28% off', 'stock': 'Available'}}, 
             {4: {'name': 'Samsung Galaxy J7 Prime 2 (Black, 32 GB)', 'rate': '4.3 ★','price': '₹11,990', 'mrp': 'Not Available', 'off': 'Not Available', 'stock': 'Available'}}, 
             {5: {'name': 'Samsung Galaxy J7 Prime (Gold, 16 GB)', 'rate': '4.2 ★', 'price': '₹10,890', 'mrp': 'Not Available', 'off': 'Not Available', 'stock': 'Available'}}, 
             {6: {'name': 'Samsung Galaxy J7 Prime (Black, 16 GB)', 'rate': '4.2 ★', 'price': '₹10,990', 'mrp':'Not Available', 'off': 'Not Available', 'stock': 'Available'}}]
    
    p = person(store)
    """
    name = []
    mrp = []
    stock = [] #off
    price =[] 
    for i in store:
        for j in i.items():
            for k in j[1].items():2 
                if 'name' in k:
                    name.append(k[1])
                elif 'price' in k:
                    price.append(k[1])
                elif 'mrp' in k:
                    mrp.append(k[1])
                elif 'off' in k:
                    if 'Not Available' == k[1]:
                        name.pop()
                        mrp.pop()
                        price.pop()
                    else:
                        stock.append(k[1])
    for i,j,k,l in zip(name,mrp,stock,price):
        print(i,"->",j,"-->",k,"--->",l)
    """
