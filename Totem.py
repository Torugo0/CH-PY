# Imports utilizados
import json
import os
from PIL import Image
import qrcode

#Exceções personalizadas
class TelefoneError(Exception):
    pass
class CpfError(Exception):
    pass
class VerificaError(Exception):
    pass
class DataError(Exception):
    pass

# Verificações
 
def verifica_json_dados():
    if not os.path.exists('./Dados_JSON'):
            os.makedirs('./Dados_JSON')

    try:
        with open('./Dados_JSON/dados.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = {}
    
    return dados

def verifica_json_produtos():
    if not os.path.exists('./Produtos_JSON'):
        os.makedirs('./Produtos_JSON')

    try:
        with open('./Produtos_JSON/produtos.json', 'r', encoding='utf-8') as arquivo:
            produtos = json.load(arquivo)
    except FileNotFoundError:
        produtos = {}
    
    return produtos

def validar_cpf(cpf, dados):
    for id, cadastro in dados.items():
        if cadastro["CPF"] == cpf:
            return True
    return False

def validar_login():
    dados = verifica_json_dados()

    cpf, senha = login()

    for id, dados_login in dados.items():
        if dados_login["CPF"] == cpf and dados_login["Senha"] == senha:
            return True
    return False
    

#PRODUTOS

def exibe_produto():
    '''Função que exibe os produtos existentes no arquivo JSON'''
    produtos = verifica_json_produtos()

    while True:
        try:
            if len(produtos) == 0:
                opcao_produto = 0
                print("Nenhum produto disponivel")
                return opcao_produto
            else:
                print("Produtos")
                for opcao,produto in produtos.items():
                    print(f"{int(opcao)}- {produto}")
                
                print("\n")
                opcao_produto = int(input(f"Escolha um produto/opção (0 - voltar): "))
                if opcao_produto < 0 or opcao_produto > len(produtos):
                        raise VerificaError
                return opcao_produto
        except ValueError:
            print("O valor informado não é um número \n")
        except VerificaError:
            print("Digite apenas as opções exibidas em tela \n")

def QrCode():
    '''Gera o QRcode para o "pagamento" '''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data('https://www.fiap.com.br/')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

def escolha_produto():
    """
    Permite ao usuário escolher um produto e realizar a compra.
    """
    
    produtos = verifica_json_produtos()

    produtos_dict = produtos
    produto_escolhido = exibe_produto()
    roda = True
    while roda:
        try:
            if produto_escolhido == 0:
                print("\n")
                roda = False
            else:
                if str(produto_escolhido) in produtos_dict:
                    nome_produto = produtos_dict[str(produto_escolhido)].split(" - ")[0].upper()
                
                    print(f'''{produtos_dict[str(produto_escolhido)]}
- Deseja comprar o produto?
(1- SIM // 2- NÃO)
''')
                    comprar = int(input("Comprar: "))
                    if comprar <= 0 or comprar > 2:
                            raise VerificaError

                    if comprar == 1:
                        with open('./Produtos_JSON/produtos.json', 'r', encoding='utf-8') as arquivo:
                            produtos = json.load(arquivo)
                        del produtos[str(produto_escolhido)]

                        new_produtos = {}
                        i = 1
                        for chave, valor in produtos.items():
                            new_produtos[str(i)] = valor
                            i += 1

                        with open('./Produtos_JSON/produtos.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(new_produtos, arquivo, indent=4, ensure_ascii=False)

                        print("Escaneie o QR CODE para o pagamento via PIX")
                        QrCode()
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
    """
    Exibe o menu de descarte de produtos e solicita a escolha do usuário.

    Returns:
        int: A opção escolhida pelo usuário.
    """

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
    '''Função que armazena o produto descartado pelo usuario em um arquivo json'''

    produtos = verifica_json_produtos()
    
    produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
    produto_modelo = input("Modelo do produto: ")
    defeito = input("Em uma palavra descreva o problema: ")
    valor = float(input("Valor para a venda do residuo: R$: "))
    juntar_string = f"{produto_modelo} {defeito} - R$: {valor:.2f}"
    id = len(produtos)+1
    print("\n")

    pagamento()
    aviso(produto_marca, produto_modelo, defeito, valor)
    produtos[id] = juntar_string

    with open('./Produtos_JSON/produtos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    
def pagamento():
    """
    Permite ao usuário configurar o método de pagamento.
    """

    roda = True
    nome = input("Digite o nome de quem vai receber: ")

    while roda:
        try:
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
                    cpf()
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
    """
    Exibe um aviso com informações sobre o produto disponível para compra.
    """
    print(f"O produto de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento por R$: {valor}! \n") 
    print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
    print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !! \n")

def descarte():
    """
    Permite ao usuário escolher o tipo de produto para descarte.
    """
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
            add_produto() 
            roda = False

#Contato & CPF
def formata_dados(nascimento: str = "" , cpf: str = "" , telefone: str = "" ):
    nascimento_formatado = f"{nascimento[:2]}/{nascimento[2:4]}/{nascimento[4:]}"
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:11]}"
    
    return nascimento_formatado, cpf_formatado, telefone_formatado

def cpf():
    """
    Solicita e verifica o CPF do usuário.
    """

    cpf = formata_dados(cpf = input("Digite seu CPF: "))[1]
    if len(cpf) < 14 or len(cpf) > 14:
        raise CpfError
    return cpf


def numero():
    """
    Solicita e verifica um número de telefone.
    """

    telefone = formata_dados(telefone = input("Digite seu telefone: "))[2]
    if len(telefone) < 15 or len(telefone) > 15:
        raise TelefoneError
    
    return telefone

def nascimento():
    """
    Solicita e verifica a data de nascimento.
    """
    data = formata_dados(nascimento=input("Digite sua data de nascimento: "))[0]
    if len(data) < 10 or len(data) > 10:
        raise DataError
    
    return data
    
# Menus

def cadastro():
    dados = verifica_json_dados()

    while True:
        try: 
            id = (len(dados) + 1)
            print("Informe seus dados")

            nome = input("Digite seu nome completo: ")

            var_cpf = cpf()
            if validar_cpf(var_cpf, dados):
                print("CPF já cadastrado. Não é possível criar um novo cadastro com o mesmo CPF.")
                break
                
            data = nascimento()

            email = input("Digite seu E-mail: ")

            var_telefone = numero()

            senha = input("Criar uma senha: ")

            novo_cadastro = {"Nome" : nome,
                                     "Nascimento": data,
                                     "CPF" : var_cpf,
                                     "Número": var_telefone,
                                     "E-mail": email,
                                     "Senha" : senha }
            
            dados[id] = novo_cadastro

            with open('./Dados_JSON/dados.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                
            print("Cadastro realizado com sucesso! \n")

            opcao = 0
            return opcao
        except ValueError:
            print("O valor informado não é um número \n")
        except CpfError:
             print("O cpf informado não é valido. \nExemplo: 12345678910 \n")
        except TelefoneError:
             print("O telefone informado não é válida. \nExemplo: 11912345678 \n")  
        except DataError:
            print("A data de nascimento não é valida. \nExemplo: 12122005 \n")

def login():
    while True:
        try:    
            cpf = formata_dados(cpf = input("Digite seu CPF: "))[1]
            if len(cpf) < 14 or len(cpf) > 14 :
                raise CpfError
            senha = input("Digite sua senha: ")
            return cpf, senha
        except CpfError:
            print("O cpf informado não é valido. \nExemplo: 12345678910 \n")


def menu():
    """
    Função principal que controla o menu principal e as ações do usuário.

    """

    opcao = 0
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
                            print("Finalizando sessão")
                            break
                
            except ValueError:
                print("O valor informado não é um número \n")
            except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")

def programa():
    print("BEM-VINDO AO PONTO DE DESCARTE INTELIGENTE, ELEKSELL AGRADECE A SUA PRESENÇA !!! \n")
    opcao = 0
    while opcao != 3:
        while True:
            try:
                print("1 - Cadastro")
                print("2 - Login")
                print("3 - Encerrar programa \n")

                opcao = int(input("Escolha a opção desejada: "))
                if opcao <= 0 or opcao > 3:
                    raise VerificaError
                print("\n")

                if opcao == 1:
                    cadastro()
                    break
                elif opcao == 2:
                    if validar_login():
                        print("Login efetuado com sucesso \n")
                        menu()
                        opcao = 3
                        break
                    else:
                        print("Login inválido")
                elif opcao == 3: 
                    print("ElekSell agradece a sua vinda, muito obrigado !")
                    break

            except ValueError:
                print("O valor informado não é um número \n")
            except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")

programa()