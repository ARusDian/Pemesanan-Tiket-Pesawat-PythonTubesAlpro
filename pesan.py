from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector



class UiWindowPemesanan(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tubes',
        )
        self.ukuran = [0, 150, 150, 150, 150, 90, 90, 100, 150, 100]
        self.mycursor = self.mydb.cursor()

    def pesan_tiket(self,Window):
        self.mycursor.execute(f"SELECT * FROM penerbangan WHERE no_penerbangan = '{self.comboBox_selectID.currentText()}'")
        self.data_pemesanan = self.mycursor.fetchall()[0]
        if int(self.data_pemesanan[9]) >= self.spinBox_total_orang.value():
            from order import OrderDialog
            self.dialog = QtWidgets.QDialog()
            self.ui = OrderDialog(self.data_pemesanan, self.spinBox_total_orang.value())
            self.ui.setupUi(self.dialog)
            Window.close()
            self.dialog.show()
        else:
            message_box = QtWidgets.QMessageBox(Window)
            message_box.setWindowTitle("Tidak Bisa memesan Tiket")
            message_box.setText("Jumlah tiket tersedia\nKurang dari jumlah pemesanan")
            message_box.exec_()

    def tampilkan(self):
        for i in range(len(self.list_flight), -1, -1):
            self.table_penerbangan.removeRow(i)
        if self.comboBox_asal.currentText() and self.comboBox_tujuan.currentText():
            self.mycursor.execute(f"SELECT * FROM penerbangan WHERE "
                                  f"asal = '{self.comboBox_asal.currentText()}' AND tujuan = '{self.comboBox_tujuan.currentText()}'")
        elif self.comboBox_asal.currentText():
            self.mycursor.execute(f"SELECT * FROM penerbangan WHERE asal = '{self.comboBox_asal.currentText()}'")
        elif self.comboBox_tujuan.currentText():
            self.mycursor.execute(f"SELECT * FROM penerbangan WHERE tujuan = '{self.comboBox_tujuan.currentText()}'")
        else:
            self.mycursor.execute("SELECT * FROM penerbangan")
        self.list_flight = self.mycursor.fetchall()
        self.flight_id = [i[1] for i in self.list_flight]
        self.comboBox_selectID.clear()
        self.comboBox_selectID.addItems(self.flight_id)
        for i in range(len(self.list_flight)):
            self.table_penerbangan.insertRow(i)
            for j in range(len(self.list_flight[i])):
                if j == 8:
                    self.table_penerbangan.setItem(i, j, QTableWidgetItem
                    ("Rp. "+f"{int(self.list_flight[i][8]):,.2f}"[:-3].replace(",","." )))
                else:
                    self.table_penerbangan.setItem(i, j, QTableWidgetItem(self.list_flight[i][j]))

    def act_kembali(self):
        from landing import Landing
        self.window_landing = QtWidgets.QMainWindow()
        self.ui_landing = Landing()
        self.ui_landing.tampil(self.window_landing)
        self.window_landing.show()

    def get_list_kota(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT * FROM penerbangan")
        self.list_flight = self.mycursor.fetchall()
        self.list_kota = list(set([self.x[i] for self.x in self.list_flight for i in range(2, 4)]))
        self.list_kota.insert(0, "")
        self.list_kota.sort()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 740)
        MainWindow.setWindowIcon(QtGui.QIcon('assets\icon.png'))
        self.label_bg = QtWidgets.QLabel(MainWindow)
        self.label_bg.setPixmap(QtGui.QPixmap('assets\logo-01.jpg'))
        self.label_bg.setScaledContents(True)
        self.label_bg.setGeometry(0, 0, 1200, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1171, 691))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_judul = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_judul.setObjectName("tittle_l")
        self.font_24 = QtGui.QFont()
        self.font_24.setPointSize(24)
        self.label_judul.setFont(self.font_24)
        self.verticalLayout_3.addWidget(self.label_judul)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 4)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.get_list_kota()
        self.label_asal = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_asal.setObjectName("asal_l")
        self.horizontalLayout.addWidget(self.label_asal)
        self.comboBox_asal = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_asal.setObjectName("asal")
        self.comboBox_asal.addItems(self.list_kota)
        self.horizontalLayout.addWidget(self.comboBox_asal)

        self.label_tujuan = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_tujuan.setObjectName("tujuan_l")
        self.horizontalLayout.addWidget(self.label_tujuan)
        self.comboBox_tujuan = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_tujuan.setObjectName("comboBox")
        self.comboBox_tujuan.addItems(self.list_kota)
        self.horizontalLayout.addWidget(self.comboBox_tujuan)

        self.btn_cari = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_cari.setObjectName("pushButton")
        self.btn_cari.setStyleSheet("border-radius : 10; border : 2px solid black;background-color:white;"
                                    "font-size:20px;background-color:#BDDCFF;")

        self.horizontalLayout.addWidget(self.btn_cari)
        self.btn_kembali = QtWidgets.QPushButton(MainWindow)
        self.btn_kembali.setGeometry(1025, 10, 150, 50)
        self.btn_kembali.setObjectName("btn_kembali")
        self.btn_kembali.setStyleSheet("border-radius : 10; border : 2px solid black;background-color:white;"
                                       "font-size:27px;background-color:#94C6FF;")
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.table_penerbangan = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_penerbangan.setRowCount(0)
        self.table_penerbangan.setColumnCount(10)
        self.table_penerbangan.setObjectName("tableWidget")
        for i in range(len(self.ukuran)):
            self.table_penerbangan.setColumnWidth(i, self.ukuran[i])
        self.table_penerbangan.horizontalHeader().setVisible(True)
        self.verticalLayout_3.addWidget(self.table_penerbangan)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_selectID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_selectID.setObjectName("selectID_l")
        self.font_12 = QtGui.QFont()
        self.font_12.setPointSize(12)
        self.font_12.setBold(True)
        self.label_selectID.setFont(self.font_12)
        self.horizontalLayout_2.addWidget(self.label_selectID)

        self.comboBox_selectID = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_selectID.setObjectName("Pilih")
        self.horizontalLayout_2.addWidget(self.comboBox_selectID)

        self.label_total_orang = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_total_orang.setText("Jumlah Tiket = ")
        self.label_total_orang.setFont(self.font_12)
        self.horizontalLayout_2.addWidget(self.label_total_orang)

        self.spinBox_total_orang = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_total_orang.setRange(0, 100)
        self.spinBox_total_orang.setSingleStep(1)
        self.spinBox_total_orang.setValue(1)
        self.horizontalLayout_2.addWidget(self.spinBox_total_orang)

        self.btn_pesan = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_pesan.setObjectName("Pesan")
        self.btn_pesan.setFixedSize(200, 35)
        self.btn_pesan.setStyleSheet("border-radius : 10; border : 2px solid black;background-color:white;"
                                     "font-size:21px;background-color:#BDDCFF;")
        self.horizontalLayout_2.addWidget(self.btn_pesan)
        self.horizontalLayout_2.setStretch(1, 1,)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tampilkan()
        self.btn_kembali.clicked.connect(self.act_kembali)
        self.btn_kembali.clicked.connect(MainWindow.close)
        self.btn_cari.clicked.connect(self.tampilkan)
        self.btn_pesan.clicked.connect(lambda x :self.pesan_tiket(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Halaman Pemesanan"))
        self.label_judul.setText(_translate("MainWindow", "Form Pemesanan"))
        self.label_tujuan.setText(_translate("MainWindow", "   Tujuan : "))
        self.label_asal.setText(_translate("MainWindow", "Asal : "))
        self.btn_cari.setText(_translate("MainWindow", "Cari"))
        self.btn_kembali.setText(_translate("MainWindow", "Kembali"))
        self.table_penerbangan.setSortingEnabled(True)
        self.table_penerbangan.setHorizontalHeaderLabels(["No", "Id Penerbangan", "Asal", "Tujuan",
                                                          "Tanggal", "Berangkat", "Sampai", "Maskapai",
                                                          "Harga", "Sisa Kursi"])
        self.label_selectID.setText(_translate("MainWindow", "ID Penerbangan Yang Dipilih :  "))
        self.btn_pesan.setText(_translate("MainWindow", "Pesan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pesan = QtWidgets.QMainWindow()
    ui = UiWindowPemesanan()
    ui.setupUi(pesan)
    pesan.show()
    sys.exit(app.exec_())