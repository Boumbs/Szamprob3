from tinydb import TinyDB, Query, where

def befilenyit():
    hiba = True
    while hiba:
        try:
            print("Írd be a bemeneti fájl nevét!")
            filenév = "lakasok.csv"
            befile = open(filenév,"rt",encoding="utf-8")
            hiba = False
        except:
            print("Nem létező fájlnevet adtál meg!")
    print("A bemeneti fájl sikeresen megnyílt")
    return (befile,filenév)

def csv_file_adatbázisba(befile):
    ab = TinyDB("lakasok.json")
    sor = befile.readline().strip()
    sor = befile.readline().strip()
    cellahatároló = ";"
    while sor != "":
        sorlista = sor.split(cellahatároló)
        adat = {}
        if sorlista[3]=="fsz" or sorlista[3]=="mfsz":
            sorlista[3]=0
        adat = { "kerulet": int(sorlista[0]),
                 "hely": sorlista[1],
                 "ar": float(sorlista[2]),
                 "emelet": int(sorlista[3]),
                 "nagysag": int(sorlista[4]),
                 "szobak": int(sorlista[5]),
                 "felszobak": sorlista[6]}
        ab.insert(adat)
        sor = befile.readline().strip()
    befile.close()
    return ab

def Lekerdezes(adatbazis):
    info=Query()
    draga=adatbazis.search((info.kerulet==8) & (info.ar>=20.0))
    atlag=sum([elem["ar"] for elem in draga])/len(draga)
    print(atlag)
    lista=adatbazis.search((info.kerulet==21) & (info.szobak>2) & (info.emelet<3))
    print(lista)
    maximum=max([elem["ar"] for elem in adatbazis])
    nagyondraga=adatbazis.search(info.ar==maximum)
    print(nagyondraga[0]["kerulet"])
    kislakas=adatbazis.search((info.nagysag>=40) & (info.nagysag<=50))
    print(len(kislakas))
    vaneolyanlakas=adatbazis.contains((info.kerulet==11) & (info.ar<20))
    print(vaneolyanlakas)
    
    
    

(befile,filenev)=befilenyit()
adatbazis=csv_file_adatbázisba(befile)
Lekerdezes(adatbazis)
adatbazis.truncate()

