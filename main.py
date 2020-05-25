# maak hier de hele enigma machine in python :D
alfabet = "abcdefghijklmnopqrstuvwxyz"

#Dit wordt dus de input later
TeVertalenString = "abc"

#De TeVertalenString wordt een list:
TeVertalenLijst = [char for char in TeVertalenString.lower()]

#functie voor het draaien van een rotor
def RotorDraai(draaiingen, rotor):
  rotor = (rotor.lettervolgorde[-draaiingen:] + rotor.lettervolgorde)[0: 26]
  return rotor


class Rotor:
  def __init__(self, nummer, lettervolgorde, beginstand, draaiingensindsbegin):
    self.nummer = nummer
    self.beginstand = beginstand
    self.draaiingensindsbegin = draaiingensindsbegin
    self.lettervolgorde = lettervolgorde


#Rotor 1 wordt aangemaakt met de class. Nummer van rotor, beginwaarde = het alfabet, beginwaarde kan worden ingevoerd. Dus hier met beginwaarde 2 , 0, 0
rotor1 = Rotor(1, alfabet, 0, 0)
rotor2 = Rotor(2, alfabet, 0, 0)
rotor3 = Rotor(3, alfabet, 0, 0)

print("rotor1 lettervolgorde: " + str(rotor1.lettervolgorde))
print("rotor2 lettervolgorde: " + str(rotor2.lettervolgorde))

#draai rotor1 één keer
rotor1.lettervolgorde = RotorDraai(24, rotor1)
rotor1.beginstand += 24
rotor2.lettervolgorde = RotorDraai(3, rotor2)
rotor2.beginstand += 3
rotor3.lettervolgorde = RotorDraai(4, rotor3)
rotor3.beginstand += 4

VertaaldeTekst = []
for x in TeVertalenLijst:
  x = rotor1.lettervolgorde[alfabet.index(x)]
  x = rotor2.lettervolgorde[alfabet.index(x)]
  x = rotor3.lettervolgorde[alfabet.index(x)]
  x = alfabet[::-1][alfabet.index(x)]
  x = rotor3.lettervolgorde[alfabet.index(x)]
  x = rotor2.lettervolgorde[alfabet.index(x)]
  x = rotor1.lettervolgorde[alfabet.index(x)]
  VertaaldeTekst.append(x)
  rotor1.lettervolgorde = RotorDraai(1, rotor1)
  rotor1.beginstand += 1
  if rotor1.beginstand % 26 == 0:
    rotor2.lettervolgorde = RotorDraai(1, rotor2)
    rotor2.beginstand += 1
  print("Rotor1 " + str(rotor1.beginstand))
  print("Rotor2 " + str(rotor2.beginstand))
print(VertaaldeTekst)