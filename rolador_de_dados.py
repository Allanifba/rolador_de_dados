'''
Siga os passos para rodar o programa no PyCharm (recomendado)
(1) Crie um novo projeto no PyCharm rolador_de_dados (recomendado)
(2) Copie o código do arquivo rolador_de_dados.py para a janela de execução
(3) Instale o módulo PySimpleGUI
	No terminal digite: pip install PySimpleGUI
(4) Copie a pasta imagens_rolador_de_dados e para o mesmo diretório que o arquivo
principal do seu projeto rolador_de_dados (mesma pasta que o arquivo main ou
rolador_de_dados caso tenha editado)
(5) Execute o arquivo: shift+f10

Siga os passos para criar um arquivo .exe (continuando do passo 5)
(6) No terminal digite: pip install pyinstaller
(7) Novamente, no terminal: pyinstaller --onefile -w rolador_de_dados.py
(8) O arquivo exe encontra-se na pasta dist
(9) Copie o arquivo rolador_de_dados.exe para um mesmo diretório contendo a pasta
imagens_rolador_de_dados. Você só precisará deste dois para rodar em qualquer
máquina.
'''


import PySimpleGUI as sg    #Biblioteca responsável pela criação da interface
import random
import webbrowser
import os

# Caminho completo até a pasta com as imagens
IMAGES_FOLDER = os.path.join(os.getcwd(), 'imagens_rolador_de_dados')

layout = [
            [sg.Text('Rolador de Dados by Allan',font='Times 16 bold')],
            [sg.Text('Tipo (dx): ',font='Times 14 bold'),
             sg.Input(key='tipo', do_not_clear=True,size=(4,1),font='Times 14 bold'),
             sg.Text('Quantidade: ',font='Times 14 bold'),
             sg.Input(key='quantidade', do_not_clear=True,size=(4,1),font='Times 14 bold')],
            [sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im1',visible=True),
             sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im2',visible=True),
             sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im3',visible=True),
             sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im4',visible=True),
             sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im5',visible=True)],
            [sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im6',visible=True),
             sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im7',visible=True),
             sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im8',visible=True),
             sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im9',visible=True),
             sg.Image(filename=os.path.join(IMAGES_FOLDER, 'img0.png'),key='im10',visible=True)],
            [sg.Text('Bônus: ',font='Times 14 bold'),
             sg.Input(key='bonus', do_not_clear=True,size=(4,1),font='Times 14 bold')],
            [sg.Text('                    ',font='Times 14 bold'),
             sg.Button('Rolar', bind_return_key=True,font='Times 22 bold'),
             sg.Output(size=(10,2),font='Times 14 bold')],
            [sg.Button('Exit',bind_return_key=True)]
]

window = sg.Window('Rolador de Dados', layout)     #Criação de uma janela de interface gráfica do usuário (GUI)

event = 0

while event != 'Exit':
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    tipo = values['tipo']
    quantidade = values['quantidade']
    bonus = values['bonus']

    if event == 'Código':
        os.system("start \"\" https://github.com/Allanifba/rolador_de_dados")
        continue

    if event == 'Vídeo':
        os.system("start \"\" https://www.youtube.com/watch?v=OZHzVkdRVd4")
        continue

    if tipo != '' and quantidade != '':
        try:
            tipo = int(tipo)
            if tipo < 2 or tipo > 20:
                raise ValueError()
        except:
            sg.popup('Entre com o tipo de dado (2 para d2, 3 para d3, ..., 20 para d20) e a quantidade de dados (1 a 10).')
            continue

        try:
            quantidade = int(quantidade)
            if quantidade < 1 or quantidade > 10:
                raise ValueError()
        except:
            sg.popup('Entre com o tipo de dado (2 para d2, 3 para d3, ..., 20 para d20) e a quantidade de dados (1 a 10).')
            continue

        if bonus == '':
            bonus = 0
        else:
            try:
                bonus = int(bonus)
            except:
                sg.popup("Digite um valor inteiro, +1, -1, +2, -2,....")
                continue
        lista = []
        i = 0
        if event == 'Rolar':
            while i < 10:
                window[str(f'im{i + 1}')].Update(filename=str(f'imagens_rolador_de_dados/img0.png'), visible=True)
                i = i + 1
            i = 0
            while i < quantidade:
                lista.append(random.randint(1, tipo))
                window[str(f'im{i + 1}')].Update(filename=str(f'imagens_rolador_de_dados/img{lista[i]}.png'), visible=True)
                i += 1
            print(sum(lista) + bonus)
            i = 0
    else:
        sg.popup('Entre com o tipo de dado (2 para d2, 3 para d3, ..., 20 para d20) e a quantidade de dados (1 a 10).')

    lista = []
    i = 0


window.close()