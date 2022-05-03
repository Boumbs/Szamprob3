from tinydb import TinyDB, Query, where

def befilenyit():
    hiba = True
    while hiba:
        try:
            print("Írd be a bemeneti fájl nevét!")
            filenév = "autok.csv"
            befile = open(filenév,"rt",encoding="utf-8")
            hiba = False
        except:
            print("Nem létező fájlnevet adtál meg!")
    print("A bemeneti fájl (",filenév,") sikeresen megnyílt")
    return (befile,filenév)

def csv_file_adatbázisba(befile):
    ab = TinyDB("vásárlás.json")
    sor = befile.readline().strip() # Fejsor ki
    sor = befile.readline().strip() # Első valódi adat
    cellahatároló = ";"
    while sor != "":
        sorlista = sor.split(cellahatároló)
        adat = {}
        adat = { "név": sorlista[0],
                 "szülév": int(sorlista[1]),
                 "város": sorlista[2],
                 "játék": sorlista[3],
                 "szín": sorlista[4],
                 "ár": int(sorlista[5])}
        ab.insert(adat)
        sor = befile.readline().strip()
    befile.close()
    return ab

def csv_autok(befile):
    ab = TinyDB("autok.json")
    sor = befile.readline().strip() # Fejsor ki
    sor = befile.readline().strip() # Első valódi adat
    cellahatároló = ";"
    while sor != "":
        sorlista = sor.split(cellahatároló)
        adat = {}
        adat = { "telepules": sorlista[0],
                 "tulajdonos": int(sorlista[1]),
                 "marka": sorlista[2],
                 "orszag": sorlista[3],
                 "evjarat": int(sorlista[4]),
                 "kivitel": sorlista[5],
                 "hengertartalom": int(sorlista[6]),
                 "ar": int(sorlista[7])}
        ab.insert(adat)
        sor = befile.readline().strip()
    befile.close()
    return ab

        

def Lekérdez(adatbázis):
    info = Query()
#     kvincék = adatbázis.search(where("név") == "Kovács Vince")
#     print(kvincék)
#     adatbázis.update({"játék": "roller"}, info.név == "Kovács Vince")
#     kvincék = adatbázis.search(where("név") == "Kovács Vince")
#     print(kvincék)
#     kvincék = adatbázis.remove(info.név=="Kovács Vince")
#     kvincék = adatbázis.search(where("név") == "Kovács Vince")
#     print(kvincék)
#     bvelkezd=adatbázis.search(info.Név[1]=='o')
#     print(bvelkezd)
#     bennevan=lambda érték, keresNév: keresNév in érték
#     vince = adatbázis.search(info.név.test(bennevan,"Vince"))
#     print(vince)
#     bennevan=lambda érték, keresNév: érték[-5:]==keresNév
#     vince = adatbázis.search(info.név.test(bennevan,"Vince"))
#     print(vince)
#     ibolyavagykukas = adatbázis.search((info.játék=="kukásautó") | (info.szín=="ibolya"))
#     print(ibolyavagykukas)
    ibolyavagykukaskeres = adatbázis.get((info.játék=="kukásautó") | (info.szín=="ibolya"))
    print(ibolyavagykukaskeres)
    ibolyavagykukasvane = adatbázis.contains((info.játék=="kukásautó") | (info.szín=="ibolya"))
    print(ibolyavagykukasvane)
    db = adatbázis.count((info.játék=="kukásautó") | (info.szín=="ibolya"))
    print(db)
    tábla = adatbázis.table("Autók")
    tábla.insert({"márka": "Ford", "Típus": "Mustang", "év": 1987})
    tábla.insert_multiple([{"márka": "Volvo", "Típus": "V80", "év": 1995},
                           {"márka": "Trabant", "Típus": "1.1", "év": 1960},
                           {"márka": "Tesla", "Típus": "Model S", "év": 2015}])
    print(tábla.all())
    for i in tábla:
        print(i)
    return tábla

def Autok(adatbázis):
    info = Query()
    usa = adatbázis.search(info.orszag=="USA")
    print(usa)
    
    lada=adatbázis.search(info.marka=="Lada")
    print(lada)
    print(sum([a["ar"] for a in lada])/len(lada))
    
    orosz=adatbázis.search((info.orszag=="Oroszország") & (info.ar < 9000000))
    print(orosz)
    
    vanmagyar=lambda ertek, keresNev: keresNev in ertek
    magyar=adatbázis.contains(info.orszag.test(vanmagyar,"Magyar"))
    print(magyar)
    
    japan=adatbázis.search((info.orszag=="Japán") & (info.evjarat>=2000) & (info.evjarat<=2010))
    ertek=sum([elem["ar"] for elem in japan])
    print(ertek)
    
        
#     print(ladaar)
        
    
    
    
# Főprogram
(befile,befilenév) = befilenyit()
#adatbázis = csv_file_adatbázisba(befile)
#tábla=Lekérdez(adatbázis)
adatbázis =csv_autok(befile)
# for rekord in adatbázis:
#     print(rekord)
Autok(adatbázis)

adatbázis.truncate()
#tábla.truncate()

