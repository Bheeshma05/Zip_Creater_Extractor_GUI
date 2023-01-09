import PySimpleGUI as sg
import Zip_converter

label_1 = sg.Text("Select Files to Compress: ")
input_box_1 = sg.InputText(tooltip='choose files')
browse_button_1 = sg.FilesBrowse("Browse", key='files')

label_2 = sg.Text("Select Destination Folder:")
input_box_2 = sg.InputText()
browse_button_2 = sg.FolderBrowse("choose", key='Folder')

compress_button = sg.Button("Compress")
window = sg.Window("File Compressor",
                   layout=[[label_1, input_box_1, browse_button_1],
                           [label_2, input_box_2, browse_button_2],
                           [compress_button]])
while True:
    event, values = window.read()

    filepaths = values['files'].split(';')
    Folder = values['Folder']
    Zip_converter.make_archive(filepaths, Folder)
    break

window.close()
