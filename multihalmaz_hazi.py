class Darabszam:
    def __init__(self):
        self.__elemek=[]
        for i in range(10):
            self.__elemek.append(0)
    
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
        for i in range(10):
            self.__elemek.append(0)
        
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
    
    def Resze(self, masikH): # csak akkor igaz, ha minden eleme a masikH-nak benne van az eredetiben
        i=0
        while i < len(self.__elemek) and masikH.Benne({ "ertek": i, "multi": self.__elemek[i]}):
            i+=1
        return i >= len(self.__elemek)
    
    def Unio(self, masikH):
        unioh=Darabszam()
        for i in range(len(self.__elemek)):
            unioh.__elemek[i]=self.__elemek[i]
        for i in range(len(masikH.__elemek)):
            unioh.__elemek[i]+=masikH.__elemek[i]
        return unioh
    
    def __add__(self,masikH):
        unioh=Darabszam()
        for i in range(len(self.__elemek)):
            unioh.__elemek[i]=self.__elemek[i]
        for i in range(len(masikH.__elemek)):
            unioh.__elemek[i]+=masikH.__elemek[i]
        return unioh
    
    def Metszet(self, masikH):
        metszeth=Darabszam()
        for i in range(len(self.__elemek)):
            if self.__elemek[i]>0 and masikH.__elemek[i]>0:
                metszeth.__elemek[i]=min(self.__elemek[i],masikH.__elemek[i])
        return metszeth
    
    def __mul__(self,masikH):
        metszeth=Darabszam()
        for i in range(len(self.__elemek)):
            if self.__elemek[i]>0 and masikH.__elemek[i]>0:
                metszeth.__elemek[i]=min(self.__elemek[i],masikH.__elemek[i])
        return metszeth
    
    def Kulonbseg(self, masikH):
        kulonh=Darabszam()
        for i in range(len(self.__elemek)):
            if self.__elemek[i]>0 and masikH.__elemek[i]>0:
                if (self.__elemek[i] - masikH.__elemek[i])>0:
                    kulonh.__elemek[i]=self.__elemek[i] - masikH.__elemek[i]
                else:
                    kulonh.__elemek[i]=0
        return kulonh
    
    def Maximum(self, masikH):
        maxh=Darabszam()
        for i in range(len(self.__elemek)):
            if self.__elemek[i]>0 and masikH.__elemek[i]>0:
                maxh.__elemek[i]=max(self.__elemek[i],masikH.__elemek[i])
        return maxh

        
                    
            
        
#ures, ures_e, Multihalmazbol, Multihalmazba, Eleme, Multiplicitas, Benne, Resze, Unio, Metszet, Kulonbseg, Maximum           
    
    
    
db=Darabszam()
db.Beolvasas()
#print(db.Ures_e())
#db.Ures()
#db.Multihalmazba(1)
#db.Multihalmazbol(1)
#print(db.Eleme(0))
#print(db.Eleme(1))
# print(db.Multiplicitas(0))
# print(db.Multiplicitas(1))
# print("Benne")
# print(db.Benne({ "ertek": 0, "multi": 3}))
# print(db.Benne({ "ertek": 0, "multi": 2}))
proba=Darabszam()
proba.Beolvasas()
# print("rezse")
# print(db.Resze(proba))
# print(db.Resze(proba))
print("unio")
db.Unio(proba).Kiir()
(db+proba).Kiir()
print("metszet")
db.Metszet(proba).Kiir()
(db*proba).Kiir()
# print("Kulonbseg")
# db.Kulonbseg(proba).Kiir()
# print("maximum")
# db.Maximum(proba).Kiir()

print("vegso kiir")
db.Kiir()

