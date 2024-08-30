import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 900)
        self.setWindowTitle("Segredo do Gênio - Adivinhe o número")
        self.initUI()

        # Estilo da janela principal
        self.setStyleSheet("background-color: #2bacfc;")

    def initUI(self):
        # Estilos
        style_label = """
            color: white;
            font-size: 40px;
            font-family: Arial;
            text-align: center;
            font-weight: bold;
        """
        style_line_edit = """
            font-size: 30px;
            font-family: Arial;
            background-color: white;
        """
        style_botao = """
            color: white;
            font-size: 25px;
            background-color: #052b82;
            font-weight: bold;
            border-radius: 5px;
        """
        style_hovered_botao = """
            color: white;
            font-size: 25px;
            background-color: #024898;
            font-weight: bold;
            border-radius: 5px;
        """
        style_contador = """
            font-size: 20px;
            font-weight: bold;
            color: white;
        """

        # Label 1 - Texto
        self.label1 = QLabel("Adivinhe o número entre 1 e 100", self)
        self.label1.setGeometry(0, 0, 800, 200)
        self.label1.setStyleSheet(style_label)
        self.label1.setAlignment(Qt.AlignCenter)

        # Label 2 - Imagem
        self.label2 = QLabel(self)
        self.label2.setGeometry(280, 200, 400, 400)
        self.atualizar_imagem("akinator.png")

        # Input
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(300, 600, 200, 40)
        self.line_edit.setStyleSheet(style_line_edit)

        # Botão
        self.botao = QPushButton("Verificar", self)
        self.botao.setGeometry(275, 700, 250, 70)
        self.botao.setStyleSheet(style_botao)
        self.botao.clicked.connect(self.submit)
        self.botao.enterEvent = lambda event: self.botao.setStyleSheet(style_hovered_botao)
        self.botao.leaveEvent = lambda event: self.botao.setStyleSheet(style_botao)

        # Contador
        self.contador = QLabel("Tentativas: 0", self)
        self.contador.setGeometry(300, 800, 300, 40)
        self.contador.setStyleSheet(style_contador)

        # Atributos adicionais
        self.num = random.randint(1, 100)
        self.cont = 0
        self.total = 0

    def atualizar_imagem(self, imagem):
        pixmap = QPixmap(imagem)
        self.label2.setPixmap(pixmap)

    def jogar_novamente(self):
        self.num = random.randint(1, 100)
        self.cont = 0
        self.total = 0
        self.contador.setText("Tentativas: 0")
        self.label1.setText("Adivinhe o número entre 1 e 100")
        self.atualizar_imagem("akinator.png")
        self.line_edit.setText("")
        self.botao.setText("Verificar")
        self.botao.clicked.disconnect()
        self.botao.clicked.connect(self.submit)

    def submit(self):
        entrada = self.line_edit.text()

        if entrada.isdigit():
            numero = int(entrada)

            if numero > 100:
                self.label1.setText("Digite um número entre 1 e 100")
                self.line_edit.setText("")
                return

            self.cont += 1
            self.total += 1
            self.contador.setText(f"Tentativas: {self.cont}")

            if numero > self.num:
                self.label1.setText("Muito alto")
                self.atualizar_imagem("akinator_alto.png")
                self.line_edit.setText("")
            elif numero < self.num:
                self.label1.setText("Muito baixo")
                self.atualizar_imagem("akinator_baixo.png")
                self.line_edit.setText("")
            else:
                self.label1.setText("VOCÊ ACERTOU!")
                self.atualizar_imagem("akinator_feliz.png")
                self.contador.setText(f"Total de tentativas: {self.total}")
                self.line_edit.setText("")
                self.botao.setText("Jogar novamente?")
                self.botao.clicked.disconnect()
                self.botao.clicked.connect(self.jogar_novamente)
        else:
            self.label1.setText("Por favor, digite um valor válido")
            self.line_edit.setText("")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
