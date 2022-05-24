import PySimpleGUI as sg

from views.ViewController import ViewController


view_controller = ViewController()

# This is your master table.... keys are what will be shown on the bar.  The item is what you want to happen.
launcher_buttons = {
                     sg.SYMBOL_DOWN_ARROWHEAD : None,
                     'A Estrella': view_controller.launch_main_win,
                    'Ejemplos' : view_controller.launch_examples_view,
                     'Guia Rápida': view_controller.launch_guide,
                     sg.EMOJI_BASE64_HAPPY_BIG_SMILE: view_controller.launch_repo,
                     'Documentación' : view_controller.print_docs,
                     'Créditos' : view_controller.launch_view_credits,
                     'Exit': None}

MINIMIZED_IMAGE = sg.EMOJI_BASE64_HAPPY_THUMBS_UP

DEFAULT_SCREEN_BACKGROUND_COLOR = 'black'
DEFAULT_BUTTON_SIZE = (12, 5)

def make_window():

    screen_background_color = sg.user_settings_get_entry('-screen color-', DEFAULT_SCREEN_BACKGROUND_COLOR)
    old_bg = sg.theme_background_color()
    sg.theme_background_color(screen_background_color)
    button_row = []
    for item in launcher_buttons.keys():
        tip = 'Seleccione una opción'
        if isinstance(item, bytes):
            button = sg.Button(image_data=item, key=item, metadata=launcher_buttons[item], button_color=screen_background_color,tooltip=tip, border_width=0)
        else:
            button = sg.Button(item, key=item, metadata=launcher_buttons[item],  tooltip=tip, border_width=0)
        button_row.append(button)

    col_buttons = sg.Column([button_row], p=0, k='-BUTTON COL-')
    col_minimized = sg.Column([[sg.Button(image_data=MINIMIZED_IMAGE, k='-MINIMIZED IMAGE-', button_color=sg.theme_background_color(), border_width=0)]], visible=False, k='-MINIMIZED COL-')

    layout = [[sg.pin(col_minimized), sg.pin(col_buttons)]]

    screen_size = sg.Window.get_screen_size()
    location = screen_size[0] // 2, screen_size[1] - 200        # set a default location centered and near the bottom of the screen
    location = sg.user_settings_get_entry('-window location-', location)
    keep_on_top = sg.user_settings_get_entry('-keep on top-', True)



    window = sg.Window('Window Title', layout, location=location,
                       keep_on_top=keep_on_top, no_titlebar=True, grab_anywhere=True, background_color=screen_background_color,
                       auto_size_buttons=False, default_button_element_size=DEFAULT_BUTTON_SIZE, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT,
                       enable_close_attempted_event=True, use_default_focus=False)
    sg.theme_background_color(old_bg)

    return window





def main():
    print('MAIN')
    window = make_window()

    while True:
        event, values = window.read(timeout=1000)        # Not needed but handy while debugging
        # print(event, values)
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit', sg.WIN_CLOSED):
            if event != sg.WIN_CLOSED:
                if sg.user_settings_get_entry('-auto save location-', True):
                    print('saving locatoin', window.current_location())
                    sg.user_settings_set_entry('-window location-', window.current_location())
            break
        if event in launcher_buttons:
            action = window[event].metadata
            if isinstance(action, str):
                if action.endswith(('.py', '.pyw')):
                    sg.execute_py_file(action)
                else:
                    sg.execute_command_subprocess(action)
            elif callable(action):
                action()
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(view_controller.get_credits())
        elif event == sg.SYMBOL_DOWN_ARROWHEAD:
            window['-BUTTON COL-'].update(visible=False)
            window['-MINIMIZED COL-'].update(visible=True)
        elif event == '-MINIMIZED IMAGE-':
            window['-BUTTON COL-'].update(visible=True)
            window['-MINIMIZED COL-'].update(visible=False)
    window.close()



if __name__ == '__main__':
    main()