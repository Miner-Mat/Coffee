import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableView, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUI()

    def initUI(self):
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('coffee.sqlite')
        # И откроем подключение
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('cofe')
        model.select()

        self.tableView.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())