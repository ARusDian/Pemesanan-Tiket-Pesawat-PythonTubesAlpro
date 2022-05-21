from PyQt5 import QtCore, QtGui, QtWidgets


class ui_konverter(object):

    def act_btnclear(self):
        self.lineEdit_inputan.clear()
        self.lineEdit_hasil.clear()
    def act_btnkonvert(self):  # ['°C','°R','°F','K']
        try:
            self.inputan = eval(self.lineEdit_inputan.text())
            # Awal Celcius
            if self.comboBox_inputan.currentText() == "°C":
                if self.comboBox_hasil.currentText() == "°C":  # Celcius ke Celcius
                    self.lineEdit_hasil.setText(str(self.inputan))
                elif self.comboBox_hasil.currentText() == "°R":  # Celcius ke Reamur
                    self.lineEdit_hasil.setText(str(4 * self.inputan / 5))
                elif self.comboBox_hasil.currentText() == "°F":  # Celcius ke Fahrenheit
                    self.lineEdit_hasil.setText(str(9 * self.inputan / 5 + 32))
                elif self.comboBox_hasil.currentText() == "K":  # Celcius ke Kelvin
                    self.lineEdit_hasil.setText(str(self.inputan + 273))
            # Awal Reamur
            elif self.comboBox_inputan.currentText() == "°R":
                if self.comboBox_hasil.currentText() == "°C":  # Reamur ke Celcius
                    self.lineEdit_hasil.setText(str((5 / 4) * self.inputan))
                elif self.comboBox_hasil.currentText() == "°R":  # Reamur ke Reamur
                    self.lineEdit_hasil.setText(str(self.inputan))
                elif self.comboBox_hasil.currentText() == "°F":  # Reamur ke Fahrenheit
                    self.lineEdit_hasil.setText(str(9 * self.inputan / 4 + 32))
                elif self.comboBox_hasil.currentText() == "K":  # Reamur ke Kelvin
                    self.lineEdit_hasil.setText(str(5 * self.inputan / 4 + 273))
            # Awal Fahrenheit
            elif self.comboBox_inputan.currentText() == "°F":
                if self.comboBox_hasil.currentText() == "°C":  # Fahrenheit ke Celcius
                    self.lineEdit_hasil.setText(str((5 / 9) * (self.inputan - 32)))
                elif self.comboBox_hasil.currentText() == "°R":  # Fahrenheit ke Reamur
                    self.lineEdit_hasil.setText(str((self.inputan - 32) * 4 / 9))
                elif self.comboBox_hasil.currentText() == "°F":  # Fahrenheit ke Fahrenheit
                    self.lineEdit_hasil.setText(str(self.inputan))
                elif self.comboBox_hasil.currentText() == "K":  # Fahrenheit ke Kelvin
                    self.lineEdit_hasil.setText(str((self.inputan - 32) * 5 / 9 + 273))
            # Awal Kelvin
            elif self.comboBox_inputan.currentText() == "K":
                if self.comboBox_hasil.currentText() == "°C":  # Kelvin ke Celcius
                    self.lineEdit_hasil.setText(str(self.inputan - 273))
                elif self.comboBox_hasil.currentText() == "°R":  # Kelvin ke Reamur
                    self.lineEdit_hasil.setText(str((self.inputan - 273) * 4 / 5))
                elif self.comboBox_hasil.currentText() == "°F":  # Kelvin ke Fahrenheit
                    self.lineEdit_hasil.setText(str((self.inputan - 273) * 9 / 5 + 32))
                elif self.comboBox_hasil.currentText() == "K":  # Kelvin ke Kelvin
                    self.lineEdit_hasil.setText(str(self.inputan))
        except:
            QMesgBox = QtWidgets.QMessageBox()
            QMesgBox.setText("Pastikan Angka yang ingin di konversi benar")
            QMesgBox.exec()

    def setupUi(self, MainWindow):
        self.bg = QtWidgets.QLabel(MainWindow)
        self.bg.setFixedSize(500, 600)
        self.bg.setStyleSheet("background-color:#c9d8e8")
        self.navbarbg = QtWidgets.QLabel(MainWindow)
        self.navbarbg.setFixedSize(500, 75)
        self.navbarbg.setStyleSheet("background-color:#007acc")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.jfif'))
        MainWindow.setWindowTitle(" SuhuKu")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_judul = QtWidgets.QLabel(self.centralwidget)
        self.label_judul.setGeometry(QtCore.QRect(20, 20, 301, 41))
        self.label_judul.setObjectName("label_judul")
        self.label_judul.setText("Konverter Suhu")
        self.label_judul.setStyleSheet("font-size:32px;color:white;font:bold Arial,sans-serif")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 320, 460, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_0.setObjectName("btn_0")
        self.btn_0.setText("0")
        self.btn_0.setFixedHeight(50)
        self.btn_0.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "0"))
        self.btn_0.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.gridLayout.addWidget(self.btn_0, 3, 0, 1, 1)

        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName("btn_1")
        self.btn_1.setText("1")
        self.btn_1.setFixedHeight(50)
        self.btn_1.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_1.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "1"))
        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName("btn_2")
        self.btn_2.setText("2")
        self.btn_2.setFixedHeight(50)
        self.btn_2.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_2.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "2"))
        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName("btn_3")
        self.btn_3.setText("3")
        self.btn_3.setFixedHeight(50)
        self.btn_3.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_3.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "3"))
        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName("btn_4")
        self.btn_4.setText("4")
        self.btn_4.setFixedHeight(50)
        self.btn_4.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_4.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "4"))
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName("btn_5")
        self.btn_5.setText("5")
        self.btn_5.setFixedHeight(50)
        self.btn_5.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_5.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "5"))
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_6.setObjectName("btn_6")
        self.btn_6.setText("6")
        self.btn_6.setFixedHeight(50)
        self.btn_6.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_6.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "6"))
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName("btn_7")
        self.btn_7.setText("7")
        self.btn_7.setFixedHeight(50)
        self.btn_7.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_7.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "7"))
        self.gridLayout.addWidget(self.btn_7, 2, 0, 1, 1)

        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName("btn_8")
        self.btn_8.setText("8")
        self.btn_8.setFixedHeight(50)
        self.btn_8.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_8.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "8"))
        self.gridLayout.addWidget(self.btn_8, 2, 1, 1, 1)

        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName("btn_9")
        self.btn_9.setText("9")
        self.btn_9.setFixedHeight(50)
        self.btn_9.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_9.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "9"))
        self.gridLayout.addWidget(self.btn_9, 2, 2, 1, 1)

        self.btn_C = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_C.setObjectName("btn_C")
        self.btn_C.setText("C")
        self.btn_C.setFixedHeight(50)
        self.btn_C.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_C.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text()[:-1]))
        self.gridLayout.addWidget(self.btn_C, 0, 3, 1, 1)

        self.btn_dot = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_dot.setText(".")
        self.btn_dot.setFixedHeight(50)
        self.btn_dot.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_dot.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "."))
        self.gridLayout.addWidget(self.btn_dot, 3, 1, 1, 1)

        self.btn_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_minus.setText("-")
        self.btn_minus.setFixedHeight(50)
        self.btn_minus.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 40px;")
        self.btn_minus.clicked.connect(lambda klik:self.lineEdit_inputan.setText(self.lineEdit_inputan.text() + "-"))
        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_clear.setObjectName("btn_pindah")
        self.btn_clear.setText("AC")
        self.btn_clear.setFixedHeight(50)
        self.btn_clear.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 20px;")
        self.btn_clear.clicked.connect(self.act_btnclear)
        self.gridLayout.addWidget(self.btn_clear, 1, 3, 1, 1)

        self.btn_konvert = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_konvert.setObjectName("pushButton")
        self.btn_konvert.setText("=")
        self.btn_konvert.setFixedHeight(50)
        self.btn_konvert.setStyleSheet("border-style:inset;border-width: 1px;background-color:white;font-size: 25px;")
        self.btn_konvert.clicked.connect(self.act_btnkonvert)
        self.gridLayout.addWidget(self.btn_konvert, 3, 2, 1, 2)

        self.label_inputan = QtWidgets.QLabel(self.centralwidget)
        self.label_inputan.setGeometry(QtCore.QRect(10, 120, 91, 41))
        self.label_inputan.setObjectName("label_inputan")
        self.label_inputan.setText("Input")
        self.label_inputan.setStyleSheet("font-size:20px")

        self.lineEdit_inputan = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_inputan.setGeometry(QtCore.QRect(100, 110, 309, 61))
        self.lineEdit_inputan.setObjectName("lineEdit_inputan")
        self.lineEdit_inputan.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit_inputan.setReadOnly(True)

        self.comboBox_inputan = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_inputan.setGeometry(QtCore.QRect(408, 110, 71, 61))
        self.comboBox_inputan.setObjectName("comboBox_inputan")
        self.comboBox_inputan.addItems(['°C', '°R', '°F', 'K'])

        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(10, 230, 91, 41))
        self.label_output.setObjectName("label_output")
        self.label_output.setText("Output")
        self.label_output.setStyleSheet("font-size:20px")

        self.lineEdit_hasil = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_hasil.setGeometry(QtCore.QRect(100, 220, 309, 61))
        self.lineEdit_hasil.setObjectName("lineEdit_hasil")
        self.lineEdit_hasil.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit_hasil.setReadOnly(True)

        self.comboBox_hasil = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_hasil.setGeometry(QtCore.QRect(408, 220, 71, 61))
        self.comboBox_hasil.setObjectName("comboBox_hasil")
        self.comboBox_hasil.addItems(['°C', '°R', '°F', 'K'])

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_konverter()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
