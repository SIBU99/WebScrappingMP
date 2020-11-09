"""
    in this program we ll scrap the flipkart site as per the requirement of the item to search
"""
#importing section
import requests as req
import bs4
from sys import exit 
from time import sleep
#..end

#class section
class flipkart:
    """
    in this site we ll perform the scrapping of  flipkart site using req for the navigation and the 
    bs4 for the content pulling out or data mining
    """

    def __init__(self,key=None):
        "this is a constructor for the flipkart site"
        self.key = key
        self.url = "https://www.flipkart.com"
        self.search_url = "https://www.flipkart.com/search"
        self.page = 1
        self.db = []
        self.search ={'q':key,
                 'otracker':'search',
                 'otracker1':'search',
                 'marketplace':'FLIPKART',
                 'as-show':'on',
                 'as':'off'}
        if key is not None:
            rp = req.get(self.search_url,params=self.search)
            self.link = self._adder(rp.url)
            rq = req.get(self.link)
            self.soup = bs4.BeautifulSoup(rq.text,'lxml')
        
    def searching(self):
        "this method will perform the searching if the value is not passed in the __init__"
        key = input("Enter the item you want to saerch ]:::[ ")
        print("]::: Please wait will we are seraching your product...  :::[")
        self.search ={'q':key,
                 'otracker':'search',
                 'otracker1':'search',
                 'marketplace':'FLIPKART',
                 'as-show':'on',
                 'as':'off'}
        rp = req.get(self.search_url,params=self.search)
        self.link = self._adder(rp.url)
        rq = req.get(self.link)
        self.soup = bs4.BeautifulSoup(rq.text,'lxml')

    def _adder(self,key):
        "this method will change the key into the required format"
        ter = [i for i in key]
        try:
            t=ter.index('+')
            ter[t]="%20"
            st = "".join(i for i in ter)
            return self._adder(st)
        except ValueError:
            return "".join(i for i in ter)
    
    def _nav(self):
        "this will be help in navigating throug web pages"
        self.page += 1
        fotter = self.soup.find('div',{'class':'_2zg3yZ'})
        # a chnage added
        link = ''
        final = ''
        for i in fotter.find_all('a'):
            if i.text == 'Next':
                link = i['href']
                final = self.url + link
        rq = req.get(final)
        self.soup = bs4.BeautifulSoup(rq.text,'lxml')
    
    def collector100(self):
        "this method is for the rowbased and  used for the data mining of the each section of the div"
        main = self.soup.find_all('div',{'class':'_1UoZlX'})
        trp = 100
        for i in main:
            self.sl += 1
            trp += 1
            ptr = {}
            ptr['name'] = i.find('div',{'class':'_3wU53n'}).text
            try:
                ptr['rate'] = i.find('div',{'class':'hGSR34 _2beYZw'}).text
            except AttributeError:
                ptr['rate'] = "Not Available"
            try:
                ptr['price'] = i.find('div',{'class':'_1vC4OE _2rQ-NK'}).text
            except AttributeError:
                ptr['price'] = 'Not Available'
            try:
                ptr['mrp'] = i.find('div',{'class':'_3auQ3N _2GcJzG'}).text
            except AttributeError:
                ptr['mrp'] = 'Not Available'
            try:
                ptr['off'] = i.find('div',{'class':'VGWI6T'}).text
            except AttributeError:
                ptr['off'] = 'Not Available'
            try:
                ptr['stock'] = i.find('div',{'class':'_3aV9Tq'}).text
            except AttributeError:
                ptr['stock'] = 'Available'
            tr = [{self.sl:ptr}]
            self.db += tr
            del ptr,tr
    
    def collector25(self):
        "this method is for the grid based and  used for the data mining of the each section of the div"
        main = self.soup.find_all('div',{'class':'_3liAhj _1R0K0g'})
        trp = 100
        for i in main:
            ptr={}
            self.sl += 1
            trp += 1
            ptr['name'] = i.find('a',{'class','_2cLu-l'}).text
            try:
                ptr['rate'] = i.find('div',{'class':'hGSR34 _2beYZw'}).text
            except AttributeError:
                ptr['rate'] = 'Not Available'
            try:
                ptr['price'] = i.find('div',{'class':'_1vC4OE'}).text
            except AttributeError:
                ptr['price'] = 'Not Available'
            try:
                ptr['mrp'] = i.find('div',{'class':'_3auQ3N'}).text
            except:
                ptr['mrp'] = 'Not Available'
            try:
                ptr['off'] = i.find('div',{'class':'VGWI6T'}).text
            except AttributeError:
                ptr['off'] = 'Not Available'
            ptr['stock'] = 'May Be Available'
            tr = [{self.sl:ptr}]
            self.db += tr
            del ptr,tr
            
    def decider(self):
        "this function will decide weather the collecter23 or collector100 will call"
        alot = self.soup.find_all('div',{'class':'_3O0U0u'})
        let = alot[0].find('div')
        try:
            if let['style'] == 'width:25%':
                return self.collector25
            elif let['style'] == 'width:100%':
                return self.collector100
            else:
                raise AttributeError
        except AttributeError:
            exit('ERROR:Execution failed....////')

    def checker(self):
        "this method will check the top weather a data is  contained or not"
        try:
            _ = self.soup.find('div',{'class':'_3O0U0u'})
        except AttributeError:
            return 'stop'

    
    def main(self):
        "this function is reponsible for the main execution of the class"
        if self.key is None:
            self.searching()
        self.sl = 0
        page = 1
        while(True):
            #this is the main room of execution of the work -> the repeater
            try:
                func = self.decider()
                let = True
                while(True):
                    if page != self.page:
                        raise IndexError
                    
                    topper = 'set'
                    topper = self.checker()

                    if topper == 'stop':
                        raise AttributeError
                    """if self.page is :
                        raise AttributeError"""
                    func()

                    #footer is the lower end  check
                    footer = self.soup.find('div',{'class':'_2zg3yZ'})
                    navi = footer.find('nav')
                    sleep(1)
                    page += 1
                    let = True
                    for i in navi.find_all('a'):
                        if i.text == 'Next':
                            self._nav()
                            let = False
                    if let is True:
                        break
                        
            except AttributeError:
                print("work of searching is completed.")
                print(" We are able to find %d product according to your search." %(len(self.db)))
                ch = input("Press 'Y' to search again for fresh data or Press 'N' to stop execution and pass the selcted data ]:::::[ ")
                if ch == 'y' or ch == 'Y':
                    self.searching()
                elif ch == 'n' or ch == 'N':
                    print("]::: We are able find some result for are serach which are as follow :- [ \n")
                    return self.db
                else:
                    exit('Please enter the right option and read the above instruction')
            except IndexError:
                print("work of searching is completed.")
                print(" We are able to find %d product according to your search." %(len(self.db)))
                ch = input("Press 'Y' to search again for fresh data or Press 'N' to stop execution and pass the selcted data ]:::::[ ")
                if ch == 'y' or ch == 'Y':
                    self.page = 1
                    page = 1
                    print(page,"]===[",self.page)
                    self.searching()
                elif ch == 'n' or ch == 'N':
                    print("]::: We are able find some result for are serach which are as follow :- [ \n")
                    return self.db
                else:
                    exit('Please enter the right option and read the above instruction')

#..end

#main start
if __name__ == "__main__":
    f = flipkart()
    st = None
    st = f.main()

    for i in st:
        print(i)
#main end