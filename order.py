from PyQt5 import QtCore, QtGui, QtWidgets


class OrderDialog(object):
    def __init__(self, data_pesan, jumlah):
        self.data_pemesanan = data_pesan
        self.jumlah = jumlah
        self.list_nama_pemesan = []
        self.i = int()

    def kembali(self):
        from pesan import UiWindowPemesanan
        self.window_pemesanan = QtWidgets.QMainWindow()
        self.ui_pesan = UiWindowPemesanan()
        self.ui_pesan.setupUi(self.window_pemesanan)
        self.window_pemesanan.show()

    def set_Font(self):
        self.font_12 = QtGui.QFont()
        self.font_12.setBold(True)
        self.maskapai_item.setFont(self.font_12)
        self.asal_item.setFont(self.font_12)
        self.tujuan_item.setFont(self.font_12)
        self.harga_item.setFont(self.font_12)
        self.date_item.setFont(self.font_12)
        self.datang_item.setFont(self.font_12)
        self.berangkat_item.setFont(self.font_12)

    def act_pesan(self,Dialog):
        if len(self.list_nama_pemesan) == self.jumlah:
            if self.radio_token.isChecked():
                from token_tiket import ui_token
                self.dialog = QtWidgets.QDialog()
                self.ui = ui_token(self.data_pemesanan,self.jumlah)
                self.ui.setupUi(self.dialog)
                self.dialog.show()
                Dialog.close()
            elif self.radio_transfer.isChecked():
                from transfer import UiTransfer
                self.dialog = QtWidgets.QDialog()
                self.ui = UiTransfer(self.data_pemesanan,
                                     f"""{int(self.data_pemesanan[8])*self.jumlah:,.2f}"""[:-3].replace(",", "."),
                                     self.jumlah,self.list_nama_pemesan)
                self.ui.setupUi(self.dialog)
                self.dialog.show()
                Dialog.close()
            else:
                message_box = QtWidgets.QMessageBox(Dialog)
                message_box.setWindowTitle("Tidak Bisa Memesan Tiket")
                message_box.setText("Pilih Metode pembayaran            ")
                message_box.exec_()
        else:
            message_box = QtWidgets.QMessageBox(Dialog)
            message_box.setWindowTitle("Tidak Bisa Memesan Tiket")
            message_box.setText("Masukkan nama-nama pemesan tiket secara lengkap")
            message_box.exec_()

    def isi_daftar_nama(self):
        if self.i < self.jumlah:
            for i in range(self.i, - 1, -1):
                self.tabel_NamaPemesan.removeRow(i)
            self.i += 1
            self.list_nama_pemesan.append(self.get_name.text())
            for i in range(self.i):
                self.tabel_NamaPemesan.insertRow(i)
                self.tabel_NamaPemesan.setItem(i, 0, QtWidgets.QTableWidgetItem(self.list_nama_pemesan[i]))
                self.get_name.clear()

    def detail_tiket(self):
        # Cetak pada Form
        self.maskapai_item.setText(self.data_pemesanan[7])
        self.asal_item.setText(self.data_pemesanan[2])
        self.tujuan_item.setText(self.data_pemesanan[3])
        self.berangkat_item.setText(self.data_pemesanan[5])
        self.datang_item.setText(self.data_pemesanan[6])
        self.date_item.setText(self.data_pemesanan[4])
        self.harga_item.setText("Rp. " + f"""{int(self.data_pemesanan[8])
        *self.jumlah:,.2f}"""[:-3].replace(",", "."))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1008, 720)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setWindowIcon(QtGui.QIcon('assets\icon.png'))
        self.gambar = QtWidgets.QLabel(Dialog)
        self.gambar.setPixmap(QtGui.QPixmap('assets\logo-01.jpg'))
        self.gambar.setScaledContents(True)
        self.gambar.setGeometry(0, 0, 1008, 720)
        self.order = QtWidgets.QDialogButtonBox(Dialog)
        self.order.setGeometry(QtCore.QRect(250, 675, 621, 32))
        self.order.setOrientation(QtCore.Qt.Horizontal)
        self.order.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.order.setObjectName("order")
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(5, 50, 975, 600)
        self.bg.setStyleSheet("background-color:#C2DEFF;border:3px solid;")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 960, 500))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_l = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.name_l.setObjectName("name_l")
        self.horizontalLayout.addWidget(self.name_l)
        self.get_name = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.get_name.setObjectName("get_name")
        self.horizontalLayout.addWidget(self.get_name)
        self.btn_masukkan = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_masukkan.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.btn_masukkan)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.harga_l = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.harga_l.setObjectName("harga_l")
        self.gridLayout.addWidget(self.harga_l, 6, 0, 1, 1)
        self.asal_l = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.asal_l.setObjectName("asal_l")
        self.gridLayout.addWidget(self.asal_l, 1, 0, 1, 1)
        self.date_item = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.date_item.setObjectName("date_item")
        self.gridLayout.addWidget(self.date_item, 5, 1, 1, 1)
        self.harga_item = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.harga_item.setObjectName("harga_item")
        self.gridLayout.addWidget(self.harga_item, 6, 1, 1, 1)
        self.datang_item = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.datang_item.setObjectName("datang_l")
        self.gridLayout.addWidget(self.datang_item, 4, 1, 1, 1)
        self.berangkat_item = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.berangkat_item.setObjectName("berangkat_item")
        self.gridLayout.addWidget(self.berangkat_item, 2, 1, 1, 1)
        self.tujuan_l = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.tujuan_l.setObjectName("tujuan_l")
        self.gridLayout.addWidget(self.tujuan_l, 3, 0, 1, 1)
        self.asal_item = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.asal_item.setObjectName("asal_item")
        self.gridLayout.addWidget(self.asal_item, 2, 0, 1, 1)
        self.tujuan_item = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.tujuan_item.setObjectName("tujuan_item")
        self.gridLayout.addWidget(self.tujuan_item, 4, 0, 1, 1)
        self.date_l = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.date_l.setObjectName("date_l")
        self.gridLayout.addWidget(self.date_l, 5, 0, 1, 1)
        self.maskapai_l = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.maskapai_l.setObjectName("maskapai_l")
        self.gridLayout.addWidget(self.maskapai_l, 0, 0, 1, 1)
        self.maskapai_item = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.maskapai_item.setObjectName("maskapai_item")
        self.gridLayout.addWidget(self.maskapai_item, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.tabel_NamaPemesan = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.tabel_NamaPemesan.setObjectName("list_NamaPemesan")
        self.tabel_NamaPemesan.setRowCount(0)
        self.tabel_NamaPemesan.setColumnCount(1)
        self.tabel_NamaPemesan.setColumnWidth(0, 300)
        self.tabel_NamaPemesan.setHorizontalHeaderLabels(["Nama Pemesan"])
        self.gridLayout_2.addWidget(self.tabel_NamaPemesan, 1, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(420, 580, 411, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radio_transfer = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.radio_transfer.setObjectName("radioButton_2")
        self.gridLayout_3.addWidget(self.radio_transfer, 1, 1, 1, 1)
        self.bayar_l = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.bayar_l.setObjectName("bayar_l")
        self.gridLayout_3.addWidget(self.bayar_l, 0, 0, 1, 1)
        self.radio_token = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.radio_token.setObjectName("btn_token")
        self.gridLayout_3.addWidget(self.radio_token, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setRowStretch(0, 1)
        self.tittle_l = QtWidgets.QLabel(Dialog)
        self.tittle_l.setGeometry(QtCore.QRect(10, 20, 221, 31))
        self.tittle_l.setObjectName("tittle_l")
        self.tittle_f = QtGui.QFont()
        self.tittle_f.setPointSize(14)
        self.tittle_l.setFont(self.tittle_f)

        self.retranslateUi(Dialog)
        self.btn_masukkan.clicked.connect(self.isi_daftar_nama)

        self.order.rejected.connect(Dialog.close)
        self.order.rejected.connect(self.kembali)
        self.order.accepted.connect(lambda  : self.act_pesan(Dialog))
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.set_Font()
        self.detail_tiket()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pengisian Form Tiket"))
        self.name_l.setText(_translate("Dialog", "Nama Depan Penumpang : "))
        self.btn_masukkan.setText(_translate("Dialog", "Masukkan"))
        self.harga_l.setText(_translate("Dialog", "Total Biaya Pemesanan"))
        self.asal_l.setText(_translate("Dialog", "Asal"))
        self.date_item.setText(_translate("Dialog", "Tanggal"))
        self.harga_item.setText(_translate("Dialog", "Harga"))
        self.datang_item.setText(_translate("Dialog", "jam_mendarat"))
        self.berangkat_item.setText(_translate("Dialog", "jam_berangkat"))
        self.tujuan_l.setText(_translate("Dialog", "Tujuan"))
        self.asal_item.setText(_translate("Dialog", "kota"))
        self.tujuan_item.setText(_translate("Dialog", "kota"))
        self.date_l.setText(_translate("Dialog", "Tanggal Penerbangan"))
        self.maskapai_l.setText(_translate("Dialog", "Maskapai"))
        self.maskapai_item.setText(_translate("Dialog", "nama maskapai"))
        self.label_2.setText(_translate("Dialog", "   Detail Pemesanan Tiket"))
        self.radio_transfer.setText(_translate("Dialog", "Pembayaran Via Transfer"))
        self.bayar_l.setText(_translate("Dialog", "Metode Pembayaran"))
        self.radio_token.setText(_translate("Dialog", "Pembayaran Via Token"))
        self.tittle_l.setText(_translate("Dialog", "Data Pemesanan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_order = QtWidgets.QDialog()
    ui = OrderDialog("ID 5517", 5)
    ui.setupUi(dialog_order)
    dialog_order.show()
    sys.exit(app.exec_())