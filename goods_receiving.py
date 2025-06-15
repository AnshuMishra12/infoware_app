from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)

class GoodsReceivingForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goods Receiving Form")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.product_name = QLineEdit()
        self.supplier_name = QLineEdit()
        self.quantity = QLineEdit()
        self.unit = QLineEdit()
        self.rate = QLineEdit()
        self.tax = QLineEdit()

        self.total = QLabel("Total: ₹0.00")
        self.final_amount = QLabel("Final Amount (with tax): ₹0.00")

        submit_button = QPushButton("Calculate Total")
        submit_button.clicked.connect(self.calculate_total)

        # Labels and Inputs
        layout.addWidget(QLabel("Product Name"))
        layout.addWidget(self.product_name)

        layout.addWidget(QLabel("Supplier Name"))
        layout.addWidget(self.supplier_name)

        layout.addWidget(QLabel("Quantity"))
        layout.addWidget(self.quantity)

        layout.addWidget(QLabel("Unit of Measurement"))
        layout.addWidget(self.unit)

        layout.addWidget(QLabel("Rate per Unit"))
        layout.addWidget(self.rate)

        layout.addWidget(QLabel("Tax (%)"))
        layout.addWidget(self.tax)

        layout.addWidget(submit_button)
        layout.addWidget(self.total)
        layout.addWidget(self.final_amount)

        self.setLayout(layout)

    def calculate_total(self):
        try:
            qty = float(self.quantity.text())
            rate = float(self.rate.text())
            tax_percent = float(self.tax.text())

            total_rate = qty * rate
            tax_amount = (total_rate * tax_percent) / 100
            final = total_rate + tax_amount

            self.total.setText(f"Total: ₹{total_rate:.2f}")
            self.final_amount.setText(f"Final Amount (with tax): ₹{final:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers in Quantity, Rate, and Tax fields.")
