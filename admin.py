from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector


class ui_window_admin(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tubes',
        )
        self.ukuran = [0, 150, 150, 150, 150, 90, 90, 100, 150, 100]
        
    def act_tambah_data(self):
        from tambah_data import Ui_dialog_tambah_data
        self.dialog_tambahdata = QDialog()
        self.ui_dialog_tambah = Ui_dialog_tambah_data()
        self.ui_dialog_tambah.setupUi(self.dialog_tambahdata)
        self.dialog_tambahdata.show()
        
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
        self.list_kota = [""]
        self.list_kota = list(set([self.x[i] for self.x in self.list_flight for i in range(2, 4)]))
        self.list_kota.insert(0, "")
        self.list_kota.sort()

    def act_hapus_data(self):
        from hapus import ui_hapus_data
        self.dialog_hapusdata = QDialog()
        self.ui_hapus_data = ui_hapus_data(self.Pilih.currentText())
        self.ui_hapus_data.setupUi(self.dialog_hapusdata)
        self.dialog_hapusdata.show()

    def act_edit_data(self):
        from edit_data import Ui_dialog_edit_data
        self.dialog_editdata = QDialog()
        self.ui_dialog_edit = Ui_dialog_edit_data(self.Pilih.currentText())
        self.ui_dialog_edit.setupUi(self.dialog_editdata)
        self.dialog_editdata.show()

    def tampilkan(self):
        for i in range(len(self.list_flight), -1, -1):
            self.table_penerbangan.removeRow(i)
        self.mycursor = self.mydb.cursor()
        if self.asal.currentText() and self.tujuan.currentText():
            self.mycursor.execute(f"SELECT * FROM penerbangan WHERE "
                                  f"asal = '{self.asal.currentText()}' AND tujuan = '{self.tujuan.currentText()}'")
        elif self.asal.currentText():
            self.mycursor.execute(f"SELECT * FROM penerbangan WHERE asal = '{self.asal.currentText()}'")
        elif self.tujuan.currentText():
            self.mycursor.execute(f"SELECT * FROM penerbangan WHERE tujuan = '{self.tujuan.currentText()}'")
        else:
            self.mycursor.execute("SELECT * FROM penerbangan")
        self.list_flight = self.mycursor.fetchall()
        self.flight_id = [i[1] for i in self.list_flight]
        self.Pilih.clear()
        self.Pilih.addItems(self.flight_id)
        for i in range(len(self.list_flight)):
            self.table_penerbangan.insertRow(i)
            for j in range(len(self.list_flight[i])):
                if j == 8:
                    self.table_penerbangan.setItem(i, j, QTableWidgetItem
                    ("Rp. "+f"{int(self.list_flight[i][8]):,.2f}"[:-3].replace(",","." )))
                else:
                    self.table_penerbangan.setItem(i, j, QTableWidgetItem(self.list_flight[i][j]))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 740)
        MainWindow.setWindowIcon(QtGui.QIcon('assets\icon.png'))
        self.bg = QtWidgets.QLabel(MainWindow)
        self.bg.resize( 1200, 740)
        self.bg.setStyleSheet("background-color:#2369B8;border:5px solid;")
        self.header_f = QtGui.QFont()
        self.header_f.setPointSize(12)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1171, 691))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tittle_f = QtGui.QFont()
        self.tittle_f.setPointSize(16)
        self.tittle_f.setBold(True)
        self.tittle_l = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tittle_l.setObjectName("tittle_l")
        self.tittle_l.setFont(self.tittle_f)
        self.horizontalLayout_4.addWidget(self.tittle_l)
        self.btn_kembali = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_kembali.setObjectName("btn_kembali")
        self.btn_kembali.setStyleSheet("border-radius : 10; border : 2px solid black;background-color:white;"
                                       "font-size:27px;background-color:#94C6FF;")
        self.horizontalLayout_4.addWidget(self.btn_kembali)
        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 4)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.get_list_kota()
        self.asal_l = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.asal_l.setObjectName("asal_l")
        self.asal_l.setFont(self.header_f)
        self.horizontalLayout.addWidget(self.asal_l)
        self.asal = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.asal.setObjectName("asal")
        self.asal.addItems(self.list_kota)
        self.horizontalLayout.addWidget(self.asal)
        self.tujuan_l = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tujuan_l.setObjectName("tujuan_l")
        self.tujuan_l.setFont(self.header_f)
        self.horizontalLayout.addWidget(self.tujuan_l)
        self.tujuan = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.tujuan.setObjectName("tujuan")
        self.tujuan.addItems(self.list_kota)
        self.horizontalLayout.addWidget(self.tujuan)
        self.btn_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_refresh.setObjectName("sortir")
        self.btn_refresh.setFixedHeight(40)
        self.btn_refresh.setStyleSheet("border-radius : 1; border : 2px solid black;background-color:white;"
                                       "font-size:20px;background-color:#94C6FF;margin:2px;")
        self.horizontalLayout.addWidget(self.btn_refresh)
        self.btn_tambah = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_tambah.setObjectName("btn_tambah")
        self.btn_tambah.setFixedSize(150,40)
        self.btn_tambah.setStyleSheet("border-radius : 1; border : 2px solid black;background-color:white;"
                                      "font-size:20px;background-color:#0066DB;margin:2px;")
        self.horizontalLayout.addWidget(self.btn_tambah)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.table_penerbangan = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_penerbangan.setRowCount(0)
        self.table_penerbangan.setColumnCount(10)
        self.table_penerbangan.setObjectName("table_penerbangan")
        for i in range(len(self.ukuran)):
            self.table_penerbangan.setColumnWidth(i,self.ukuran[i])

        self.table_penerbangan.horizontalHeader().setVisible(True)
        self.verticalLayout_3.addWidget(self.table_penerbangan)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selectID_l = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.selectID_l.setObjectName("selectID_l")
        self.selectID_l.setFont(self.header_f)
        self.horizontalLayout_2.addWidget(self.selectID_l)
        self.Pilih = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.Pilih.setObjectName("Pilih")
        self.horizontalLayout_2.addWidget(self.Pilih)
        self.btn_hapus = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_hapus.setObjectName("btn_hapus")
        self.btn_hapus.setStyleSheet("border-radius : 1; border : 2px solid black;background-color:white;"
                                     "font-size:20px;background-color:#FF230F;")
        self.btn_hapus.setFixedSize(150, 50)
        self.horizontalLayout_2.addWidget(self.btn_hapus)
        self.btn_edit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_edit.setObjectName("btn_edit")
        self.btn_edit.setStyleSheet("border-radius : 1; border : 2px solid black;background-color:white;"
                                    "font-size:20px;background-color:#E6BF33;")
        self.btn_edit.setFixedSize(150, 50)
        self.horizontalLayout_2.addWidget(self.btn_edit)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_refresh.clicked.connect(lambda terclick: self.tampilkan())
        self.btn_kembali.clicked.connect(self.act_kembali)
        self.btn_kembali.clicked.connect(MainWindow.close)
        self.btn_tambah.clicked.connect(self.act_tambah_data)
        self.btn_tambah.clicked.connect(MainWindow.close)
        self.btn_edit.clicked.connect(self.act_edit_data)
        self.btn_edit.clicked.connect(MainWindow.close)
        self.btn_hapus.clicked.connect(self.act_hapus_data)
        self.btn_hapus.clicked.connect(MainWindow.close)
        self.tampilkan()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard Admin"))
        self.tittle_l.setText(_translate("MainWindow", "DashBoard Admin"))
        self.btn_kembali.setText(_translate("MainWindow", "Keluar"))
        self.tujuan_l.setText(_translate("MainWindow", "  Tujuan : "))
        self.asal_l.setText(_translate("MainWindow", "   Asal : "))
        self.btn_refresh.setText(_translate("MainWindow", "Refresh"))
        self.btn_tambah.setText(_translate("MainWindow", "Tambah"))
        self.table_penerbangan.setSortingEnabled(True)
        self.table_penerbangan.setHorizontalHeaderLabels(["No", "Id Penerbangan", "Asal", "Tujuan",
                                                          "Tanggal", "Berangkat", "Sampai", "Maskapai",
                                                          "Harga", "Sisa Kursi"])

        self.selectID_l.setText(_translate("MainWindow", "ID Penerbangan Yang Dipilih :  "))
        self.btn_hapus.setText(_translate("MainWindow", "Hapus"))
        self.btn_edit.setText(_translate("MainWindow", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_admin = QtWidgets.QMainWindow()
    ui = ui_window_admin()
    ui.setupUi(window_admin)
    window_admin.show()
    sys.exit(app.exec_())