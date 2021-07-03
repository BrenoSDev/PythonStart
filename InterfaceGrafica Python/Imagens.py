import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Imagens'
        
        botao1 = QPushButton('Botao 1', self)
        botao1.move(150,200)
        botao1.resize(150, 80)
        botao1.setStyleSheet('QPushButton {background-color:#FF1328;font:bold;font-size:20px}')
        botao1.clicked.connect(self.botao1_click)
        
        botao2 = QPushButton('Botao 2', self)
        botao2.move(350, 200)
        botao2.resize(150, 80)
        botao2.setStyleSheet('QPushButton {background-color: #0600A0;font:bold;font-size:20px}')
        botao2.clicked.connect(self.botao2_click)
        
        self.label_1 = QLabel(self)
        self.label_1.move(50, 100)
        self.label_1.setStyleSheet('QLabel {font: bold; font-size:30px;color:"blue"}')
        self.label_1.resize(400,50)
        self.label_1.setText('Aperte um botão')
        
        self.carro = QLabel(self)
        self.carro.move(50, 400)
        self.carro.resize(400, 200)
        self.carro.setPixmap(QtGui.QPixmap('carro1.png'))
        
        self.CarregarJanela()
        
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label_1.setText('Carro 1 selecionado')
        self.label_1.setStyleSheet('QLabel {font:bold;font-size:30px;color:"green"}')
        self.carro.setPixmap(QtGui.QPixmap('carro1.png'))
    def botao2_click(self):
        self.label_1.setText('Carro 2 selecionado')
        self.label_1.setStyleSheet('QLabel {font:bold;font-size:30px;color:"red"}')
        self.carro.setPixmap(QtGui.QPixmap('carro2.png'))   

app = QApplication(sys.argv)
j= Janela()
sys.exit(app.exec())