import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
button1 = sg.FileBrowse("Choose", key="files")
label2 = sg.Text("Select destiantion folder")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key="folder")

compress = sg.Button("compress")
output=sg.Text(key="output", text_color="green")

window=sg.Window('File Compressor',
                 layout=[[label1, input1, button1],
                         [label2, input2, button2],
                         [compress, output]])
while True:

    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder=values["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="compression completed")

window.close()