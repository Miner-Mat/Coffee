import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('coffee.sqlite')
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('cofe')
        model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(0, 10)
        view.resize(617, 315)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
