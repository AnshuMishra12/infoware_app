from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys
from login import LoginForm
from db import create_tables
from goods_receiving import GoodsReceivingForm
from sales_form import SalesForm
from product_master import ProductMasterForm  # ✅ added

app = QApplication(sys.argv)
create_tables()

# Global references
login_window = LoginForm()
goods_form = None
sales_form = None
master_form = None
main_menu = None

# ✅ After Login - Main Menu
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setGeometry(200, 200, 300, 250)

        layout = QVBoxLayout()

        goods_btn = QPushButton("Goods Receiving Form")
        goods_btn.clicked.connect(self.open_goods_form)

        sales_btn = QPushButton("Sales Form")
        sales_btn.clicked.connect(self.open_sales_form)

        master_btn = QPushButton("Product Master Form")
        master_btn.clicked.connect(self.open_product_master)

        layout.addWidget(goods_btn)
        layout.addWidget(sales_btn)
        layout.addWidget(master_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_goods_form(self):
        global goods_form
        goods_form = GoodsReceivingForm()
        goods_form.show()

    def open_sales_form(self):
        global sales_form
        sales_form = SalesForm()
        sales_form.show()

    def open_product_master(self):
        global master_form
        master_form = ProductMasterForm()
        master_form.show()

# ✅ Custom Login Checker
def check_login_custom():
    global main_menu
    username = login_window.username_input.text()
    password = login_window.password_input.text()

    if (username == "operator1" and password == "pass1") or (username == "operator2" and password == "pass2"):
        login_window.close()
        main_menu = MainMenu()
        main_menu.show()
    else:
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.critical(login_window, "Login Failed", "Invalid username or password.")

# ✅ Override Login Logic
login_window.check_login = check_login_custom

# ✅ Show Login Window
login_window.show()
sys.exit(app.exec())
