from PyQt5 import QtCore, QtGui, QtWidgets


class UiDialogValid(object):
    def __init__(self):
        self.password = "manahatigantenk123"
        self.jumlah_salah = 0

    def act_kembali(self):
        from landing import Landing
        self.window_landing = QtWidgets.QMainWindow()
        self.ui_landing = Landing()
        self.ui_landing.tampil(self.window_landing)
        self.window_landing.show()

    def act_submit(self,Dialog):
        if self.form_kode_administrator.text() == self.password:
            from admin import ui_window_admin
            self.window_admin = QtWidgets.QMainWindow()
            self.ui_admin = ui_window_admin()
            self.ui_admin.setupUi(self.window_admin)
            self.window_admin.show()
            self.jumlah_salah = 0
            Dialog.close()
        elif self.form_kode_administrator.text() != self.password and self.jumlah_salah < 3:
            self.salah_l.setText("Kode yang anda masukkan tidak valid")
            self.jumlah_salah += 1
        else:
            self.salah_l.setText("Kode yang anda masukkan tidak valid")
            self.clue_l.setText("Clue :")
            self.clue_item.setText("Orang Terganteng di Alpro D")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(840, 600)
        Dialog.setWindowIcon(QtGui.QIcon('assets\icon.png'))
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.resize(840, 600)
        self.bg.setStyleSheet("background-color:#C2DEFF;border:3px solid;")
        self.header_f = QtGui.QFont()
        self.header_f.setPointSize(12)

        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 100, 821, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.form_header = QtWidgets.QLabel(self.formLayoutWidget)
        self.form_header.setObjectName("form_header")
        self.form_header.setFont(self.header_f)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.form_header)
        self.administrator_l = QtWidgets.QLabel(self.formLayoutWidget)
        self.administrator_l.setObjectName("administrator_l")
        self.administrator_l.setFont(self.header_f)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.administrator_l)
        self.form_kode_administrator = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.form_kode_administrator.setObjectName("form_kode_administrator")
        self.form_kode_administrator.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.form_kode_administrator)
        self.form_header.raise_()
        self.form_kode_administrator.raise_()
        self.administrator_l.raise_()

        self.tittle_f = QtGui.QFont()
        self.tittle_f.setPointSize(14)
        self.tittle_l = QtWidgets.QLabel(Dialog)
        self.tittle_l.setGeometry(QtCore.QRect(10, 40, 350, 61))
        self.tittle_l.setObjectName("tittle_l")
        self.tittle_l.setFont(self.tittle_f)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 280, 451, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clue_l = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.clue_l.setObjectName("clue_l")
        self.clue_l.setFont(self.header_f)
        self.verticalLayout.addWidget(self.clue_l)
        self.clue_item = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.clue_item.setObjectName("clue_item")
        self.clue_item.setFont(self.header_f)
        self.verticalLayout.addWidget(self.clue_item)
        self.btn_submit = QtWidgets.QPushButton(Dialog)
        self.btn_submit.setGeometry(QtCore.QRect(650, 500, 131, 51))
        self.btn_submit.setObjectName("pushButton")
        self.btn_submit.setStyleSheet("border-radius : 20; border : 2px solid black;background-color:white;"
                                      "font-size:27px;background-color:#4783F0;")
        self.salah_l = QtWidgets.QLabel(Dialog)
        self.salah_l.setGeometry(QtCore.QRect(530, 60, 401, 20))
        self.salah_l.setObjectName("salah_l")
        self.salah_l.setStyleSheet("color:red;")
        self.btn_kembali = QtWidgets.QPushButton(Dialog)
        self.btn_kembali.setObjectName("btn_kembali")
        self.btn_kembali.setGeometry(QtCore.QRect(250, 500, 351, 51))
        self.btn_kembali.setStyleSheet("border-radius : 10; border : 2px solid black;background-color:white;"
                                       "font-size:25px;background-color:#94C6FF;")

        self.btn_kembali.clicked.connect(self.act_kembali)
        self.btn_kembali.clicked.connect(Dialog.close)
        self.btn_submit.clicked.connect(lambda klik:self.act_submit(Dialog))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Validasi Akses"))
        self.form_header.setText(_translate("Dialog", "Masukkan Kode Administrator"))
        self.administrator_l.setText(_translate("Dialog", "Kode Administrator      :"))
        self.tittle_l.setText(_translate("Dialog", "Form Validasi Administrator"))
        self.btn_submit.setText(_translate("Dialog", "Submit"))
        self.btn_kembali.setText(_translate("Dialog", "Kembali ke Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_valid = QtWidgets.QDialog()
    ui = UiDialogValid()
    ui.setupUi(dialog_valid)
    dialog_valid.show()
    sys.exit(app.exec_())