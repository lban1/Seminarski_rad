from datetime import date
from iznimke import IznimkaPrazanTekst, IznimkaTelefon

def unos_pozitivnog_cijelog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))
            if broj < 0:
                raise Exception('Morate upisati cijeli pozitivni broj!')
        except ValueError:
            print('Morate upisati cijeli broj!')
        except Exception as ex:
            print(ex)
        else:
            return broj

def unos_pozitivnog_realnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati pozitivan realni broj')
        except ValueError:
            print('Morate upisati realni broj!')
        except Exception as ex:
            print(ex)
        else:
            return broj

def unos_datuma():
    while True:
        try:
            dan = provjera_datuma('dan', 1, 31)
            mjesec = provjera_datuma('mjesec', 1, 12)
            godina = unos_pozitivnog_cijelog_broja('Unesite godinu isteka prodaje: ')
            datum = date(godina,mjesec,dan)
        except ValueError as ve:
            print(ve)
        else:
            return datum

def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f'Unesite cijeli broj unutar intervala {min}-{max}: '))
            if broj < min or broj > max:
                raise Exception(f'Unesite broj unutar intervala {min}-{max}!')
        except ValueError:
            print('Morate unesti cijeli broj!')
        except Exception as ex:
            print(ex)
        else:
            return broj

def provjera_datuma(rijec, min, max):
    while True:
        try:
            broj = int(input(f'Unesite {rijec} isteka oglasa: '))
            if broj < min or broj > max:
                raise Exception(f'Unesite broj unutar intervala {min}-{max}!')
        except ValueError:
            print('Morate unesti cijeli broj!')
        except Exception as ex:
            print(ex)
        else:
            return broj

def unos_telefona(poruka):
    while True:
        try:
            broj = str(unos_pozitivnog_cijelog_broja(poruka))

            if len(broj) != 8:
                raise Exception(f"Broj telefona mora imati 8 znamenaka!")

        except Exception as e:
            print(e)
        else:
            return broj

def provjera_korisnickog_unosa(ime, prezime, tel, email):
    while True:
        try:
            if len(ime) == 0 or len(prezime) == 0 or len(tel) == 0 or len(email) == 0:
                raise IznimkaPrazanTekst()
            elif len(str(tel)) != 8:
                raise IznimkaTelefon()
            int(tel)

        except IznimkaPrazanTekst as ipt:
            return str(ipt)

        except IznimkaTelefon as it:
            return str(it)

        except ValueError:
            return ('Telefon mora biti broj!')

        else:
            return None