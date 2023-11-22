import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('coffee')

        self.button_create_circle.clicked.connect(self.get_data)

    def get_data(self):
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("coffee.sqlite")
        if not con.open():
            print("Unable to open the database")
            return

        query = QSqlQuery("SELECT * FROM coffee")
        data = []
        while query.next():
            row_data = [str(query.value(i)) for i in
                        range(query.record().count())]
            data.append(", ".join(row_data))

        con.close()

        self.label.setText("\n".join(data))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
