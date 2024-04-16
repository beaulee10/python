def table(class_name, attributes, methods):
    print("|---------------------------------------|")
    print(f"| Class Name         {class_name.capitalize()}           |")
    print("|---------------------------------------|")
    print("| Variables                             |")
    for atr in attributes:
        print(f"|                    -{atr}     |")
    print("|---------------------------------------|")
    print("| Methods                               |")
    for mth in methods:
        print(f"|                    +{mth} |")
    print("|---------------------------------------|")

def main():
    class_name = "CoffePot"
    attributes = ["brand: String", "color: String", "space: Integer", "water_level: Integer"]
    methods = ["brewCoffee(): void", "setTimer(time): void", "checkWaterLevel(): Integer", "turnOff(): void"]

    table(class_name, attributes, methods)

main()
