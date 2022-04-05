import math

class IntHalmaz:
    def __init__(self):
        self.__db=0
        self.__kezd=[]
        self.__veg=[]
        
    def Beolvasas(self):
        print("Hány db intervallumbol áll a halmaz")
        self.__db=int(input())
        for i in range(self.__db):
            print("ird be az intervallum kezdot")
            self.__kezd.append(int(input()))
            print("ird a veget ide")
            self.__veg.append(int(input()))
            
    def Kiir(self):
        for i in range(self.__db):
            print("[ ",self.__kezd[i]," - ",self.__veg[i]," ]")
            
    def Eleme(self,elem):
        e = 0 #elso index
        u = self.__db-1 #utso index
        k = (e+u)//2
        while e<=u and (elem < self.__kezd[k] or elem>self.__veg[k]):
            if elem < self.__kezd[k]:
                u=k-1
            else:
                e=k+1
            k=(e+u)//2
        return e<=u
    
    def Resze(self,a,b):
        e = 0 #elso index
        u = self.__db-1 #utso index
        k = (e+u)//2
        while e<=u and (b < self.__kezd[k] or a > self.__veg[k]):
            if a < self.__kezd[k]:
                u=k-1
            else:
                e=k+1
            k=(e+u)//2
        return e<=u and a>= self.__kezd[k] and b<= self.__veg[k]
    
    
    def Metszet(self,masikH):
        metszeth=IntHalmaz()
        i=0
        j=0
        k=0
        while i<self.__db and j<masikH.__db:
            if self.__veg[i]<masikH.__kezd[j]:
                i+=1
            elif masikH.__veg[j]<self.__kezd[i]:
                j+=1
            else:
                k+=1
                metszeth.__kezd.append(max(self.__kezd[i],masikH.__kezd[j]))
                metszeth.__veg.append(min(self.__veg[i],masikH.__veg[j]))
                if self.__veg[i]<self.__veg[j]:
                    i+=1
                elif self.__veg[i]>self.__veg[j]:
                    j+=1
                else:
                    j+=1
                    i+=1
        metszeth.__db=k
        return metszeth
    
    def Unio(self,masikH):
        i=0
        j=0
        k=0
        unioh=IntHalmaz()
        self.__kezd.append(math.inf)
        self.__veg.append(math.inf)
        masikH.__kezd.append(math.inf)
        masikH.__veg.append(math.inf)
        unioh.__kezd.append(min(self.__kezd[i],masikH.__kezd[j]))
        while i<self.__db+1 and j<masikH.__db+1:
            if self.__veg[i] < masikH.__kezd[j]:
                unioh.__veg.append(self.__veg[i])
                i+=1
                k+=1
                unioh.__kezd.append(min(self.__kezd[i],masikH.__kezd[j]))
            elif self.__veg[i] > masikH.__kezd[j]:
                unioh.__veg.append(masikH.__veg[i])
                j+=1
                k+=1
                unioh.__kezd.append(min(self.__kezd[i],masikH.__kezd[j]))
            elif self.__veg[i] < masikH.__veg[j]:
                i+=1
            elif self.__veg[i] > masikH.__veg[j]:
                j+=1
            else:
                unioh.__veg.append(masikH.__veg[j])
                i+=1
                j+=1
                k+=1
                if i<self.__db+1 and j<self.__db+1:
                    unioh.__kezd.append(min(self.__kezd[i],masikH.__kezd[j]))
        unioh.__db=k-1
        return unioh
                    
        
    
    
                
    
    
        