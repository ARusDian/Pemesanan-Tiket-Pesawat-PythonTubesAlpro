from PyQt5 import QtCore, QtWidgets, QtGui
import qrcode
from PIL.ImageQt import ImageQt
import os

class UiTransfer(object):
    def __init__(self,data,harga,jumlah,list_nama_pemesan):
        self.data = data
        self.harga = harga
        self.jumlah = jumlah
        self.list_nama_pemesan = list_nama_pemesan

    def buat_qr(self):
        self.qr_pay = "TYK"+self.data[1][3:]+"TF"+self.data[1][:2]+self.harga
        img = qrcode.make(self.qr_pay)
        qr = ImageQt(img)
        self.label_QR.setPixmap(QtGui.QPixmap.fromImage(qr))

    def confirm(self,Dialog):
        import mysql.connector
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tubes',
        )
        self.mycursor = self.mydb.cursor()
        self.hasil = int(self.data[9]) - self.jumlah
        self.mycursor.execute(f""" UPDATE penerbangan SET kursi = '{int(self.data[9])-self.jumlah}'
                              WHERE no_penerbangan = '{self.data[1]}'""")
        self.mydb.commit()
        self.generate_seat()
        os.mkdir(f"Pesanan/{self.data[1]}-{self.jumlah}")
        for i in range(self.jumlah):
            self.cetak_tiket(self.list_nama_pemesan[i],self.seat[i])
        from pesan import UiWindowPemesanan
        self.window_pemesanan = QtWidgets.QMainWindow()
        self.ui_pesan = UiWindowPemesanan()
        self.ui_pesan.setupUi(self.window_pemesanan)
        self.msgBox = QtWidgets.QMessageBox(Dialog)
        self.msgBox.setWindowTitle("Tiket Dipesan")
        self.msgBox.setText("Tiket Berhasil di pesan dan dicetak ;)\nSilahkan ambil Tiket anda\n"
                            "Terimakasih telah Menggunakan TiketinYuk")
        self.msgBox.show()
        Dialog.close()
        self.window_pemesanan.show()

    def generate_seat(self):
        import random
        self.res = random.randint(0, 25)
        self.seat = []
        self.row_seat = self.j = int()
        for i in range(self.jumlah):
            if i % 6 != 0:
                self.j += 1
                self.seat.append(str(self.res + self.row_seat) + chr(ord("A") + self.j))
            else:
                self.row_seat += 1
                self.j = 0
                self.seat.append(str(self.res + self.row_seat) + chr(ord("A") + self.j))

    def cetak_tiket(self,nama,seat):
        from PIL import Image,ImageDraw,ImageFont

        self.nama = nama
        self.seatperson = seat
        self.hargaorang = str(int(self.data[8])/self.jumlah)[:-2]
        self.qr_payed = str("TYK"+"-"+self.data[1][3:]+"-"+"TF"+"-"+self.data[1][:2]
                            +"-"+"Terbayar"+"-"+self.nama+"-"+self.seatperson+"-"+self.hargaorang)
        qr_payed = qrcode.make(self.qr_payed)
        qr_payed.save('assets/tempqr.jpg')
        tiket = Image.open('assets/ticket depan.PNG')
        tempqr = Image.open('assets/tempqr.jpg').resize((300,300),Image.ANTIALIAS)
        tiket.paste(tempqr,(50,250,350,550))
        tempqr = Image.open('assets/tempqr.jpg').resize((175, 175), Image.ANTIALIAS)
        tiket.paste(tempqr, (1625, 450, 1800, 625))
        os.remove('assets/tempqr.jpg')
        gambar =ImageDraw.Draw(tiket)
        #Bagian Tiket
        gambar.text((1200, 210), "SEAT", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=40),
                    fill=(1, 52, 111))
        gambar.text((1200, 255), self.seatperson, font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=70),
                    fill=(1, 52, 111))
        gambar.text((400, 200), "Nama", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=50),
                    fill=(1, 52, 111))
        gambar.text((575, 200), self.nama, font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=50),
                    fill=(1, 52, 111))
        gambar.text((400, 270), "ID Penerbangan", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((400, 310), self.data[1], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((400, 370), "Tanggal", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((400, 410), self.data[4], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((900, 200), "Maskapai", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=50),
                    fill=(1, 52, 111))
        gambar.text((900, 275), self.data[7], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=50),
                    fill=(1, 52, 111))
        gambar.text((900, 370), "Jam Keberangkatan", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((900, 410), self.data[5], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((400, 470), "Dari", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=40),
                    fill=(1, 52, 111))
        gambar.text((400, 525),self.data[2] , font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=45),
                    fill=(1, 52, 111))
        gambar.text((900, 470), "Menuju", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=40),
                    fill=(1, 52, 111))
        gambar.text((900, 525), self.data[3], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=45),
                    fill=(1, 52, 111))
        #Bagian Boarding Pass
        gambar.text((1500, 200), "Maskapai", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=20),
                    fill=(1, 52, 111))
        gambar.text((1500, 225), self.data[7], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((1500, 280), "ID Penerbangan", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=20),
                    fill=(1, 52, 111))
        gambar.text((1500, 305), self.data[1], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((1500, 355), "Jam Keberangkatan",font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=20),
                    fill=(1, 52, 111))
        gambar.text((1500, 380), self.data[5], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((1750, 200), "Dari", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=20),
                    fill=(1, 52, 111))
        gambar.text((1750, 225), self.data[2], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((1750, 280), "Menuju", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=20),
                    fill=(1, 52, 111))
        gambar.text((1750, 305), self.data[3], font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=35),
                    fill=(1, 52, 111))
        gambar.text((1750, 355), "SEAT", font=ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", size=20),
                    fill=(1, 52, 111))
        gambar.text((1750, 380), self.seatperson, font=ImageFont.truetype("assets/fonts/OpenSans-Semibold.ttf", size=40),
                    fill=(1, 52, 111))
        tiket.save(f"Pesanan/{self.data[1]}-{self.jumlah}/tiket{self.nama}-{self.data[1]}-{self.seatperson}.png")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(720, 600)
        Dialog.setWindowIcon(QtGui.QIcon('assets\icon.png'))
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(0, 0, 720, 600)
        self.bg.setStyleSheet("background-color:#BFD7F3;border:3px solid;")
        self.label_QR = QtWidgets.QLabel(Dialog)
        self.label_QR.setGeometry(QtCore.QRect(390, 160, 331, 331))
        self.label_QR.setObjectName("label_QR")
        self.buat_qr()
        self.label_Perusahaan = QtWidgets.QLabel(Dialog)
        self.label_Perusahaan.setGeometry(QtCore.QRect(370, 50, 331, 41))
        self.label_Perusahaan.setObjectName("label_Perusahaan")
        self.label_Perusahaan.setStyleSheet("font-size:50px bold;")
        self.label_Perusahaan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_atau = QtWidgets.QLabel(Dialog)
        self.label_atau.setGeometry(QtCore.QRect(450, 110, 240, 70))
        self.label_atau.setObjectName("label_atau")
        self.btn_konfirmasi = QtWidgets.QPushButton(Dialog)
        self.btn_konfirmasi.setGeometry(QtCore.QRect(160, 490, 391, 81))
        self.btn_konfirmasi.setObjectName("pushButton")
        self.btn_konfirmasi.setStyleSheet(
            "border-radius : 1; border : 2px solid black;background-color:white;"
            "font-size:30px;background-color:#94C6FF;")
        self.btn_konfirmasi.clicked.connect(lambda : self.confirm(Dialog))
        # self.btn_konfirmasi.clicked.connect(Dialog.close)
        self.label_IDPenerbangan_header = QtWidgets.QLabel(Dialog)
        self.label_IDPenerbangan_header.setGeometry(QtCore.QRect(20, 70, 171, 31))
        self.label_IDPenerbangan_header.setObjectName("label_IDPenerbangan_Header")
        self.label_IDPenerbangan_header.setStyleSheet("font-size:20px")
        self.label_IDPenerbangan_item = QtWidgets.QLabel(Dialog)
        self.label_IDPenerbangan_item.setGeometry(QtCore.QRect(20, 110, 281, 61))
        self.label_IDPenerbangan_item.setObjectName("label_IDPenerbangan_Item")
        self.label_IDPenerbangan_item.setStyleSheet("font-size:30px")
        self.label_harga_header = QtWidgets.QLabel(Dialog)
        self.label_harga_header.setGeometry(QtCore.QRect(20, 260, 281, 41))
        self.label_harga_header.setObjectName("label_harga_header")
        self.label_harga_header.setStyleSheet("font-size:20px")
        self.label_harga_item = QtWidgets.QLabel(Dialog)
        self.label_harga_item.setGeometry(QtCore.QRect(20, 310, 281, 51))
        self.label_harga_item.setStyleSheet("font-size:30px bold;")
        self.label_harga_item.setObjectName("label_harga_item")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pembayaran Via Transfer"))
        self.label_Perusahaan.setText(_translate("Dialog", "TiketinYuk"))
        self.label_atau.setText(_translate("Dialog", "Scan Code QR dibawah\n     untuk Membayar"))
        self.btn_konfirmasi.setText(_translate("Dialog", "Konfirmasi Pembayaran"))
        self.label_IDPenerbangan_header.setText(_translate("Dialog", "ID Penerbangan"))
        self.label_IDPenerbangan_item.setText(self.data[1])
        self.label_harga_header.setText(_translate("Dialog", "Total Pembayaran :"))
        self.label_harga_item.setText("Rp "+self.harga)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UiTransfer()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())