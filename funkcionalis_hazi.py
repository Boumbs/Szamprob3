def befilenyit():
    hiba = True
    while hiba:
        try:
            print("Írd be a bemeneti fájl nevét!")
            filenév = "vásárlás.csv" # input()
            befile = open(filenév,"rt",encoding="utf-8")
            hiba = False
        except:
            print("Nem létező fájlnevet adtál meg!")
    print("A bemeneti fájl (",filenév,") sikeresen megnyílt")
    return (befile,filenév)

def csv_fileolvas_listába(befile):
    sor = befile.readline().strip() # Fejsor ki
    sor = befile.readline().strip() # Első valódi adat
    cellahatároló = ";"
    lista = []
    while sor != "":
        sorlista = sor.split(cellahatároló)
        adat = {}
        adat = { "Név": sorlista[0],
                 "Születés": int(sorlista[1]),
                 "Város": sorlista[2],
                 "Játék": sorlista[3],
                 "Szín": sorlista[4],
                 "Ár": int(sorlista[5])}
        # print(adat)
        lista.append(adat)
        sor = befile.readline().strip()
    befile.close()
    return lista

def Labda(lista):
    db = sum([elem["Játék"]=="labda" for elem in lista])
    print(db)
    
def LabdaAr(lista):
    ar = sum([elem["Ár"] for elem in lista if elem["Játék"]=="labda"])
    print(ar)
    
def IbolyaKukas(lista):
    ibolyakukas = [elem for elem in lista if (elem["Játék"]=="kukásautó" and elem["Szín"]=="ibolya")]
    print(ibolyakukas)
    
def Jatekonkent(lista):
    jatekok = {elem["Játék"]: {"db": 0, "osszar": 0} for elem in lista}
    
    for jatek in lista:
        jatekok[jatek["Játék"]]["db"] += 1
        jatekok[jatek["Játék"]]["osszar"] += jatek["Ár"]
    for elem, adat in jatekok.items():
        print(elem, adat["db"],adat["osszar"])

def Fiatal(lista):
    fiatal = max([elem["Születés"] for elem in lista])
    print(fiatal)
    print([elem for elem in lista if elem["Születés"]==fiatal])
    fiatal2 = max(9,7)
    print(fiatal2)

(befile,filenev)=befilenyit()
lista=csv_fileolvas_listába(befile)
Labda(lista)
LabdaAr(lista)
IbolyaKukas(lista)
print("Masik")
Jatekonkent(lista)
Fiatal(lista) 