from math import radians, sin, cos, acos
import sys
from api import geocoding_adress


def main():
    menu()


def menu():
    print("************MAIN MENU**************")

    choice = int(
        input(
            """
            A distância euclidiana representa a menor distância existente
            entre dois objetos no plano multidimensional.

            Para calcular use o menu abaixo e cadastre dois endereços
            e depois use a opção 3 - "Calcular a distância euclidiana".

            O resultado mostrará a distância em quilômetros (Km).

        1 - Cadastrar um endereço
        2 - Ver os endereços cadastrados
        3 - Calcular a distância euclidiana
        0 - Sair

        Escolha: """
        )
    )
    if choice == 1:
        write_address()
    elif choice == 2:
        see_addresses()
    elif choice == 3:
        euclidean_distance()
    elif choice == 0:
        sys.exit
    else:
        print("Selecione uma opção válida.")
        menu()


addresses_list = []


def see_addresses():
    print(addresses_list)
    menu()


def write_address():
    address = input("Escreva um endereço: ")
    confirm = input(f"O endereço cadastrado foi {address}. Confirma (y/n): ")

    if confirm == "y" or "Y":
        addresses_list.append(address)
        print("Ok, endereço cadastrado! ")
        anykey()
    elif confirm == "n" or "N":
        print("Ok, endereço excluído!")
        anykey()
    else:
        anykey()


def anykey():
    print("Pressione qualquer tecla para retornar ao menu principal.")
    input("")
    menu()


def transform_address_in_geocode(addresses_list):
    geocode_list = []
    print(addresses_list)
    for address in addresses_list:
        geocode = geocoding_adress(address)
        geocode = geocode[0]["geometry"]["location"]

        geocode_list.append(geocode)
    return geocode_list


def euclidean_distance():
    coordinates = transform_address_in_geocode(addresses_list)

    x_lat = radians(coordinates[0]["lat"])
    x_lng = radians(coordinates[0]["lng"])
    y_lat = radians(coordinates[1]["lat"])
    y_lng = radians(coordinates[1]["lng"])

    dist = 6371.01 * acos(
        sin(x_lat) * sin(y_lat) + cos(x_lat) * cos(y_lat) * cos(x_lng - y_lng)
    )
    print("A distância entre os dois endereços é de %.2fkm." % dist)


main()
