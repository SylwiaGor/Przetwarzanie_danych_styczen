from sqlalchemy import func

from models import Ksiezniczki, Smoki


def add_princess(session, imie, czy_dziewica, szerokosc, wysokosc):
    new_princess = Ksiezniczki(
        imie=imie,
        czy_dziewica=czy_dziewica,
        szerokosc=szerokosc,
        wysokosc=wysokosc
    )
    session.add(new_princess)
    session.commit()

    #po wpisaniu comit operacja zostanie wykonana = ksiezniczka zostanie dodana

def show_sala_bankietowa(session):
    return session.query(Ksiezniczki)

def add_dragon(session, szerokosc, wysokosc):
    dragon = Smoki(
        szerokosc=szerokosc,
        wysokosc=wysokosc
    )
    session.add(dragon)
    session.commit()

def eat_princess(session):
    smoki = session.query(Smoki).all()

    for smok in smoki:
        szerokosc = smok.szerokosc
        wysokosc = smok.wysokosc


        eatable_princess = (
            session.query(Ksiezniczki, Smoki)
            .filter(Ksiezniczki.czy_dziewica == True)
            .filter(func.abs(Ksiezniczki.szerokosc - szerokosc) < 25)
            .filter(func.abs(Ksiezniczki.wysokosc - wysokosc) < 25)
        )

    for princess in eatable_princess:
        session.delete(princess)

    session.commit()

if __name__ == '__main__':
    from database import Session
    session = Session()
    for ksiezniczka in show_sala_bankietowa(session):
        print(ksiezniczka.imie)
