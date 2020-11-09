"""
In this python program we ll create a user freindly interface with the merging of the 
flipkart.py and the processing_data.py to make it a complete use of it effectively.
"""

import flipkart as f

import processing_data as pd 


def display1():
    "this is a instruction display function "
    print("]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::[" )
    print("]*********************************   MY HUNDI PROGRAM *************************************[")
    print("]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::[")
    print("]------------------------------------------------------------- -----------------------------[")
    print("]:::::::::::::::::::::::::::::::::::::: Instruction  ::::::::::::::::::::::::::::::::::::::[")
    print("]------------------------------------------------------------------------------------------[")
    print("]::: Plesae follow all the further in instruction for smooth use of the program            [")
    print("]::: Now you have to enter the search item and then we ll pass it for further process      [")
    print("]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::[")
    print("                                                                                            ")

if __name__ == "__main__":
    #this is the main area for the excution
    display1()
    flip = f.flipkart()
    st = None
    st = flip.main()
    if st != None and len(st) != 0:
        p = pd.person(st)
    else:
        print("<<< Sorry there is no item available in fllipkart and thank you for using >>>")