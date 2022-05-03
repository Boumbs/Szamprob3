negyzet = lambda x: x**2
negyzet(3)
print(type(negyzet))
print(negyzet(3))
osszead = lambda x, y: x+y
print(osszead(3,4))
gyumi=[[20,"korte"],[30,"szilva"],[40,"alma"]]
print(sorted(gyumi,key=lambda x: x[1]))
adatok = [{1,2,3},{4},{5,6}]
elemszam=len(map(len,adatok))
print(elemszam) 