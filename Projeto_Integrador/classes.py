import random
import datetime
from select import select
import sqlite3
from stringprep import map_table_b2

#-=-=-=-=-=-=-=-=-=-=-=-=-= Banco de Dados;
conexão = sqlite3.connect("Projeto_Integrador\Estoque.db")
cursor = conexão.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS produto("
"Codigo INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,"
"Nome TEXT UNIQUE NOT NULL,"
"Quantidade REAL"
")")
conexão.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS produtos("
"Codigo NUM NOT NULL,"
"Nome TEXT NOT NULL,"
"Quantidade REAL NOT NULL,"
"NotaFiscal NUM NOT NULL,"
"Data NUM NOT NULL,"
"Qualidade TEXT,"
"Localização TEXT"
")")
conexão.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS listaDeEspera("
"NotaFiscal NUM NOT NULL,"
"Data NUM NOT NULL"
")")
conexão.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS listaDeEspera2("
"NotaFiscal NUM NOT NULL,"
"Data NUM NOT NULL"
")")
conexão.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS estoque("
"Torre NUM NOT NULL,"
"Piso NUM NOT NULL,"
"Estado TEXT NOT NULL"
")")
conexão.commit()

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

    ## FUnção de Devolução de Produtos Reprovados na Triagem....

    ## ACESSO: Comprador
    def cadastroProdutos(self):
        Confirmação = True
        while Confirmação:
            print("")
            nome = input("Digite o nome do Produto: ")
            nome = nome.strip().upper()
            confirm = int(input(f"Você gostaria de Cadastrar o Produto: {nome}  (1-S / 2-N)"))
            if confirm == 1:
                try:
                    print("")
                    cursor.execute("INSERT INTO produto (Nome) VALUES (?) ",(nome,))
                    conexão.commit()
                    cursor.execute("SELECT Codigo FROM produto WHERE Nome = (?)",(nome,))
                    for linha in cursor.fetchall():
                        codigo = linha[0]
                    print("Produto Cadastrado Com Sucesso!")
                    print(f"Nome : {nome}")
                    print(f"Código : {codigo}")
                    print("")
                    Confirmação = False
                except:
                    print("")
                    print("Produto já existente no Sistema!")
                    cursor.execute("SELECT Codigo FROM produto WHERE Nome = (?)",(nome,))
                    for linha in cursor.fetchall():
                        codigo = linha[0]
                    print("")
                    print(f"Nome: {nome}")
                    print(f"Código: {codigo}")
                    print("")

    ## ACESSO: Recebimento
    def entradaDeProduto(self):
        Confirmação = True
        Confirmação2 = True
        Confirmação3 = True
        while Confirmação:
            while Confirmação3:
                ## Entrada dos Dados;
                nome = input("Digite o nome do Produto: ")
                nome = nome.strip().upper()
                ## Recuperando Código:
                codigo = ""
                cursor.execute("SELECT Codigo FROM produto WHERE Nome = (?)",(nome,))
                for linha in cursor.fetchall():
                    codigo = linha[0]
                if codigo != "":
                    Confirmação3 = False
                else:
                    print("")
                    print("Este Item não está Cadastrado no Sistema! Favor entrar em Contato com o setor de Compra...")
                    print("")
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

    ## ACESSO: Automatico
    def adicionandoBanco(self):
        cursor.execute("INSERT INTO produtos (NotaFiscal,Nome,Codigo,Quantidade,Data) VALUES (?,?,?,?,?) ",(self.nF,self.nomeProduto,self.codigo,self.quantidade,self.data_hora))
        conexão.commit()
        cursor.execute('UPDATE produto SET Quantidade = Quantidade + ? WHERE Codigo = ?',(self.quantidade, self.codigo))
        conexão.commit()
    
    ## ACESSO: Automatico;
    def transferencia1(self):
        ## Adicionando Hora;
        dataAtual = datetime.datetime.now()
        dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M")
        cursor.execute("INSERT INTO listaDeEspera (NotaFiscal,Data) VALUES (?,?) ",(self.nF,dataFormatada))
        conexão.commit()
        print("")
        print(f"Foi adicionado o produto N°{self.nF} a fila de espera da Triagem")
        print("")
        
class Triagem(Empresa):
    def __init__(self):
        super().__init__()
        self.filaEspera = ""
        self.cod = 0
    
    ## ACESSO: Triagem;
    def exibirFila(self):
        contador = 1
        cursor.execute("SELECT * FROM listaDeEspera")
        for linha in cursor.fetchall():
            notaFiscal,Data = linha
            print(f"")
            print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={contador}°")
            print(f"")
            print(f"Produto Cod. {notaFiscal}")
            print(f"Data e Hora da entrada: {Data}")
            print(f"")
            contador += 1

    ## ACESSO: Triagem;
    def atualizarQualidade(self):
        Confirmação = True
        Confirmação2 = True
        while Confirmação:
            while Confirmação2:
                cod = 0
                print("")
                codigo = int(input("Digite o número da Nota Fiscal do item inspecionado: "))
                cursor.execute("SELECT NotaFiscal FROM listaDeEspera")
                for linha in cursor.fetchall():
                    cod = linha
                if cod == 0:
                    print("Ops, esta NF não está na Fila de Espera!")
                else: 
                    cursor.execute("SELECT NotaFiscal FROM produtos WHERE NotaFiscal = ?",(codigo,))
                    for linha in cursor.fetchall():
                        nf = linha
                        nf = nf[0]
                    self.cod = nf
                    Confirmação2 = False
            print("")
            qualidade = int(input("O item Passou no teste de qualidade? (S-1 / N-2) "))
            if qualidade == 1:
                Confirmação = False
                ## DELETE do banco da Fila;
                cursor.execute('DELETE FROM listaDeEspera WHERE NotaFiscal = ?',(nf,))
                conexão.commit()
                ## UPDATE qualidade;
                cursor.execute('UPDATE produtos SET Qualidade = ? WHERE NotaFiscal = ?',("Aprovado",nf))
                conexão.commit()
            elif qualidade == 2:
                Confirmação =False
                ## DELETE do banco da Fila;
                cursor.execute('DELETE FROM listaDeEspera WHERE NotaFiscal = ?',(nf,))
                conexão.commit()
                ## UPDATE qualidade;
                cursor.execute('UPDATE produtos SET Qualidade = ? WHERE NotaFiscal = ?',("Reprovado",nf))
                conexão.commit()
            else:
                print("O Valor de qualidade inserido não está correto!")
    
    ## ACESSO: Automatico;
    def transferencia2(self):
        ## Adicionando Hora;
        dataAtual = datetime.datetime.now()
        dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M")
        cursor.execute("INSERT INTO listaDeEspera2 (NotaFiscal,Data) VALUES (?,?) ",(self.nF,dataFormatada))
        conexão.commit()
        print("")
        print(f"Foi adicionado o produto N°{self.cod} a fila de espera da Triagem")
        print("")

class Estoque(Empresa):
    def __init__(self):
        super().__init__()
        self.mapa = []
        self.torre = 0
        self.piso = 0

    ## ACESSO: Gerente;
    def gerarMapa(self):
        ## Entrada de Dados;
        torre = int(input("Qual a Quantidade de Torres para estoque: "))
        piso = int(input("Qual a Quantidade de pisos em cada torre: "))
        self.torre = torre
        self.piso = piso
        ## Geração de Mapa;
        for  i in range(1,(torre+1)):
            for e in range(1,(piso+1)):
                mapa  = {"Torre":i,
                         "Piso":e,
                         "Estado": "Vaziu"
                        }
                self.mapa.append(mapa)
        print(self.mapa)

    ## ACESSO: Automático;
    def salvaMapa(self):
        ## Separação;
        for i in range(0,len(self.mapa)):
            print(i)
            cursor.execute("INSERT INTO estoque (Torre,Piso,Estado) VALUES (?,?,?) ",(self.mapa[i]["Torre"],self.mapa[i]["Piso"],self.mapa[i]["Estado"]) )
            conexão.commit()

    ## ACESSO: Automático;
    def carregarMapa(self):
        ## União;
        cursor.execute("SELECT * FROM estoque")
        for linha in cursor.fetchall():
            torre,piso,estado = linha
            mapa ={"Torre":torre,
                    "Piso":piso,
                    "Estado":estado
                  }
            self.torre = torre
            self.piso = piso
            self.mapa.append(mapa)

    ## ACESSO: Almoxarifado;
    def mostrarMapa(self):
        contador = 0
        for i in range(0,self.torre):
            for e in range(0,self.piso):
                if self.mapa[contador]['Piso'] == 1:
                    print("")
                    print(f"           Torre {self.mapa[contador]['Torre']}")
                    print("")
                    print("            ----------")
                    print(f"Piso {self.mapa[contador]['Piso']}     | {self.mapa[contador]['Estado']} |")
                    print("            ----------")
                else:
                    print("            ----------")
                    print(f"Piso {self.mapa[contador]['Piso']}     | {self.mapa[contador]['Estado']} |")
                    print("            ----------")
                contador +=1                           

    ## ACESSO: Almoxarifado;
    def exibirFila2(self):
        contador = 1
        cursor.execute("SELECT * FROM listaDeEspera2")
        for linha in cursor.fetchall():
            notaFiscal,Data = linha
            print(f"")
            print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={contador}°")
            print(f"")
            print(f"Produto Cod. {notaFiscal}")
            print(f"Data e Hora da entrada: {Data}")
            print(f"")
            contador += 1

    ## ACESSO: Almoxarifado;
    def endereçarProduto(self):
        # Entrada de Dados;
        # torre = int(input("Digite a Torre:"))
        # piso = int(input("Digite o Piso:"))
        # nf = int(input("Digite a Nota Fiscal do Produto:"))
        print(self.mapa[0]["Torre"])
        print(self.mapa[1]["Torre"])
        print(self.mapa[2]["Torre"])
        print(self.mapa[3]["Torre"])
        print("")
        print("")
        print(self.mapa[0]["Piso"])
        print(self.mapa[1]["Piso"])
        print(self.mapa[2]["Piso"])
        print(self.mapa[3]["Piso"])
        print("")
        print("")
        print(self.mapa[0]["Estado"])
        print(self.mapa[1]["Estado"])
        print(self.mapa[2]["Estado"])
        print(self.mapa[3]["Estado"])
        
        pass

#-=-=-=-=-=-=-=-=-=-=-=-=-= Classe Neto;
class Sistema(Recebimento, Triagem, Estoque):
    pass

# empresa1 = Recebimento()

## Comprador;
# empresa1.cadastroProdutos()
## Recebimento;
# empresa1.entradaDeProduto()
## Automatico:
# empresa1.adicionandoBanco()
# empresa1.transferencia1()

# traigem1 = Triagem()

## Triagem;
# traigem1.exibirFila()
# traigem1.atualizarQualidade()
## Automático;
# traigem1.transferencia2()

estoque1 = Estoque()

# Estoque;
estoque1.exibirFila2()
# estoque1.gerarMapa()
#estoque1.salvaMapa()
estoque1.carregarMapa()
estoque1.mostrarMapa()
estoque1.endereçarProduto()




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