import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Простой калькулятор")
        layout = QGridLayout()

        self.num1_edit = QLineEdit("0")
        self.num2_edit = QLineEdit("0")

        self.result_edit = QLineEdit()
        self.result_edit.setReadOnly(True)

        add_btn = QPushButton("+")
        sub_btn = QPushButton("-")
        mul_btn = QPushButton("×")
        div_btn = QPushButton("÷")

        add_btn.clicked.connect(self.add)
        sub_btn.clicked.connect(self.sub)
        mul_btn.clicked.connect(self.mul)
        div_btn.clicked.connect(self.div)

        layout.addWidget(QLabel("Первое число:"), 0, 0)
        layout.addWidget(self.num1_edit, 0, 1)

        layout.addWidget(QLabel("Второе число:"), 1, 0)
        layout.addWidget(self.num2_edit, 1, 1)

        layout.addWidget(QLabel("Результат:"), 2, 0)
        layout.addWidget(self.result_edit, 2, 1)

        layout.addWidget(add_btn, 3, 0)
        layout.addWidget(sub_btn, 3, 1)
        layout.addWidget(mul_btn, 4, 0)
        layout.addWidget(div_btn, 4, 1)

        self.setLayout(layout)
        self.show()

    def get_numbers(self):
        try:
            a = float(self.num1_edit.text())
            b = float(self.num2_edit.text())
            return a, b
        except ValueError:
            self.result_edit.setText("Ошибка ввода")
            return None, None

    def add(self):
        nums = self.get_numbers()
        if nums:
            result = nums[0] + nums[1]
            self.result_edit.setText(str(result))

    def sub(self):
        nums = self.get_numbers()
        if nums:
            result = nums[0] - nums[1]
            self.result_edit.setText(str(result))

    def mul(self):
        nums = self.get_numbers()
        if nums:
            result = nums[0] * nums[1]
            self.result_edit.setText(str(result))

    def div(self):
        nums = self.get_numbers()
        if nums:
            if nums[1] != 0:
                result = nums[0] / nums[1]
                self.result_edit.setText(str(result))
            else:
                self.result_edit.setText("Деление на 0!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec())