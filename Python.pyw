from random import randint
import PySimpleGUI as sg
import os

sg.LOOK_AND_FEEL_TABLE['RNGwindows'] = {'BACKGROUND': '#7d7d7d',
                                        'TEXT': '#ffffff',
                                        'INPUT': '#545454',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('white', '#808080'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }

sg.theme('RNGwindows')

layout = [  [sg.Text('what should be the max number?')],
            [sg.Text('Type here.'), sg.InputText()],
            [sg.Text(' ')],
            [sg.OK(), sg.Cancel()]]

window = sg.Window('RNG Generator', layout)

while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        window.close()
        exit()
    if event in (sg.WIN_CLOSED, 'OK'):
        break

window.close()

print('You entered', values[0])
window.close()

while True:
    rang = values[0]
    try:
        rang = int(rang)
    except ValueError:
        print ("The number has to be an integer, try again.")
    else:
        break

number = randint(1, rang)
print ("Random Number is %s" % number)

os.system('echo %s | clip ' % number)

sg.theme('RNGwindows')

layout2 = [  [sg.Text('Your Random Number Is...')],
            [sg.Text(number)],
            [sg.Text(' ')],
            [sg.Text('Text also copied to clipboard.')],
            [sg.OK(), sg.Cancel()]]

window = sg.Window('RNG Generator', layout2)

while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        window.close()
        exit()
    if event in (sg.WIN_CLOSED, 'OK'):
        break

window.close()