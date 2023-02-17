import PySimpleGUI as sg    #Biblioteca responsável pela criação da interface
import random
import webbrowser
import os


layout = [
            [sg.Text('Rolador de Dados by Allan',font='Times 16 bold')],
            [sg.Text('Tipo (dx): ',font='Times 14 bold'),
             sg.Input(key='tipo', do_not_clear=True,size=(4,1),font='Times 14 bold'),
             sg.Text('Quantidade: ',font='Times 14 bold'),
             sg.Input(key='quantidade', do_not_clear=True,size=(4,1),font='Times 14 bold')],
            [sg.Image(filename='img0.png',key='im1',visible=True),
             sg.Image(filename='img0.png',key='im2',visible=True),
             sg.Image(filename='img0.png',key='im3',visible=True),
             sg.Image(filename='img0.png',key='im4',visible=True),
             sg.Image(filename='img0.png',key='im5',visible=True)],
            [sg.Image(filename='img0.png',key='im6',visible=True),
             sg.Image(filename='img0.png',key='im7',visible=True),
             sg.Image(filename='img0.png',key='im8',visible=True),
             sg.Image(filename='img0.png',key='im9',visible=True),
             sg.Image(filename='img0.png',key='im10',visible=True)],
            [sg.Text('Bônus: ',font='Times 14 bold'),
             sg.Input(key='bonus', do_not_clear=True,size=(4,1),font='Times 14 bold')],
            [sg.Text('                                ',font='Times 14 bold'),
             sg.Button('Rolar', bind_return_key=True,font='Times 22 bold'),
             sg.Output(size=(10,2),font='Times 14 bold')],
            [sg.Button('Exit',bind_return_key=True),
             sg.Button('Código',bind_return_key=True),
             sg.Button('Vídeo',bind_return_key=True)]
]

window = sg.Window('Rolador de Dados', layout)     #Criação de uma janela de interface gráfica do usuário (GUI)

event = 0


while event != 'Exit':
    event, values = window.read()

    tipo = values['tipo']
    quantidade = values['quantidade']
    bonus = values['bonus']

    if event == 'Código':
        os.system("start \"\" https://github.com/Allanifba/rolador_de_dados")
        continue

    if event == 'Vídeo':
        os.system("start \"\" https://www.youtube.com/@prof_allanIFBA")
        continue

    if tipo != '' and quantidade != '':
        try:
            tipo = int(tipo)
            if tipo < 2 or tipo > 20:
                raise ValueError()
        except:
            sg.popup('Entre com o tipo de dado (2 para d2, 3 para d3, ..., 20 para d20 e com '
                     'a quantidade de dados 1 a 10.')
            continue

        try:
            quantidade = int(quantidade)
            if quantidade < 1 or quantidade > 10:
                raise ValueError()
        except:
            sg.popup('Entre com o tipo de dado (2 para d2, 3 para d3, ..., 20 para d20 e com '
                     'a quantidade de dados 1 a 10.')
            continue

        if bonus == '':
            bonus = 0
        else:
            try:
                bonus = int(bonus)
            except:
                sg.popup("Digite um valor inteiro, +1, -1, +2, -2,....")
                continue
        if event == 'Rolar':
            while i < 10:
                window[str(f'im{i + 1}')].Update(filename=str(f'img0.png'), visible=True)
                i = i + 1
            i = 0
            while i < quantidade:
                lista.append(random.randint(1, tipo))
                window[str(f'im{i + 1}')].Update(filename=str(f'img{lista[i]}.png'), visible=True)
                i += 1
            print(sum(lista) + bonus)
            i = 0
    else:
        sg.popup('Entre com o tipo de dado (2 para d2, 3 para d3, ..., 20 para d20 e com '
                 'a quantidade de dados 1 a 10.')

    lista = []
    i = 0









window.close()


