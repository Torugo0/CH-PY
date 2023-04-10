print(" BEM-VINDO !!! ")

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
                    print("1- Sim // 2- Não")

                    comprar = int(input("Comprar: "))
                    
                    if comprar == 1:
                        print("Escanei o QR CODE para pagamento via PIX")
                        print("Obrigado por comprar conosco !!")
                    else:
                        print("Operação cancelada")
                
                elif opcao_produto == 2:
                    print("Carcaça Notebook Lenovo")
                    print("Valor: R$: 300,00")
                    print("1- Sim // 2- Não")

                    comprar = int(input("Comprar: "))
                    
                    if comprar == 1:
                        print("Escanei o QR CODE para pagamento via PIX")
                        print("Obrigado por comprar conosco !!")
                    else:
                            print("Operação cancelada")
                
                elif opcao_produto == 3:
                    print("Monitor 20' sem imagem")
                    print("Valor: R$: 100,00")
                    print("1- Sim // 2- Não")

                    comprar = int(input("Comprar: "))
                    
                    if comprar == 1:
                        print("Escanei o QR CODE para pagamento via PIX")
                        print("Obrigado por comprar conosco !!")
                    else:
                            print("Operação cancelada")
                
                elif opcao_produto == 4:
                    print("Samsung Note 20 placa queimada")
                    print("Valor: R$: 500,00")
                    print("1- Sim // 2- Não")

                    comprar = int(input("Comprar: "))
                    
                    if comprar == 1:
                        print("Escanei o QR CODE para pagamento via PIX")
                        print("Obrigado por comprar conosco !!")
                    else:
                            print("Operação cancelada")
                
                elif opcao_produto == 5:
                    print("Luminária queimada")
                    print("Valor: R$: 20,00")
                    print("1- Sim // 2- Não")

                    comprar = int(input("Comprar: "))
                    
                    if comprar == 1:
                        print("Escanei o QR CODE para pagamento via PIX")
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
                     print("")
                ##FAZER OS IF'S E ELIF'S PARA CADA PRODUTO