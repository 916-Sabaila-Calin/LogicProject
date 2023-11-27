import functions
import user_interface as ui

def main():
    while True:
        ui.PrintMenu()
        option = ui.InputString()
        ui.HandleOptions(option)


if __name__ == "__main__":
    main()