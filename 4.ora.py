#hajo
class Hajo:
    #osztályszintű statikus változo
    __MINIRANY = 0
    __MAXIRANY = 359
    __MINSEB = 0.0
    __MAXSEB = 40.0
    __Db = 0
    def __init__(self,név="",irány=0,seb=0.0):
        self.__Név = név
        self.__Irány = irány % (Hajo.__MAXSEB + 1)
        if seb < Hajo.__MINSEB:
            self.__Sebesség = Hajo.__MINSEB
        elif seb > Hajo.__MAXSEB:
            self.__Sebesség = Hajo.__MAXSEB
        else:
            self.__Sebesség = seb
        Hajo.__Db += 1 #statikus valtozo
    
    @property
    def Név(self):
        return self.__Név
    @Név.setter
    def Név(self,név):
        self.__Név = név
    
    @property
    def Irány(self):
        return self.__Irány
    @Irány.setter
    def Irány(self,irány):
        if isinstance(irány,int):
            self.__Irány = irány % (Hajo.__MAXSEB + 1)
        else:
            print("Nem egész")
        
    @property
    def Sebesség(self):
        return self.__Sebesség
    @Sebesség.setter
    def Sebesség(self,seb):
        if isinstance(seb,str):
            print("Nem szám")
        else:
            if seb < Hajo.__MINSEB:
                self.__Sebesség = Hajo.__MINSEB
            elif seb > Hajo.__MAXSEB:
                self.__Sebesség = Hajo.__MAXSEB
            else:
                self.__Sebesség = seb
                
    @property
    def Db(self):
        return self.__Db
    
    def Kiír(self):
        print("A hajó neve",self.Név,"A hajó iránya", self.Irány)
        
    def Jobbra(self,irány=1):
        self.Irány += irány
            
        
#főprogram
Hajó1 = Hajo()
Hajó2 = Hajo("Kuka",23,12)
print(Hajó2.Név)
Hajó2.Név="Kiscica"
print(Hajó2.Név)
Hajó2.Irány = 200
print(Hajó2.Irány)


Hajó2.Kiír
            
            
            
            
            