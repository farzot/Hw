import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QCheckBox, QLabel, QPushButton

class MenuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Retoran Menu')
        self.setGeometry(100, 100, 300, 300)

        self.taomlar = {
            '1-taom': {'name': 'Taom 1', 'narx': 10},
            '2-taom': {'name': 'Taom 2', 'narx': 15},
            'ichimlik': {'name': 'Ichimlik', 'narx': 5},
            'desert': {'name': 'Desert', 'narx': 8}
        }

        self.selected_taomlar = {
            '1-taom': [],
            '2-taom': [],
            'ichimlik': [],
            'desert': []
        }

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        taomlar_groupbox = self.create_taomlar_groupbox()
        layout.addWidget(taomlar_groupbox)

        button = QPushButton('Chek ro\'yxatni chiqarish')
        button.clicked.connect(self.print_chek_royxat)
        layout.addWidget(button)

        self.setLayout(layout)

    def create_taomlar_groupbox(self):
        groupbox = QGroupBox('Taomlar')

        layout = QVBoxLayout()

        for key, value in self.taomlar.items():
            checkbox = QCheckBox(value['name'])
            checkbox.stateChanged.connect(lambda state, key=key: self.taom_state_changed(state, key))

            layout.addWidget(checkbox)

        groupbox.setLayout(layout)

        return groupbox

    def taom_state_changed(self, state, key):
        if state == 2:
            self.selected_taomlar[key].clear()
            self.selected_taomlar[key].append(self.taomlar[key])

    def print_chek_royxat(self):
        for key, value in self.selected_taomlar.items():
            if value:
                print(key + ':')
                for taom in value:
                    print(taom['name'] + ' (' + str(taom['narx']) + ')')
                print('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = MenuApp()
    menu.show()
    sys.exit(app.exec_())

