# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/img/note.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import os.path
import datetime
from pathlib import Path

class Ui_MainWindow(object):
    def __init__(self):
        self.script_path = os.getcwd() + "/mmd/"
        self.state = "start"

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
        return self

    def getTableIndex(self):
        return self.tableIndex

    def setTableIndex(self, index):
        self.tableIndex = index
        return self

    def getScriptPath(self):
        return self.script_path

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 703)
        MainWindow.setMinimumSize(QtCore.QSize(891, 703))
        MainWindow.setMaximumSize(QtCore.QSize(891, 703))
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.historyComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.historyComboBox.setGeometry(QtCore.QRect(10, 30, 431, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(99)
        self.historyComboBox.setFont(font)
        self.historyComboBox.setStyleSheet("background-color: rgb(165, 12, 70);\n"
                                           "color: rgb(238, 238, 236);\n"
                                           "font-weight: 800")
        self.historyComboBox.setObjectName("historyComboBox")
        self.historyComboBox.addItem("")
        self.refreshHistoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshHistoryButton.setGeometry(QtCore.QRect(450, 30, 211, 21))
        self.refreshHistoryButton.setStyleSheet("background-color: rgb(165, 12, 70);\n"
                                                "color: rgb(238, 238, 236);\n"
                                                "font-weight: 800")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{self.getScriptPath()}data/img/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshHistoryButton.setIcon(icon)
        self.refreshHistoryButton.setObjectName("refreshHistoryButton")
        self.secondLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondLabel.setGeometry(QtCore.QRect(0, 60, 891, 20))
        self.secondLabel.setStyleSheet("background-color: rgb(117, 80, 123);\n"
                                       "font-weight: 800")
        self.secondLabel.setObjectName("secondLabel")
        self.firstLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstLabel.setGeometry(QtCore.QRect(0, 0, 891, 21))
        self.firstLabel.setStyleSheet("background-color: rgb(117, 80, 123);\n"
                                      "font-weight: 800")
        self.firstLabel.setObjectName("firstLabel")
        self.newRecordButton = QtWidgets.QPushButton(self.centralwidget)
        self.newRecordButton.setGeometry(QtCore.QRect(10, 88, 211, 21))
        self.newRecordButton.setStyleSheet("background-color: rgb(165, 12, 70);\n"
                                           "color: rgb(238, 238, 236);\n"
                                           "font-weight: 800")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(f"{self.getScriptPath()}data/img/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newRecordButton.setIcon(icon1)
        self.newRecordButton.setObjectName("newRecordButton")
        self.saveRecordButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveRecordButton.setGeometry(QtCore.QRect(230, 88, 211, 21))
        self.saveRecordButton.setStyleSheet("background-color: rgb(165, 12, 70);\n"
                                            "color: rgb(238, 238, 236);\n"
                                            "font-weight: 800")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(f"{self.getScriptPath()}data/img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveRecordButton.setIcon(icon2)
        self.saveRecordButton.setObjectName("saveRecordButton")
        self.deleteRecordButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteRecordButton.setGeometry(QtCore.QRect(450, 88, 211, 21))
        self.deleteRecordButton.setStyleSheet("background-color: rgb(165, 12, 70);\n"
                                              "color: rgb(238, 238, 236);\n"
                                              "font-weight: 800")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(f"{self.getScriptPath()}data/img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteRecordButton.setIcon(icon3)
        self.deleteRecordButton.setObjectName("deleteRecordButton")
        self.thirdLabel = QtWidgets.QLabel(self.centralwidget)
        self.thirdLabel.setGeometry(QtCore.QRect(0, 117, 891, 20))
        self.thirdLabel.setStyleSheet("background-color: rgb(117, 80, 123);\n"
                                      "font-weight: 800")
        self.thirdLabel.setObjectName("thirdLabel")
        self.recordText = QtWidgets.QTextEdit(self.centralwidget)
        self.recordText.setGeometry(QtCore.QRect(6, 173, 881, 501))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.recordText.setFont(font)
        self.recordText.setStyleSheet("background-color: rgb(173, 127, 168);\n"
                                      "color: rgb(238, 238, 236);")
        self.recordText.setDocumentTitle("")
        self.recordText.setObjectName("recordText")
        self.editRecordButton = QtWidgets.QPushButton(self.centralwidget)
        self.editRecordButton.setGeometry(QtCore.QRect(670, 89, 211, 21))
        self.editRecordButton.setStyleSheet("background-color: rgb(165, 12, 70);\n"
                                            "color: rgb(238, 238, 236);\n"
                                            "font-weight: 800")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(f"{self.getScriptPath()}data/img/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editRecordButton.setIcon(icon4)
        self.editRecordButton.setObjectName("editRecordButton")
        self.fourthLabel = QtWidgets.QLabel(self.centralwidget)
        self.fourthLabel.setGeometry(QtCore.QRect(-7, 146, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fourthLabel.setFont(font)
        self.fourthLabel.setStyleSheet("color: rgb(238, 238, 236);\n"
                                       "background-color: rgb(117, 80, 123);")
        self.fourthLabel.setObjectName("fourthLabel")
        self.recordName = QtWidgets.QLineEdit(self.centralwidget)
        self.recordName.setGeometry(QtCore.QRect(140, 146, 711, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(99)
        self.recordName.setFont(font)
        self.recordName.setToolTip("")
        self.recordName.setStyleSheet("color: rgb(238, 238, 236);\n"
                                      "font-weight: 800")
        self.recordName.setObjectName("recordName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.savePortfolio = QtWidgets.QAction(MainWindow)
        self.savePortfolio.setObjectName("savePortfolio")
        self.exitProgram = QtWidgets.QAction(MainWindow)
        self.exitProgram.setObjectName("exitProgram")
        self.openPortfolio = QtWidgets.QAction(MainWindow)
        self.openPortfolio.setObjectName("openPortfolio")
        self.actionUlo_it = QtWidgets.QAction(MainWindow)
        self.actionUlo_it.setObjectName("actionUlo_it")
        self.actionUkon_it = QtWidgets.QAction(MainWindow)
        self.actionUkon_it.setObjectName("actionUkon_it")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Hide not required items
        self.startupHideAction()

        # Check if DB records exist and is valid
        self.db_check()

        # load items to ComboBox
        self.initialComboBoxLoad()

        # map method to comboBox 'historie zaznamu' - method call on click
        self.historyComboBox.activated.connect(self.loadHistoryRecord)
        # map method to 'Obnovit zaznamy' button
        self.refreshHistoryButton.clicked.connect(self.refreshButton)
        # map method to 'Smazat zaznam'
        self.deleteRecordButton.clicked.connect(self.clickDeleteRecord)
        # map method to 'Novy zaznam'
        self.newRecordButton.clicked.connect(self.newRecord)

    def newRecord(self):
        self.enableButton(self.saveRecordButton)
        self.disableButton(self.deleteRecordButton).disableButton(self.editRecordButton)


    def saveRecord(self):
        date = datetime.datetime.now()
        print(str(date.year) + "-" + str(date.strftime("%m")) + "-" + str(date.strftime("%d")) + " "
              + str(date.strftime("%H")) + ":" + str(date.strftime("%M")) + ":" + str(date.strftime("%S")))

    def clickDeleteRecord(self):
        if self.historyComboBox.currentIndex() > 0:
            date = self.getSelectedRecordDate(self.historyComboBox)

            connect = self.db_connect()
            cursor = connect.cursor()
            result = cursor.execute(f"SELECT * FROM note WHERE date = \"{date}\"")
            data = result.fetchone()
            self.db_disconnect(connect)

            msg = QMessageBox()
            msg.setWindowTitle("Varování1")
            msg.setText(f"Chcete odstranit záznam z deníku jménem '{data[1]}'?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            msg.setDefaultButton(QMessageBox.No)
            msg.setInformativeText(f"Jedná se o záznam, který byl uložen dne {date}")

            msg.buttonClicked.connect(self.popupButtonAnswer)

            # show message box
            x = msg.exec_()

    def popupButtonAnswer(self, i):
        print(i.text())
        if i.text() == "&Yes" or i.text() == "Yes":
            if self.historyComboBox.currentIndex() > 0:
                date = self.getSelectedRecordDate(self.historyComboBox)

                connection = self.db_connect()
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM note WHERE date = '{date}'")
                connection.commit()
                self.db_disconnect(connection)
                self.refreshButton()
                self.startupHideAction()

    def refreshButton(self):
        self.historyComboBox.clear()
        self.historyComboBox.addItem("Vyberte z historie záznamů")
        self.db_check()
        self.initialComboBoxLoad()
        self.startupHideAction()

    def loadHistoryRecord(self):
        if self.historyComboBox.currentIndex() > 0:
            date = self.getSelectedRecordDate(self.historyComboBox)
            # Show label 'zaznam ze dne XYZ'
            self.thirdLabel.show()
            self.thirdLabel.setText("   " + f"Záznam ze dne {date}")
            self.thirdLabel.setStyleSheet("background-color: rgb(117, 80, 123);font-weight: 800;color: rgb(238, 238, 236);")
            # Show delete and edit button
            self.editRecordButton.show()
            self.deleteRecordButton.show()
            # Show save button as well ... but make it disabled
            self.saveRecordButton.show()
            self.disableButton(self.saveRecordButton)

            # find DB record
            connect = self.db_connect()
            cursor = connect.cursor()
            result = cursor.execute(f"SELECT * FROM note WHERE date = \"{date}\"")
            data = result.fetchone()
            self.db_disconnect(connect)

            # Show label 'Nazev zaznamu' + 'Record name'
            self.fourthLabel.show()
            self.recordName.show()
            self.disableWidget(self.recordName)
            self.recordName.setPlaceholderText(data[1])

            # Show record text
            self.recordText.show()
            self.recordText.setText(data[2])

    def getSelectedRecordDate(self, combobox):
        text = combobox.currentText()
        left = text.find("[")
        right = text.find("]")
        date = text[left + 1:right]
        return date

    def enableButton(self, button):
        button.setStyleSheet("background-color: rgb(165, 12, 70);"
                             "color: rgb(238, 238, 236);\n"
                             "font-weight: 800")
        self.enableWidget(button)
        return self

    def disableButton(self, button):
        button.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.disableWidget(button)
        return self

    def enableWidget(self, widget):
        widget.setEnabled(True)
        return self

    def disableWidget(self, widget):
        widget.setEnabled(False)
        return self

    def initialComboBoxLoad(self):
        db = self.db_connect()
        cursor = db.cursor()
        records = cursor.execute("SELECT * FROM note ORDER BY date ASC")
        records_data = records.fetchall()
        for one_record in records_data:
            date = one_record[0]
            name = one_record[1]
            comboBoxitem = f"[{date}] {name}"
            self.historyComboBox.addItem(comboBoxitem)

    def db_connect(self):
        connection = sqlite3.connect(f"{self.getScriptPath()}data/db/note.db")
        return connection

    def db_disconnect(self, connection):
        connection.close()
        return self

    def db_check(self):
        path = Path(f"{self.getScriptPath()}data/db/note.db")
        if not path.is_file():
            self.createNewDB()
        else:
            self.isDBfilevalid()

    def isDBfilevalid(self):
        test_connection = self.db_connect()
        test_cursor = test_connection.cursor()
        try:
            test_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{note}';")
        # file is not DB file -> delete file -> create new valid DB file
        except sqlite3.DatabaseError:
            os.remove(f"{self.getScriptPath()}data/db/note.db")
            self.createNewDB()

    def createNewDB(self):
        connection = self.db_connect()
        # https://docs.python.org/3/library/sqlite3.html
        # In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor.
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE note (date text PRIMARY KEY, name text NOT NULL, record text NOT NULL);")
        self.db_disconnect(connection)

    def startupHideAction(self):
        self.saveRecordButton.hide()
        self.deleteRecordButton.hide()
        self.editRecordButton.hide()
        self.thirdLabel.hide()
        self.fourthLabel.hide()
        self.recordName.hide()
        self.recordText.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Můj milý deníčku"))
        self.historyComboBox.setStatusTip(_translate("MainWindow", "Vyberte záznam z Vaší historie dle datumu a jména záznamu."))
        self.historyComboBox.setCurrentText(_translate("MainWindow", "Vyberte z historie záznamů"))
        self.historyComboBox.setItemText(0, _translate("MainWindow", "Vyberte z historie záznamů"))
        self.refreshHistoryButton.setStatusTip(_translate("MainWindow", "Obnovit historii záznamů. Používejte pouze, pokud nemůžete najít Váš záznam."))
        self.refreshHistoryButton.setText(_translate("MainWindow", "Obnovit záznamy"))
        self.secondLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#eeeeec;\">    Vytvořte nový záznam</span></p></body></html>"))
        self.firstLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#eeeeec;\">&nbsp;&nbsp;&nbsp;&nbsp;Historie záznamů</span></p></body></html>"))
        self.newRecordButton.setStatusTip(_translate("MainWindow", "Vytvořte nový záznam, který se uloží do historie Vašeho deníku."))
        self.newRecordButton.setText(_translate("MainWindow", "Nový záznam"))
        self.saveRecordButton.setStatusTip(_translate("MainWindow", "Uložit deník. Posléze jej můžete naleznout v historii záznamů."))
        self.saveRecordButton.setText(_translate("MainWindow", "Uložit záznam"))
        self.deleteRecordButton.setStatusTip(_translate("MainWindow", "Smazat záznam z deníku. Tento krok je nevratný!"))
        self.deleteRecordButton.setText(_translate("MainWindow", "Smazat záznam"))
        self.thirdLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#eeeeec;\">&nbsp;&nbsp;&nbsp;&nbsp;Záznam ze dne XYZ</span></p></body></html>"))
        self.recordText.setStatusTip(_translate("MainWindow", "Vložte prosím Váš text."))
        self.recordText.setPlaceholderText(_translate("MainWindow", "Místo pro Váš text ..."))
        self.editRecordButton.setToolTip(_translate("MainWindow", "Upravit Vámi zvolený záznam z historie."))
        self.editRecordButton.setStatusTip(_translate("MainWindow", "Smazat záznam z deníku. Tento krok je nevratný!"))
        self.editRecordButton.setText(_translate("MainWindow", "Upravit záznam"))
        self.fourthLabel.setText(_translate("MainWindow", "     Název záznamu:"))
        self.recordName.setStatusTip(_translate("MainWindow", "Zadejte jména pro Váš záznam."))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the program"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy the file"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste into the file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.savePortfolio.setText(_translate("MainWindow", "Uložit"))
        self.savePortfolio.setStatusTip(_translate("MainWindow", "Uložit otevřené portfólio"))
        self.savePortfolio.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.exitProgram.setText(_translate("MainWindow", "Ukončit"))
        self.exitProgram.setStatusTip(_translate("MainWindow", "Zavřít program"))
        self.exitProgram.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.openPortfolio.setText(_translate("MainWindow", "Otevřít"))
        self.openPortfolio.setStatusTip(_translate("MainWindow", "Otevřít uložené portfólio"))
        self.openPortfolio.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionUlo_it.setText(_translate("MainWindow", "Uložit"))
        self.actionUlo_it.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionUkon_it.setText(_translate("MainWindow", "Ukončit"))
        self.actionUkon_it.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
