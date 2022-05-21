from PyQt5 import QtCore, QtWidgets,QtGui


class ui_token(object):
    def __init__(self,data,jumlah):
        self.data = data
        self.jumlah = jumlah

    def generate_token(self):
        self.token_pay = "TYK"+self.data[1][3:]+"IDMRT"+self.data[1][:2]
        self.item_kodebayar.setText(self.token_pay)

    def act_accepted(self):
        import mysql.connector
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tubes',
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(f""" UPDATE penerbangan SET kursi = '{int(self.data[9])-self.jumlah}'
                              WHERE no_penerbangan = '{self.data[1]}'""")
        self.mydb.commit()
        from pesan import UiWindowPemesanan
        self.window_pemesanan = QtWidgets.QMainWindow()
        self.ui_pesan = UiWindowPemesanan()
        self.ui_pesan.setupUi(self.window_pemesanan)
        self.window_pemesanan.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(900, 600)
        Dialog.setWindowIcon(QtGui.QIcon('assets\icon.png'))
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(0, 0, 900, 600)
        self.bg.setStyleSheet("background-color:#BFD7F3;border:3px solid;")
        self.btn_accept = QtWidgets.QPushButton(Dialog)
        self.btn_accept.setGeometry(QtCore.QRect(70, 490, 760, 90))
        self.btn_accept.setObjectName("buttonBox")
        self.btn_accept.setText("Saya Sudah Bayar")
        self.btn_accept.setStyleSheet("border-radius : 1; border : 2px solid black;background-color:white;"
                                      "font-size:30px;background-color:#FCBA12;")
        self.btn_accept.clicked.connect(self.act_accepted)
        self.btn_accept.clicked.connect(Dialog.close)
        self.item_kodebayar = QtWidgets.QLabel(Dialog)
        self.item_kodebayar.setGeometry(QtCore.QRect(100, 150, 740, 151))
        self.item_kodebayar.setAlignment(QtCore.Qt.AlignCenter)
        self.item_kodebayar.setObjectName("item_kodebayar")
        self.item_kodebayar.setStyleSheet("font-size:40px;border:3px solid;")
        self.label_kodebayar = QtWidgets.QLabel(Dialog)
        self.label_kodebayar.setGeometry(QtCore.QRect(10, 30, 350, 101))
        self.label_kodebayar.setStyleSheet("font-size:35px")
        self.label_kodebayar.setObjectName("label_kodebayar")
        self.label_langkah = QtWidgets.QLabel(Dialog)
        self.label_langkah.setGeometry(QtCore.QRect(30, 300,800, 221))
        self.label_langkah.setObjectName("label_langkah")
        self.label_langkah.setStyleSheet("font-size:20px")
        self.label_kemudahan = QtWidgets.QLabel(Dialog)
        self.label_kemudahan.setStyleSheet("background-color:#2E8FFF;font-size:20px")
        self.label_kemudahan.setGeometry(QtCore.QRect(350, 30, 500, 101))
        self.label_kemudahan.setObjectName("label_kemudahan")
        self.generate_token()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Token Pembayaran"))
        self.label_kodebayar.setText(_translate("Dialog", "Kode Pembayaran\nIndomaret"))
        self.label_langkah.setText(_translate("Dialog", """Ikuti pentujuk berikut untuk melakukan pembayaran di indomaret
1. Sampaikan pada kasir bahwa Anda hendak membayar pemesanan tiket TiketinYuk
2. Tunjukan kode pembayaran di atas kepada kasir
3. Biaya tambahan sebesar Rp.2.500/transaksi di luar harga total akan dikenakan 
4. Setelah transaksi selesai,Anda akan menerima bukti pembayaran dari Indomaret

        """))
        self.label_kemudahan.setText(_translate("Dialog", """
    Untuk Kemudahan Pembayaran, Tunjukkan Instruksi  
                       
        Pembayaran Ini Ke Kasir Indomaret Terdekat
        """))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ui_token("JT 0889")
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())