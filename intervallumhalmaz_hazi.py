class nemDiszjunkt:
    def __init__(self):
        self.__db=0
        self.__kezd=[]
        self.__veg=[]
        self.__gyakorisag=[]
        
    def Beolvasas(self):
        print("Hény intervallum lesz")
        N=int(input())
        for i in range(N):
            print("Az intervallumot add meg")
            adatsor=input().split()
            self.__kezd.append(int(adatsor[0]))
            self.__veg.append(int(adatsor[1]))
        print(self.__kezd)
        print(self.__veg)
        for j in range(min(self.__kezd),max(self.__veg)+1):
            self.__gyakorisag.append(0)
        print(self.__gyakorisag)
        for z in range(N):
            for k in range(self.__kezd[z],(self.__veg[z]+1)):
                print(k)
                self.__gyakorisag[k-min(self.__kezd)]+=1
                
    def NemTartozikBele(self,a,b):
        xtomb=[]
        db=0
        for i in range(a,b+1):
            if self.__gyakorisag[i]==0:
                db+=1
                xtomb.append(i)
        return xtomb
    
    def Kiir(self):
        for i in self.__kezd:
            print(i)
        print("veg")
        for i in self.__veg:
            print(i)
        print("gyakorisag")
        for i in self.__gyakorisag:
            print(i)
    
    def Metszet(self):
        metszeth.nemDiszjunkt()
        van=False
        i=min(self.__kezd)
        self.__gyakorisag[max(self.__veg)]=-1
        while i<=max(self.__veg) and self.__gyakorisag[i]!=len(self.__kezd):
            i+=1
        if i<=max(self.__veg):
            metszeth.__kezd=i
            van=True
            while self.__gyakorisag[i+1]==len(self.__kezd):
                i+=1
            metszeth.__veg=i
        return meszeth
            
            
    def Unio(self):
        unioh=nemDiszjunkt()
        self.__gyakorisag.insert(0,0)
        self.__gyakorisag.append(0)
        k=0
        for i in range(len(self.__gyakorisag)-1):
            if self.__gyakorisag[i-1]==0 and self.__gyakorisag[i]>0:
                k+=1
                unioh.__kezd.append(i)
            if self.__gyakorisag[i+1]==0 and self.__gyakorisag[i]>0:
                unioh.__veg.append(i)
                
        return unioh
        
    def db_int_resze(self,db):
        db_int.nemDiszjunkt()
        self.__gyakorisag.insert(0,-1)
        self.__gyakorisag[len(self.__gyakorisag)]=-1
        k=0
        for i in range(min(self.__kezd),max(self.__veg)+1):
            if self.__gyakorisag[i-1]!=db and self.__gyakorisag[i]==db:
                k+=1
                db_int.__kezd.append(i)
            if self.__gyakorisag[i+1]!=db and self.__gyakorisag[i]==db:
                db_int.__veg.append(i)
        return db_int
                    
                    
                    
                    
halmaz=nemDiszjunkt()
halmaz.Beolvasas()
halmaz.Kiir()
print(halmaz.NemTartozikBele(2,5))
halmaz.Unio().Kiir()


                    
                    
            
          
        
        
            
        