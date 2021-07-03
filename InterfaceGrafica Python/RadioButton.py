from PyQt5 import uic, QtWidgets
def funcao_principal():
    if formulario.radioButton.isChecked():
        opcao = "Azul"
        estilo = 'QLabel{background-color: #0000FF};'
    elif formulario.radioButton_2.isChecked():
        opcao = "Verde"
        estilo = 'QLabel{background-color: #008000};'
    elif formulario.radioButton_3.isChecked():
        opcao = "Amarelo"
        estilo = 'QLabel{background-color: #FFFF00};'
    elif formulario.radioButton_4.isChecked():
        opcao = "Vermelho"
        estilo = 'QLabel{background-color: #FF0000};'
    else:
        opcao = ""
        estilo = 'QLabel {background-color:#D3D3D3};'
    formulario.label_2.setText("Cor selecionada: "+opcao)
    formulario.label_2.setStyleSheet(estilo)

app=QtWidgets.QApplication([])
formulario=uic.loadUi("RadioButton.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()