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
    print("Calculadora de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Fahrenheit para Kelvin")
    print("6. Kelvin para Fahrenheit")
    
    choice = int(input("Escolha uma opção: "))
    temp = float(input("Digite a temperatura: "))
    
    if choice == 1:
        print(f"{temp} Celsius é igual a {celsius_to_fahrenheit(temp)} Fahrenheit")
    elif choice == 2:
        print(f"{temp} Fahrenheit é igual a {fahrenheit_to_celsius(temp)} Celsius")
    elif choice == 3:
        print(f"{temp} Celsius é igual a {celsius_to_kelvin(temp)} Kelvin")
    elif choice == 4:
        print(f"{temp} Kelvin é igual a {kelvin_to_celsius(temp)} Celsius")
    elif choice == 5:
        print(f"{temp} Fahrenheit é igual a {fahrenheit_to_kelvin(temp)} Kelvin")
    elif choice == 6:
        print(f"{temp} Kelvin é igual a {kelvin_to_fahrenheit(temp)} Fahrenheit")
    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()