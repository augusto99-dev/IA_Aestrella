import PySimpleGUI as sg

def create(information_array, headings):

    layout = [
        [sg.Table(values=information_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='right',
                    num_rows=10,
                    enable_events=True,
                    key='-CONTACT_TABLE-',
                    row_height=35,
                    tooltip='Reservations Table')],
    ]

    contact_information_window = sg.Window("Tabla",layout, modal=True)

    while True:
        event, values = contact_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == '-CONTACT_TABLE-':
            selected_index = values['-CONTACT_TABLE-'][0]
            selected_row = information_array[selected_index]
            popup_message = "Nodo: " + selected_row[0] + "\n" + "Heuristica: " + selected_row[1]
            sg.popup(popup_message)
            print(selected_row)
          
        
    contact_information_window.close()
