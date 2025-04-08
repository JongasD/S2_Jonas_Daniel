print("Quitanda da Esquina")
print("""
        Em nossa quitanda temos:
        - Tomates
        - Alface
        - Batata
        - Cebola
        - Laranja
        - Melancia
        - 
        - Kiwi
      Para acessar um produto, digite a letra inicial do produto.
""")
def acessar_produto(): #Função para acessar o produto 
    print("Alface 1,00 cada unidade")
    produto = input("Digite a letra inicial do produto: ") #Pode ser maiuscula ou minuscula
    if produto == "T" or produto == "t":
        print("Tomates: 1,50 cada unidade")
    elif produto == "A" or produto == "a":
        print("Alface 1,00 cada unidade")
    elif produto == "B" or produto == "b":
        print("Batata 1,20 cada unidade")
    elif produto == "C" or produto == "c":
        print("Cebola  cada unidade")
    elif produto == "L" or produto == "l":
        print("Laranja 2,00 cada unidade")
    elif produto == "M" or produto == "m":
        print("Melancia 25,00 cada unidade")
    elif produto == "F" or produto == "f":
        print("Feijao 4,00 cada unidade")
    elif produto == "K" or produto == "":
        print("Kiwi 5,00 cada unidade")
    else:
        print("Produto não encontrado")

acessar_produto()
print("Muito obrigado pela visita em nossa ")