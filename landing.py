from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon


class Landing(object):

    def pencet(self):
        from pesan import UiWindowPemesanan
        self.window_pemesanan = QMainWindow()
        self.ui_pesan = UiWindowPemesanan()
        self.ui_pesan.setupUi(self.window_pemesanan)
        self.window_pemesanan.show()

    def admin(self):
        from valid import UiDialogValid
        self.dialog_valid = QDialog()
        self.ui_valid = UiDialogValid()
        self.ui_valid.setupUi(self.dialog_valid)
        self.dialog_valid.show()

    def tampil(self, window_land):
        window_land.setWindowIcon(QIcon('assets\icon.png'))
        window_land.setWindowTitle("Landing Page")
        window_land.move(350, 120)
        window_land.setFixedSize(1200, 740)

        self.bggambar = QLabel(window_land)
        self.bggambar.setPixmap(QPixmap('assets\logo-01.jpg'))
        self.bggambar.setScaledContents(True)
        self.bggambar.setGeometry(0, 0, 1200, 740)

        self.btn_to_pesan = QPushButton(window_land)
        self.btn_to_pesan.setGeometry(150, 600, 200, 70)
        self.btn_to_pesan.setText("Pesan")
        self.btn_to_pesan.setStyleSheet("border-radius : 28; border : 2px solid black;background-color:white;"
                                        "font-size:27px;background-color:#4783F0;")

        self.btn_to_admin = QPushButton(window_land)
        self.btn_to_admin.setGeometry(800, 600, 200, 70)
        self.btn_to_admin.setText("Admin")
        self.btn_to_admin.setStyleSheet("border-radius : 28; border : 2px solid black;background-color:white;"
                                        "font-size:27px;background-color:#4783F0;")

        self.btn_quit = QPushButton(window_land)
        self.btn_quit.setGeometry(1050, 30, 100, 50)
        self.btn_quit.setText("Keluar")
        self.btn_quit.setStyleSheet("border-radius : 20; border : 2px solid black;background-color:white;"
                                    "font-size:22px;background-color:#FF707A;")

        self.btn_to_pesan.clicked.connect(self.pencet)
        self.btn_to_pesan.clicked.connect(window_land.close)
        self.btn_to_admin.clicked.connect(self.admin)
        self.btn_to_admin.clicked.connect(window_land.close)
        self.btn_quit.clicked.connect(window_land.close)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    landing_window = QMainWindow()
    ui_landing = Landing()
    ui_landing.tampil(landing_window)
    landing_window.show()
    sys.exit(app.exec_())