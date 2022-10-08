## Importações;
from function import *

## Declarando Variáveis;
sistema = Sistema()
Confirmação1 = True
Confirmação2 = True
 
## Iniciando Programa login ou Cadastro;
while Confirmação1:
    Cadastro = int(input("Deseja efetuar o login ou realizar um Cadastro? (1- Cadastro / 2-Login )"))
    match Cadastro:
        case 1:
            sistema.cadastroDeFuncionarios()
        case 2:
            sistema.login()
    Confirmação1 = False

## Menu de Funções;
print("\n","-="*30,)
print("Bem Vindo ao Menu")
print("\n1- Cadastro de Itens;")
print("2- Entrada de Produtos;")
print("3- Exibir Fila de Espera Traigem;")
print("4- Teste de Qualidade;")
print("5- Exibir Fila de Espera Estoque;")
print("6- Exibir Mapa do Estoque;")
print("7- Endereçar Produto;")
print("8- Transferencia de Produtos;")
print("9- Gerar Mapa;")
while Confirmação2:
    print("")
    escolha = int(input("Digite o número correspondente ao menu:"))
    if escolha > 0 and escolha < 10:
        Confirmação3 = sistema.menu(sistema,escolha)
        if Confirmação3:
            resp = int(input("Deseja Efetuar outra Operação? (1-S/2-N) "))
            match resp:
                case 1:
                    pass
                case 2:
                    Confirmação2 = False
        else:
            pass
    else:
        print("O valor digitado está incorreto!")