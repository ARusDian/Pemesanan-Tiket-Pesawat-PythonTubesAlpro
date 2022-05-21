from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class ui_hapus_data(object):
    def __init__(self,id):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tubes',
        )
        self.mycursor = self.mydb.cursor()
        self.id = id

    def act_hapusdata(self,Dialog):
        try:
            self.mycursor.execute(f"DELETE FROM penerbangan WHERE no_penerbangan = '{self.id}'")
            self.mydb.commit()
            from admin import ui_window_admin
            self.window_admin = QtWidgets.QMainWindow()
            self.ui_admin = ui_window_admin()
            self.ui_admin.setupUi(self.window_admin)
            Dialog.close()
            self.window_admin.show()

        except :
            print("data gagal dihapus")

    def act_batal(self):
        from admin import ui_window_admin
        self.window_admin = QtWidgets.QMainWindow()
        self.ui_admin = ui_window_admin()
        self.ui_admin.setupUi(self.window_admin)
        self.window_admin.show()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(640, 400)
        Dialog.setWindowIcon(QtGui.QIcon('assets\icon.png'))
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.resize(640, 400)
        self.bg.setStyleSheet("background-color:#FF707A;border:5px solid;")
        self.header_f = QtGui.QFont()
        self.header_f.setPointSize(10)
        self.memastikan_l = QtWidgets.QLabel(Dialog)
        self.memastikan_l.setGeometry(QtCore.QRect(30, 70, 581, 111))
        self.memastikan_l.setObjectName("memastikan_l")
        self.memastikan_l.setFont(self.header_f)
        self.btn_hapusdata = QtWidgets.QPushButton(Dialog)
        self.btn_hapusdata.setGeometry(QtCore.QRect(470, 300, 111, 61))
        self.btn_hapusdata.setObjectName("btn_hapusdata")
        self.btn_hapusdata.setStyleSheet("border-radius : 10; border : 2px solid black;background-color:white;"
                                         "font-size:25px;background-color:#FF230F;")
        self.btn_batalhapus = QtWidgets.QPushButton(Dialog)
        self.btn_batalhapus.setGeometry(QtCore.QRect(330, 300, 111, 61))
        self.btn_batalhapus.setObjectName("btn_batalhapus")
        self.btn_batalhapus.setStyleSheet("border-radius : 10; border : 2px solid black;background-color:white;"
                                          "font-size:25px;background-color:#94C6FF;")
        self.memastikan_l.setText(f"Yakin Ingin Menghapus Data Penerbangan\n"
                                  f"dengan No Penerbangan {self.id} ?")
        
        self.btn_hapusdata.clicked.connect(lambda x :self.act_hapusdata(Dialog))
        self.btn_hapusdata.clicked.connect(Dialog.close)
        self.btn_batalhapus.clicked.connect(self.act_batal)
        self.btn_batalhapus.clicked.connect(Dialog.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Hapus Data"))
        self.btn_hapusdata.setText(_translate("Dialog", "Hapus"))
        self.btn_batalhapus.setText(_translate("Dialog", "Batal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ui_hapus_data()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())