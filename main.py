import user_interface as ui
import tests as tests


def main():
    ui.OutputString("Săbăilă Călin-Ioan, Group: 916")

    tests.RunAllTests()

    while True:
        ui.PrintMenu()
        option = ui.InputString()
        ui.HandleOptions(option)


# Săbăilă Călin-Ioan, Group: 916
if __name__ == "__main__":
    main()
