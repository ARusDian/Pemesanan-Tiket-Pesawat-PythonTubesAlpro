from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_dialog_tambah_data(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tubes',
        )
        self.mycursor = self.mydb.cursor()

    def act_submit_tambahdata(self):
        self.mycursor.execute(f"""INSERT INTO
        penerbangan (no_penerbangan, asal, tujuan, date_berangkat, time_berangkat, time_datang,
        maskapai, harga, kursi)
        VALUES ('{self.no_penerbangan_form.text()}','{self.asal_form.text()}','{self.tujuan_form.text()}',
        '{self.tanggal_form.text()}','{self.keberangkatan_form.text()}','{self.kedatangan_form.text()}',
        '{self.maskapai_form.text()}','{self.harga_form.text()}','{self.kursi_form.text()}')""")
        self.mydb.commit()
        from admin import ui_window_admin
        self.window_admin = QtWidgets.QMainWindow()
        self.ui_admin = ui_window_admin()
        self.ui_admin.setupUi(self.window_admin)
        self.window_admin.show()

    def act_kembali(self):
        from admin import ui_window_admin
        self.window_admin = QtWidgets.QMainWindow()
        self.ui_admin = ui_window_admin()
        self.ui_admin.setupUi(self.window_admin)
        self.window_admin.show()

    def setting_font(self):
        self.tittle_f = QtGui.QFont()
        self.tittle_f.setPointSize(16)
        self.tittle_f.setBold(True)
        self.tittle_l.setFont(self.tittle_f)
        self.header_f = QtGui.QFont()
        self.header_f.setPointSize(12)
        self.no_penerbangan_l.setFont(self.header_f)
        self.asal_l.setFont(self.header_f)
        self.tujuan_l.setFont(self.header_f)
        self.tanggal_l.setFont(self.header_f)
        self.keberangkatan_l.setFont(self.header_f)
        self.kedatangan_l.setFont(self.header_f)
        self.maskapai_l.setFont(self.header_f)
        self.harga_l.setFont(self.header_f)
        self.kursi_l.setFont(self.header_f)

    def setupUi(self, dialog_tambah_data):
        dialog_tambah_data.setObjectName("dialog_tambah_data")
        dialog_tambah_data.setFixedSize(960, 565)
        dialog_tambah_data.setWindowIcon(QtGui.QIcon('assets\icon.png'))
        self.bg = QtWidgets.QLabel(dialog_tambah_data)
        self.bg.resize(960, 565)
        self.bg.setStyleSheet("background-color:#C2DEFF;border:5px solid;")

        self.tittle_l = QtWidgets.QLabel(dialog_tambah_data)
        self.tittle_l.setGeometry(QtCore.QRect(10, 5, 451, 71))
        self.tittle_l.setObjectName("tittle_l")
        self.formLayoutWidget = QtWidgets.QWidget(dialog_tambah_data)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 70, 931, 571))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.no_penerbangan_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.no_penerbangan_l.setObjectName("no_penerbangan_l")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.no_penerbangan_l)
        self.no_penerbangan_form = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.no_penerbangan_form.setObjectName("no_penerbangan_form")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.no_penerbangan_form)
        self.asal_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.asal_l.setObjectName("asal_l")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.asal_l)
        self.asal_form = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.asal_form.setObjectName("asal_form")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.asal_form)
        self.tujuan_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.tujuan_l.setObjectName("tujuan_l")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tujuan_l)
        self.tujuan_form = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.tujuan_form.setObjectName("tujuan_form")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tujuan_form)
        self.tanggal_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.tanggal_l.setObjectName("tanggal_l")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.tanggal_l)
        self.tanggal_form = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.tanggal_form.setObjectName("tanggal_form")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tanggal_form)
        self.keberangkatan_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.keberangkatan_l.setObjectName("keberangkatan_l")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.keberangkatan_l)
        self.keberangkatan_form = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.keberangkatan_form.setObjectName("keberangkatan_form")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.keberangkatan_form)
        self.kedatangan_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.kedatangan_l.setObjectName("kedatangan_l")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.kedatangan_l)
        self.kedatangan_form = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kedatangan_form.setObjectName("kedatangan_form")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.kedatangan_form)
        self.maskapai_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.maskapai_l.setObjectName("maskapai_l")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.maskapai_l)
        self.maskapai_form = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.maskapai_form.setObjectName("maskapai_form")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.maskapai_form)
        self.harga_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.harga_l.setObjectName("harga_l")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.harga_l)
        self.harga_form = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.harga_form.setObjectName("harga_form")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.harga_form)
        self.kursi_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.kursi_l.setObjectName("kursi_l")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.kursi_l)
        self.kursi_form = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kursi_form.setObjectName("kursi_form")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.kursi_form)
        self.btn_tambahdata = QtWidgets.QPushButton(dialog_tambah_data)
        self.btn_tambahdata.setGeometry(QtCore.QRect(700, 450, 151, 71))
        self.btn_tambahdata.setObjectName("btn_tambahdata")
        self.btn_tambahdata.setFixedSize(200, 70)
        self.btn_tambahdata.setStyleSheet("border-radius : 10; border : 2px solid black;background-color:white;"
                                          "font-size:25px;background-color:#0066DB;")
        self.btn_tambahdata.clicked.connect(self.act_submit_tambahdata)
        self.btn_tambahdata.clicked.connect(dialog_tambah_data.close)
        self.btn_kembali = QtWidgets.QPushButton(dialog_tambah_data)
        self.btn_kembali.setObjectName("btn_kembali")
        self.btn_kembali.setGeometry(50,450,200, 70)
        self.btn_kembali.setStyleSheet("border-radius : 10; border : 2px solid black;background-color:white;"
                                       "font-size:25px;background-color:#94C6FF;")
        self.btn_kembali.clicked.connect(self.act_kembali)
        self.btn_kembali.clicked.connect(dialog_tambah_data.close)
        self.setting_font()
        self.retranslateUi(dialog_tambah_data)
        QtCore.QMetaObject.connectSlotsByName(dialog_tambah_data)

    def retranslateUi(self, dialog_tambah_data):
        _translate = QtCore.QCoreApplication.translate
        dialog_tambah_data.setWindowTitle(_translate("dialog_tambah_data", "Tambah Data"))
        self.tittle_l.setText(_translate("dialog_tambah_data", "Tambah Data Penerbangan"))
        self.no_penerbangan_l.setText(_translate("dialog_tambah_data", "No Penerbangan                         "))
        self.asal_l.setText(_translate("dialog_tambah_data", "Asal                                           "))
        self.tujuan_l.setText(_translate("dialog_tambah_data", "Tujuan                                      "))
        self.tanggal_l.setText(_translate("dialog_tambah_data", "Tanggal Penerbangan                  "))
        self.keberangkatan_l.setText(_translate("dialog_tambah_data", "Jam Keberangkatan"))
        self.kedatangan_l.setText(_translate("dialog_tambah_data", "Jam Kedatangan "))
        self.maskapai_l.setText(_translate("dialog_tambah_data", "Maskapai"))
        self.harga_l.setText(_translate("dialog_tambah_data", "Harga"))
        self.kursi_l.setText(_translate("dialog_tambah_data", "Sisa kursi"))
        self.btn_tambahdata.setText(_translate("dialog_tambah_data", "Tambahkan Data"))
        self.btn_kembali.setText(_translate("MainWindow", "Kembali"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_tambah_data = QtWidgets.QDialog()
    ui = Ui_dialog_tambah_data()
    ui.setupUi(dialog_tambah_data)
    dialog_tambah_data.show()
    sys.exit(app.exec_())