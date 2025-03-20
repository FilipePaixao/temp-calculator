def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    conversions = []
    while True:
        print("Calculadora de Temperatura")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Celsius para Kelvin")
        print("4. Kelvin para Celsius")
        print("5. Fahrenheit para Kelvin")
        print("6. Kelvin para Fahrenheit")
        print("7. Sair")
        
        choice = int(input("Escolha uma opção: "))
        
        if choice == 7:
            break
        
        temp = float(input("Digite a temperatura: "))
        
        if choice == 1:
            result = celsius_to_fahrenheit(temp)
            print(f"{temp} Celsius é igual a {result} Fahrenheit")
            conversions.append(f"{temp} Celsius -> {result} Fahrenheit")
        elif choice == 2:
            result = fahrenheit_to_celsius(temp)
            print(f"{temp} Fahrenheit é igual a {result} Celsius")
            conversions.append(f"{temp} Fahrenheit -> {result} Celsius")
        elif choice == 3:
            result = celsius_to_kelvin(temp)
            print(f"{temp} Celsius é igual a {result} Kelvin")
            conversions.append(f"{temp} Celsius -> {result} Kelvin")
        elif choice == 4:
            result = kelvin_to_celsius(temp)
            print(f"{temp} Kelvin é igual a {result} Celsius")
            conversions.append(f"{temp} Kelvin -> {result} Celsius")
        elif choice == 5:
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp} Fahrenheit é igual a {result} Kelvin")
            conversions.append(f"{temp} Fahrenheit -> {result} Kelvin")
        elif choice == 6:
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp} Kelvin é igual a {result} Fahrenheit")
            conversions.append(f"{temp} Kelvin -> {result} Fahrenheit")
        else:
            print("Opção inválida")
    
    print("\nHistórico de conversões:")
    for conversion in conversions:
        print(conversion)

if __name__ == "__main__":
    main()