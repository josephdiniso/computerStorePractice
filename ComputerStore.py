marketList=[]

class Computer:
    def __init__(self,model,value, brand):
        self.model=model
        self.value=value
        self.brand=brand
    def __repr__(self):
        return "Model {model} laptop from {brand}, worth ${value}".format(brand=self.brand,model=self.model,value=self.value)
   
    def forSale(self, salePrice, forSale):
        self.salePrice=salePrice
        self.forSale=forSale
        self.computerMarket=Marketplace(self, self.salePrice)
class Owner:
    def __init__(self, name, computer):
        self.name=name
        self.computer=computer
        self.computerList={1:computer}
    
    def __repr__(self):
        return "{name}'s {brand} {model} laptop, valued at ${value}".format(name=self.name,brand=self.computer.brand,model=self.computer.model, value=self.computer.value)
    
    def addComputer(self, computer):
        self.computerList[(len(self.computerList)+1)]=computer
    
    def sellComputer(self, computerIndex, salePrice, marketplace):
        marketplace.addStock(self.computerList[computerIndex], salePrice)
        self.computerList.pop(computerIndex)
        
        
        
class Marketplace:

    def __init__(self, location):
        self.computerListing={}
        self.location=location
    
    def __repr__(self):
        return self.computerListing
    #Shows computer listings when printing instantiated class
    
    def addStock(self, computer, salePrice):
        self.computerListing[len(self.computerListing)+1]=computer
    #Used for Owner class sellComputer function
    
    def showStock(self):
        print(self.computerListing)
    #Prints stock index    
    def sellStock(self, computerIndex):
        self.newComputerListing={}
        self.computerListing.pop(computerIndex)
        i=1
        for key in self.computerListing.keys():
            self.newComputerListing[i]=self.computerListing[key]
            i+=1
        self.computerListing=self.newComputerListing    
    
joeLaptop=Computer("Spectre",1500,'HP')
joeBackup=Computer('Inspiron', 1100, 'Dell')
joseph=Owner('Joseph',joeLaptop)
joseph.addComputer(joeBackup)
target=Marketplace('Garden City')
joseph.sellComputer(1, 1200, target)
joseph.sellComputer(2, 1500, target)
target.showStock()
print(target.sellStock(1))
target.showStock()


