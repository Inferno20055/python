import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QRadioButton, QPushButton, QTextEdit
)
from PyQt6.QtCore import QDateTime

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Конвертер валют")

        self.rate_usd_to_rub = 90
        self.rate_rub_to_usd = 0.011

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Введите сумму")
        self.layout.addWidget(self.input_line)

        self.radio_layout = QHBoxLayout()

        self.radio_usd_to_rub = QRadioButton("USD → RUB")
        self.radio_rub_to_usd = QRadioButton("RUB → USD")

        self.radio_usd_to_rub.setChecked(True)

        self.radio_layout.addWidget(self.radio_usd_to_rub)
        self.radio_layout.addWidget(self.radio_rub_to_usd)
        self.layout.addLayout(self.radio_layout)

        self.convert_button = QPushButton("Конвертировать")
        self.layout.addWidget(self.convert_button)

        self.history_text = QTextEdit()
        self.history_text.setReadOnly(True)
        self.layout.addWidget(self.history_text)

        self.convert_button.clicked.connect(self.perform_conversion)
        self.input_line.returnPressed.connect(self.perform_conversion)
        self.radio_usd_to_rub.toggled.connect(self.clear_input)
        self.radio_rub_to_usd.toggled.connect(self.clear_input)

    def clear_input(self):
        self.input_line.clear()

    def perform_conversion(self):
        amount_text = self.input_line.text()
        try:
            amount = float(amount_text)
        except ValueError:
            self.append_history("Некорректная сумма.")
            return

        if self.radio_usd_to_rub.isChecked():
            result = amount * self.rate_usd_to_rub
            direction = "USD → RUB"
        else:
            result = amount * self.rate_rub_to_usd
            direction = "RUB → USD"

        timestamp = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        history_entry = f"{timestamp} | {amount} ({direction}) = {result:.2f}"

        self.append_history(history_entry)

    def append_history(self, text):
        self.history_text.append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverter()
    window.show()
    sys.exit(app.exec())