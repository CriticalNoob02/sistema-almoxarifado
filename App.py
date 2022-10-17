#-=-=-=-=-=-=-=-=-=-=-=-=-= Importações;
from function import *
import os
from Ferramentas import coresTerminal

#-=-=-=-=-=-=-=-=-=-=-=-=-= Declarando Variáveis;
sistema = Sistema()
Confirmação1 = True
Confirmação2 = True

#-=-=-=-=-=-=-=-=-=-=-=-=-= Declarando Cores;
Verde,Base = coresTerminal(0,3,0)
Vermelho,Base = coresTerminal(0,2,0)
Amarelo,Base = coresTerminal(0,4,0)
 
## Iniciando Programa login ou Cadastro;
os.system("cls")
while Confirmação1: 
    try:
        Cadastro = int(input("Deseja efetuar o login ou realizar um Cadastro? (1- Cadastro / 2-Login ) "))
        match Cadastro:
            case 1:
                sistema.cadastroDeFuncionarios()
                Confirmação1 = False
            case 2:
                sistema.login()
                Confirmação1 = False
            case _:
                print(f"{Vermelho}O valor digitado está incorreto!{Base}")
    except:
        print(f"{Vermelho}O valor digitado está incorreto!{Base}")

while Confirmação2:
## Menu de Funções;
    print("\n","-="*30,)
    print("Bem Vindo ao Menu!")
    print(f"\n{Amarelo}1- Cadastro de Itens;")
    print("2- Entrada de Produtos;")
    print("3- Exibir Fila de Espera Traigem;")
    print("4- Teste de Qualidade;")
    print("5- Exibir Fila de Espera Estoque;")
    print("6- Exibir Mapa do Estoque;")
    print("7- Endereçar Produto;")
    print("8- Transferencia de Produtos;")
    print(f"9- Gerar Mapa;{Base}")
    print("")
    try:
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
            print(f"{Vermelho}O valor digitado está incorreto!{Base}")
    except:
        print(f"{Vermelho}O valor digitado está incorreto!{Base}")