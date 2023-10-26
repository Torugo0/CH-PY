# Totem Eletrônico 
Este projeto é um protótipo de um "Totem Eletrônico", desenvolvido pelos alunos do curso de Engenharia de Software da FIAP.

</br>

## Equipe
- Felipe Arnus – RM: 550923
- João Pedro Vieira – RM: 99805
- João Pedro Chambrone – RM: 97857
- Vitor Hugo – RM: 97758

</br>

## Sobre o Projeto
O projeto foi desenvolvido no Visual Studio Code e tem o objetivo de permitir que os usuários possam visualizar os resíduos eletrônicos disponíveis em um determinado local para a compra, além de poderem inserir os dados necessários para o descarte e venda dos resíduos.

</br>

## Funcionalidades
Ao iniciar o programa, o usuário é solicitado a digitar seu nome, CPF e número de telefone para possíveis futuros contatos. Em seguida, é exibido um menu com três opções:
- Ver produtos: exibe uma lista de produtos disponíveis para compra, com seus respectivos defeitos e preços. O usuário pode escolher um produto a partir da numeração exibida e, em seguida, decidir se deseja efetuar a compra ou não.
- Depositar produtos: exibe um menu com opções para descarte de diferentes resíduos eletrônicos, como celulares, notebooks, televisores (máximo de 20 polegadas), periféricos e pilhas. Se o usuário escolher a opção "Celulares", "Notebooks", "Televisores" ou "Periféricos", será solicitado que ele digite informações sobre o produto, como marca, modelo, defeito e, caso o produto seja comprado futuramente, a sua chave PIX (CPF, Telefone ou E-mail). Em seguida, o programa exibe uma mensagem informando que o produto está disponível para compra e que, se não for vendido em 30 dias, será levado para a área de tratamento adequado.
- Sair: encerra o programa.

O programa continuará em um loop até que o usuário escolha a opção "Sair".

## ATUALIZÇÕES DO TOTEM DA SEGUNDA SPRINT - 21/05/2023
Nesta sprint foram feitas poucas modificações ao usuário, e mais focada a quem for trabalhar futuramente neste programa, as modificações foram as seguintes:
### Usuário
- Mensagem dizendo ao usuário que após ele ter escaniado o QR CODE que sua transação foi aceita e informando a ele o resíduo que foi adquirido.
- Na parte do descarte foi mantido o resumo do produto que está sendo descartado e o informe da disponibilidade do produto no ponto.
- Mensagens de aviso caso digite alguma informação invalida em algum campo de input.
### Desenvolvedor 
- Código dividido em funções, facilitando a visualização e o entendimento dele.
- Foi acrescentado também o tratamento de erros, para que o programa não pare caso o usuário digite alguma informação invalida em aglum input. 


## ATUALIZÇÕES DO TOTEM DA TERCEIRA SPRINT - 17/09/2023
Sprint focada para a melhora do programa, nenhuma alteração para o usuário.

### Desenvolvedor
- Adicionado Docstrings as funções para melhor entendimento do que se trata.
- Implementação de dicionários contendo os produtos.
- Atualização dos dicionários toda vez que o usuário adiciona o produto.

## ATUALIZÇÕES DO TOTEM DA QUARTA SPRINT - 12/11/2023
Nesta sprint a principal implementação foi um sistema de cadastro/login 

### Usuário
- Agora o usuário pode criar uma conta 
- Após o usuário escolher comprar um produto é gerado o QRcode
- Lista de produtos totalmente atualizada durante a rodagem do programa

### Desenvolvedor
- Implementação de armazenamento de dados e produtos em JSON