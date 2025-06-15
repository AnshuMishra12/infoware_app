from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton,
    QComboBox, QTextEdit, QFileDialog, QMessageBox,
    QTableWidget, QTableWidgetItem
)
import db  # Database file jisme connect_db() hai

class ProductMasterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master Form")
        self.setGeometry(100, 100, 600, 600)

        layout = QVBoxLayout()

        self.barcode = QLineEdit()
        self.sku = QLineEdit()
        self.category = QComboBox()
        self.category.addItems(["Electronics", "Clothing", "Grocery"])

        self.subcategory = QComboBox()
        self.subcategory.addItems(["Mobile", "Shirt", "Snacks"])

        self.product_name = QLineEdit()
        self.description = QTextEdit()
        self.tax = QLineEdit()
        self.price = QLineEdit()
        self.unit = QLineEdit()

        self.image_path = QLineEdit()
        self.image_path.setPlaceholderText("No image selected")
        self.image_button = QPushButton("Upload Image")
        self.image_button.clicked.connect(self.upload_image)

        self.save_button = QPushButton("Save Product")
        self.save_button.clicked.connect(self.save_product)

        layout.addWidget(QLabel("Barcode"))
        layout.addWidget(self.barcode)

        layout.addWidget(QLabel("SKU ID"))
        layout.addWidget(self.sku)

        layout.addWidget(QLabel("Category"))
        layout.addWidget(self.category)

        layout.addWidget(QLabel("Subcategory"))
        layout.addWidget(self.subcategory)

        layout.addWidget(QLabel("Product Name"))
        layout.addWidget(self.product_name)

        layout.addWidget(QLabel("Description"))
        layout.addWidget(self.description)

        layout.addWidget(QLabel("Tax (%)"))
        layout.addWidget(self.tax)

        layout.addWidget(QLabel("Price"))
        layout.addWidget(self.price)

        layout.addWidget(QLabel("Default Unit"))
        layout.addWidget(self.unit)

        layout.addWidget(QLabel("Product Image"))
        layout.addWidget(self.image_path)
        layout.addWidget(self.image_button)

        layout.addWidget(self.save_button)

        # Table to show saved products
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels([
            "Barcode", "SKU", "Category", "Subcategory", "Name",
            "Description", "Tax", "Price", "Unit", "Image"
        ])
        layout.addWidget(self.table)

        self.setLayout(layout)

        # Load existing products
        self.load_products()

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Product Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.image_path.setText(file_name)

    def save_product(self):
        # Get all inputs
        data = (
            self.barcode.text(),
            self.sku.text(),
            self.category.currentText(),
            self.subcategory.currentText(),
            self.product_name.text(),
            self.description.toPlainText(),
            self.tax.text(),
            self.price.text(),
            self.unit.text(),
            self.image_path.text()
        )

        conn = db.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_master (
                barcode TEXT,
                sku TEXT,
                category TEXT,
                subcategory TEXT,
                name TEXT,
                description TEXT,
                tax TEXT,
                price TEXT,
                unit TEXT,
                image_path TEXT
            )
        """)
        cursor.execute("""
            INSERT INTO product_master (
                barcode, sku, category, subcategory, name,
                description, tax, price, unit, image_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Saved", "Product saved successfully!")
        self.load_products()  # Refresh the table

    def load_products(self):
        conn = db.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product_master")
        rows = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.table.setItem(row_idx, col_idx, item)
