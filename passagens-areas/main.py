from passagens import PassagensAereasManager, Passagem
from apresentações import mostra_menu, menu_compra_passagem, lista_passagens

while True:
    passagens_aereas_manager = PassagensAereasManager()

    mostra_menu()

    # Receber a entrada do usuário
    entrada_do_usuario = int(input())

    if entrada_do_usuario == 1:
        origem, destino, preço = menu_compra_passagem()
        passagem = Passagem(origem, destino, preço)
        passagens_aereas_manager.adicionar_passagem(passagem)
        print()

    elif entrada_do_usuario == 2:
        lista_passagens(passagens_aereas_manager.listar_passagens())
        print()

    # se o usuário escolher sair do programa, usar break para encerrar o programa
    elif entrada_do_usuario == 3:
        print("Encerrando o programa, volte sempre!")
        print()
        break