import PySimpleGUI as sg
sg.theme("BluePurple")
sg.theme_text_color("#007FFF")
Window = sg.Window(title="Profil",
                   layout=[[sg.Text ("SELAMAT DATANG DIKELAS",
                            font=("Arial",25,"italic","bold","underline"))],
                          [sg.Text ("NAMA       : Muhammad Ervan Alpani")],
                          [sg.Text ("NPM        : 2210010076")],  
                          [sg.Text ("Kelas      : TI 5A NonReg Banjarmasin")],
                          [sg.Text ("Matkul     : Pemprograman Visual 3")]
                        ],
                        size=(520,200),
                        font=("Times",10)) 
Window()
Window.close()