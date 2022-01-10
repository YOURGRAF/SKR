from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_all_connections(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 530, 530))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.all_connections = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.all_connections.setGeometry(QtCore.QRect(20, 20, 490, 490))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.all_connections.setFont(font)
        self.all_connections.setStyleSheet("QPlainTextEdit{\n"
                                           " background: rgba(255, 255, 255, 0.05);\n"
                                           " border-radius: 8px;\n"
                                           " color: #e3eded;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           " background: rgba(255, 255, 255, 0.1);\n"
                                           "}")
        self.all_connections.setPlainText("")
        self.all_connections.setObjectName("all_connections")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))


class Ui_changing_router_data(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 650, 350))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(10, 7, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color:#e3eded")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(10, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color:#e3eded")
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(340, 7, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3.setFont(font)
        self.text_3.setStyleSheet("color:#e3eded")
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(340, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4.setFont(font)
        self.text_4.setStyleSheet("color:#e3eded")
        self.text_4.setObjectName("text_4")
        self.login_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.login_1.setGeometry(QtCore.QRect(10, 83, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.login_1.setFont(font)
        self.login_1.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                   "border-radius: 8px;\n"
                                   "color:#e3eded;\n"
                                   "")
        self.login_1.setText("")
        self.login_1.setObjectName("login_1")
        self.password_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_1.setGeometry(QtCore.QRect(340, 83, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.password_1.setFont(font)
        self.password_1.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                      "border-radius: 8px;\n"
                                      "color:#e3eded;\n"
                                      "")
        self.password_1.setText("")
        self.password_1.setObjectName("password_1")
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(10, 123, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_5.setFont(font)
        self.text_5.setStyleSheet("color:#e3eded")
        self.text_5.setObjectName("text_5")
        self.text_6 = QtWidgets.QLabel(self.centralwidget)
        self.text_6.setGeometry(QtCore.QRect(10, 153, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_6.setFont(font)
        self.text_6.setStyleSheet("color:#e3eded")
        self.text_6.setObjectName("text_6")
        self.login_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.login_2.setGeometry(QtCore.QRect(10, 196, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.login_2.setFont(font)
        self.login_2.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                   "border-radius: 8px;\n"
                                   "color:#e3eded;\n"
                                   "")
        self.login_2.setText("")
        self.login_2.setObjectName("login_2")
        self.password_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_2.setGeometry(QtCore.QRect(340, 196, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.password_2.setFont(font)
        self.password_2.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                      "border-radius: 8px;\n"
                                      "color:#e3eded;\n"
                                      "")
        self.password_2.setText("")
        self.password_2.setObjectName("password_2")
        self.text_7 = QtWidgets.QLabel(self.centralwidget)
        self.text_7.setGeometry(QtCore.QRect(340, 120, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_7.setFont(font)
        self.text_7.setStyleSheet("color:#e3eded")
        self.text_7.setObjectName("text_7")
        self.text_8 = QtWidgets.QLabel(self.centralwidget)
        self.text_8.setGeometry(QtCore.QRect(340, 153, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_8.setFont(font)
        self.text_8.setStyleSheet("color:#e3eded")
        self.text_8.setObjectName("text_8")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setGeometry(QtCore.QRect(165, 280, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.accept_button.setFont(font)
        self.accept_button.setStyleSheet("QPushButton{\n"
                                         " background: rgba(255, 255, 255, 0.05);\n"
                                         " border-radius: 8px;\n"
                                         " color:#e3eded;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: rgba(255, 255, 255, 0.1);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: rgba(0, 0, 0, 0.1);\n"
                                         "}")
        self.accept_button.setObjectName("accept_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", "Введите новый"))
        self.text_2.setText(_translate("MainWindow", "логин:"))
        self.text_3.setText(_translate("MainWindow", "Введите новый"))
        self.text_4.setText(_translate("MainWindow", "пароль:"))
        self.text_5.setText(_translate("MainWindow", "Подтвердите новый"))
        self.text_6.setText(_translate("MainWindow", "логин:"))
        self.text_7.setText(_translate("MainWindow", "Подтвердите новый"))
        self.text_8.setText(_translate("MainWindow", "пароль:"))
        self.accept_button.setText(_translate("MainWindow", "Принять"))


class Ui_data_change_wifi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 650, 350))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(10, 7, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color:#e3eded")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(10, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color:#e3eded")
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(340, 7, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3.setFont(font)
        self.text_3.setStyleSheet("color:#e3eded")
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(340, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4.setFont(font)
        self.text_4.setStyleSheet("color:#e3eded")
        self.text_4.setObjectName("text_4")
        self.login_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.login_1.setGeometry(QtCore.QRect(10, 83, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.login_1.setFont(font)
        self.login_1.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                   "border-radius: 8px;\n"
                                   "color:#e3eded;\n"
                                   "")
        self.login_1.setText("")
        self.login_1.setObjectName("login_1")
        self.password_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_1.setGeometry(QtCore.QRect(340, 83, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.password_1.setFont(font)
        self.password_1.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                      "border-radius: 8px;\n"
                                      "color:#e3eded;\n"
                                      "")
        self.password_1.setText("")
        self.password_1.setObjectName("password_1")
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(10, 123, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_5.setFont(font)
        self.text_5.setStyleSheet("color:#e3eded")
        self.text_5.setObjectName("text_5")
        self.text_6 = QtWidgets.QLabel(self.centralwidget)
        self.text_6.setGeometry(QtCore.QRect(10, 153, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_6.setFont(font)
        self.text_6.setStyleSheet("color:#e3eded")
        self.text_6.setObjectName("text_6")
        self.login_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.login_2.setGeometry(QtCore.QRect(10, 196, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.login_2.setFont(font)
        self.login_2.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                   "border-radius: 8px;\n"
                                   "color:#e3eded;\n"
                                   "")
        self.login_2.setText("")
        self.login_2.setObjectName("login_2")
        self.password_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_2.setGeometry(QtCore.QRect(340, 196, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.password_2.setFont(font)
        self.password_2.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                      "border-radius: 8px;\n"
                                      "color:#e3eded;\n"
                                      "")
        self.password_2.setText("")
        self.password_2.setObjectName("password_2")
        self.text_7 = QtWidgets.QLabel(self.centralwidget)
        self.text_7.setGeometry(QtCore.QRect(340, 120, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_7.setFont(font)
        self.text_7.setStyleSheet("color:#e3eded")
        self.text_7.setObjectName("text_7")
        self.text_8 = QtWidgets.QLabel(self.centralwidget)
        self.text_8.setGeometry(QtCore.QRect(340, 153, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_8.setFont(font)
        self.text_8.setStyleSheet("color:#e3eded")
        self.text_8.setObjectName("text_8")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setGeometry(QtCore.QRect(165, 280, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.accept_button.setFont(font)
        self.accept_button.setStyleSheet("QPushButton{\n"
                                         " background: rgba(255, 255, 255, 0.05);\n"
                                         " border-radius: 8px;\n"
                                         " color:#e3eded;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: rgba(255, 255, 255, 0.1);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: rgba(0, 0, 0, 0.1);\n"
                                         "}")
        self.accept_button.setObjectName("accept_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", "Введите новый"))
        self.text_2.setText(_translate("MainWindow", "логин:"))
        self.text_3.setText(_translate("MainWindow", "Введите новый"))
        self.text_4.setText(_translate("MainWindow", "пароль:"))
        self.text_5.setText(_translate("MainWindow", "Подтвердите новый"))
        self.text_6.setText(_translate("MainWindow", "логин:"))
        self.text_7.setText(_translate("MainWindow", "Подтвердите новый"))
        self.text_8.setText(_translate("MainWindow", "пароль:"))
        self.accept_button.setText(_translate("MainWindow", "Принять"))


class Ui_deleting_and_adding_groups(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 900, 530))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.info_group = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.info_group.setGeometry(QtCore.QRect(490, 20, 391, 490))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.info_group.setFont(font)
        self.info_group.setStyleSheet("QPlainTextEdit{\n"
                                      " background: rgba(255, 255, 255, 0.05);\n"
                                      " border-radius: 8px;\n"
                                      " color: #e3eded;\n"
                                      "}\n"
                                      "QPlainTextEdit:hover{\n"
                                      " background: rgba(255, 255, 255, 0.1);\n"
                                      "}")
        self.info_group.setPlainText("")
        self.info_group.setObjectName("info_group")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(20, 20, 450, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_1.setObjectName("text_1")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setGeometry(QtCore.QRect(20, 360, 450, 150))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.accept_button.setFont(font)
        self.accept_button.setStyleSheet("QPushButton{\n"
                                         " background: rgba(255, 255, 255, 0.05);\n"
                                         " border-radius: 8px;\n"
                                         " color: #fff;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: rgba(255, 255, 255, 0.1);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: rgba(0, 0, 0, 0.1);\n"
                                         "}")
        self.accept_button.setObjectName("accept_button")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(20, 80, 440, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_2.setObjectName("text_2")
        self.input_group = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_group.setGeometry(QtCore.QRect(20, 150, 450, 190))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.input_group.setFont(font)
        self.input_group.setStyleSheet("QPlainTextEdit{\n"
                                       " background: rgba(255, 255, 255, 0.05);\n"
                                       " border-radius: 8px;\n"
                                       " color: #e3eded;\n"
                                       "}\n"
                                       "QPlainTextEdit:hover{\n"
                                       " background: rgba(255, 255, 255, 0.1);\n"
                                       "}")
        self.input_group.setPlainText("")
        self.input_group.setObjectName("input_group")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", ""))
        self.accept_button.setText(_translate("MainWindow", "Принять"))
        self.text_2.setText(_translate("MainWindow", "(Каждую с новой строки):"))


class Ui_error(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 145)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 440, 145))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/error.png"))
        self.gradient.setObjectName("gradient")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(80, 40, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.text_1.setFont(font)
        self.text_1.setText("")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(80, 60, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.text_2.setFont(font)
        self.text_2.setText("")
        self.text_2.setObjectName("text_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ошибка"))


class Ui_general_network_settings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 700, 540))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.connect_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_info_button.setGeometry(QtCore.QRect(19, 19, 321, 241))
        self.connect_info_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.connect_info_button.setText("")
        self.connect_info_button.setObjectName("connect_info_button")
        self.all_connections_button = QtWidgets.QPushButton(self.centralwidget)
        self.all_connections_button.setGeometry(QtCore.QRect(20, 280, 320, 240))
        self.all_connections_button.setStyleSheet("QPushButton{\n"
                                                  " background: rgba(255, 255, 255, 0.05);\n"
                                                  " border-radius: 8px;\n"
                                                  " color: #fff;\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  " background: rgba(255, 255, 255, 0.1);\n"
                                                  "}\n"
                                                  "QPushButton:pressed{\n"
                                                  " background: rgba(0, 0, 0, 0.1);\n"
                                                  "}")
        self.all_connections_button.setText("")
        self.all_connections_button.setObjectName("all_connections_button")
        self.data_change_router_button = QtWidgets.QPushButton(self.centralwidget)
        self.data_change_router_button.setGeometry(QtCore.QRect(360, 20, 320, 240))
        self.data_change_router_button.setStyleSheet("QPushButton{\n"
                                                     " background: rgba(255, 255, 255, 0.05);\n"
                                                     " border-radius: 8px;\n"
                                                     " color: #fff;\n"
                                                     "}\n"
                                                     "QPushButton:hover{\n"
                                                     " background: rgba(255, 255, 255, 0.1);\n"
                                                     "}\n"
                                                     "QPushButton:pressed{\n"
                                                     " background: rgba(0, 0, 0, 0.1);\n"
                                                     "}")
        self.data_change_router_button.setText("")
        self.data_change_router_button.setObjectName("data_change_router_button")
        self.initial_settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.initial_settings_button.setGeometry(QtCore.QRect(360, 280, 320, 240))
        self.initial_settings_button.setStyleSheet("QPushButton{\n"
                                                   " background: rgba(255, 255, 255, 0.05);\n"
                                                   " border-radius: 8px;\n"
                                                   " color: #fff;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   " background: rgba(255, 255, 255, 0.1);\n"
                                                   "}\n"
                                                   "QPushButton:pressed{\n"
                                                   " background: rgba(0, 0, 0, 0.1);\n"
                                                   "}")
        self.initial_settings_button.setText("")
        self.initial_settings_button.setObjectName("initial_settings_button")
        self.data_change_wifi_button = QtWidgets.QPushButton(self.centralwidget)
        self.data_change_wifi_button.setGeometry(QtCore.QRect(20, 20, 320, 240))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.data_change_wifi_button.setFont(font)
        self.data_change_wifi_button.setStyleSheet("QPushButton{\n"
                                                   " background: rgba(255, 255, 255, 0.05);\n"
                                                   " border-radius: 8px;\n"
                                                   " color: #fff;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   " background: rgba(255, 255, 255, 0.1);\n"
                                                   "}\n"
                                                   "QPushButton:pressed{\n"
                                                   " background: rgba(0, 0, 0, 0.1);\n"
                                                   "}")
        self.data_change_wifi_button.setText("")
        self.data_change_wifi_button.setObjectName("data_change_wifi_button")
        self.text_1_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1_1.setGeometry(QtCore.QRect(35, 90, 290, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1_1.setFont(font)
        self.text_1_1.setStyleSheet("color:#e3eded")
        self.text_1_1.setObjectName("text_1_1")
        self.text_1_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_1_2.setGeometry(QtCore.QRect(145, 140, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1_2.setFont(font)
        self.text_1_2.setStyleSheet("color:#e3eded")
        self.text_1_2.setObjectName("text_1_2")
        self.text_2_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_2_1.setGeometry(QtCore.QRect(375, 90, 290, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2_1.setFont(font)
        self.text_2_1.setStyleSheet("color:#e3eded")
        self.text_2_1.setObjectName("text_2_1")
        self.text_2_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2_2.setGeometry(QtCore.QRect(460, 140, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2_2.setFont(font)
        self.text_2_2.setStyleSheet("color:#e3eded")
        self.text_2_2.setObjectName("text_2_2")
        self.text_3_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_3_1.setGeometry(QtCore.QRect(95, 350, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3_1.setFont(font)
        self.text_3_1.setStyleSheet("color:#e3eded")
        self.text_3_1.setObjectName("text_3_1")
        self.text_4_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_4_1.setGeometry(QtCore.QRect(365, 350, 310, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4_1.setFont(font)
        self.text_4_1.setStyleSheet("color:#e3eded")
        self.text_4_1.setObjectName("text_4_1")
        self.text_3_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_3_2.setGeometry(QtCore.QRect(75, 400, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3_2.setFont(font)
        self.text_3_2.setStyleSheet("color:#e3eded")
        self.text_3_2.setObjectName("text_3_2")
        self.text_4_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_4_2.setGeometry(QtCore.QRect(450, 400, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4_2.setFont(font)
        self.text_4_2.setStyleSheet("color:#e3eded")
        self.text_4_2.setObjectName("text_4_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1_1.setText(_translate("MainWindow", "Изменение данных"))
        self.text_1_2.setText(_translate("MainWindow", "WIFI"))
        self.text_2_1.setText(_translate("MainWindow", "Изменение данных"))
        self.text_2_2.setText(_translate("MainWindow", "роутера"))
        self.text_3_1.setText(_translate("MainWindow", "Показ всех"))
        self.text_4_1.setText(_translate("MainWindow", "Сброс до начальных"))
        self.text_3_2.setText(_translate("MainWindow", "подключений"))
        self.text_4_2.setText(_translate("MainWindow", "настроек"))


class Ui_group_action(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 700, 680))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.group_creation_button = QtWidgets.QPushButton(self.centralwidget)
        self.group_creation_button.setGeometry(QtCore.QRect(19, 19, 321, 241))
        self.group_creation_button.setStyleSheet("QPushButton{\n"
                                                 " background: rgba(255, 255, 255, 0.05);\n"
                                                 " border-radius: 8px;\n"
                                                 " color: #fff;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 " background: rgba(255, 255, 255, 0.1);\n"
                                                 "}\n"
                                                 "QPushButton:pressed{\n"
                                                 " background: rgba(0, 0, 0, 0.1);\n"
                                                 "}")
        self.group_creation_button.setText("")
        self.group_creation_button.setObjectName("group_creation_button")
        self.rename_users_button = QtWidgets.QPushButton(self.centralwidget)
        self.rename_users_button.setGeometry(QtCore.QRect(20, 280, 320, 240))
        self.rename_users_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.rename_users_button.setText("")
        self.rename_users_button.setObjectName("rename_users_button")
        self.remove_from_group_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_from_group_button.setGeometry(QtCore.QRect(360, 20, 320, 240))
        self.remove_from_group_button.setStyleSheet("QPushButton{\n"
                                                    " background: rgba(255, 255, 255, 0.05);\n"
                                                    " border-radius: 8px;\n"
                                                    " color: #fff;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    " background: rgba(255, 255, 255, 0.1);\n"
                                                    "}\n"
                                                    "QPushButton:pressed{\n"
                                                    " background: rgba(0, 0, 0, 0.1);\n"
                                                    "}")
        self.remove_from_group_button.setText("")
        self.remove_from_group_button.setObjectName("remove_from_group_button")
        self.rename_group_button = QtWidgets.QPushButton(self.centralwidget)
        self.rename_group_button.setGeometry(QtCore.QRect(360, 280, 320, 240))
        self.rename_group_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.rename_group_button.setText("")
        self.rename_group_button.setObjectName("rename_group_button")
        self.add_to_group_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_to_group_button.setGeometry(QtCore.QRect(20, 20, 320, 240))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.add_to_group_button.setFont(font)
        self.add_to_group_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.add_to_group_button.setText("")
        self.add_to_group_button.setObjectName("add_to_group_button")
        self.text_1_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1_1.setGeometry(QtCore.QRect(35, 90, 285, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1_1.setFont(font)
        self.text_1_1.setStyleSheet("color:#e3eded")
        self.text_1_1.setObjectName("text_1_1")
        self.text_1_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_1_2.setGeometry(QtCore.QRect(115, 140, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1_2.setFont(font)
        self.text_1_2.setStyleSheet("color:#e3eded")
        self.text_1_2.setObjectName("text_1_2")
        self.text_2_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_2_1.setGeometry(QtCore.QRect(390, 90, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2_1.setFont(font)
        self.text_2_1.setStyleSheet("color:#e3eded")
        self.text_2_1.setObjectName("text_2_1")
        self.text_2_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2_2.setGeometry(QtCore.QRect(440, 140, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2_2.setFont(font)
        self.text_2_2.setStyleSheet("color:#e3eded")
        self.text_2_2.setObjectName("text_2_2")
        self.text_3_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_3_1.setGeometry(QtCore.QRect(60, 350, 240, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3_1.setFont(font)
        self.text_3_1.setStyleSheet("color:#e3eded")
        self.text_3_1.setObjectName("text_3_1")
        self.text_4_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_4_1.setGeometry(QtCore.QRect(400, 350, 240, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4_1.setFont(font)
        self.text_4_1.setStyleSheet("color:#e3eded")
        self.text_4_1.setObjectName("text_4_1")
        self.text_3_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_3_2.setGeometry(QtCore.QRect(115, 400, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3_2.setFont(font)
        self.text_3_2.setStyleSheet("color:#e3eded")
        self.text_3_2.setObjectName("text_3_2")
        self.text_4_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_4_2.setGeometry(QtCore.QRect(469, 400, 102, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4_2.setFont(font)
        self.text_4_2.setStyleSheet("color:#e3eded")
        self.text_4_2.setObjectName("text_4_2")
        self.delete_group_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_group_button.setGeometry(QtCore.QRect(20, 540, 660, 120))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.delete_group_button.setFont(font)
        self.delete_group_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.delete_group_button.setObjectName("delete_group_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1_1.setText(_translate("MainWindow", "Добавить пользов."))
        self.text_1_2.setText(_translate("MainWindow", "в группу"))
        self.text_2_1.setText(_translate("MainWindow", "Удалить пользов."))
        self.text_2_2.setText(_translate("MainWindow", "из группы"))
        self.text_3_1.setText(_translate("MainWindow", "Переименовать "))
        self.text_4_1.setText(_translate("MainWindow", "Переименовать"))
        self.text_3_2.setText(_translate("MainWindow", "пользов."))
        self.text_4_2.setText(_translate("MainWindow", "группу"))
        self.delete_group_button.setText(_translate("MainWindow", "Удалить группу"))


class Ui_group_creation(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 530, 330))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.info = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(20, 20, 490, 130))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.info.setFont(font)
        self.info.setStyleSheet("QPlainTextEdit{\n"
" background: rgba(255, 255, 255, 0.05);\n"
" border-radius: 8px;\n"
" color: #e3eded;\n"
"}\n"
"QPushButton:hover{\n"
" background: rgba(255, 255, 255, 0.1);\n"
"}")
        self.info.setPlainText("")
        self.info.setObjectName("info")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setGeometry(QtCore.QRect(20, 250, 490, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.accept_button.setFont(font)
        self.accept_button.setStyleSheet("QPushButton{\n"
" background: rgba(255, 255, 255, 0.05);\n"
" border-radius: 8px;\n"
" color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
" background: rgba(255, 255, 255, 0.1);\n"
"}\n"
"QPushButton:pressed{\n"
" background: rgba(0, 0, 0, 0.1);\n"
"}")
        self.accept_button.setObjectName("accept_button")
        self.input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(20, 170, 490, 65))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.input.setFont(font)
        self.input.setStyleSheet("QPlainTextEdit{\n"
" background: rgba(255, 255, 255, 0.05);\n"
" border-radius: 8px;\n"
" color: #e3eded;\n"
"}\n"
"QPushButton:hover{\n"
" background: rgba(255, 255, 255, 0.1);\n"
"}")
        self.input.setPlainText("")
        self.input.setObjectName("input")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.accept_button.setText(_translate("MainWindow", "Принять"))


class Ui_group_setting(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 700, 540))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.group_import_button = QtWidgets.QPushButton(self.centralwidget)
        self.group_import_button.setGeometry(QtCore.QRect(20, 280, 320, 240))
        self.group_import_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.group_import_button.setText("")
        self.group_import_button.setObjectName("group_import_button")
        self.group_action_button = QtWidgets.QPushButton(self.centralwidget)
        self.group_action_button.setGeometry(QtCore.QRect(360, 20, 320, 240))
        self.group_action_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.group_action_button.setText("")
        self.group_action_button.setObjectName("group_action_button")
        self.group_export_button = QtWidgets.QPushButton(self.centralwidget)
        self.group_export_button.setGeometry(QtCore.QRect(360, 280, 320, 240))
        self.group_export_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.group_export_button.setText("")
        self.group_export_button.setObjectName("group_export_button")
        self.automatic_group_creation_button = QtWidgets.QPushButton(self.centralwidget)
        self.automatic_group_creation_button.setGeometry(QtCore.QRect(20, 20, 320, 240))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.automatic_group_creation_button.setFont(font)
        self.automatic_group_creation_button.setStyleSheet("QPushButton{\n"
                                                           " background: rgba(255, 255, 255, 0.05);\n"
                                                           " border-radius: 8px;\n"
                                                           " color: #fff;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           " background: rgba(255, 255, 255, 0.1);\n"
                                                           "}\n"
                                                           "QPushButton:pressed{\n"
                                                           " background: rgba(0, 0, 0, 0.1);\n"
                                                           "}")
        self.automatic_group_creation_button.setText("")
        self.automatic_group_creation_button.setObjectName("automatic_group_creation_button")
        self.text_1_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1_1.setGeometry(QtCore.QRect(40, 90, 280, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1_1.setFont(font)
        self.text_1_1.setStyleSheet("color:#e3eded")
        self.text_1_1.setObjectName("text_1_1")
        self.text_1_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_1_2.setGeometry(QtCore.QRect(125, 140, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1_2.setFont(font)
        self.text_1_2.setStyleSheet("color:#e3eded")
        self.text_1_2.setObjectName("text_1_2")
        self.text_2_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_2_1.setGeometry(QtCore.QRect(450, 90, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2_1.setFont(font)
        self.text_2_1.setStyleSheet("color:#e3eded")
        self.text_2_1.setObjectName("text_2_1")
        self.text_2_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2_2.setGeometry(QtCore.QRect(445, 140, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2_2.setFont(font)
        self.text_2_2.setStyleSheet("color:#e3eded")
        self.text_2_2.setObjectName("text_2_2")
        self.text_3_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_3_1.setGeometry(QtCore.QRect(35, 350, 290, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3_1.setFont(font)
        self.text_3_1.setStyleSheet("color:#e3eded")
        self.text_3_1.setObjectName("text_3_1")
        self.text_4_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_4_1.setGeometry(QtCore.QRect(375, 350, 290, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4_1.setFont(font)
        self.text_4_1.setStyleSheet("color:#e3eded")
        self.text_4_1.setObjectName("text_4_1")
        self.text_3_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_3_2.setGeometry(QtCore.QRect(135, 400, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3_2.setFont(font)
        self.text_3_2.setStyleSheet("color:#e3eded")
        self.text_3_2.setObjectName("text_3_2")
        self.text_4_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_4_2.setGeometry(QtCore.QRect(475, 400, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4_2.setFont(font)
        self.text_4_2.setStyleSheet("color:#e3eded")
        self.text_4_2.setObjectName("text_4_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1_1.setText(_translate("MainWindow", "Автомат. создание"))
        self.text_1_2.setText(_translate("MainWindow", "группы"))
        self.text_2_1.setText(_translate("MainWindow", "Действия"))
        self.text_2_2.setText(_translate("MainWindow", "с группой"))
        self.text_3_1.setText(_translate("MainWindow", "Выполнить импорт"))
        self.text_4_1.setText(_translate("MainWindow", "Выполнить экспорт"))
        self.text_3_2.setText(_translate("MainWindow", "групп"))
        self.text_4_2.setText(_translate("MainWindow", "групп"))


class Ui_info_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 265)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 650, 300))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(10, 5, 655, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color:#e3eded")
        self.text_1.setObjectName("text_1")
        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(30, 120, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_4.setFont(font)
        self.text_4.setStyleSheet("color:#e3eded")
        self.text_4.setObjectName("text_4")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(30, 50, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color:#e3eded")
        self.text_2.setObjectName("text_2")
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(30, 155, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_5.setFont(font)
        self.text_5.setStyleSheet("color:#e3eded")
        self.text_5.setObjectName("text_5")
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(30, 85, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_3.setFont(font)
        self.text_3.setStyleSheet("color:#e3eded")
        self.text_3.setObjectName("text_3")
        self.text_6 = QtWidgets.QLabel(self.centralwidget)
        self.text_6.setGeometry(QtCore.QRect(30, 190, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_6.setFont(font)
        self.text_6.setStyleSheet("color:#e3eded")
        self.text_6.setObjectName("text_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", "Доступ к Интернету включает в себя:"))
        self.text_4.setText(_translate("MainWindow", "- Установление доступа по группам"))
        self.text_2.setText(_translate("MainWindow", "- Установление доступа без пароля"))
        self.text_5.setText(_translate("MainWindow", "- Снятие доступа по группам"))
        self.text_3.setText(_translate("MainWindow", "- Установление доступа с паролем"))
        self.text_6.setText(_translate("MainWindow", "- Установление запрета на доступ"))


class Ui_info_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 650, 200))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(10, 5, 655, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color:#e3eded")
        self.text_1.setObjectName("text_1")
        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(30, 120, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_4.setFont(font)
        self.text_4.setStyleSheet("color:#e3eded")
        self.text_4.setObjectName("text_4")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(30, 50, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color:#e3eded")
        self.text_2.setObjectName("text_2")
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(30, 155, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_5.setFont(font)
        self.text_5.setStyleSheet("color:#e3eded")
        self.text_5.setObjectName("text_5")
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(30, 85, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_3.setFont(font)
        self.text_3.setStyleSheet("color:#e3eded")
        self.text_3.setObjectName("text_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", "Настройка групп включает в себя:"))
        self.text_4.setText(_translate("MainWindow", "- Работу с группами"))
        self.text_2.setText(_translate("MainWindow", "- Создание групп"))
        self.text_5.setText(_translate("MainWindow", "- Импорт/экспорт групп"))
        self.text_3.setText(_translate("MainWindow", "- Получение информации о группах"))


class Ui_info_3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 650, 200))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(10, 5, 655, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color:#e3eded")
        self.text_1.setObjectName("text_1")
        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(30, 120, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_4.setFont(font)
        self.text_4.setStyleSheet("color:#e3eded")
        self.text_4.setObjectName("text_4")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(30, 50, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color:#e3eded")
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(30, 85, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_3.setFont(font)
        self.text_3.setStyleSheet("color:#e3eded")
        self.text_3.setObjectName("text_3")
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(30, 155, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.text_5.setFont(font)
        self.text_5.setStyleSheet("color:#e3eded")
        self.text_5.setObjectName("text_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", "Общие настройки сети включают в себя:"))
        self.text_4.setText(_translate("MainWindow", "- Показ всех подключений"))
        self.text_2.setText(_translate("MainWindow", "- Изменение данных WIFI"))
        self.text_3.setText(_translate("MainWindow", "- Изменение данных роутера"))
        self.text_5.setText(_translate("MainWindow", "- Сброс до начальных настроек"))


class Ui_info_connection(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 140)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 330, 140))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient_table.png"))
        self.gradient.setObjectName("gradient")
        self.table_1_1 = QtWidgets.QLabel(self.centralwidget)
        self.table_1_1.setGeometry(QtCore.QRect(5, 8, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.table_1_1.setFont(font)
        self.table_1_1.setStyleSheet("color: #ffffff;")
        self.table_1_1.setObjectName("table_1_1")
        self.table_1_2 = QtWidgets.QLabel(self.centralwidget)
        self.table_1_2.setGeometry(QtCore.QRect(5, 44, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.table_1_2.setFont(font)
        self.table_1_2.setStyleSheet("color: #ffffff;")
        self.table_1_2.setObjectName("table_1_2")
        self.table_1_3 = QtWidgets.QLabel(self.centralwidget)
        self.table_1_3.setGeometry(QtCore.QRect(5, 76, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.table_1_3.setFont(font)
        self.table_1_3.setStyleSheet("color: #ffffff;")
        self.table_1_3.setObjectName("table_1_3")
        self.table_1_4 = QtWidgets.QLabel(self.centralwidget)
        self.table_1_4.setGeometry(QtCore.QRect(5, 108, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.table_1_4.setFont(font)
        self.table_1_4.setStyleSheet("color: #ffffff;")
        self.table_1_4.setObjectName("table_1_4")
        self.table_2_1 = QtWidgets.QLabel(self.centralwidget)
        self.table_2_1.setGeometry(QtCore.QRect(145, 8, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.table_2_1.setFont(font)
        self.table_2_1.setStyleSheet("color: #ffffff;")
        self.table_2_1.setText("")
        self.table_2_1.setObjectName("table_2_1")
        self.table_2_2 = QtWidgets.QLabel(self.centralwidget)
        self.table_2_2.setGeometry(QtCore.QRect(145, 44, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.table_2_2.setFont(font)
        self.table_2_2.setStyleSheet("color: #ffffff;")
        self.table_2_2.setText("")
        self.table_2_2.setObjectName("table_2_2")
        self.table_2_3 = QtWidgets.QLabel(self.centralwidget)
        self.table_2_3.setGeometry(QtCore.QRect(145, 76, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.table_2_3.setFont(font)
        self.table_2_3.setStyleSheet("color: #ffffff;")
        self.table_2_3.setText("")
        self.table_2_3.setObjectName("table_2_3")
        self.table_2_4 = QtWidgets.QLabel(self.centralwidget)
        self.table_2_4.setGeometry(QtCore.QRect(145, 108, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.table_2_4.setFont(font)
        self.table_2_4.setStyleSheet("color: #ffffff;")
        self.table_2_4.setText("")
        self.table_2_4.setObjectName("table_2_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(140, 0, 2, 200))
        self.line.setStyleSheet("background-color: #000000;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.all_group = QtWidgets.QPushButton(self.centralwidget)
        self.all_group.setGeometry(QtCore.QRect(305, 115, 15, 15))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.all_group.setFont(font)
        self.all_group.setStyleSheet("QPushButton{\n"
                                     " background: #000000;\n"
                                     " border-radius: 7px;\n"
                                     " color: #ffffff;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     " background: #595959;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     " background: #ffffff;\n"
                                     " color: #000000;\n"
                                     "}\n"
                                     "")
        self.all_group.setObjectName("all_group")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.table_1_1.setText(_translate("MainWindow", "Логин WIFI"))
        self.table_1_2.setText(_translate("MainWindow", "Пароль WIFI"))
        self.table_1_3.setText(_translate("MainWindow", "Безопасность"))
        self.table_1_4.setText(_translate("MainWindow", "Группы"))
        self.all_group.setText(_translate("MainWindow", "i"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'internet_access.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_internet_access(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 700, 680))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.connect_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_info_button.setGeometry(QtCore.QRect(19, 19, 321, 241))
        self.connect_info_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.connect_info_button.setText("")
        self.connect_info_button.setObjectName("connect_info_button")
        self.group_access_button = QtWidgets.QPushButton(self.centralwidget)
        self.group_access_button.setGeometry(QtCore.QRect(20, 280, 320, 240))
        self.group_access_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color: #fff;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.group_access_button.setText("")
        self.group_access_button.setObjectName("group_access_button")
        self.password_access_button = QtWidgets.QPushButton(self.centralwidget)
        self.password_access_button.setGeometry(QtCore.QRect(365, 20, 320, 240))
        self.password_access_button.setStyleSheet("QPushButton{\n"
                                                  " background: rgba(255, 255, 255, 0.05);\n"
                                                  " border-radius: 8px;\n"
                                                  " color: #fff;\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  " background: rgba(255, 255, 255, 0.1);\n"
                                                  "}\n"
                                                  "QPushButton:pressed{\n"
                                                  " background: rgba(0, 0, 0, 0.1);\n"
                                                  "}")
        self.password_access_button.setText("")
        self.password_access_button.setObjectName("password_access_button")
        self.group_off_access_button = QtWidgets.QPushButton(self.centralwidget)
        self.group_off_access_button.setGeometry(QtCore.QRect(365, 280, 320, 240))
        self.group_off_access_button.setStyleSheet("QPushButton{\n"
                                                   " background: rgba(255, 255, 255, 0.05);\n"
                                                   " border-radius: 8px;\n"
                                                   " color: #fff;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   " background: rgba(255, 255, 255, 0.1);\n"
                                                   "}\n"
                                                   "QPushButton:pressed{\n"
                                                   " background: rgba(0, 0, 0, 0.1);\n"
                                                   "}")
        self.group_off_access_button.setText("")
        self.group_off_access_button.setObjectName("group_off_access_button")
        self.passwordless_access_button = QtWidgets.QPushButton(self.centralwidget)
        self.passwordless_access_button.setGeometry(QtCore.QRect(20, 20, 320, 240))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.passwordless_access_button.setFont(font)
        self.passwordless_access_button.setStyleSheet("QPushButton{\n"
                                                      " background: rgba(255, 255, 255, 0.05);\n"
                                                      " border-radius: 8px;\n"
                                                      " color: #fff;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      " background: rgba(255, 255, 255, 0.1);\n"
                                                      "}\n"
                                                      "QPushButton:pressed{\n"
                                                      " background: rgba(0, 0, 0, 0.1);\n"
                                                      "}")
        self.passwordless_access_button.setText("")
        self.passwordless_access_button.setObjectName("passwordless_access_button")
        self.text_1_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1_1.setGeometry(QtCore.QRect(45, 90, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1_1.setFont(font)
        self.text_1_1.setStyleSheet("color:#e3eded")
        self.text_1_1.setObjectName("text_1_1")
        self.text_1_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_1_2.setGeometry(QtCore.QRect(95, 140, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1_2.setFont(font)
        self.text_1_2.setStyleSheet("color:#e3eded")
        self.text_1_2.setObjectName("text_1_2")
        self.text_2_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_2_1.setGeometry(QtCore.QRect(390, 90, 270, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2_1.setFont(font)
        self.text_2_1.setStyleSheet("color:#e3eded")
        self.text_2_1.setObjectName("text_2_1")
        self.text_2_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2_2.setGeometry(QtCore.QRect(435, 140, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2_2.setFont(font)
        self.text_2_2.setStyleSheet("color:#e3eded")
        self.text_2_2.setObjectName("text_2_2")
        self.text_3_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_3_1.setGeometry(QtCore.QRect(50, 350, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3_1.setFont(font)
        self.text_3_1.setStyleSheet("color:#e3eded")
        self.text_3_1.setObjectName("text_3_1")
        self.text_4_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_4_1.setGeometry(QtCore.QRect(385, 350, 280, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4_1.setFont(font)
        self.text_4_1.setStyleSheet("color:#e3eded")
        self.text_4_1.setObjectName("text_4_1")
        self.text_3_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_3_2.setGeometry(QtCore.QRect(95, 400, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3_2.setFont(font)
        self.text_3_2.setStyleSheet("color:#e3eded")
        self.text_3_2.setObjectName("text_3_2")
        self.text_4_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_4_2.setGeometry(QtCore.QRect(435, 400, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4_2.setFont(font)
        self.text_4_2.setStyleSheet("color:#e3eded")
        self.text_4_2.setObjectName("text_4_2")
        self.denied_access_button = QtWidgets.QPushButton(self.centralwidget)
        self.denied_access_button.setGeometry(QtCore.QRect(20, 540, 660, 120))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.denied_access_button.setFont(font)
        self.denied_access_button.setStyleSheet("QPushButton{\n"
                                                " background: rgba(255, 255, 255, 0.05);\n"
                                                " border-radius: 8px;\n"
                                                " color: #fff;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                " background: rgba(255, 255, 255, 0.1);\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                " background: rgba(0, 0, 0, 0.1);\n"
                                                "}")
        self.denied_access_button.setObjectName("denied_access_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1_1.setText(_translate("MainWindow", "Разрешить доступ"))
        self.text_1_2.setText(_translate("MainWindow", "без пароля"))
        self.text_2_1.setText(_translate("MainWindow", "Разрешить доступ"))
        self.text_2_2.setText(_translate("MainWindow", "по паролю"))
        self.text_3_1.setText(_translate("MainWindow", "Включить доступ"))
        self.text_4_1.setText(_translate("MainWindow", "Выключить доступ"))
        self.text_3_2.setText(_translate("MainWindow", "по группам"))
        self.text_4_2.setText(_translate("MainWindow", "по группам"))
        self.denied_access_button.setText(_translate("MainWindow", "Запретить доступ всем"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 540)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 900, 540))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.transition_tg_button = QtWidgets.QPushButton(self.centralwidget)
        self.transition_tg_button.setGeometry(QtCore.QRect(10, 450, 880, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.transition_tg_button.setFont(font)
        self.transition_tg_button.setStyleSheet("QPushButton{\n"
                                                " background: rgba(255, 255, 255, 0.05);\n"
                                                " border-radius: 8px;\n"
                                                " color: #e3eded;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                " background: rgba(255, 255, 255, 0.1);\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                " background: rgba(0, 0, 0, 0.1);\n"
                                                "}")
        self.transition_tg_button.setObjectName("transition_tg_button")
        self.connect_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_info_button.setGeometry(QtCore.QRect(10, 130, 370, 290))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.connect_info_button.setFont(font)
        self.connect_info_button.setStyleSheet("QPushButton{\n"
                                               " background: rgba(255, 255, 255, 0.05);\n"
                                               " border-radius: 8px;\n"
                                               " color:#e3eded;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               " background: rgba(255, 255, 255, 0.1);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               " background: rgba(0, 0, 0, 0.1);\n"
                                               "}")
        self.connect_info_button.setText("")
        self.connect_info_button.setObjectName("connect_info_button")
        self.internet_access_button = QtWidgets.QPushButton(self.centralwidget)
        self.internet_access_button.setGeometry(QtCore.QRect(400, 130, 490, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.internet_access_button.setFont(font)
        self.internet_access_button.setStyleSheet("QPushButton{\n"
                                                  " background: rgba(255, 255, 255, 0.05);\n"
                                                  " border-radius: 8px;\n"
                                                  " color:#e3eded;\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  " background: rgba(255, 255, 255, 0.1);\n"
                                                  "}\n"
                                                  "QPushButton:pressed{\n"
                                                  " background: rgba(0, 0, 0, 0.1);\n"
                                                  "}")
        self.internet_access_button.setObjectName("internet_access_button")
        self.general_network_settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.general_network_settings_button.setGeometry(QtCore.QRect(400, 340, 490, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.general_network_settings_button.setFont(font)
        self.general_network_settings_button.setStyleSheet("QPushButton{\n"
                                                           " background: rgba(255, 255, 255, 0.05);\n"
                                                           " border-radius: 8px;\n"
                                                           " color:#e3eded;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           " background: rgba(255, 255, 255, 0.1);\n"
                                                           "}\n"
                                                           "QPushButton:pressed{\n"
                                                           " background: rgba(0, 0, 0, 0.1);\n"
                                                           "}\n"
                                                           "")
        self.general_network_settings_button.setObjectName("general_network_settings_button")
        self.group_setting_button = QtWidgets.QPushButton(self.centralwidget)
        self.group_setting_button.setGeometry(QtCore.QRect(400, 234, 490, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.group_setting_button.setFont(font)
        self.group_setting_button.setStyleSheet("QPushButton{\n"
                                                " background: rgba(255, 255, 255, 0.05);\n"
                                                " border-radius: 8px;\n"
                                                " color:#e3eded;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                " background: rgba(255, 255, 255, 0.1);\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                " background: rgba(0, 0, 0, 0.1);\n"
                                                "}\n"
                                                "")
        self.group_setting_button.setObjectName("group_setting_button")
        self.top_text_1 = QtWidgets.QLabel(self.centralwidget)
        self.top_text_1.setGeometry(QtCore.QRect(20, 10, 641, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.top_text_1.setFont(font)
        self.top_text_1.setStyleSheet("color:#e3eded")
        self.top_text_1.setObjectName("top_text_1")
        self.top_text_2 = QtWidgets.QLabel(self.centralwidget)
        self.top_text_2.setGeometry(QtCore.QRect(20, 50, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.top_text_2.setFont(font)
        self.top_text_2.setStyleSheet("color:#e3eded")
        self.top_text_2.setObjectName("top_text_2")
        self.transition_tg_img = QtWidgets.QLabel(self.centralwidget)
        self.transition_tg_img.setGeometry(QtCore.QRect(800, 460, 61, 61))
        self.transition_tg_img.setText("")
        self.transition_tg_img.setPixmap(QtGui.QPixmap("Images/telegram.png"))
        self.transition_tg_img.setObjectName("transition_tg_img")
        self.connect_info_text_1 = QtWidgets.QLabel(self.centralwidget)
        self.connect_info_text_1.setGeometry(QtCore.QRect(75, 200, 240, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.connect_info_text_1.setFont(font)
        self.connect_info_text_1.setStyleSheet("color:#e3eded")
        self.connect_info_text_1.setObjectName("connect_info_text_1")
        self.connect_info_text_2 = QtWidgets.QLabel(self.centralwidget)
        self.connect_info_text_2.setGeometry(QtCore.QRect(75, 250, 240, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.connect_info_text_2.setFont(font)
        self.connect_info_text_2.setStyleSheet("color:#e3eded")
        self.connect_info_text_2.setObjectName("connect_info_text_2")
        self.connect_info_text_3 = QtWidgets.QLabel(self.centralwidget)
        self.connect_info_text_3.setGeometry(QtCore.QRect(45, 300, 300, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.connect_info_text_3.setFont(font)
        self.connect_info_text_3.setStyleSheet("color:#e3eded")
        self.connect_info_text_3.setObjectName("connect_info_text_3")
        self.top_style = QtWidgets.QLabel(self.centralwidget)
        self.top_style.setGeometry(QtCore.QRect(9, 10, 880, 81))
        self.top_style.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                     "border-radius: 8px;\n"
                                     "color: #fff;")
        self.top_style.setText("")
        self.top_style.setObjectName("top_style")
        self.top_setting_button = QtWidgets.QPushButton(self.centralwidget)
        self.top_setting_button.setGeometry(QtCore.QRect(713, 30, 161, 33))
        self.top_setting_button.setStyleSheet("QPushButton{\n"
                                              "background: rgba(255, 255, 255, 0);\n"
                                              " color: #ffffff;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              " color: #595959;\n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              " color: #000000;\n"
                                              "}\n"
                                              "\n"
                                              "")
        self.top_setting_button.setObjectName("top_setting_button")
        self.info_button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.info_button_1.setGeometry(QtCore.QRect(850, 140, 27, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.info_button_1.setFont(font)
        self.info_button_1.setStyleSheet("QPushButton{\n"
                                         " background: #000000;\n"
                                         " border-radius: 13px;\n"
                                         " color: #ffffff;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: #595959;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: #ffffff;\n"
                                         " color: #000000;\n"
                                         "}\n"
                                         "")
        self.info_button_1.setObjectName("info_button_1")
        self.info_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.info_button_2.setGeometry(QtCore.QRect(850, 244, 27, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.info_button_2.setFont(font)
        self.info_button_2.setStyleSheet("QPushButton{\n"
                                         " background: #000000;\n"
                                         " border-radius: 13px;\n"
                                         " color: #ffffff;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: #595959;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: #ffffff;\n"
                                         " color: #000000;\n"
                                         "}\n"
                                         "")
        self.info_button_2.setObjectName("info_button_2")
        self.info_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.info_button_3.setGeometry(QtCore.QRect(850, 350, 27, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.info_button_3.setFont(font)
        self.info_button_3.setStyleSheet("QPushButton{\n"
                                         " background: #000000;\n"
                                         " border-radius: 13px;\n"
                                         " color: #ffffff;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: #595959;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: #ffffff;\n"
                                         " color: #000000;\n"
                                         "}\n"
                                         "")
        self.info_button_3.setObjectName("info_button_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.transition_tg_button.setText(_translate("MainWindow", "Для консультации и поддержки ждём в Telegram"))
        self.internet_access_button.setText(_translate("MainWindow", "Доступ к Интернету"))
        self.general_network_settings_button.setText(_translate("MainWindow", "Общие настройки сети"))
        self.group_setting_button.setText(_translate("MainWindow", "Настройка групп"))
        self.top_text_1.setText(_translate("MainWindow", "SKR - программа для удобного управления "))
        self.top_text_2.setText(_translate("MainWindow", "роутерами на платформе ASUS"))
        self.connect_info_text_1.setText(_translate("MainWindow", "Информация о"))
        self.connect_info_text_2.setText(_translate("MainWindow", "подключении к "))
        self.connect_info_text_3.setText(_translate("MainWindow", "беспроводной сети"))
        self.top_setting_button.setText(_translate("MainWindow", "Настройка программы  ⚙"))
        self.info_button_1.setText(_translate("MainWindow", "i"))
        self.info_button_2.setText(_translate("MainWindow", "i"))
        self.info_button_3.setText(_translate("MainWindow", "i"))


class Ui_password_access(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 190)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 605, 190))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(10, 7, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color:#e3eded")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(10, 93, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color:#e3eded")
        self.text_2.setObjectName("text_2")
        self.password_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_1.setGeometry(QtCore.QRect(10, 50, 260, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.password_1.setFont(font)
        self.password_1.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                      "border-radius: 8px;\n"
                                      "color:#e3eded;\n"
                                      "")
        self.password_1.setText("")
        self.password_1.setObjectName("password_1")
        self.password_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_2.setGeometry(QtCore.QRect(10, 136, 260, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.password_2.setFont(font)
        self.password_2.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                      "border-radius: 8px;\n"
                                      "color:#e3eded;\n"
                                      "")
        self.password_2.setText("")
        self.password_2.setObjectName("password_2")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setGeometry(QtCore.QRect(450, 20, 145, 145))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.accept_button.setFont(font)
        self.accept_button.setStyleSheet("QPushButton{\n"
                                         " background: rgba(255, 255, 255, 0.05);\n"
                                         " border-radius: 8px;\n"
                                         " color: #fff;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: rgba(255, 255, 255, 0.1);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: rgba(0, 0, 0, 0.1);\n"
                                         "}")
        self.accept_button.setObjectName("accept_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", "Введите новый пароль:"))
        self.text_2.setText(_translate("MainWindow", "Подтвердите новый пароль:"))
        self.accept_button.setText(_translate("MainWindow", "Принять"))


class Ui_adding_and_removing_and_rename_users_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 900, 530))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.info_group = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.info_group.setGeometry(QtCore.QRect(490, 20, 391, 490))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.info_group.setFont(font)
        self.info_group.setStyleSheet("QPlainTextEdit{\n"
                                      " background: rgba(255, 255, 255, 0.05);\n"
                                      " border-radius: 8px;\n"
                                      " color: #e3eded;\n"
                                      "}\n"
                                      "QPlainTextEdit:hover{\n"
                                      " background: rgba(255, 255, 255, 0.1);\n"
                                      "}")
        self.info_group.setPlainText("")
        self.info_group.setObjectName("info_group")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(20, 20, 450, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_1.setObjectName("text_1")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setGeometry(QtCore.QRect(20, 360, 450, 150))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.accept_button.setFont(font)
        self.accept_button.setStyleSheet("QPushButton{\n"
                                         " background: rgba(255, 255, 255, 0.05);\n"
                                         " border-radius: 8px;\n"
                                         " color: #fff;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: rgba(255, 255, 255, 0.1);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: rgba(0, 0, 0, 0.1);\n"
                                         "}")
        self.accept_button.setObjectName("accept_button")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(20, 80, 440, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_2.setObjectName("text_2")
        self.input_group = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_group.setGeometry(QtCore.QRect(20, 274, 450, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.input_group.setFont(font)
        self.input_group.setStyleSheet("QPlainTextEdit{\n"
                                       " background: rgba(255, 255, 255, 0.05);\n"
                                       " border-radius: 8px;\n"
                                       " color: #e3eded;\n"
                                       "}\n"
                                       "QPlainTextEdit:hover{\n"
                                       " background: rgba(255, 255, 255, 0.1);\n"
                                       "}")
        self.input_group.setPlainText("")
        self.input_group.setObjectName("input_group")
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(20, 140, 440, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_3.setFont(font)
        self.text_3.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(20, 200, 440, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_4.setFont(font)
        self.text_4.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_4.setObjectName("text_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", "Введите имя группы, чтобы"))
        self.accept_button.setText(_translate("MainWindow", "Продолжить"))
        self.text_2.setText(_translate("MainWindow", "продолжить работу с ней"))
        self.text_3.setText(_translate("MainWindow", "(Вам будет доступно увидеть"))
        self.text_4.setText(_translate("MainWindow", "пользователей группы)"))


class Ui_adding_and_removing_and_rename_users_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 900, 530))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.info_group = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.info_group.setGeometry(QtCore.QRect(490, 20, 391, 490))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.info_group.setFont(font)
        self.info_group.setStyleSheet("QPlainTextEdit{\n"
                                      " background: rgba(255, 255, 255, 0.05);\n"
                                      " border-radius: 8px;\n"
                                      " color: #e3eded;\n"
                                      "}\n"
                                      "QPlainTextEdit:hover{\n"
                                      " background: rgba(255, 255, 255, 0.1);\n"
                                      "}")
        self.info_group.setPlainText("")
        self.info_group.setObjectName("info_group")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(20, 20, 450, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_1.setObjectName("text_1")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setGeometry(QtCore.QRect(20, 360, 450, 150))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.accept_button.setFont(font)
        self.accept_button.setStyleSheet("QPushButton{\n"
                                         " background: rgba(255, 255, 255, 0.05);\n"
                                         " border-radius: 8px;\n"
                                         " color: #fff;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: rgba(255, 255, 255, 0.1);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: rgba(0, 0, 0, 0.1);\n"
                                         "}")
        self.accept_button.setObjectName("accept_button")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(20, 80, 440, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_2.setObjectName("text_2")
        self.input_group = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_group.setGeometry(QtCore.QRect(20, 150, 450, 190))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.input_group.setFont(font)
        self.input_group.setStyleSheet("QPlainTextEdit{\n"
                                       " background: rgba(255, 255, 255, 0.05);\n"
                                       " border-radius: 8px;\n"
                                       " color: #e3eded;\n"
                                       "}\n"
                                       "QPlainTextEdit:hover{\n"
                                       " background: rgba(255, 255, 255, 0.1);\n"
                                       "}")
        self.input_group.setPlainText("")
        self.input_group.setObjectName("input_group")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", ""))
        self.accept_button.setText(_translate("MainWindow", "Принять"))
        self.text_2.setText(_translate("MainWindow", "(Каждое с новой строки):"))


class Ui_rename_group(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 900, 530))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.info_group = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.info_group.setGeometry(QtCore.QRect(490, 20, 391, 490))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.info_group.setFont(font)
        self.info_group.setStyleSheet("QPlainTextEdit{\n"
                                      " background: rgba(255, 255, 255, 0.05);\n"
                                      " border-radius: 8px;\n"
                                      " color: #e3eded;\n"
                                      "}\n"
                                      "QPlainTextEdit:hover{\n"
                                      " background: rgba(255, 255, 255, 0.1);\n"
                                      "}")
        self.info_group.setPlainText("")
        self.info_group.setObjectName("info_group")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(20, 20, 450, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_1.setObjectName("text_1")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setGeometry(QtCore.QRect(20, 360, 450, 150))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.accept_button.setFont(font)
        self.accept_button.setStyleSheet("QPushButton{\n"
                                         " background: rgba(255, 255, 255, 0.05);\n"
                                         " border-radius: 8px;\n"
                                         " color: #fff;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: rgba(255, 255, 255, 0.1);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: rgba(0, 0, 0, 0.1);\n"
                                         "}")
        self.accept_button.setObjectName("accept_button")
        self.input_group = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_group.setGeometry(QtCore.QRect(20, 90, 450, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.input_group.setFont(font)
        self.input_group.setStyleSheet("QPlainTextEdit{\n"
                                       " background: rgba(255, 255, 255, 0.05);\n"
                                       " border-radius: 8px;\n"
                                       " color: #e3eded;\n"
                                       "}\n"
                                       "QPlainTextEdit:hover{\n"
                                       " background: rgba(255, 255, 255, 0.1);\n"
                                       "}")
        self.input_group.setPlainText("")
        self.input_group.setObjectName("input_group")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(20, 180, 450, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color: #e3eded;\n"
                                  "")
        self.text_2.setObjectName("text_2")
        self.input_group_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_group_2.setGeometry(QtCore.QRect(20, 250, 450, 75))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.input_group_2.setFont(font)
        self.input_group_2.setStyleSheet("QPlainTextEdit{\n"
                                         " background: rgba(255, 255, 255, 0.05);\n"
                                         " border-radius: 8px;\n"
                                         " color: #e3eded;\n"
                                         "}\n"
                                         "QPlainTextEdit:hover{\n"
                                         " background: rgba(255, 255, 255, 0.1);\n"
                                         "}")
        self.input_group_2.setPlainText("")
        self.input_group_2.setObjectName("input_group_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", "Введите старое имя группы:"))
        self.accept_button.setText(_translate("MainWindow", "Принять"))
        self.text_2.setText(_translate("MainWindow", "Введите новое имя группы:"))


class Ui_settings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 460, 410))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/gradient.png"))
        self.gradient.setObjectName("gradient")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(20, 20, 351, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_1.setFont(font)
        self.text_1.setStyleSheet("color:#e3eded")
        self.text_1.setObjectName("text_1")
        self.wifi = QtWidgets.QLineEdit(self.centralwidget)
        self.wifi.setGeometry(QtCore.QRect(20, 70, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.wifi.setFont(font)
        self.wifi.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                "border-radius: 8px;\n"
                                "color:#e3eded;\n"
                                "")
        self.wifi.setText("")
        self.wifi.setObjectName("wifi")
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(20, 120, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_5.setFont(font)
        self.text_5.setStyleSheet("color:#e3eded")
        self.text_5.setObjectName("text_5")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(20, 170, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.login.setFont(font)
        self.login.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                 "border-radius: 8px;\n"
                                 "color:#e3eded;\n"
                                 "")
        self.login.setText("")
        self.login.setObjectName("login")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setGeometry(QtCore.QRect(70, 330, 320, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.accept_button.setFont(font)
        self.accept_button.setStyleSheet("QPushButton{\n"
                                         " background: rgba(255, 255, 255, 0.05);\n"
                                         " border-radius: 8px;\n"
                                         " color:#e3eded;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         " background: rgba(255, 255, 255, 0.1);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         " background: rgba(0, 0, 0, 0.1);\n"
                                         "}")
        self.accept_button.setObjectName("accept_button")
        self.text_6 = QtWidgets.QLabel(self.centralwidget)
        self.text_6.setGeometry(QtCore.QRect(20, 220, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.text_6.setFont(font)
        self.text_6.setStyleSheet("color:#e3eded")
        self.text_6.setObjectName("text_6")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(20, 270, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.password.setFont(font)
        self.password.setStyleSheet("background: rgba(255, 255, 255, 0.05);\n"
                                    "border-radius: 8px;\n"
                                    "color:#e3eded;\n"
                                    "")
        self.password.setText("")
        self.password.setObjectName("password")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Keeper Router"))
        self.text_1.setText(_translate("MainWindow", "Введите имя WIFI сети:"))
        self.text_5.setText(_translate("MainWindow", "Введите логин от роутера:"))
        self.accept_button.setText(_translate("MainWindow", "Принять"))
        self.text_6.setText(_translate("MainWindow", "Введите пароль от роутера:"))


class Ui_successfully(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 145)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gradient = QtWidgets.QLabel(self.centralwidget)
        self.gradient.setGeometry(QtCore.QRect(0, 0, 440, 145))
        self.gradient.setText("")
        self.gradient.setPixmap(QtGui.QPixmap("Images/successfully.png"))
        self.gradient.setObjectName("gradient")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(80, 40, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.text_1.setFont(font)
        self.text_1.setText("")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(80, 60, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.text_2.setFont(font)
        self.text_2.setText("")
        self.text_2.setObjectName("text_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Успешно"))
