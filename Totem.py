# Menus
def menuproduto():

    print("Produtos")
    print("1 - Iphone 6s com bateria inchada - R$: 800,00")
    print("2 - Carcaça Notebook Lenovo - R$: 300,00")
    print("3 - Monitor 20' sem imagem - R$: 100,00")
    print("4 - Samsung Note 20 placa queimada - R$: 500,00")
    print("5 - Luminária queimada - R$: 20,00")
    print("6 - Sair \n")
    
    opcao_produto = int(input("Escolha um produto/opção: "))
    return opcao_produto

def menudescarte():
    print("Qual o tipo de produto que deseja descartar ? \n")
    print("1- Celulares")
    print("2- Notebooks")
    print("3- Televisores (Máximo de 20' polegadas)")
    print("4- Perifericos")
    print("5- Pilhas \n")

    opcao_descarte = int(input("Digite a opção desejada: "))
    return opcao_descarte

def menume():
    print("BEM-VINDO AO PONTO DE DESCARTE INTELIGENTE, ELEKSELL AGRADECE A SUA PRESENÇA !!! \n")

    print("Informe seus dados")
    nome = input("Digite seu nome: ")
    cpf = int(input(f"Olá {nome}, digite seu CPF: "))
    telefone = int(input("Número para contato: "))
    print("\n")

    opcao = 0
    return opcao

def comprarproduto(opcao_produto):
    if opcao_produto == 1:
        print("Iphone 6s com bateria inchada")
        print("Valor: R$: 800,00")
        print("Deseja comprar o produto? (1- Sim // 2- Não) \n")

        comprar = int(input("Comprar: "))
        
        if comprar == 1:
            print("Escaneie o QR CODE para o pagamento via PIX")
            print("Obrigado por comprar conosco !! \n")
        else:
            print("Operação cancelada \n")
    
    elif opcao_produto == 2:
        print("Carcaça Notebook Lenovo")
        print("Valor: R$: 300,00")
        print("Deseja comprar o produto? (1- Sim // 2- Não)")

        comprar = int(input("Comprar: "))
        
        if comprar == 1:
            print("Escaneie o QR CODE para o pagamento via PIX")
            print("Obrigado por comprar conosco !! \n")
        else:
            print("Operação cancelada \n")
    
    elif opcao_produto == 3:
        print("Monitor 20' sem imagem")
        print("Valor: R$: 100,00")
        print("Deseja comprar o produto? (1- Sim // 2- Não)")

        comprar = int(input("Comprar: "))
        
        if comprar == 1:
            print("Escaneie o QR CODE para o pagamento via PIX")
            print("Obrigado por comprar conosco !! \n")
        else:
            print("Operação cancelada \n")
    
    elif opcao_produto == 4:
        print("Samsung Note 20 placa queimada")
        print("Valor: R$: 500,00")
        print("Deseja comprar o produto? (1- Sim // 2- Não)")

        comprar = int(input("Comprar: "))
        
        if comprar == 1:
            print("Escaneie o QR CODE para o pagamento via PIX")
            print("Obrigado por comprar conosco !!\n")
        else:
            print("Operação cancelada\n")
    
    elif opcao_produto == 5:
        print("Luminária queimada")
        print("Valor: R$: 20,00")
        print("Deseja comprar o produto? (1- Sim // 2- Não)")

        comprar = int(input("Comprar: "))
        
        if comprar == 1:
            print("Escaneie o QR CODE para o pagamento via PIX")
            print("Obrigado por comprar conosco !!\n")
        else:
            print("Operação cancelada\n")
    elif opcao_produto == 6:
        print("Sessão finalizada \n")

def produtos():
    opcao_produto = menuproduto()
    # fazer uma def para cada produto
    print("\n")

    comprarproduto(opcao_produto)

# Ajustar que caso o usuario digite strings (IF compra true (Executa os outros ifs), else print (digite um para o desejo de comprar ou dois para não comprar)
 

def descarte():
    opcao_descarte = menudescarte()
    print("\n")

    if opcao_descarte == 1:
        produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
        produto_modelo = input("Modelo do celular: ")
        defeito = input("Em uma palavra descreva o problema: ")
        valor = float(input("Valor para a venda do residuo: R$: "))
        print("\n")
        
        print("Insira seu pix para receber o pagamento do seu produto quando for vendido \n")
        print("1- CPF")
        print("2- Telefone")
        print("3- E-mail \n")

        pix = int(input("Qual será a chave PIX escolhida: "))
        print("\n")

        if pix == 1:
                cpf = int(input("Digite seu CPF: "))
        elif pix == 2:
                telefone = int(input("Digite seu número telefone: "))
        elif pix == 3:
                email = input("Digite seu E-mail: ")
        print("\n")

        print(f"O celular de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento ! \n") 
        print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
        print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !! \n")
    
    elif opcao_descarte == 2:
        produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
        produto_modelo = input("Modelo do notebook: ")
        defeito = input("Em uma palavra descreva o problema: ")
        valor = float(input("Valor para a venda do residuo: R$: "))
        print("\n")
        
        print("Insira seu pix para receber o pagamento do seu produto quando for vendido \n")
        print("1- CPF")
        print("2- Telefone")
        print("3- E-mail \n")

        pix = int(input("Qual será a chave PIX escolhida: "))
        print("\n")

        if pix == 1:
                cpf = int(input("Digite seu CPF: "))
        elif pix == 2:
                telefone = int(input("Digite seu número telefone: "))
        elif pix == 3:
                email = input("Digite seu E-mail: ")
        print("\n")
        
        print(f"O notebook de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento ! \n")
        print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
        print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !! \n")
    
    elif opcao_descarte == 3:
        produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
        produto_modelo = input("Modelo do televisor: ")
        defeito = input("Em uma palavra descreva o problema: ")
        valor = float(input("Valor para a venda do residuo: R$: "))
        print("\n")

        print("Insira seu pix para receber o pagamento do seu produto quando for vendido \n")
        print("1- CPF")
        print("2- Telefone")
        print("3- E-mail \n")

        pix = int(input("Qual será a chave PIX escolhida: "))
        print("\n")

        if pix == 1:
                cpf = int(input("Digite seu CPF: "))
        elif pix == 2:
                telefone = int(input("Digite seu número telefone: "))
        elif pix == 3:
                email = input("Digite seu E-mail: ")
        print("\n")
        
        print(f"O televisor de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento ! \n")
        print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
        print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !! \n")
    
    elif opcao_descarte == 4:
        produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
        produto_modelo = input("Modelo do periferico: ")
        defeito = input("Em uma palavra descreva o problema: ")
        valor = float(input("Valor para a venda do residuo: R$: "))
        print("\n")

        print("Insira seu pix para receber o pagamento do seu produto quando for vendido \n")
        print("1- CPF")
        print("2- Telefone")
        print("3- E-mail \n")

        pix = int(input("Qual será a chave PIX escolhida: "))
        print("\n")

        if pix == 1:
                cpf = int(input("Digite seu CPF: "))
        elif pix == 2:
                telefone = int(input("Digite seu número telefone: "))
        elif pix == 3:
                email = input("Digite seu E-mail: ")
        print("\n")
        
        print(f"O periferico de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento ! \n")
        print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
        print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !! \n")
# Quando a pessoa fazer o deposito do produto, exibir na opção de VER PRODUTOS. 

def menu():
    opcao = menume()
    
    while opcao != 3:
        print("1 - Ver Produtos")
        print("2 - Depositar Produto(s)")
        print("3 - Sair \n")

        opcao = int(input("Escolha a opção desejada: "))
        print("\n")

        match opcao:
                case 1: 
                    produtos()
                
                case 2:
                    descarte()
                case 3:
                    print("ElekSell agradece a sua vinda, muito obrigado !")
# Fazer uma função para que o usuario decida se quer continuar no programa ou encerra-lo, se possivel quando o usuario fazer a compra do produto ou digitar que não quer efetuar a compra 

menu()

# Armazenamento de dados em variáveis, estruturas condicionais e de repetição, definição de funções (Ver se é necessário a passagem de parâmetros e retorno)

# Armazenar inputs do usuário e guardá-los em variáveis e saber realizar buscas e comparações entre elementos

# Listar o resumo da operação realizada, permitindo ao usuário realizar uma nova operação ou encerrar o programa (Ver se o resumo feito na hora de descarte do produto conta)