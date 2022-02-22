import PySimpleGUI as sg

class BuscaCEP:
    def __init__(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Bem vindo ao BuscaCEP!')],
            [sg.Input(size =(25,0), key='CEP'), sg.Button('Buscar')]
        ]
        self.tela = sg.Window('BuscaCEP', layout)
    
    def iniciar(self):
        while True:
            event, values = self.tela.read()

            if event == sg.WIN_CLOSED:
                break

            print('Você pressionou:', values)

app = BuscaCEP()
app.iniciar()