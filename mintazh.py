class Futo:
    def __init__(self):
        self.__azonosito=[]
        self.__nev=[]
        self.__idok=[]
        self.__csucs=[]
        self.__vilagcsucs=[]
        self.__futok=[]
        
    def Befilenyit(self):
        hiba = True
        while hiba:
            try:
                print("Írd be a bemeneti fájl nevét!")
                befileFutok = open("futok.csv","rt",encoding="utf-8")
                befileIdok = open("idok.csv","rt",encoding="utf-8")
                hiba = False
            except:
                print("Nem létező fájlnevet adtál meg!")
        print("A bemeneti fájl sikeresen megnyílt")
        return befileFutok,befileIdok

    def Beolvasas(self,befileFutok,befileIdok):
        sor=befileFutok.readline().strip()
        sor=befileFutok.readline().strip()
        while sor!= "":
            sorlista=sor.split(";")
            adat = {}
            adat = {"azonosito": sorlista[0],
                   "nev": sorlista[1],
                   "idok": [],
                   "szint": "",
                   "csucs": 0 }
            self.__futok.append(adat)
            sor=befileFutok.readline().strip()
        befileFutok.close()
        sor=befileIdok.readline().strip()
        sor=befileIdok.readline().strip()
        while sor!="":
            sorlista=sor.split(";")
            i=0
            while i<len(self.__futok) and sorlista[0]!=self.__futok[i]["azonosito"]:
                i+=1
            if i<len(self.__futok):
                self.__futok[i]["idok"].append(float(sorlista[1]))
            sor=befileIdok.readline().strip()
        befileIdok.close()

    def Csucsok(self):
        for i in self.__futok:
            csucs=min(i["idok"])
            i["csucs"]=csucs
        vilagcsucs=self.__futok[0]["csucs"]
        for i in range(1,len(self.__futok)):
            if vilagcsucs>self.__futok[i]["csucs"]:
                vilagcsucs=self.__futok[i]["csucs"]
        self.__vilagcsucs=vilagcsucs
        print(self.__vilagcsucs)
        
    def Szintek(self):
        for i in self.__futok:
            if i["csucs"]>=1.7*self.__vilagcsucs:
                i["szint"]="amatőr"
            elif i["csucs"]<1.7*self.__vilagcsucs and i["csucs"]>=1.25*self.__vilagcsucs:
                i["szint"]="profi"
            elif i["csucs"]<1.25*self.__vilagcsucs and i["csucs"]>self.__vilagcsucs:
                 i["szint"]="világszínvonalú"
            else:
                i["szint"]="világcsúcstartó"
        print(self.__futok)
        
    def Vilagcsucstarto(self):
        for i in self.__futok:
            if i["csucs"]==self.__vilagcsucs:
                print("neve: ",i["nev"],", egyéni csúcsa: ",i["csucs"])
    
    def Megoszlasok(self):
        amator=0
        profi=0
        vilagszinv=0
        csucstart=0
        for i in self.__futok:
            if i["szint"]=="amatőr":
                amator+=1
            elif i["szint"]=="profi":
                profi+=1
            elif i["szint"]=="világszínvonalú":
                vilagszinv+=1
            else:
                csucstart+=1
        print("amatőr: ",amator, " fő, profi: ",profi," fő, világszínvonalú: ", vilagszinv, " fő, csúcstartó: ",csucstart," fő")
    
    def Javulok(self):
        for i in self.__futok:
            if i["idok"][-1]<i["idok"][0]:
                print("Javuló neve: ",i["nev"]," javult idő: ", round(i["idok"][0]-i["idok"][-1],2))
            
                
                
                
           
           
       
futok=Futo()
befileFutok,befileIdok=futok.Befilenyit()
futok.Beolvasas(befileFutok,befileIdok)
futok.Csucsok()
futok.Szintek()
futok.Vilagcsucstarto()
futok.Megoszlasok()
futok.Javulok()

       
        