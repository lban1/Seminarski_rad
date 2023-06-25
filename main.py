from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QMessageBox
from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import sqlite3
from utilities import provjera_korisnickog_unosa
from narucitelj import Narucitelj

narucitelji = []

con = sqlite3.connect("faksDB.db")
cur = con.cursor()

query_lukovi = """
    SELECT id, naziv FROM table_lukovi;
    """
data_lukovi = cur.execute(query_lukovi).fetchall()

query_narucitelji = """
    SELECT id, dob FROM table_dob_narucitelja;
    """
data_narucitelji = cur.execute(query_narucitelji).fetchall()


class MojProzor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Izrade lukova")
        self.setGeometry(500, 300, 700, 400)
        self.initUI()

    def initUI(self):
        self.izbornik1 = QComboBox(self)
        self.izbornik2 = QComboBox(self)
        self.font = QtGui.QFont('Areal', 10)

        for narucitelj in data_narucitelji:
            self.izbornik1.addItem(narucitelj[1])

        self.izbornik1.setGeometry(QtCore.QRect(150, 25, 150, 25))

        for luk in data_lukovi:
            self.izbornik2.addItem(luk[1])

        self.izbornik2.setGeometry(QtCore.QRect(150, 60, 150, 25))

        # Text Izbornika 1
        self.text_izbornik1 = QtWidgets.QLabel(self)
        self.text_izbornik1.setFont(self.font)
        self.text_izbornik1.setText('Dob narucitelja:')
        self.text_izbornik1.move(25, 25)

        # Text Izbornika 2
        self.text_izbornik2 = QtWidgets.QLabel(self)
        self.text_izbornik2.setFont(self.font)
        self.text_izbornik2.setText('Vrsta luka:')
        self.text_izbornik2.move(25, 60)

        # Text ime
        self.text_ime = QtWidgets.QLabel(self)
        self.text_ime.setFont(self.font)
        self.text_ime.setText('Ime:')
        self.text_ime.move(25, 95)

        # Input ime
        self.input_ime = QtWidgets.QLineEdit(self)
        self.input_ime.setGeometry(QtCore.QRect(150, 95, 150, 25))

        # Text prezime
        self.text_prezime = QtWidgets.QLabel(self)
        self.text_prezime.setFont(self.font)
        self.text_prezime.setText('Prezime:')
        self.text_prezime.move(25, 130)

        # Input prezime
        self.input_prezime = QtWidgets.QLineEdit(self)
        self.input_prezime.setGeometry(QtCore.QRect(150, 130, 150, 25))

        # Text telefon
        self.text_tel = QtWidgets.QLabel(self)
        self.text_tel.setFont(self.font)
        self.text_tel.setText('Telefon:')
        self.text_tel.move(25, 165)

        # Input telefon
        self.input_tel = QtWidgets.QLineEdit(self)
        self.input_tel.setGeometry(QtCore.QRect(150, 165, 150, 25))

        # Text email
        self.text_email = QtWidgets.QLabel(self)
        self.text_email.setFont(self.font)
        self.text_email.setText('Email:')
        self.text_email.move(25, 200)

        # Input email
        self.input_email = QtWidgets.QLineEdit(self)
        self.input_email.setGeometry(QtCore.QRect(150, 200, 150, 25))

        # Button unos narudzbe
        self.button_unosnarudzbe = QtWidgets.QPushButton(self)
        self.button_unosnarudzbe.setFont(self.font)
        self.button_unosnarudzbe.setText('Unesi narudzbu')
        self.button_unosnarudzbe.setGeometry(QtCore.QRect(100, 235, 150, 30))
        self.button_unosnarudzbe.clicked.connect(self.unos_narucitelja)

        # Button ispis narudzba
        self.button_ispisnarudzba = QtWidgets.QPushButton(self)
        self.button_ispisnarudzba.setFont(self.font)
        self.button_ispisnarudzba.setText('Ispisi svih narudzbi')
        self.button_ispisnarudzba.setGeometry(QtCore.QRect(100, 270, 150, 30))
        self.button_ispisnarudzba.clicked.connect(self.ispis_narudzba)

        # Button brisanje narudzba
        self.button_brisanjenarudzba = QtWidgets.QPushButton(self)
        self.button_brisanjenarudzba.setFont(self.font)
        self.button_brisanjenarudzba.setText('Brisanje narudzbe')
        self.button_brisanjenarudzba.setGeometry(QtCore.QRect(425, 235, 150, 30))
        self.button_brisanjenarudzba.clicked.connect(self.brisanje_narudzba)

        # Lista narudzbi
        self.lista_narudzbi = QtWidgets.QListWidget(self)
        self.lista_narudzbi.setGeometry(350, 25, 300, 200)

        # Text greska
        self.text_error = QtWidgets.QLabel(self)
        self.text_error.setFont(self.font)
        self.text_error.setAlignment(QtCore.Qt.AlignCenter)
        self.text_error.setStyleSheet('color : red')
        self.text_error.setGeometry(QtCore.QRect(25, 300, 650, 50))

        query_pocetno_citanje = f"""
                                SELECT ime, prezime, telefon, email, dob, naziv FROM table_narucitelji
                                LEFT JOIN table_dob_narucitelja ON table_narucitelji.id_dob = table_dob_narucitelja.id
                                LEFT JOIN table_lukovi ON table_narucitelji.id_luk = table_lukovi.id
                                """
        pocetno_citanje_narudzba = cur.execute(query_pocetno_citanje).fetchall()
        for item in pocetno_citanje_narudzba:
            self.lista_narudzbi.addItem(', '.join(item))


    def unos_narucitelja(self):
        error_unosa = provjera_korisnickog_unosa(self.input_ime.text(), self.input_prezime.text(), self.input_tel.text(), self.input_email.text())

        if error_unosa == None:
            narucitelji.append(Narucitelj(self.input_ime.text(), self.input_prezime.text(), self.input_tel.text(), self.input_email.text(), self.izbornik1.currentIndex()+1, self.izbornik2.currentIndex()+1))

            id_upisi = self.sljedeci_id()

            query_upis = f""" 

                       INSERT INTO table_narucitelji (id_narucitelja, ime, prezime, telefon, email, id_dob, id_luk)
                       VALUES ({id_upisi}, '{narucitelji[len(narucitelji)-1].ime}', '{narucitelji[len(narucitelji)-1].prezime}', '{narucitelji[len(narucitelji)-1].tel}', '{narucitelji[len(narucitelji)-1].email}', {narucitelji[len(narucitelji)-1].id_dob}, {narucitelji[len(narucitelji)-1].id_luk})

                       """
            cur.execute(query_upis)
            con.commit()

            query_zadnji_id = """
                            SELECT ime, prezime, telefon, email, dob, naziv FROM table_narucitelji
                            LEFT JOIN table_dob_narucitelja ON table_narucitelji.id_dob = table_dob_narucitelja.id
                            LEFT JOIN table_lukovi ON table_narucitelji.id_luk = table_lukovi.id
                            ORDER BY id_narucitelja DESC LIMIT 1
                            """
            zadnji_id = cur.execute(query_zadnji_id).fetchall()

            QMessageBox.information(self, 'Potvrda', 'Informacije uspjesno spremljene!', QMessageBox.Ok)

            for nar in zadnji_id:
                self.lista_narudzbi.addItem(', '.join(nar))

            self.input_ime.setText('')
            self.input_prezime.setText('')
            self.input_tel.setText('')
            self.input_email.setText('')
            self.text_error.setText('')
        else:
            self.text_error.setText(error_unosa)

    def ispis_narudzba(self):
        query_ispis = """
        SELECT id_narucitelja, ime, prezime, telefon, email, dob, naziv FROM table_narucitelji
        LEFT JOIN table_dob_narucitelja ON table_narucitelji.id_dob = table_dob_narucitelja.id
        LEFT JOIN table_lukovi ON table_narucitelji.id_luk = table_lukovi.id
        """

        data_ispis = cur.execute(query_ispis).fetchall()
        for d in data_ispis:
            print(d)

        QMessageBox.information(self, 'Potvrda', 'Informacije uspjesno ispisane!', QMessageBox.Ok)

    def brisanje_narudzba(self):
        odabrana_narudzba = self.lista_narudzbi.currentRow()
        odabrana_narudzba_query = odabrana_narudzba + 1

        query_brisanje = f"""
                        DELETE FROM table_narucitelji WHERE id_narucitelja = {odabrana_narudzba_query}
                        """
        cur.execute(query_brisanje)
        con.commit()

        query_update = f"""
                        UPDATE table_narucitelji SET id_narucitelja=id_narucitelja-1 WHERE id_narucitelja>{odabrana_narudzba_query}
                        """
        cur.execute(query_update)
        con.commit()

        self.lista_narudzbi.takeItem(odabrana_narudzba)

        QMessageBox.information(self, 'Potvrda', 'Informacije uspjesno izbrisana!', QMessageBox.Ok)

    def sljedeci_id(self):
        query_maxid = """
                        SELECT MAX(id_narucitelja) FROM table_narucitelji
                    """
        maxid = cur.execute(query_maxid).fetchone()[0]

        if maxid is None:
            return 1
        else:
            return maxid + 1


app = QApplication(sys.argv)
window = MojProzor()
window.show()
sys.exit(app.exec_())