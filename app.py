import math
import sys


def main():
    menu()


def menu():
    print("************MAIN MENU**************")

    choice = int(
        input(
            """
                O que deseja fazer?
        1 - Cadastrar um endereço
        2 - Ver os endereços cadastrados
        3 - Calcular a distância euclidiana
        4 - Aprender sobre a distância euclidiana
        0 - Sair

        Escolha: """
        )
    )
    if choice == 1:
        write_address()
    elif choice == 2:
        see_addresses()
    elif choice == 3:
        euclidean_distance(x, y)
    elif choice == 4:
        pass
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


x = [-23.5673784, -46.6355207]
y = [-23.5688483, -46.6467684]


def euclidean_distance(x, y):

    a = (x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2
    b = math.sqrt(a)
    print(b)
    return b


main()
