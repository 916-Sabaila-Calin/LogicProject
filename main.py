import functions
import user_interface as ui
import tests as tests


# Săbăilă Călin-Ioan, Group: 916
def main():
    ui.OutputString("Săbăilă Călin-Ioan, Group: 916")

    tests.RunAllTests()

    while True:
        ui.PrintMenu()
        option = ui.InputString()
        ui.HandleOptions(option)


if __name__ == "__main__":
    main()