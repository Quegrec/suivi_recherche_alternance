import sys 
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSql import *
import sqlite3

class SQLTableDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Suivi de recherches d'emploi")
        self.setMinimumSize(935, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.tableWidget = QTableWidget()
        main_layout.addWidget(self.tableWidget)

        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

        self.load_data()

        btn_layout = QVBoxLayout()
        main_layout.addLayout(btn_layout)
        btn_valid = QPushButton("Valider modifications", self)
        btn_layout.addWidget(btn_valid)
        btn_valid.clicked.connect(self.valider)
        btn_ajout = QPushButton("Ajouter une nouvelle offre", self)
        btn_layout.addWidget(btn_ajout)
        btn_ajout.clicked.connect(self.ajouter)
             

    def load_data(self):
        self.cursor.execute("SELECT * FROM offres")
        data = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        headers = [description[0] for description in self.cursor.description]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))
                """layout =QHBoxLayout()
                btn_suppr = QPushButton("Supprimer la ligne", self)
                layout.addWidget(btn_suppr)
                btn_suppr.clicked.connect(self.suppr)"""
    
    def valider(self):
        """try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute("SELECT postule FROM offres")

            if [postule] == "non":
                # Perform the database update here (e.g., INSERT, UPDATE, DELETE)
                conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("SQLite error:", e)"""
    def ajouter(self):
        pass
    def suppr(self):
        pass


app = QApplication(sys.argv)
window = SQLTableDisplay()
window.show()
app.exec()