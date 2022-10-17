#-=-=-=-=-=-=-=-=-=-=-=-=-= Importações;
import random
import datetime
import sqlite3
import os
from Ferramentas import coresTerminal

#-=-=-=-=-=-=-=-=-=-=-=-=-= Declarando Cores;
Verde,Base = coresTerminal(0,3,0)
Vermelho,Base = coresTerminal(0,2,0)
Amarelo,Base = coresTerminal(0,4,0)

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
"Estado TEXT NOT NULL,"
"NotaFiscal TEXT"
")")
conexão.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS perfil("
"Nome TEXT NOT NULL,"
"Matricula NUM NOT NULL UNIQUE,"
"Acesso TEXT"
")")
conexão.commit()

#-=-=-=-=-=-=-=-=-=-=-=-=-= Classe Pai;
class Empresa:
    def __init__(self):
        self.nomeEmpresa = "" 
    
    ## ATUALIZAÇÂO: Englobar mais dados da empresa...

#-=-=-=-=-=-=-=-=-=-=-=-=-= Classes Filhos;
class Recebimento(Empresa):
    def __init__(self):
        super().__init__()
        self.nF = '' ## Rastreamento Interno
        self.codigo = ''
        self.nomeProduto = ''
        self.quantidade = 0
        self.data_hora = ''

    ## ATUALIZAÇÂO: Função de Deletar Itens que não passaram no teste de qualidade...

    ## ACESSO: Comprador
    def cadastroProdutos(self):
        ## Declarando Cores;
        global verde
        global vermelho
        global base
        ## Inicio da Operação;
        os.system("cls")
        print("-="*10,f"{Amarelo}Cadastro de Produtos{Base}")
        Confirmação = True
        while Confirmação:
            Confirmação2 = True
            print("")
            try:
                while Confirmação2:
                    nome = input("Digite o nome do Produto: ")
                    nome = nome.strip().upper()
                    if nome == "":
                        print(f"{Vermelho}Nome Vaziu!{Base}")
                    else:
                        Confirmação2 = False
                confirmar = int(input(f"Você gostaria de Cadastrar o Produto: {nome}  (1-S / 2-N)"))
                match confirmar:
                    case 1:
                        codigo = ""
                        cursor.execute("SELECT Codigo FROM produto WHERE Nome = (?)",(nome,))
                        for linha in cursor.fetchall():
                            codigo = linha[0]
                        ## Caso não tenha cadastro;
                        if codigo == "":
                            cursor.execute("INSERT INTO produto (Nome,Quantidade) VALUES (?,?)",(nome,0))
                            conexão.commit()
                            cursor.execute("SELECT Codigo FROM produto WHERE Nome = (?)",(nome,))
                            for linha in cursor.fetchall():
                                codigo = linha[0]
                            print("")
                            print(f"{Verde}Produto Cadastrado com sucesso!{Base}")
                            print("-="*5)
                            print(f"{Amarelo}Nome: {nome}")
                            print(f"Código: {codigo} {Base}")
                            Confirmação = False
                        ## Caso tenha cadastro;
                        else:
                            print("")
                            print(f"{Vermelho}Produto já Cadastrado!{Base}")
                            print("-="*5)
                            print(f"{Amarelo}Nome: {nome}")
                            print(f"Código: {codigo} {Base}")
                            Confirmação = False
                    case 2:
                        print("")
                        print("🤙")
                        print("")
                    case _:
                        print("")
                        print(f"{Vermelho}Valor Inserido não é uma opção!{Base}")
                        print("")
            except:
                print(f"{Vermelho}A Opção escolhida está incorreta!{Base}")
    ## ACESSO: Recebimento
    def entradaDeProduto(self):
        ## Variáveis;
        global verde
        global vermelho
        global amarelo
        global base
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
                    print(f"{Vermelho}Este Item não está Cadastrado no Sistema! Favor entrar em Contato com o setor de Compra...{Base}")
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
                print(f"{Amarelo}Nº Nota Fiscal: {nF} ")
                print(f"Produto: {nome} ")
                print(f"Codigo do Produto: {codigo} ")
                print(f"Quantidade : {quantidade} {Base}")
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
                    print(f"{Vermelho}O valor digitado está incorreto! {Base}")

    ## ACESSO: Automatico
    def adicionandoBanco(self):
        cursor.execute("INSERT INTO produtos (NotaFiscal,Nome,Codigo,Quantidade,Data) VALUES (?,?,?,?,?) ",(self.nF,self.nomeProduto,self.codigo,self.quantidade,self.data_hora))
        conexão.commit()
        cursor.execute('UPDATE produto SET Quantidade = Quantidade + ? WHERE Codigo = ?',(self.quantidade, self.codigo))
        conexão.commit()
    
    ## ACESSO: Automatico;
    def transferencia1(self):
        global verde
        global base
        ## Adicionando Hora;
        dataAtual = datetime.datetime.now()
        dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M")
        cursor.execute("INSERT INTO listaDeEspera (NotaFiscal,Data) VALUES (?,?) ",(self.nF,dataFormatada))
        conexão.commit()
        print("")
        print(f"{Verde}Foi adicionado o produto N°{self.nF} a fila de espera da Triagem{Base}")
        print("")
        
class Triagem(Empresa):
    def __init__(self):
        super().__init__()
        self.filaEspera = ""
        self.cod = 0
    
    ## ACESSO: Triagem;
    def exibirFila(self):
        global amarelo
        global base
        contador = 1
        cursor.execute("SELECT * FROM listaDeEspera")
        for linha in cursor.fetchall():
            notaFiscal,Data = linha
            print(f"")
            print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={contador}°")
            print(f"{Amarelo}")
            print(f"Produto Cod. {notaFiscal}")
            print(f"Data e Hora da entrada: {Data}{Base}")
            print(f"")
            contador += 1

    ## ACESSO: Triagem;
    def atualizarQualidade(self):
        global vermelho
        global verde
        global base
        Confirmação = True
        Confirmação2 = True
        while Confirmação:
            while Confirmação2:
                cod = 0
                print("")
                codigo = input("Digite o número da Nota Fiscal do item inspecionado: ")
                codigo = codigo.strip()
                if codigo == "":
                    codigo = 0
                else:
                   codigo = int(codigo)
                cursor.execute("SELECT NotaFiscal FROM listaDeEspera")
                for linha in cursor.fetchall():
                    cod = linha
                if cod == 0:
                    print(f"{Vermelho}Ops, esta NF não está na Fila de Espera!{Base}")
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
                print(f"{Vermelho}O Valor de qualidade inserido não está correto!{Base}")
            print(self.cod)
    
    ## ACESSO: Automatico;
    def transferencia2(self):
        global verde
        global base
        ## Adicionando Hora;
        dataAtual = datetime.datetime.now()
        dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M")
        cursor.execute("INSERT INTO listaDeEspera2 (NotaFiscal,Data) VALUES (?,?) ",(self.cod,dataFormatada))
        conexão.commit()
        print("")
        print(f"{Verde}Foi adicionado o produto N°{self.cod} a fila de espera da Triagem{Base}")
        print("")

class Estoque(Empresa):
    def __init__(self):
        super().__init__()
        self.mapa = []
        self.torre = 0
        self.piso = 0

    ## ACESSO: Total;
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

    ## ACESSO: Automático;
    def salvaMapa(self):
        ## Separação;
        for i in range(0,len(self.mapa)):
            cursor.execute("INSERT INTO estoque (Torre,Piso,Estado) VALUES (?,?,?) ",(self.mapa[i]["Torre"],self.mapa[i]["Piso"],self.mapa[i]["Estado"]) )
            conexão.commit()

    ## ACESSO: Automático;
    def carregarMapa(self):
        ## União;
        cursor.execute("SELECT * FROM estoque")
        for linha in cursor.fetchall():
            torre,piso,estado,nf = linha
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
        torre = int(input("Digite a Torre:"))
        piso = int(input("Digite o Piso:"))
        nf = int(input("Digite a Nota Fiscal do Produto:"))
        localização = (f"Torre:{torre} / Piso:{piso}")
        ## Recuperando Informação da Tabela;
        cursor.execute("SELECT Nome,Quantidade FROM produtos WHERE NotaFiscal = ?",(nf,) )
        for linha in cursor.fetchall():
            Nome,Quantidade = linha
        produto = (f"Produto: {Nome} / Quantidade: {Quantidade}")
        ## Atualizando Banco de Dados e Self;
        contador = 0
        for i in self.mapa:
            if self.mapa[contador]["Torre"] == torre:
                if self.mapa[contador]["Piso"] == piso:
                    if self.mapa[contador]["Estado"] != "Vaziu":
                        print("")
                        print("Espaço já ocupado!!")
                        print("")
                    else:
                        print(nf)
                        self.mapa[contador]["Estado"] = produto
                        cursor.execute('UPDATE estoque SET Estado = ?, NotaFiscal = ? WHERE Torre = ? AND Piso = ?',(produto,nf,torre,piso))
                        conexão.commit()
                        cursor.execute('UPDATE produtos SET Localização = ? WHERE NotaFiscal = ?',(localização,nf))
                        conexão.commit()
                        print("Produto Endereçado com Sucesso!")
                else:
                    pass
            else:
                pass
            contador += 1
    
    ## ACESSO: Almoxarifado;
    def transferirProduto(self):
        # Entrada de Dados;
        print("")
        torre = int(input("Digite a Torre: "))
        piso = int(input("Digite o Piso: "))
        print("")
        # Recuperando Informações do Banco de Dados:
        cursor.execute("SELECT Estado, NotaFiscal FROM estoque WHERE Torre = ? AND Piso = ?",(torre, piso) )
        for linha in cursor.fetchall():
            print(linha)
            estado,nf = linha
        # Mostrandos Dados Recuperados;
        print("-="*30)
        print(f"O item selecionado é: {estado}")
        print("-="*30)
        # tipo de transferencia;
        tipo = int(input("Digite o tipo de transferencia que deseja fazer: (1- Interna /2- Externa) "))
        match tipo:
            case 1:
                # Recebendo novas Informações;
                print("")
                print("-="*15," Nova Localização")
                print("")
                torre2 = int(input("Digite a Torre: "))
                piso2 = int(input("Digite o Piso: "))
                localização = (f"Torre:{torre2} / Piso: {piso2}")
                # Deletando informação do Banco de Dados;
                cursor.execute('UPDATE estoque SET Estado = ?, NotaFiscal = ? WHERE Torre = ? AND Piso = ?',("Vaziu",0,torre,piso))
                conexão.commit()
                cursor.execute('UPDATE produtos SET Localização = ? WHERE NotaFiscal = ?',("Vaziu",nf))
                conexão.commit()
                print("Produto Excluido com Sucesso!")
                #Adicionando na nova Localização;
                cursor.execute('UPDATE estoque SET Estado = ?, NotaFiscal = ? WHERE Torre = ? AND Piso = ?',(estado,nf,torre2,piso2))
                conexão.commit()
                cursor.execute('UPDATE produtos SET Localização = ? WHERE NotaFiscal = ?',(localização,nf))
                conexão.commit()
                print("Produto Endereçado com Sucesso!")
            case 2:
                # Recebendo Info
                print("")
                print("-="*15," Nova Localização")
                print("")
                loja = input("Qual a loja que deseja trasferir?")
                # Deletando info do Banco de Dados;
                cursor.execute('UPDATE estoque SET Estado = ?, NotaFiscal = ? WHERE Torre = ? AND Piso = ?',("Vaziu",0,torre,piso))
                conexão.commit()
                cursor.execute('UPDATE produtos SET Localização = ? WHERE NotaFiscal = ?',("Transferencia",nf))
                conexão.commit()
                print("Produto Endereçado com Sucesso!")
    
    ## ATUALIZAÇÂO: Geração de métricas com Excel.

#-=-=-=-=-=-=-=-=-=-=-=-=-= Classe Neto;
class Sistema(Recebimento, Triagem, Estoque):
    def __init__(self):
        super().__init__()
        self.nomeUsuário = ""
        self.matricula = ""
        self.acesso = ""
    
    def cadastroDeFuncionarios(self):
        # Recuperando Cores para as Funções;
        global Amarelo
        global Vermelho
        global Verde
        global Base
        # Entrada e Formatação de Dados;
        Confirmação1 = True
        while Confirmação1:
            nome = input("Digite o nome do Funcionário: ")
            matricula = input("Digite a Matricula do Funcionário: ")
            print("")
            nome = nome.capitalize().strip()
            matricula = matricula.strip()
            # Conferindo dados;
            if nome == "" or len(matricula) != 6:
                print(f"{Vermelho}O Nome ou Matrícula inseridos estão incorretos!{Base}")
            else:
                Confirmação1 = False
        # Entrada e escolha do Acesso;
        print("Tipos de Acesso:")
        print(f"{Amarelo}1- TOTAL: Tem acesso a todas as abas.")
        print("2- COMPRADOR: Tem acesso ao cadastro de produtos e a relatórios de vendas.")
        print("3- RECEBIMENTO: Tem acesso a entrada de produtos na loja.")
        print("4- TRIAGEM: Tem acesso a Fila de espera 1 e ao teste de qualidade.")
        print(f"5- ALMOXARIFADO: Tem Acesso ao endereçamento de predutos e transferencias.{Base}")
        escolhaAcesso = int(input("Digite o número relacionado ao Tipo de ACESSO: "))
        match escolhaAcesso:
            case 1:
                acesso = "TOTAL"
            case 2:
                acesso = "COMPRADOR"
            case 3:
                acesso = "RECEBIMENTO"
            case 4:
                acesso = "TRIAGEM"
            case 5:
                acesso = "ALMOXARIFADO"
        # Dando entrada no Banco de Dados;
        cursor.execute("INSERT INTO perfil (Nome,Matricula,Acesso) VALUES (?,?,?) ",(nome,matricula,acesso))
        conexão.commit()
        # Inserindo na Class;
        self.nomeUsuário = nome
        self.matricula = matricula
        self.acesso = acesso
        print("")
        print(f"{Verde}Cadastro Concluido com Sucesso!{Base}")
        print("")

    def login(self):
        # Recuperando Cores para as Funções;
        global Amarelo
        global Vermelho
        global Verde
        global Base
        # Entrada e Formatação de Dados;
        Confirmação = True
        while Confirmação:
            nome = input("Digite seu Nome: ")
            matricula = input("Digite sua Matricula: ")
            print("")
            nome = nome.capitalize().strip()
            matricula = matricula.strip()
            # Testando informações;
            acesso = ""
            cursor.execute("SELECT Acesso FROM perfil WHERE Nome = ? AND Matricula = ?",(nome,matricula))
            for linha in cursor.fetchall():
                acesso = linha[0]
            if acesso == "":
                print(f"{Vermelho}Usuário ou Matrícula incorretos!{Base}")
            else:
                self.nomeUsuário = nome
                self.matricula = matricula
                self.acesso = acesso
                Confirmação = False
                print(f"{Verde}Login efetuado com Sucesso!{Base}")

    def menu(self,sistema,escolha):
        ## Declarando Variavel de Resposta;
        resp = False
        match escolha:
            ## Cadastro Item;
            case 1:
                if self.acesso == "COMPRADOR" or self.acesso == "TOTAL":
                    resp = True
                    sistema.cadastroProdutos()
                else:
                    print(f"{Vermelho}Acesso Negado!{Base}")
            ## Entrada Item;
            case 2:
                if self.acesso == "RECEBIMENTO"or self.acesso == "TOTAL":
                    resp = True
                    sistema.entradaDeProduto()
                    sistema.adicionandoBanco()
                    sistema.transferencia1()
                else:
                    print(f"{Vermelho}Acesso Negado!{Base}")
            ## Exibir Fila de Espera Triagem;
            case 3:
                if self.acesso == "TRIAGEM"or self.acesso == "TOTAL":
                    resp = True
                    sistema.exibirFila()
                else:
                    print(f"{Vermelho}Acesso Negado!{Base}")
            ## Atualiza Qualidade;
            case 4:
                if self.acesso == "TRIAGEM"or self.acesso == "TOTAL":
                    resp = True
                    sistema.atualizarQualidade()
                    sistema.transferencia2()
                else:
                    print(f"{Vermelho}Acesso Negado!{Base}")
            ## Exibir Fila de Espera Estoque;
            case 5:
                if self.acesso == "ALMOXARIFADO"or self.acesso == "TOTAL":
                    resp = True
                    sistema.exibirFila2()
                else:
                    print(f"{Vermelho}Acesso Negado!{Base}")
            ## Mostrar mapa do Estoque;
            case 6:
                if self.acesso == "ALMOXARIFADO"or self.acesso == "TOTAL":
                    resp = True
                    sistema.carregarMapa()
                    sistema.mostrarMapa()
                else:
                    print(f"{Vermelho}Acesso Negado!{Base}")
            ## Endereçar Produto;
            case 7:
                if self.acesso == "ALMOXARIFADO"or self.acesso == "TOTAL":
                    resp = True
                    sistema.carregarMapa()
                    sistema.endereçarProduto()
                else:
                    print(f"{Vermelho}Acesso Negado!{Base}")
            ## Transferir Produto;
            case 8:
                if self.acesso == "ALMOXARIFADO"or self.acesso == "TOTAL":
                    resp = True
                    sistema.carregarMapa()
                    sistema.transferirProduto()
                else:
                    print(f"{Vermelho}Acesso Negado!{Base}")
            ## Geração do Mapa do Estoque;
            case 9:
                if self.acesso == "TOTAL":
                    resp = True
                    sistema.gerarMapa()
                    sistema.salvaMapa()
                else:
                    print(f"{Vermelho}Acesso Negado!{Base}")
        return resp