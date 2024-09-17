# Python PyQt5 - Relógio Digital
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

# criando widget
class Relogio(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self) # criando label
        self.timer = QTimer(self) # criando timer
        self.initUI()

    # interface do usuário
    def initUI(self):
        self.setWindowTitle("Relógio Digital")
        self.setGeometry(0, 0, 500, 200)

        # layout manager
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        # centralizando o layout
        self.label.setAlignment(Qt.AlignCenter)

        # estilos do label
        self.label.setStyleSheet("font-size: 100px;"
                                      "font-family: Arial;"
                                      "color: #23f702;")
        # estilo da window
        self.setStyleSheet("background-color: black;")

        # conectando com a hora atual do sistema
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        # chamando a função
        self.update()

    # função para atualizar a hora
    def update(self):
        hora_atual = QTime.currentTime().toString("hh:mm:ss")
        self.label.setText(hora_atual)

# rodando o app
if __name__ == "__main__":
    app = QApplication(sys.argv) # criando o app
    relogio = Relogio() # criando o objeto
    relogio.show()
    sys.exit(app.exec_()) # método para o programa executar
