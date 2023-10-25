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

#PRODUTOS 

def exibe_produto():
    '''Função que exibe os produtos existentes no arquivo JSON'''
    with open('./Produtos_JSON/produtos.json', 'r', encoding='utf-8') as arquivo:
        produtos = json.load(arquivo)

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
    with open('./Produtos_JSON/produtos.json', 'r', encoding='utf-8') as arquivo:
        produtos = json.load(arquivo)

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
                    # fazer função de exclusão do produto
                    comprar = int(input("Comprar: "))
                    if comprar <= 0 or comprar > 2:
                            raise VerificaError

                    if comprar == 1:
                        with open('./Produtos_JSON/produtos.json', 'r', encoding='utf-8') as arquivo:
                            produtos = json.load(arquivo)
                        del produtos[str(produto_escolhido)]

                        # Atualize as chaves do dicionário para preencher lacunas
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

    if not os.path.exists('./Produtos_JSON'):
        os.makedirs('./Produtos_JSON')

    try:
        with open('./Produtos_JSON/produtos.json', 'r', encoding='utf-8') as arquivo:
            produtos = json.load(arquivo)
    except FileNotFoundError:
        produtos = {}
    
    produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
    produto_modelo = input("Modelo do produto: ")
    defeito = input("Em uma palavra descreva o problema: ")
    valor = float(input("Valor para a venda do residuo: R$: "))
    juntar_string = f"{produto_modelo} {defeito} - R$: {valor:.2f}"
    id = len(produtos)+1
    print("\n")

    pagamento()
    aviso(produto_marca, produto_modelo, defeito, valor)
    new = produtos[id] = juntar_string

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
def formatar_cpf(cpf):
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado

def cpf(nome):
    """
    Solicita e verifica o CPF do usuário.
    """

    cpf = input(f"Olá {nome}, digite seu CPF: ")
    digitos= len(cpf)
    if digitos < 11 or digitos > 11:
        raise CpfError

def numero():
    """
    Solicita e verifica um número de telefone.
    """

    telefone = int(input("Número para contato: "))
    digitost = len(str(telefone))
    if digitost < 11 or digitost > 11:
            raise TelefoneError
    print("\n")

# Menus
def menume():
    """
    Exibe um menu para que o usuário forneça informações pessoais.
    """

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
    """
    Função principal que controla o menu principal e as ações do usuário.

    """
    
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