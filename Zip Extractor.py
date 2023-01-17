import PySimpleGUI as sg
import Zip_extractor_functions as ext

sg.theme('Darkgrey14')

label1 = sg.Text('Select the Zip file ')
input_box1 = sg.InputText()
choose_button1 = sg.FileBrowse('Select')

label2 = sg.Text('Select the Destination folder')
input_box2 = sg.InputText(tooltip='select the folder')
choose_button2 = sg.FolderBrowse('Browse')

extract_button = sg.Button('Extract')
output_label = sg.Text('', key='output')

window = sg.Window('Zip Extractor',
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                           [extract_button, output_label]],
                   font=('Helvetica', 10))
while True:

    event, values = window.read()
    file = values['Select']
    folder = values['Browse']
    ext.extract_archive(file, folder)
    window['output'].update(value='Zip file extracted successfully', text_color='Green')

    if sg.WIN_CLOSED:
        break

window.close()