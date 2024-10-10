"""Matemaatilised tehted"""


# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b

# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
import math



a = float(input("Sisesta kolmnurga kaatet a: "))
b = float(input("Sisesta kolmnurga kaatet b: "))

c = (a**2 + b**2) ** 0.5
umbermoot = a + b + c
pindala = (a * b) / 2

print(f"Hüpotenuus c: {round(c, 2)}")
print(f"Kolmnurga ümbermõõt: {round(umbermoot, 2)}")
print(f"Kolmnurga pindala: {round(pindala, 2)}")
