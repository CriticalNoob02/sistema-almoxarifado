import random
import datetime

#-=-=-=-=-=-=-=-=-=-=-=-=-= Classe Pai;
class Empresa:
    def __init__(self):
        self.nomeEmpresa = "" 

#-=-=-=-=-=-=-=-=-=-=-=-=-= Classes Filhos;
class Recebimento(Empresa):
    def __init__(self):
        super().__init__()
        self.nF = '' ## Rastreamento Interno
        self.codigo = ''
        self.nomeProduto = ''
        self.quantidade = 0
        self.data_hora = ''

## Fazer a Função do Comprador.... Para Cadastrar o Produto Recebido....

    def entradaDeProduto(self):
        Confirmação = True
        Confirmação2 = True
        while Confirmação:
            ## Entrada dos Dados;
            nome = input("Digite o nome do Produto que deseja Cadastrar: ")
            codigo = input("Digite o Código do Produto: ")
            quantidade = int(input("Digite a quatidade recebida: "))
            ## Geração dos Dados;
            nfL = []
            for i in range(1,7):
                num = random.choice(["0","1","2","3","4","5","6","7","8","9"])
                nfL.append(num)
            nF = "".join(nfL)
            ## Captação da Hora;
            dataAtual = datetime.datetime.now()
            dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M")
            Confirmação2 = True
            while Confirmação2:
                ## Confirmação;
                print("")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"Nº Nota Fiscal: {nF} ")
                print(f"Produto: {nome} ")
                print(f"Codigo do Produto: {codigo} ")
                print(f"Quantidade : {quantidade} ")
                print("")
                resposta = int(input("Confirmar a entrada ?( 1-S / 2-N ) "))
                print("")
                if resposta == 1:
                    ## Salvando Dados;
                    self.nF = nF
                    self.nomeProduto = nome
                    self.codigo = codigo
                    self.quantidade = quantidade
                    self.data_hora = dataFormatada
                    Confirmação = False
                    Confirmação2 = False
                elif resposta == 2:
                    Confirmação2 = False
                else: 
                    print("O valor digitado está incorreto! ")

    def adicionandoBanco(self):
        pass
    
    def transferencia1(self):
        return self.nF

class Triagem(Empresa):

    def __init__(self):
        super().__init__()
        self.filaEspera = []
        self.horaFila = []

    def addFilaDeEspera(self,nF):
        ## Adicionando Nota Fiscal;
        self.filaEspera.append(nF)
        ## Adicionando Hora;
        dataAtual = datetime.datetime.now()
        dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M")
        self.horaFila.append(dataFormatada)
        print(f"Foi adicionado o produto N°{nF} a fila de espera da Triagem")
    
    def exibirFila(self):
        for i in range(len(self.filaEspera)):
            print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={i+1}°")
            print(f"")
            print(f"Entrega Cod.{self.filaEspera[i]}")
            print(f"Data e Hora da entrada: {self.horaFila[i]}")
            print(f"")

    def atualizarQualidade(self):
        confirmação = True
        while confirmação:
            codigo = input("Digite o número da Nota Fiscal do item inspecionado: ")
            qualidade = int(input("O intem Passou no teste de qualidade? (S-1 / N-2) "))
            if qualidade == 1:
                confirmação =False
                return codigo
                ## DELETE do Banco da Fila
                ## UPDATE qualidade
            elif qualidade == 2:
                confirmação =False
                return codigo
                ## DELETE do Banco da Fila
                ## UPDATE qualidade
            else:
                print("O Valor de qualidade inserido não está correto!")
        
class Estoque(Empresa):
    def __init__(self):
        super().__init__()
        self.filaEspera2 = []
        self.horaFila2 = []

    def addFilaDeEspera2(self,nF):
        self.filaEspera2.append(nF)
        ## Adicionando Hora;
        dataAtual = datetime.datetime.now()
        dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M")
        self.horaFila2.append(dataFormatada)
        print(f"Foi adicionado o produto N°{nF} a fila de espera do Almoxarifado")

    def exibirFila2(self):
        for i in range(len(self.filaEspera2)):
            print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={i+1}°")
            print(f"")
            print(f"Entrega Cod.{self.filaEspera2[i]}")
            print(f"Data e Hora da entrada: {self.horaFila2[i]}")
            print(f"")

    def gerarMapa(self):
        print("      ___         ___         ___") 
        print(" P-7  | |    P-7  | |    P-7  | |")
        print(" P-6  | |    P-6  | |    P-6  | |")
        print(" P-5  | |    P-5  | |    P-5  | |")
        print(" P-4  | |    P-4  | |    P-4  | |")
        print(" P-3  | |    P-3  | |    P-3  | |")
        print(" P-2  | |    P-2  | |    P-2  | |")
        print(" P-1  | |    P-1  | |    P-1  | |")
        print("---------------------------------")
        print("      T-a         T-b         T-c")

#-=-=-=-=-=-=-=-=-=-=-=-=-= Classe Neto;
class Sistema(Recebimento, Triagem, Estoque):
    pass

empresa1 = Recebimento()
empresa1.entradaDeProduto()
cod = empresa1.transferencia1()
traigem1 = Triagem()
traigem1.addFilaDeEspera(cod)
traigem1.exibirFila()
cod = traigem1.atualizarQualidade()
estoque1 = Estoque()
estoque1.addFilaDeEspera2(cod)
estoque1.exibirFila2()


#-=-=-=-=-=-=-=-=-=-=-=-=-= Desenho do Almoxarifado;

#      ___         ___         ___  
# P-7  | |    P-7  | |    P-7  | |
# P-6  | |    P-6  | |    P-6  | |
# P-5  | |    P-5  | |    P-5  | |
# P-4  | |    P-4  | |    P-4  | |
# P-3  | |    P-3  | |    P-3  | |
# P-2  | |    P-2  | |    P-2  | |
# P-1  | |    P-1  | |    P-1  | |
#-------------------------------------
#      T-a         T-b         T-c
#
#
#
