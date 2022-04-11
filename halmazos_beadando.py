class Programnyelvek:
    def __init__(self):
        self.__n=0
        self.__m=0
        self.__nyelvek=[]
        self.__valasztottNyelvek=[]
        
    def Beolvasas(self):
        adatsor=input().split()
        self.__n=int(adatsor[0])
        self.__m=int(adatsor[1])
        for i in range(self.__n):
            self.__nyelvek.append(input())
        for j in range(self.__m):
            self.__valasztottNyelvek.append(input())
            
    def Kiiras(self):
        print(self.__n)
        print(self.__m)
        for i in self.__nyelvek:
            print(i)
        print("\n")
        for j in self.__valasztottNyelvek:
            print(j)
            
    def valasztottNyelvekKulonbseg(self):
        db=0
        tiltottNyelvek=[]
        for i in range(self.__m):
            if not (self.__valasztottNyelvek[i] in self.__nyelvek):
                db+=1
                tiltottNyelvek.append(i+1)
        print(db, end=' ')
        for i in range(len(tiltottNyelvek)-1):
            print(tiltottNyelvek[i],end=', ')
        print(tiltottNyelvek[-1])
        
    
    def erdektelenNyelvek(self):
        db=0
        erdektelenNyelvek=[]
        for i in range(self.__n):
            if not (self.__nyelvek[i] in self.__valasztottNyelvek):
                db+=1
                erdektelenNyelvek.append(self.__nyelvek[i])
        if db!=0:
            print(db, end=' ')
            for i in range(db-1):
                print(erdektelenNyelvek[i],end=', ')
            print(erdektelenNyelvek[len(erdektelenNyelvek)-1])
        else:
            print(db)
    
    def NyelvGyakorisag(self):
        nyelvGyak=[]
        for i in self.__valasztottNyelvek:
            if i in self.__nyelvek:
                if len(nyelvGyak)==0:
                    nyelvGyak.append({"nev":i,"db":1})
                else:
                    j=0
                    while j<len(nyelvGyak) and nyelvGyak[j]["nev"]!=i:
                        j+=1
                    if j<len(nyelvGyak):
                        nyelvGyak[j]["db"]+=1
                    else:
                        nyelvGyak.append({"nev":i,"db":1})
        for i in range(len(nyelvGyak)-1):
            print(nyelvGyak[i]["nev"],nyelvGyak[i]["db"],sep=":",end=",")
        print(nyelvGyak[-1]["nev"],nyelvGyak[-1]["db"],sep=":")
                        
                        
     
                    
                    
        
            
                
            
nyelv=Programnyelvek()
nyelv.Beolvasas()
#print("A")
nyelv.valasztottNyelvekKulonbseg()
#print("B")
nyelv.erdektelenNyelvek()
#print("C")
nyelv.NyelvGyakorisag()