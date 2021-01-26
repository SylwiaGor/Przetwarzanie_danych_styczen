from crud import add_princess, show_sala_bankietowa, eat_princess, add_dragon
from database import Session

princesses = [
    ["Urszula", True, 45, 56],
    ["Krystyna", False, 5, 166],
    ["Izabela", True, 283, 288],
]

dragons = [
    [45, 56],
    [15, 23],
]

session = Session()

for princess in princesses:
    add_princess(session=session,
        imie=princess[0],
        czy_dziewica=princess[1],
        szerokosc=princess[2],
        wysokosc=princess[3]
    )

for dragon in dragons:
    add_dragon(
        session=session,
        szerokosc=dragon[0],
        wysokosc=dragon[1]
    )

eat_princess(session)

for ksiezniczka in show_sala_bankietowa(session):
    print(
        f"Księżniczka {ksiezniczka.imie},"
        f" dziewica: {ksiezniczka.czy_dziewica}"
    )
