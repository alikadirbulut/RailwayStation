
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

import sqlite3
import random
## ==> SPLASH SCREEN
from ui_new_splash import Ui_splashscreen


## ==> MAIN WINDOW
from ui_mainwindow import Ui_MainWindow

## ==> LOG IN SCREEN
from ui_login import Ui_Dialog

## ==> GLOBALS
counter = 0

con = sqlite3.connect("db.db")


UserName = ""
FirstName = ""
LastName = ""
Address = ""
Phone = 0


def select_from_table(tablename, compare_value="Id", id=0):
    cur = con.cursor()
    if id == 0:
        cur.execute("SELECT * FROM %s" % tablename)
    else:
        cur.execute("SELECT * FROM %s WHERE %s=%d" % (tablename, compare_value, id))
    return cur


def execute_command(string):
    cur = con.cursor()
    cur.execute(string)
    con.commit()


def does_ticket_exist(id):
    cur = select_from_table("ticket_info", "TrainId", id)
    if cur.fetchone() != None:
        return True
    else:
        return False


def insert_ticket():
    train_results = select_from_table("train")

    for row in train_results:
        train_number = row[0]
        train_seats_left = row[4]
        # TODO : SKIP IF TICKET EXISTS OR TRAIN HAS NO SEATS LEFT

        if does_ticket_exist(train_number) or train_seats_left <= 0:
            continue

        train_dtime = row[2]  # same
        train_date = row[2]  # same
        train_price = random.randint(1, 100)
        train_id = row[0]

        execute_command(
            "INSERT INTO ticket_info ('TrainNumber', 'ArrivalTime', 'Date', 'DepartureTime', 'Price', 'TrainId') VALUES (%d, '-', '%s', '%s', %d, %d)" % (
                train_number, train_dtime, train_date, train_price, train_id))


def buy_ticket(index):
    table = select_from_table("ticket_info", "Id", index).fetchone()
    fname = FirstName
    lname = LastName
    adress = Address
    phone = Phone
    username = UserName
    price = table[5]
    ticketid = table[0]

    execute_command(
        "INSERT INTO transaction_details ('Fname' , 'Lname', 'Address', 'Phone', 'Username', 'Price', 'TicketID') VALUES ('%s', '%s', '%s', %d, '%s', %d, %d)" % (
            fname, lname, adress, phone, username, price, ticketid))

    # UPDATE TRAIN TABLE (SEATS_LEFT - 1)
    train_id = table[6]
    train_info = select_from_table("train", "Id", train_id).fetchone()
    train_seats_left = train_info[4] - 1
    execute_command("UPDATE train SET SeatsLeft=%d WHERE Id=%d" % (train_seats_left, train_id))


def remove_ticket(index):
    transaction_table = select_from_table("transaction_details", "Id", index).fetchone()
    ticket_table = select_from_table("ticket_info", "Id", transaction_table[7]).fetchone()
    train_id = ticket_table[6]
    train_info = select_from_table("train", "Id", train_id).fetchone()
    train_seats_left = train_info[4] + 1
    execute_command("UPDATE train SET SeatsLeft=%d WHERE Id=%d" % (train_seats_left, train_id))
    execute_command("DELETE FROM transaction_details WHERE Id=%d" % transaction_table[0])


# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.HandleButton()

    def HandleButton(self):
        self.ui.pushButton_4.clicked.connect(self.RefreshTables)
        self.ui.buy_button.clicked.connect(self.BuyTicket)
        self.ui.cancel_button.clicked.connect(self.CancelTicket)

    def RefreshTables(self):
        #Connect to SqLite3 database and fill GUI table with data

        insert_ticket()
        write_to_table(self.ui.tableWidget_2, select_from_table("train", "Id", 0))
        write_to_table(self.ui.tableWidget, select_from_table("ticket_info", "Id", 0))
        write_to_table(self.ui.tableWidget_3, select_from_table("transaction_details"))

    def BuyTicket(self):
        index = int(self.ui.spinBox.text())
        buy_ticket(index)
        write_to_table(self.ui.tableWidget_3, select_from_table("transaction_details"))
        self.RefreshTables()

    def CancelTicket(self):
        index = int(self.ui.spinBox_2.text())
        remove_ticket(index)
        write_to_table(self.ui.tableWidget_3, select_from_table("transaction_details"))
        self.RefreshTables()
# DIALOG BOX

def write_to_table(tableWidget, result):
    tableWidget.setRowCount(0)
    for row_number, row_data in enumerate(result):
        tableWidget.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


class Dialog(QDialog):
    #def Ui_dialog(self):
    def __init__(self):
        super(Dialog,self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.show()

    def loginfunction(self):
        global FirstName, LastName, UserName, Address, Phone
        FirstName = self.fname.text()
        LastName = self.lname.text()
        UserName = self.username.text()
        Address = self.address.text()
        Phone = int(self.phone.text())
        self.main = MainWindow()
        self.main.show()
        self.close()

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_splashscreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Dialog()
            self.main.show()



            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())



