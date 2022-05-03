# Lambda - meccsek
def befilenyit():
    hiba = True
    while hiba:
        try:
            print("Írd be a bemeneti fájl nevét!")
            filenév = "meccsek.txt" # input()
            befile = open(filenév,"rt",encoding="utf-8")
            hiba = False
        except:
            print("Nem létező fájlnevet adtál meg!")
    print("A bemeneti fájl (",filenév,") sikeresen megnyílt")
    return (befile,filenév)

def txt_fileolvas_listába(befile):
    #sor = befile.readline().strip() # Fejsor ki
    sor = befile.readline().strip() # Első valódi adat
    cellahatároló = "\t"
    lista = []
    while sor != "":
        sorlista = sor.split(cellahatároló)
        adat = {}
        adat = { "ford": int(sorlista[0]),
                 "hcsapat": sorlista[1],
                 "vcsapat": sorlista[2],
                 "hgól": int(sorlista[3]),
                 "vgól": int(sorlista[4])}
        # print(adat)
        lista.append(adat)
        sor = befile.readline().strip()
    befile.close()
    return lista

def Golszazalek(lista):
    gol_szazalek = sum([meccs["hgól"] + meccs["vgól"] > 0 for meccs in lista])/len(lista)*100
    return gol_szazalek

def Legtobbgolos(lista):
    legtobbgol=max(lista,key=lambda gol: gol["hgól"]+gol["vgól"])
    print(legtobbgol)
    
def Statisztika(tabella,aktford,ford,csapat,rgól,kgól):
    
    
def bonyolult(lista):
    maxford=max(lista,key=lambda ford: ford["ford"])["ford"]
    aktford=int(input("adjad: "))
    tabella={meccs["hcsapat"]: {"rgól": 0, "kgól": 0, "pont": 0} for meccs in lista}
    
    return tabella

        

#Főprogram
(befile,befilenév) = befilenyit()
meccslista = txt_fileolvas_listába(befile)
print(Golszazalek(meccslista))
Legtobbgolos(meccslista)
print(bonyolult(meccslista))
