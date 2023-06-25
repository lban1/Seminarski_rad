class Narucitelj:
    def __init__(self, ime, prezime, tel, email, id_dob, id_luk):
        self.__ime = ime
        self.__prezime = prezime
        self.__tel = tel
        self.__email = email
        self.__id_dob = id_dob
        self.__id_luk = id_luk

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, tel):
        self.__tel = tel

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def id_dob(self):
        return self.__id_dob

    @id_dob.setter
    def id_dob(self, id_dob):
        self.__id_dob = id_dob

    @property
    def id_luk(self):
        return self.__id_luk

    @id_luk.setter
    def id_luk(self, id_luk):
        self.__id_luk = id_luk

    def ispis(self):
        print("Informacije o narucitelju: ")
        print(f'\tIme: {self.__ime}')
        print(f'\tPrezime: {self.__prezime}')
        print(f'\tTelefon: {self.__tel}')
        print(f'\tE-mail: {self.__email}')
        print(f'\tDob: {self.__id_dob}')
        print(f'\tVrsta luka: {self.__id_luk}')