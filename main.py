def min_coins(money):
    coins = [10, 5, 1]  # Denominaciones disponibles
    numcoins = [0, 0, 0]  # Inicializamos el conteo de monedas de 10, 5 y 1

    # Iteramos sobre las denominaciones disponibles
    for i, coin in enumerate(coins):
        numcoins[i] = money // coin
        money %= coin
        
    return numcoins

# Función para mostrar el resultado
def display_coins(numcoins):
    denominations = [10, 5, 1]
    results = []

    for i, coin_count in enumerate(numcoins):
        if coin_count > 0:
            results.append(f"{coin_count} moneda(s) de {denominations[i]}")

    return " + ".join(results)

# Función principal para interactuar con el usuario
def main():
    # Solicitar al usuario que ingrese la cantidad de dinero
    while True:
        try:
            money = int(input("Ingrese la cantidad de dinero (entero mayor o igual a 1): "))
            if money < 1:
                print("Por favor, ingrese un número entero mayor o igual a 1.")
            else:
                break
        except ValueError:
            print("Numero invalido Por favor, ingrese un número entero mayor o igual a 1 ")

    # Calcular la cantidad mínima de monedas necesarias
    num_coins = min_coins(money)

    # Mostrar el resultado
    print(f"Para {money} dolares, se necesitan las siguientes monedas: ")
    print(display_coins(num_coins))

# Ejecutar el programa principal
if __name__ == "__main__":
    main()