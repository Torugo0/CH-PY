print(" BEM-VINDO AO PONTO DE DESCARTE INTELIGENTE, ELEKSELL AGRADECE A SUA PRESENÇA !!! ")

nome = input("Digite seu nome: ")
cpf = int(input(f"Olá {nome}, digite seu CPF: "))
telefone = int(input("Número para contato: "))

opcao = 0

while opcao != 3:

    print("1 - Ver Produtos")
    print("2 - Depositar Produto(s)")
    print("3 - Sair")

    opcao = int(input("Escolha a opção desejada: "))

        
    match opcao:
        case 1:
            print("Produtos")
            print("1 - Iphone 6s com bateria inchada - R$: 800,00")
            print("2 - Carcaça Notebook Lenovo - R$: 300,00")
            print("3 - Monitor 20' sem imagem - R$: 100,00")
            print("4 - Samsung Note 20 placa queimada - R$: 500,00")
            print("5 - Luminária queimada - R$: 20,00")
            print("6 - Sair")
            
            opcao_produto = int(input("Escolha um produto/opção: "))
            if opcao_produto == 1:
                print("Iphone 6s com bateria inchada")
                print("Valor: R$: 800,00")
                print("Deseja comprar o produto? (1- Sim // 2- Não)")

                comprar = int(input("Comprar: "))
                
                if comprar == 1:
                    print("Escaneie o QR CODE para o pagamento via PIX")
                    print("Obrigado por comprar conosco !!")
                else:
                    print("Operação cancelada")
            
            elif opcao_produto == 2:
                print("Carcaça Notebook Lenovo")
                print("Valor: R$: 300,00")
                print("Deseja comprar o produto? (1- Sim // 2- Não)")

                comprar = int(input("Comprar: "))
                
                if comprar == 1:
                    print("Escaneie o QR CODE para o pagamento via PIX")
                    print("Obrigado por comprar conosco !!")
                else:
                        print("Operação cancelada")
            
            elif opcao_produto == 3:
                print("Monitor 20' sem imagem")
                print("Valor: R$: 100,00")
                print("Deseja comprar o produto? (1- Sim // 2- Não)")

                comprar = int(input("Comprar: "))
                
                if comprar == 1:
                    print("Escaneie o QR CODE para o pagamento via PIX")
                    print("Obrigado por comprar conosco !!")
                else:
                        print("Operação cancelada")
            
            elif opcao_produto == 4:
                print("Samsung Note 20 placa queimada")
                print("Valor: R$: 500,00")
                print("Deseja comprar o produto? (1- Sim // 2- Não)")

                comprar = int(input("Comprar: "))
                
                if comprar == 1:
                    print("Escaneie o QR CODE para o pagamento via PIX")
                    print("Obrigado por comprar conosco !!")
                else:
                        print("Operação cancelada")
            
            elif opcao_produto == 5:
                print("Luminária queimada")
                print("Valor: R$: 20,00")
                print("Deseja comprar o produto? (1- Sim // 2- Não)")

                comprar = int(input("Comprar: "))
                
                if comprar == 1:
                    print("Escaneie o QR CODE para o pagamento via PIX")
                    print("Obrigado por comprar conosco !!")
                else:
                        print("Operação cancelada")
            elif opcao_produto == 6:
                print("Sessão finalizada")
        
        case 2:
            print("Qual o tipo de produto que deseja descartar ?")
            print("1- Celulares")
            print("2- Notebooks")
            print("3- Televisores (Máximo de 20' polegadas)")
            print("4- Perifericos")
            print("5- Pilhas")

            opcao_descarte = int(input("Digite a opção desejada: "))
            if opcao_descarte == 1:
                produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
                produto_modelo = input("Modelo do celular: ")
                defeito = input("Em uma palavra descreva o problema: ")
                valor = float(input("Valor para a venda do residuo: R$: "))
                print("Insira seu pix para o pagamento caso o produto seja comprado")
                print("1- CPF")
                print("2- Telefone")
                print("3- E-mail")
                pix = int(input("Qual será a chave PIX escolhida: "))
                if pix == 1:
                     cpf = int(input("Digite seu CPF: "))
                elif pix == 2:
                     telefone = int(input("Digite seu número telefone: "))
                elif pix == 3:
                     email = input("Digite seu E-mail: ")
                print(f"O celular de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento !")
                print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
                print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !!")
            
            elif opcao_descarte == 2:
                produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
                produto_modelo = input("Modelo do notebook: ")
                defeito = input("Em uma palavra descreva o problema: ")
                valor = float(input("Valor para a venda do residuo: R$: "))
                print("Insira seu pix para o pagamento caso o produto seja comprado")
                print("1- CPF")
                print("2- Telefone")
                print("3- E-mail")
                pix = int(input("Qual será a chave PIX escolhida: "))
                if pix == 1:
                     cpf = int(input("Digite seu CPF: "))
                elif pix == 2:
                     telefone = int(input("Digite seu número telefone: "))
                elif pix == 3:
                     email = input("Digite seu E-mail: ")
                print(f"O notebook de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento !")
                print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
                print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !!")
            
            elif opcao_descarte == 3:
                produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
                produto_modelo = input("Modelo do televisor: ")
                defeito = input("Em uma palavra descreva o problema: ")
                valor = float(input("Valor para a venda do residuo: R$: "))
                print("Insira seu pix para o pagamento caso o produto seja comprado")
                print("1- CPF")
                print("2- Telefone")
                print("3- E-mail")
                pix = int(input("Qual será a chave PIX escolhida: "))
                if pix == 1:
                     cpf = int(input("Digite seu CPF: "))
                elif pix == 2:
                     telefone = int(input("Digite seu número telefone: "))
                elif pix == 3:
                     email = input("Digite seu E-mail: ")
                print(f"O televisor de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento !")
                print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
                print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !!")
            
            elif opcao_descarte == 4:
                produto_marca = input("Marca (EX: Apple, Samsung, Xiaomi, etc.): ")
                produto_modelo = input("Modelo do periferico: ")
                defeito = input("Em uma palavra descreva o problema: ")
                valor = float(input("Valor para a venda do residuo: R$: "))
                print("Insira seu pix para o pagamento caso o produto seja comprado")
                print("1- CPF")
                print("2- Telefone")
                print("3- E-mail")
                pix = int(input("Qual será a chave PIX escolhida: "))
                if pix == 1:
                     cpf = int(input("Digite seu CPF: "))
                elif pix == 2:
                     telefone = int(input("Digite seu número telefone: "))
                elif pix == 3:
                     email = input("Digite seu E-mail: ")
                print(f"O periferico de marca: {produto_marca}, modelo: {produto_modelo} e com o defeito: {defeito} está disponivel para compra neste momento !")
                print("AVISO: RESIDUOS QUE PERMANECEREM POR MAIS DE 30 DIAS SERÃO LEVADOS PARA A ÁREA DE TRATAMENTO ADEQUADO")
                print("Muito obrigado por contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !!")
            
            elif opcao_descarte == 5:
                print("Muito obrigado por depositar suas pilhas e contribuir com o meio ambiente, a Mãe natrueza e a ElekSell agradece !!")