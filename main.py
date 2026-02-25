import random

class Domanda:
    def __init__(self, livello: int, risposte: list, giusta: str,domanda:str):
        self.livello = livello
        self.risposte = risposte
        self.giusta = giusta
        self.domanda = domanda
        random.shuffle(self.risposte)
    def completa(self):
        stringa = self.domanda
        cont = 1
        for r in self.risposte:
            stringa += str(cont) + ") " + r
            cont += 1
        return stringa

with open('domande.txt', 'r', encoding="utf-8") as file:
    righe = file.readlines()

domande = list()
temp = list()

for r in righe:
    if r != "\n":
        temp.append(r)
    else:
        domande.append(Domanda(int(temp[1]), temp[2:], temp[2] , temp[0]))
        temp = []

domande.sort(key=lambda x: x.livello)

#crea giochino del cazzo

lvl = 0
gioco = True
punteggio = 0
while gioco == True:  #partita gioco
    domandeLivello = [d for d in domande if d.livello == lvl]
    if len(domandeLivello) == 0: #copre tutti i casi anche quelli in cui la lista è vuota --> livello > 4
        gioco = False
    else:
        d = random.choice(domandeLivello)
        print(f"Domanda di livello {lvl}: {d.completa()}")
        risp = int(input("Inserisci il numero della risposta corretta:"))
        while risp < 0 or risp >4:
            risp = int(input("Inserisci numero valido per la risposta, da 1 a 4 compresi:"))
        rispUtente = d.risposte[risp - 1]
        if rispUtente != d.giusta:
            print(f"Risposta errata, la risposta corretta era {d.giusta}")
            gioco = False
        elif rispUtente == d.giusta:
            lvl += 1
            punteggio += 1
            print(f"Risposta corretta, passiamo al livello {lvl}" + "\n")


utente = input("Inserisci il tuo username: ")

with open('punti.txt', 'r', encoding="utf-8") as file: #apro in lettura
    righe = file.readlines() #ogni riga è utente-punteggio
    dizUtenti = dict()
    for r in righe:
        dizUtenti[r.split(" ")[0]] = int(r.split(" ")[1])
    if utente in dizUtenti:
        dizUtenti[utente] += punteggio

    else:
        dizUtenti[utente] = punteggio
    dizOrdinato = dict(sorted(dizUtenti.items(), key=lambda x: x[1], reverse=True)) #ordina per punteggio

with open('punti.txt', 'w', encoding="utf-8") as f: #apro in scrittura
    for u in dizOrdinato: #ciclo utente in dizioinario
        f.write(f"{u} {dizOrdinato[u]}\n")



