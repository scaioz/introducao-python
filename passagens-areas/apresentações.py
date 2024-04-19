def mostra_menu():
    print("==" * 50)
    print("Escolha uma das opções abaixo: \n"
        "Digite 1 para comprar passagens \n"
        "Digite 2 para listar passagens \n"
        "Digite 3 para sair passagens"
    )
    print("==" * 50)
    print()

def menu_compra_passagem():
    print("Você escolheu compra de passagens")
    origem = input("Qual é a origem? ")
    destino = input("Qual é o destino? ")
    preço = float(input("Qual é o preço? "))
    return origem,destino,preço

def lista_passagens(passagens_compradas):
    for indice, passagem in enumerate (passagens_compradas):
        print(f"{indice+1}) {passagem}")