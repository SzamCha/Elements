import time

elements = []
dico = []

def loadElements():
    with open("elements.txt","r") as f:
        lines = f.readlines()
        for l in lines:
            elements.append(l.strip())

def loadMots():
    with open("dico.txt","r") as f:
        lines = f.readlines()
        for l in lines:
            dico.append(l.strip())


def writeCandidats():
    with open("candidats.txt","w") as f:
        for m in motsok:
            f.write(m+"\n")

def match(mot,motconcat,nb):
    if mot.lower() == motconcat.lower():
        if not motconcat in motsok:
            motsok.append(motconcat)
        return True
    elif nb == 1:
        l = mot[len(motconcat)].upper()
        try:
            p = elements.index(l)
            return match(mot, motconcat+elements[p],1) or match(mot, motconcat+elements[p],2)
        except:
            return False
    else:
        try:
            l = mot[len(motconcat)].upper()+mot[len(motconcat)+1].lower()
            p = elements.index(l)
            return match(mot, motconcat+elements[p],1) or match(mot, motconcat+elements[p],2)
        except:
            return False



loadElements()
elements.sort()
print(elements)
loadMots()
dico.sort()
print(len(dico))
nombre=0
motsok = []
monmot = ""
tps1 = time.perf_counter()

for mots in dico:
    if (match(mots,"",1) or match(mots,"",2)):
        #print(mots,"OK")
        nombre += 1
    #else:
     #   print(mots,"non")
tps2 = time.perf_counter()
print(motsok)
print(len(motsok),"en",tps2-tps1,"secondes")
writeCandidats()
