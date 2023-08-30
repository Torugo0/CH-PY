#Exceções personalizadas
class TelefoneError(Exception):
     pass
class CpfError(Exception):
     pass
class VerificaError(Exception):
     pass

#PRODUTOS 
def produtos1():
    produtos = {
        1 : "Iphone 6s com bateria inchada - R$: 800,00",
        2 : "Carcaça Notebook Lenovo - R$: 300,00",
        3 : "Monitor 20' sem imagem - R$: 100,00",
        4 : "Samsung Note 20 placa queimada - R$: 500,00",
        5 : "Luminária queimada - R$: 20,00",
    }
    return produtos

def menuproduto():
    while True:
        try:
            print("Produtos")
            for opcao,produto in produtos1().items():
                print(f"{opcao}- {produto}")
            
            print("\n")
            opcao_produto = int(input(f"Escolha um produto/opção ({len(produtos1())+1} - voltar): "))
            if opcao_produto <= 0 or opcao_produto > (len(produtos1())+1):
                    raise VerificaError
            return opcao_produto
        except ValueError:
            print("O valor informado não é um número \n")
        except VerificaError:
            print("Digite apenas as opções exibidas em tela \n")

def escolha_produto():
    produtos_dict = produtos1()
    produto_escolhido = menuproduto()
    roda = True
    while roda:
        try:
            if produto_escolhido == (len(produtos_dict)+1):
                print("\n")
                roda = False
            else:
                if produto_escolhido in produtos_dict:
                    nome_produto = produtos_dict[produto_escolhido].split(" - ")[0].upper()
                
                    print(f'''{produtos_dict[produto_escolhido]}
- Deseja comprar o produto?
(1- SIM // 2- NÃO)
''')
                    comprar = int(input("Comprar: "))
                    if comprar <= 0 or comprar > 2:
                            raise VerificaError

                    if comprar == 1:
                            print("Escaneie o QR CODE para o pagamento via PIX")
                            print(f"TRANSAÇÃO ACEITA, VOCÊ ACABOU DE COMPRAR UM(a) {nome_produto}")
                            print("Obrigado por comprar conosco !! \n")
                            roda = False
                    else:
                            print("Operação cancelada \n")
                            roda = False
        except VerificaError:
            print("Digite apenas as opções exibidas em tela \n")
        except ValueError:
            print("O valor informado não é um número \n")

#DESCARTE 


def menudescarte():
    roda = True
    while roda:
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
    

def add_produto():
    try:
        produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
        produto_modelo = input("Modelo do produto: ")
        defeito = input("Em uma palavra descreva o problema: ")
        valor = float(input("Valor para a venda do residuo: R$: "))
        juntar_string = f"{produto_modelo} {defeito} - R$: {valor:.2f}"
        print("\n")
        
        pagamento()
        aviso(produto_marca, produto_modelo, defeito, valor)
        new = produtos1()[len(produtos1())] = juntar_string
        return new # Atualizar a lista que não esta indo, e tratamento de erro da um stop, precisa de um while True
    except ValueError:
        print("O valor informado não é um número \n")
    

def pagamento():
    roda = True
    while roda:
        try:
            nome = input("Digite o nome de quem vai receber: ")
            print("Insira seu pix para receber o pagamento do seu produto quando for vendido \n")
            print("1- CPF")
            print("2- Telefone")
            print("3- E-mail \n")

            pix = int(input("Qual será a chave PIX escolhida: "))
            if pix <= 0 or pix > 3:
                raise VerificaError
            print("\n")
            
            match pix:
                case 1:
                    cpf(nome)
                    roda = False
                case 2:
                    numero()
                    roda = False
                case 3:
                    email = input("Digite seu E-mail: ")
                    roda = False
            print("\n")
        except VerificaError:
            print("Digite apenas as opções exibidas em tela \n")
        except ValueError:
            print("O valor informado não é um número \n")
        except TelefoneError:
            print("O telefone informado não é válida. \nExemplo: 11912345678 \n")
        except CpfError:
            print("O cpf informado não é valido. \nExemplo: 12345678910 \n")

def aviso(produto_marca, produto_modelo, defeito, valor):
    print(f"O produto de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento por R$: {valor}! \n") 
    print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
    print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !! \n")

def descarte():
    roda = True
    while roda:
        opcao_descarte = menudescarte()
        print("\n")
        if opcao_descarte == 6:
            print("\n")
            roda = False
        elif opcao_descarte == 5:
            print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !! \n")
            roda = False
        else:
            add_produto() # Atualizar a lista que não esta indo
            roda = False

#Contato & CPF
def formatar_cpf(cpf):
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado


def cpf(nome):
    cpf = input(f"Olá {nome}, digite seu CPF: ")
    digitos= len(cpf)
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
                            escolha_produto()
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