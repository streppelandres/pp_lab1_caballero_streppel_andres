from App import App

if __name__ == '__main__':
    # Initialize app
    app = App()

    # TODO: Think for a more dynamic option or try to move app inside
    APP_OPTIONS = {
        'A' : app.option_a,
        'B' : app.option_b,
        'X' : app.option_exit
    }

    while True:
        option = input(app.get_menu() + '\n').upper()
        if option in APP_OPTIONS:
            APP_OPTIONS[option]()
        else:
            print('Opción incorrecta, vuelva a intentar\n')