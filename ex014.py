# Python PyQt5 - Cronômetro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class Cronometro(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.label = QLabel("00:00:00.00", self)
        self.botao_comecar = QPushButton("Começar", self)
        self.botao_parar = QPushButton("Parar", self)
        self.botao_resetar = QPushButton("Resetar", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cronômetro")
        self.setGeometry(0, 0, 700, 350)

        # layout manager vertical
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.label.setAlignment(Qt.AlignCenter)

        # layout horizontal
        hbox = QHBoxLayout()

        hbox.addWidget(self.botao_comecar)
        hbox.addWidget(self.botao_parar)
        hbox.addWidget(self.botao_resetar)

        vbox.addLayout(hbox)

        # criando objetos para estilização individual
        self.botao_comecar.setObjectName("botao1")
        self.botao_parar.setObjectName("botao2")
        self.botao_resetar.setObjectName("botao3")

        # estilo
        self.setStyleSheet("""
            QPushButton, QLabel {
            font-weight: bold;
            font-family: Arial;
            padding: 20px;
            }
            QPushButton {
                font-size: 30px;
                background-color: black;
                color: white;
                border-radius: 10px;
            }
            QLabel {
            color: white;
                font-size: 80px;
                background-color: black;
                margin: 10px;
            }
        """)

        # conectando os botões
        self.botao_comecar.clicked.connect(self.comecar)
        self.botao_parar.clicked.connect(self.parar)
        self.botao_resetar.clicked.connect(self.resetar)
        self.timer.timeout.connect(self.update)

    def comecar(self):
        self.timer.start(10)  # 10 milisegundos

    def parar(self):
        self.timer.stop()

    def resetar(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.label.setText(self.formatacao(self.time))

    def formatacao(self, time):
        horas = time.hour()
        minutos = time.minute()
        segundos = time.second()
        milisegundos = time.msec() // 10
        return f"{horas:02}:{minutos:02}:{segundos:02}.{milisegundos:02}"

    def update(self):
        self.time = self.time.addMSecs(10)
        self.label.setText(self.formatacao(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cronometro = Cronometro()
    cronometro.show()
    sys.exit(app.exec_())
