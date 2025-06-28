import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog
from password import Ui_PassWordGenerator
import random
import string
import sqlite3

baglanti = sqlite3.connect("sifrelerim.db")
cursor = baglanti.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS sifreler(hesap TEXT,email TEXT,sifre TEXT)")
baglanti.commit()
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_PassWordGenerator()
        self.ui.setupUi(self)
        self.ui.btn_olustur.clicked.connect(self.olustur)
        self.ui.btn_yaz.clicked.connect(self.yazdir)
    def olustur(self):
        sifreUzunluk = int(self.ui.uzunluk.text())
        harfler = string.ascii_lowercase + string.digits + string.ascii_uppercase
        sifrem = ''.join(random.choice(harfler) for i in range(sifreUzunluk))
        hesabim = self.ui.txt_hesap.text()
        emailim = self.ui.txt_email.text()
        self.ui.txt_sifre.setText(sifrem)
        cursor.execute("INSERT INTO sifreler VALUES(?,?,?)",(hesabim,emailim,sifrem))
        baglanti.commit()
    def yazdir(self):
        cursor.execute("SELECT * FROM sifreler")
        liste = cursor.fetchall()
        for i in liste:
            self.ui.list_yaz.addItems(['Hesap bilgileri'])
            self.ui.list_yaz.addItems(i)
            
app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())    