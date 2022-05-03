#dolgozo osztaly
class Munkavallalo:
    def __init__(self):
        self._Azon = ""
        self._Nev = ""
        self._AdoAzon = ""
        self._Tipus = ""
        self._Ora = 0
        self._Bevetel = 0
    
    @property
    def Azon(self):
        return self._Azon
    Azon.setter
    def Azon(self, ujAzon):
        self._Azon = ujAzon 
        
    @property
    def Nev(self):
        return self._Nev
    Nev.setter
    def Nev(self, ujNev):
        self._Nev = ujNev 
        
    @property
    def AdoAzon(self):
        return self._AdoAzon
    AdoAzon.setter
    def AdoAzon(self, ujAdoAzon):
        self._AdoAzon = ujAdoAzon 
        
    @property
    def Tipus(self):
        return self._Tipus
    Tipus.setter
    def Tipus(self, ujTipus):
        self._Tipus = ujTipus
        
    @property
    def Ora(self):
        return self._Ora
    Ora.setter
    def Ora(self, ujOra):
        self._Ora = ujOra
        
    @property
    def Bevetel(self):
        return self._Bevetel
    
#Szellemi munkavallalok leszármaztatott osztálya
    
class Szellemi(Munkavallalo):
    def __init__(self):
        super().__init__()
        self._Fizetes = 0
        self._Tuloradij = 0
        self._Tulora = 0
        
    @property
    def Fizetes(self):
        return self._Fizetes
    Fizetes.setter
    def Fizetes(self, ujFizetes):
        self._Fizetes = ujFizetes
        
    @property
    def Tuloradij(self):
        return self._Tuloradij
    Tuloradij.setter
    def Tuloradij(self, ujTuloradij):
        self._Tuloradij = ujTuloradij
        
    @property
    def Tulora(self):
        return self._Tulora
    Tulora.setter
    def Tulora(self, ujTulora):
        self._Tulora = ujTulora
    
    def BevetelSzamol(self):
        self._Bevetel = self._Fizetes + (self._Tulora * self._Tuloradij)
        
    def Kiir(self):
        print(self._Azon,self._Nev,self._AdoAzon,self._Tipus,self._Ora,self._Bevetel,self._Fizetes,self._Tuloradij,self._Tulora)
        print(" ")
        
#Fizikai munkavallalok leszármaztatott osztálya
        
class Fizikai(Munkavallalo):
    def __init__(self):
        super().__init__()
        self._Oradij = 0
        
    @property
    def Oradij(self):
        return self._Oradij
    Oradij.setter
    def Oradij(self,ujOradij):
        self._Oradij = ujOradij
        
    def BevetelSzamol(self):
        self._Bevetel = self._Ora * self._Oradij
        
    def Kiir(self):
        print(self._Azon,self._Nev,self._AdoAzon,self._Tipus,self._Ora,self._Bevetel,self._Oradij)
        print(" ")
        
#innentől kezdve már nem az osztályhoz tartozunk
#innentől a programok fognak kovetkezni
        
def Parameter():
    paramfile = open("paraméterek.txt","rt",encoding = "utf-8")
    param = int(paramfile.readline().strip())
    print("A parameter fájl feldolgozva")
    paramfile.close()
    return param

def FeltoltListak():
    befile = open("munkatársak.txt","rt",encoding = "utf-8")
    szellemi = []
    fizikai = []
    sor = befile.readline().strip()
    
    while sor!="":
        sorlista = sor.split(";")
        if sorlista[3] == "SZ":
            szmunkas = Szellemi()
            szmunkas.Azon = sorlista[0]
            szmunkas.Nev = sorlista[1]
            szmunkas.AdoAzon = sorlista[2]
            szmunkas.Tipus = sorlista[3]
            szmunkas.Fizetes = int(sorlista[4])
            szmunkas.Tuloradij = int(sorlista[5])
            szmunkas.Kiir()
            szellemi.append(szmunkas)
        else:
            fmunkas = Fizikai()
            fmunkas.Azon = sorlista[0]
            fmunkas.Nev = sorlista[1]
            fmunkas.AdoAzon = sorlista[2]
            fmunkas.Tipus = sorlista[3]
            fmunkas.Oradij = int(sorlista[4])
            fmunkas.Kiir()
            fizikai.append(fmunkas)
        sor = befile.readline().strip(";")
    befile.close()
    print("Készen van a kiválogatás")
   
    return (szellemi,fizikai)

def OrakBe(szellemi,fizikai):
    befile = open("ledolgozottÓrák.txt","rt",encoding = "utf-8")
    sor = befile.readline().strip()
    while sor != "":
        sorlista = sor.split(";")
        if sorlista[2] == "SZ":
            i = 0
            while szellemi[i].Azon != sorlista[0]:
                i = i + 1
            szellemi[i].Ora = int(sorlista[1])
        else:
            i = 0
            while fizikai[i].Azon != sorlista[0]:
                i = i + 1
            fizikai[i].Ora = int(sorlista[1])
        sor = befile.readline().strip()
    befile.close()
    print("Beolvastuk a ledolgozott órákat")
    
    
def BevetelSzamol(szellemi,fizikai,alapora):
    for i in range(len(szellemi)):
        tulora = szellemi[i].Ora - alapora
        if tulora > 0:
            szellemi[i].Tulora = tulora
        else:
            szellemi[i].Tulora = 0
        szellemi[i].BevetelSzamol()
    for i in range(len(fizikai)):
        fizikai[i].BevetelSzamol()
    print("A bevetelek kiszamolva")
    
alapora = Parameter()
szellemi,fizikai = FeltoltListak()
OrakBe(szellemi,fizikai)
BevetelSzamol(szellemi,fizikai,alapora)
for i in range(len(szellemi)):
    szellemi[i].Kiir()
    
for i in range(len(fizikai)):
    fizikai[i].Kiir()
    
