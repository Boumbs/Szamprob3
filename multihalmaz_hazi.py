class Darabszam:
    def __init__(self):
        self.elemek=[]
        for i in range(10):
            self.elemek[i]=0
    
    def Beolvasas(self):
        print("Add meg hány számcsoportot szeretnél eltárolni 0-9")
        N=int(input())
        for i in range(N):
            print("Add meg mely számot 0-9 szeretnéd eltárolni és hányat")
            adatsor=input().split()
            self.__elemek[int(adatsor[0])]=int(adatsor[1])
            
    def Kiir(self):
        for i in range(len(self.__elemek)):
            print(self.__elemek[i])

    def Ures_e(self):
        return len(self.__elemek)==0
    
    def Ures(self):
        self.__elemek=[]
        
    def Multihalmazba(self,elem):
        self.__elemek[elem]+=1
        
    def Multihalmazbol(self,elem):
        if self.__elemek[elem]==0:
            pass
        else:
            self.__elemek[elem]-=1
            
    def Eleme(self,elem):
        return self.__elemek[elem]>0
    
    def Multiplicitas(self,elem):
        if self.Eleme(elem):
            return self.__elemek[elem]
        else:
            return 0
        
    def Benne(self,multiElem):
        return self.__elemek[multiElem["ertek"]]==multiElem["multi"]
    
    def Resze(self, masikH):
         i=0
        while i < len(self.__elemek) and masikH.Benne({ "ertek": i, "multi": self.__elemek[i]}):
            i+=1
        return i >= len(self.__elemek)
    
    def Unio(self, masikH):
        
    
    
    
    
    