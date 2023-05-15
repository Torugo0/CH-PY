#Exceções personalizadas
class TelefoneError(Exception):
     pass
class CpfError(Exception):
     pass
class VerificaError(Exception):
     pass

#PRODUTOS 
def menuproduto():
    while True:
        try:
            print("Produtos")
            print("1 - Iphone 6s com bateria inchada - R$: 800,00")
            print("2 - Carcaça Notebook Lenovo - R$: 300,00")
            print("3 - Monitor 20' sem imagem - R$: 100,00")
            print("4 - Samsung Note 20 placa queimada - R$: 500,00")
            print("5 - Luminária queimada - R$: 20,00")
            print("6 - Voltar \n")
            
            opcao_produto = int(input("Escolha um produto/opção: "))
            if opcao_produto <= 0 or opcao_produto > 6:
                    raise VerificaError
            return opcao_produto
        except ValueError:
            print("O valor informado não é um número \n")
        except VerificaError:
            print("Digite apenas as opções exibidas em tela \n")

# Sem o while sai do comprar mas caso de algum erro ele vai ao incio, pedindo para fazer a escolha do produto novamente
# Com o while, entra em loop o comprar e não volta ao inicio

def produto1():
    roda = True
    while roda:
        try:
            print("Iphone 6s com bateria inchada")
            print("Valor: R$: 800,00")
            print("Deseja comprar o produto? \n(1- SIM // 2- NÃO) \n")

            comprar = int(input("Comprar: "))
            if comprar <= 0 or comprar > 2:
                raise VerificaError
            
            if comprar == 1:
                print("Escaneie o QR CODE para o pagamento via PIX")
                print("Obrigado por comprar conosco !! \n")
                roda = False
            else:
                print("Operação cancelada \n")
                roda = False
        except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")
        except ValueError:
            print("O valor informado não é um número \n")
            

def produto2(opcao_produto):
  
    if opcao_produto == 2:
        print("Carcaça Notebook Lenovo")
        print("Valor: R$: 300,00")
        print("Deseja comprar o produto? (1- Sim // 2- Não)")

        comprar = int(input("Comprar: "))
        if comprar <= 0 or comprar > 2:
            raise VerificaError
        
        if comprar == 1:
            print("Escaneie o QR CODE para o pagamento via PIX")
            print("Obrigado por comprar conosco !! \n")
        else:
            print("Operação cancelada \n")

def produto3(opcao_produto):
    while True:
        try:
            if opcao_produto == 3:
                print("Monitor 20' sem imagem")
                print("Valor: R$: 100,00")
                print("Deseja comprar o produto? (1- Sim // 2- Não)")

                comprar = int(input("Comprar: "))
                if comprar <= 0 or comprar > 2:
                    raise VerificaError
                
                if comprar == 1:
                    print("Escaneie o QR CODE para o pagamento via PIX")
                    print("TRANSAÇÃO ACEITA, VOCÊ ACABOU DE COMPRAR UM MONITOR DE 20'")
                    print("Obrigado por comprar conosco !! \n")
                else:
                    print("Operação cancelada \n")
        except VerificaError:
            print("Digite apenas as opções exibidas em tela \n")
        except ValueError:
            print("O valor informado não é um número \n")
    
def produto4(opcao_produto):
    while True:
        try:
            if opcao_produto == 4:
                print("Samsung Note 20 placa queimada")
                print("Valor: R$: 500,00")
                print("Deseja comprar o produto? (1- Sim // 2- Não)")

                comprar = int(input("Comprar: "))
                if comprar <= 0 or comprar > 2:
                    raise VerificaError
                
                if comprar == 1:
                    print("Escaneie o QR CODE para o pagamento via PIX")
                    print("Obrigado por comprar conosco !!\n")
                else:
                    print("Operação cancelada\n")
        except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")
        except ValueError:
            print("O valor informado não é um número \n")

def produto5(opcao_produto):
    while True:
        try:
            if opcao_produto == 5:
                print("Luminária queimada")
                print("Valor: R$: 20,00")
                print("Deseja comprar o produto? (1- Sim // 2- Não)")

                comprar = int(input("Comprar: "))
                if comprar <= 0 or comprar > 2:
                            raise VerificaError
                
                if comprar == 1:
                    print("Escaneie o QR CODE para o pagamento via PIX")
                    print("Obrigado por comprar conosco !!\n")
                else:
                    print("Operação cancelada\n")
        except VerificaError:
                    print("Digite apenas as opções exibidas em tela \n")
        except ValueError:
            print("O valor informado não é um número \n")

def comprarproduto(opcao_produto):
    match opcao_produto:
        case 1:
            produto1()
        case 2:
            produto2(opcao_produto)
        case 3:
            produto3(opcao_produto)
        case 4:
            produto4(opcao_produto)
        case 5:
            produto5(opcao_produto)
    
'''
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
'''

def produtos():
    opcao_produto = menuproduto()
    print("\n")

    comprarproduto(opcao_produto)

#DESCARTE 

# Sem o while true ele para
# Com o while true ele entra em loop
def menudescarte():
    
        try:
            print("Qual o tipo de produto que deseja descartar ? \n")
            print("1- Celulares")
            print("2- Notebooks")
            print("3- Televisores (Máximo de 20' polegadas)")
            print("4- Perifericos")
            print("5- Pilhas")
            print("6- Voltar \n")

            opcao_descarte = int(input("Digite a opção desejada: "))
            if opcao_descarte <= 0 or opcao_descarte > 6:
                 raise VerificaError
            return opcao_descarte 
        except VerificaError:
            print("Digite apenas as opções exibidas em tela \n")
        except ValueError:
            print("O valor informado não é um número \n")
    

def descarte():
    opcao_descarte = menudescarte()
    print("\n")

    while opcao_descarte != 6:
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

#Contato & CPF
def cpf(nome):
    cpf = int(input(f"Olá {nome}, digite seu CPF: "))
    digitos= len(str(cpf))
    if digitos < 11 or digitos > 11:
        raise CpfError

def numero():
    telefone = int(input("Número para contato: "))
    digitost = len(str(telefone))
    if digitost < 11 or digitost > 11:
            raise TelefoneError
    print("\n")

# Menus
def menume():
    while True:
        try:
            print("BEM-VINDO AO PONTO DE DESCARTE INTELIGENTE, ELEKSELL AGRADECE A SUA PRESENÇA !!! \n")

            print("Informe seus dados")
            nome = input("Digite seu nome: ")
            cpf(nome)
            numero()

            opcao = 0
            return opcao
        except ValueError:
            print("O valor informado não é um número \n")
        except CpfError:
             print("O cpf informado não é valido. \nExemplo: 12345678910 \n")
        except TelefoneError:
             print("O telefone informado não é válida. \nExemplo: 11912345678 \n")          

def menu():
    opcao = menume()
    
    while opcao != 3:
        while True:
            try:
                print("1 - Ver Produtos")
                print("2 - Depositar Produto(s)")
                print("3 - Finalizar sessão \n")

                opcao = int(input("Escolha a opção desejada: "))
                if opcao <= 0 or opcao > 3:
                    raise VerificaError
                print("\n")

                match opcao:
                        case 1: 
                            produtos()
                        case 2:
                            descarte()
                        case 3:
                            print("ElekSell agradece a sua vinda, muito obrigado !")
                            break
            except ValueError:
                print("O valor informado não é um número \n")
            except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")

menu()


