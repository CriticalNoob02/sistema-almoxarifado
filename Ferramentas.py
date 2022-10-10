## Importações;
import random
import re
import os

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Modo de Uso;

def instruções():
    os.system("cls")
    print("\033[42m#######################################################\033[40m \033[35mBem-vindo a Biblioteca de Ferramentas\033[37m \033[42m#######################################################\033[40m")
    print("")
    print("Aqui você ira ver algumas instruções Básicas para o uso das funções")
    print("Para iniciar...")
    print("")
    print("Importe o arquivo 'Ferramentas.py' para seu projeto, e a seguir importe as funções desejadas de cada arquivo;")
    print("")
    print("\033[32m-=-=-=-=-=-=-=-= Funções de Verificação...\033[37m")
    print("")
    print("São funções que iram retornar se a informação inserida é True ou False então siga os passos seguintes:")
    print("")
    print("1- Crie uma variavel para receber a resposta da função Ex: 'verificação = verificarSenha(senha)'")
    print("2- Todas as funções precisam que seja inserida um argumento a verificar")
    print("3- Algumas das funções (ex:Verificador de CPF) recebem argumento no formato 'String' ao inves de valor númerico, mude o formato se ocorrer este erro: ' 'int' object is not iterable' '")
    print("")
    print("\033[32m-=-=-=-=-=-=-=-= Funções de Geração...\033[37m")
    print("")
    print("São funções que iram retornar a própria informação para uma variavel sem precisar de nenhum argumento;")
    print("")
    print("1- Ex = cpf = gerarCPF()")
    print("2-      print(cpf) ")
    print("3-    'ira printar o um cpf válido' ")
    print("")
    print("\033[32m-=-=-=-=-=-=-=-= Funções Diversas...\033[37m")
    print("")
    print("Essas são funções mais aleatórias, mas que podem ser muito úteis, mas aqui vou explicar uma por uma, pois a forma de usar tambem é diversa ")
    print("")
    print("1- modo de cor no terminal, essa função irá retornar 2 variaveis, a primeira será o estilo escolhido e a segunda é o estilo base do terminal...")
    print("2- Ex = tema,base = coresTerminal(1,4,0)")
    print("3- A função ira receber 3 argumentos, relacionados ao; 1º Estilo de fonte / 2º cor de texto / 3º cor de fundo")
    print("4- Segue a tabela referente ao valor de cada cor e estilo;")
    print("5- *Estilo*;")
    print("")
    print("6- / 0 = \033[0mPadrão\033[0m / 1 = \033[1mNegrito\033[0m / 2 = \033[4mSublinhado\033[0m / 3 = \033[7mNegativo\033[0m")
    print("")
    print("7- *Cor de Texto*;")
    print("")
    print("8- / 0 = \033[37mPadrão\033[37m / 1 = \033[30mCinza\033[37m / 2 = \033[31mVermelho\033[37m / 3 = \033[32mVerde\033[37m / 4 = \033[33mAmarelo\033[37m / 5 = \033[34mRoxo\033[37m / 6 = \033[35mRosa\033[37m / 7 = \033[36mAzul\033[37m")
    print("")
    print("7- *Cor de Fundo*;")
    print("")
    print("8- / 0 = \033[40mPadrão\033[40m / 1 = \033[47mCinza\033[40m / 2 = \033[41mVermelho\033[40m / 3 = \033[42mVerde\033[40m / 4 = \033[43mAmarelo\033[40m / 5 = \033[44mRoxo\033[40m / 6 = \033[45mRosa\033[40m / 7 = \033[46mAzul\033[40m")
    print("")
  
# instruções()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Verificadores, retorna variavel False or True;

## Senhas, 1- Maior ou igual a 8 digitos / 2- Conter 1 ou mais caracteres especiais / 3- Conter 3 ou mais números;
def verificarSenha(Senha):
    ## Definindo Variaveis;
    caracter = 0
    numero = 0
    senhaL = []
    Verificação = False
    ## Separando letra por letra da Senha;
    for i in Senha:
        senhaL.append(i)
    ## Tamanho da Senha;
    if len(Senha) < 8:
        print("\033[31mSenha Inválida - Erro na quantidade de Caracteres\033[37m")
        return
    for i in range(0,len(senhaL)):
        if senhaL[i] == "@" or senhaL[i] == "!" or senhaL[i] == "&" or senhaL[i] == "/" or senhaL[i] == "?" or senhaL[i] == "_" or senhaL[i] == "*" or senhaL[i] == "#" or senhaL[i] == "%" or senhaL[i] == "$" or senhaL[i] == "|":
            caracter += 1
        if senhaL[i] == "0" or senhaL[i] == "1" or senhaL[i] == "2" or senhaL[i] == "3" or senhaL[i] == "4" or senhaL[i] == "5" or senhaL[i] == "6" or senhaL[i] == "7" or senhaL[i] == "8" or senhaL[i] == "9": 
            numero += 1 
    if numero >= 3 and caracter >= 1:
        Verificação = True
    else:
        print("\033[31mSenha Inválida - Sua senha não segue as regras!\033[37m")
    return Verificação

## Emails, 1- Deve conter '@' / 2- Deve conter ".com" / 3- Pode ou não conter ".br" no final / 4- Não contem limite de letras e Números / 5- Não pode conter caracter especial além do "@";
def verificarEmail(Email):
    Verificação = False
    emailRegex = '^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.+[a-z]+)?$'
    if re.search(emailRegex,Email):
        Verificação = True
    else:
        print("\033[31mEmail Inválido\033[37m")
    return Verificação

## CPF, inserir valor no formato de STRING!;
def verificarCPF(cpf):
    ## Criando as Variavéis para a primeira conta;
    Verificação = True
    cpf_1 = []
    total = 0
    n1 = 10
    e = 0
    igualdade = 0
    ## Adicionando CPF em Lista;
    for i in cpf:
        i = int(i)
        cpf_1.append(i)
    for i in cpf_1:
        if(cpf_1.count(i) > 10):
            igualdade = 1
        else:
            pass
    ## 1º Multiplicação;
    for i in range(2, 11):
        total += (cpf_1[e]*n1)
        n1 -= 1
        e += 1                  
    ## Verificando o 1º Digito;
    digito1 = (11- (total % 11))
    if digito1 > 9:
        digito1 = 0          
    if (digito1 == cpf_1[-2]):
        if (igualdade == 1):
            print("\033[31m CPF invalido!\033[37m")
            Verificação = False
            return
    else:
        print("\033[31m CPF invalido!\033[37m")
        Verificação = False
        return
    ## Zerando as Variaveis;
    n1 = 11
    e = 0
    total = 0
    ## 2º Multiplicação;
    for i in range(2, 12):
        total += (cpf_1[e]*n1)
        n1 -= 1
        e += 1
    ## Verificando o 2º Digito;    
    digito2 = (11- (total % 11))
    if digito2 > 9:
        digito2 = 9
    if (digito2 == cpf_1[-1]):
            Confirmação_2 = False  
    else:
        print("\033[31m CPF invalido!\033[37m")
        Verificação = False
    
    return Verificação

## Telefone, Digitar apenas os Digitos, incluindo o DDD; 
def verificarTelefone(Telefone):
    ## Váriaveis;
    Verificação = False
    tel = str(Telefone)
    ddds = ["61","62","64","65","66","67","82","71","73","74","75","77","85","88","98","99","83","81","87","86","89","84","79","68","96","92","97","91","93","94","95","69","63","27","28","21","31","32","33","34","35","37","38","22","24","11","12","13","14","15","16","17","18","19","41","42","43","44","45","46","51","53","54","55","47","48","49"]
    confirma = 0
    ## Validando Tamanho;
    if len(tel) == 11:
        pass
    else:
        print("\033[31mNúmero Incorreto - Quantidade de Digitos incorreta!\033[37m")
        return
    ## Validando DDD;
    ddd = tel[0]+tel[1]
    for i in range(0,len(ddds)):
        if ddd == ddds[i]:
            confirma += 1
        else:
            confirma += 0
    match confirma:
        case 0:
            print("\033[31mNúmero Incorreto - DDD Inexistente!\033[37m")
        case 1:
            Verificação = True
    return Verificação

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Geradores, retornam as informações;

## Primeiro Nome;
def gerarPrimeiroNome():
    vogais = ["a","e","i","o","u",""]
    consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","y","w","z",""]
    nomeL = []
    nome = ""
    silabas = random.randint(1,5)

    for i in range(0,silabas):
        nomeL += random.choices(consoantes)
        nomeL += random.choices(vogais)

    nome =''.join(nomeL)
    nome = nome.capitalize()
    return nome

## Apenas um Sobrenome;
def gerarSobrenome():
    sobrenomeL = ["Phareman","Boschetti","Scariot","Thybaut","Gautzelin","Godfree","Girardus","Gerould","Gualterius","Gocelinus","Urhan","Ugovras","Azadium","Chavez","Olzoxon","Da Silva","Santos","Nubis","Skullblood","Geimadra"]
    sobrenome = random.choices(sobrenomeL)
    sobrenome = ''.join(sobrenome)
    
    return sobrenome

## Um Nome Completo, com Nome + Sobrenome;
def gerarNomeCompleto():
    PrimeiroNome = gerarPrimeiroNome()
    sobrenome = gerarSobrenome()

    nome = (f"{PrimeiroNome} {sobrenome}")
    
    return nome

## Token de Segurança Aleatório;
def gerarTokens():
    vogais = ["a","e","i","o","u"]
    consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","y","w","z"]
    numeros = ["1","2","3","4","5","6","7","8","9"]
    outros = ["@","!","&","/","?","_"]
    tokenL = []
    token = ""

    for i in range(1,10):
        valor = random.randint(1,3)
        match valor:
            case 1:
                tokenL += random.choices(vogais)
            case 2:
                tokenL += random.choices(consoantes)
            case 3:
                tokenL += random.choices(numeros)
            case 4:
                tokenL += random.choices(outros)

    token =''.join(tokenL)
    return token

## Gera apenas CPF Válidos;
def gerarCPF():
    Verificação = False
    while not Verificação:
        ## Declarando Váriaveis;
        cpf1 = []
        ## Criação de CPF;
        for i in range (1,12):
            i = random.randint(0,9)
            i = str(i)
            cpf1.append(i)
        cpf = "".join(cpf1)
        os.system("cls")
        Verificação = verificarCPF(cpf)
    print(cpf)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Diversor, retornam uma ou mais informações;

## Colorindo
def coresTerminal(Estilo,Cor,Fundo):
    match Estilo:
        case 0:
            estilo = "0" ## Padrão
        case 1:
            estilo = "1" ## Negrito
        case 2:
            estilo = "4" ## Sublinhado 
        case 3:
            estilo = "7" ## Negativo
    match Cor:
        case 0:
            cor = "37" ## Padrão
        case 1:
            cor = "30" ## Cinza
        case 2:
            cor = "31" ## Vermelho
        case 3:
            cor = "32" ## Verde
        case 4:
            cor = "33" ## Amarelo
        case 5:
            cor = "34" ## Roxo
        case 6:
            cor = "35" ## Rosa
        case 7:
            cor = "36" ## Azul
    match Fundo:
        case 0:
            fundo = "40" ## Padrão
        case 1:
            fundo = "47" ## Cinza
        case 2:
            fundo = "41" ## Vermelho
        case 3:
            fundo = "42" ## Verde
        case 4:
            fundo = "43" ## Amarelo
        case 5:
            fundo = "44" ## Roxo
        case 6:
            fundo = "45" ## Rosa
        case 7:
            fundo = "46" ## Azul
    base = "\033[0;37;40m"
    padrão = (f"\033[{estilo};{cor};{fundo}m")

    return padrão,base