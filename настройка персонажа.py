import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QSlider, QLabel, QProgressBar
)
from PyQt6.QtCore import Qt

class ToDoTime(QWidget):
    def __init__(self):
        super().__init__()
        self.total_points = 200
        self.initialize()

    def initialize(self):
        self.setWindowTitle("Настройка персонажа")
        self.setGeometry(300, 300, 400, 550)
        self.setup_window()
        self.set_dark_theme()
        self.show()

    def setup_window(self):
        self.main_layout = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Введите имя")

        self.main_layout.addWidget(self.name_edit)

        self.character_name_label = QLabel("Имя персонажа: ")
        self.main_layout.addWidget(self.character_name_label)

        self.name_edit.textChanged.connect(self.update_character_name)

        self.slider_strength = self.create_slider()
        self.slider_dexterity = self.create_slider()
        self.slider_intelligence = self.create_slider()

        self.main_layout.addLayout(self.create_slider_layout("Сила", self.slider_strength))
        self.main_layout.addLayout(self.create_slider_layout("Ловкость", self.slider_dexterity))
        self.main_layout.addLayout(self.create_slider_layout("Интеллект", self.slider_intelligence))

        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(self.total_points)
        self.progress_bar.setValue(self.total_points)
        self.main_layout.addWidget(QLabel("Осталось очков:"))
        self.main_layout.addWidget(self.progress_bar)

        self.class_label = QLabel("Класс: ")
        self.main_layout.addWidget(self.class_label)

        self.setLayout(self.main_layout)

        for slider in [self.slider_strength, self.slider_dexterity, self.slider_intelligence]:
            slider.valueChanged.connect(self.update_points)

        self.update_points()

    def create_slider(self):
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(1, 100)
        slider.setValue(1)
        return slider

    def create_slider_layout(self, label_text, slider):
        layout = QHBoxLayout()
        label = QLabel(label_text + ":")
        value_label = QLabel(str(slider.value()))
        slider.valueChanged.connect(lambda val, lbl=value_label: lbl.setText(str(val)))
        layout.addWidget(label)
        layout.addWidget(slider)
        layout.addWidget(value_label)
        return layout

    def update_points(self):
        strength = self.slider_strength.value()
        dexterity = self.slider_dexterity.value()
        intelligence = self.slider_intelligence.value()

        total_used = (strength - 1) + (dexterity - 1) + (intelligence - 1)
        remaining = self.total_points - total_used

        self.progress_bar.setValue(remaining)

        sliders = [self.slider_strength, self.slider_dexterity, self.slider_intelligence]
        for s in sliders:
            s.setEnabled(True)

        for s in sliders:
            current_value = s.value()
            max_possible = current_value + remaining
            s.setMaximum(max_possible if max_possible <= 100 else 100)

        for s in sliders:
            if s.maximum() == s.value():
                s.setEnabled(False)

        self.update_class()

    def update_class(self):
        strength = self.slider_strength.value()
        dexterity = self.slider_dexterity.value()
        intelligence = self.slider_intelligence.value()

        if strength > 70:
            char_class = "Воин"
        elif dexterity > 70:
            char_class = "Лучник"
        elif intelligence > 70:
            char_class = "Маг"
        else:
            char_class = "Универсал"

        self.class_label.setText(f"Класс: {char_class}")

    def update_character_name(self, text):
        self.character_name_label.setText(f"Имя персонажа: {text}")

    def set_dark_theme(self):
        self.setStyleSheet("""
            QWidget 
            {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a2e, stop:1 #16213e);
                color: #ecf0f1;
            }
            QLabel 
            {
                background: rgba(52, 73, 94, 0.3);
                border-radius: 8px;
                padding: 3px;
                font-weight: bold;
                font-size: 18px;
            }
            QPushButton
            {
                background: rgba(100, 100, 100, 0.3);
                border-radius: 8px;
                padding: 3px;
                font-weight: bold;
                font-size: 18px;
            }
            QPushButton:hover 
            {
             background: rgba(255, 100, 100, 1);
             }
            QProgressBar 
            {
                border: 2px solid #34495e;
                border-radius: 8px;
                text-align: center;
                color: white;
                font-weight: bold;
                height: 20px;
            }
            QProgressBar::chunk 
            {
                background: rgba(255, 100, 100, 0.3);
                border-radius: 6px;
            }
            QLineEdit 
            {
                background: rgba(255, 255, 255, 0.3);
                border-radius: 8px;
                padding: 3px;
                font-weight: bold;
                font-size: 14px;
                text-align: center;
                margin-right: auto;
                margin-left: auto;
            }
        """)

app = QApplication(sys.argv)
window = ToDoTime()
sys.exit(app.exec())