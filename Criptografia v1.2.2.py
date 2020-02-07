'''
================================================================================================
Sistema de criptografia ponta-a-ponta utilizando servidores cloud.

Quando você executar o arquivo na primeira vez, um arquivo "Diretorio.txt" será criado.
Nele você deve guardar o path até a pasta do programava de núvem de sua escolha (ex.: Dropbox, Google Drive).
O programa permite conversas entre dois ou mais computadores (emprestando um servidor de terceiros porque eu não tenho dinheiro para um particular, lol). 
================================================================================================
'''

import random
import string
import os
import sched, time
from threading import Timer
from glob import glob

tempo = sched.scheduler(time.time, time.sleep)

#Vai spammar 50 linhas vazias. *duh*
def novaTela():
    for i in range(50):
        print(" ")

#Eu uso isso aqui pra que os arquivos criptografados tenham nomes pseudo-randômicos; pra dar um Q à mais.
def randomString(stringLength = 10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#Criptografa uma frase embaralhadno os caracteres
def criptografar(entrada):
    entrada = entrada.lower()
    #Separa por caractere. É tipo um .split(), mas esse separa por caractere.
    entrada = list(entrada)
    for i in range(len(entrada)):
        if entrada[i] == ' ':
            b = random.randint(1,3)
            if b == 1:
                entrada[i] = "p"
            elif b == 2:
                entrada[i] = "o"
            elif b == 3:
                entrada[i] = "s"
        elif entrada[i] == 'a':
            entrada[i] = "g"
        elif entrada[i] == 'b':
            entrada[i] = "k"
        elif entrada[i] == 'c':
            entrada[i] = "j"
        elif entrada[i] == 'ç':
            entrada[i] = "°"
        elif entrada[i] == 'd':
            entrada[i] = "4"
        elif entrada[i] == 'e':
            entrada[i] = "a"
        elif entrada[i] == 'f':
            entrada[i] = "/"
        elif entrada[i] == 'g':
            entrada[i] = "6"
        elif entrada[i] == 'h':
            entrada[i] = "w"
        elif entrada[i] == 'i':
            entrada[i] = " "
        elif entrada[i] == 'j':
            entrada[i] = "¢"
        elif entrada[i] == 'k':
            entrada[i] = "y"
        elif entrada[i] == 'l':
            entrada[i] = "x"
        elif entrada[i] == 'm':
            entrada[i] = "q"
        elif entrada[i] == 'n':
            entrada[i] = "5"
        elif entrada[i] == 'o':
            entrada[i] = "ç"
        elif entrada[i] == 'p':
            entrada[i] = "f"
        elif entrada[i] == 'q':
            entrada[i] = "7"
        elif entrada[i] == '!':
            entrada[i] = "?"
        elif entrada[i] == '?':
            entrada[i] = "!"
        elif entrada[i] == '.':
            entrada[i] = "i"
        elif entrada[i] == ';':
            entrada[i] = "+"
        elif entrada[i] == 'r':
            entrada[i] = "9"
        elif entrada[i] == 's':
            entrada[i] = "8"
        elif entrada[i] == 't':
            entrada[i] = "u"
        elif entrada[i] == 'u':
            entrada[i] = "*"
        elif entrada[i] == 'v':
            entrada[i] = "0"
        elif entrada[i] == 'w':
            entrada[i] = "n"
        elif entrada[i] == 'x':
            entrada[i] = "="
        elif entrada[i] == 'y':
            entrada[i] = "c"
        elif entrada[i] == 'z':
            entrada[i] = "1"
        elif entrada[i] == '0':
            entrada[i] = "%"
        elif entrada[i] == '1':
            entrada[i] = "#"
        elif entrada[i] == '2':
            entrada[i] = "@"
        elif entrada[i] == '3':
            entrada[i] = "&"
        elif entrada[i] == '4':
            entrada[i] = "£"
        elif entrada[i] == '5':
            entrada[i] = ","
        elif entrada[i] == '6':
            entrada[i] = "§"
        elif entrada[i] == '7':
            entrada[i] = "3"
        elif entrada[i] == '8':
            entrada[i] = "2"
        elif entrada[i] == '9':
            entrada[i] = "_"
        elif entrada[i] == ':':
            entrada[i] = "-"
        elif entrada[i] == 'º':
            entrada[i] = ">"
        elif entrada[i] == 'ª':
            entrada[i] = "¬"
        elif entrada[i] == '_':
            entrada[i] = "¹"
        elif entrada[i] == '@':
            entrada[i] = "²"
        elif entrada[i] == ',':
            entrada[i] = "["

    #Rejunta todos os caracteres em um elemento só.
    entrada = ''.join(map(str, entrada))
    #Retorna a variável com a frase criptografada.
    return entrada

#Descriptografa mensagens, revertendo pra coisas legíveis.
def descriptografarParte2(entrada):
    for i in range(len(entrada)):
        if entrada[i] == 'p':
            entrada[i] = " "
        elif entrada[i] == 'o':
            entrada[i] = " "
        elif entrada[i] == 's':
            entrada[i] = " "
        elif entrada[i] == 'g':
            entrada[i] = "a"
        elif entrada[i] == 'k':
            entrada[i] = "b"
        elif entrada[i] == 'j':
            entrada[i] = "c"
        elif entrada[i] == '°':
            entrada[i] = "ç"
        elif entrada[i] == '4':
            entrada[i] = "d"
        elif entrada[i] == 'a':
            entrada[i] = "e"
        elif entrada[i] == '/':
            entrada[i] = "f"
        elif entrada[i] == '6':
            entrada[i] = "g"
        elif entrada[i] == 'w':
            entrada[i] = "h"
        elif entrada[i] == ' ':
            entrada[i] = "i"
        elif entrada[i] == '¢':
            entrada[i] = "j"
        elif entrada[i] == 'y':
            entrada[i] = "k"
        elif entrada[i] == 'x':
            entrada[i] = "l"
        elif entrada[i] == 'q':
            entrada[i] = "m"
        elif entrada[i] == '5':
            entrada[i] = "n"
        elif entrada[i] == 'ç':
            entrada[i] = "o"
        elif entrada[i] == 'f':
            entrada[i] = "p"
        elif entrada[i] == '7':
            entrada[i] = "q"
        elif entrada[i] == '?':
            entrada[i] = "!"
        elif entrada[i] == '!':
            entrada[i] = "?"
        elif entrada[i] == 'i':
            entrada[i] = "."
        elif entrada[i] == '+':
            entrada[i] = ";"
        elif entrada[i] == '9':
            entrada[i] = "r"
        elif entrada[i] == '8':
            entrada[i] = "s"
        elif entrada[i] == 'u':
            entrada[i] = "t"
        elif entrada[i] == '*':
            entrada[i] = "u"
        elif entrada[i] == '0':
            entrada[i] = "v"
        elif entrada[i] == 'n':
            entrada[i] = "w"
        elif entrada[i] == '=':
            entrada[i] = "x"
        elif entrada[i] == 'c':
            entrada[i] = "y"
        elif entrada[i] == '1':
            entrada[i] = "z"
        elif entrada[i] == '%':
            entrada[i] = "0"
        elif entrada[i] == '#':
            entrada[i] = "1"
        elif entrada[i] == '@':
            entrada[i] = "2"
        elif entrada[i] == '&':
            entrada[i] = "3"
        elif entrada[i] == '£':
            entrada[i] = "4"
        elif entrada[i] == ',':
            entrada[i] = "5"
        elif entrada[i] == '§':
            entrada[i] = "6"
        elif entrada[i] == '3':
            entrada[i] = "7"
        elif entrada[i] == '2':
            entrada[i] = "8"
        elif entrada[i] == '_':
            entrada[i] = "9"
        elif entrada[i] == '-':
            entrada[i] = ":"
        elif entrada[i] == '>':
            entrada[i] = "º"
        elif entrada[i] == '¬':
            entrada[i] = "ª"
        elif entrada[i] == '¹':
            entrada[i] = "_"
        elif entrada[i] == '²':
            entrada[i] = "@"
        elif entrada[i] == '[':
            entrada[i] = ","

    entrada = ''.join(map(str, entrada))
    return entrada

def descriptografarParte1():
    try:
        #Esse try é pra ver se existe um arquivo m*.txt
        nomeArqv = glob("m*.txt")[0]
        if os.path.exists(nomeArqv):
            #Vai abrir o arquivo em modo read-only
            arqv = open(nomeArqv, "r")

            #Vai ler o que tem lá, transformar em minúsculo e separar por caractére.
            frase = arqv.read()
            frase = frase.lower()
            frase = list(frase)
            #Vai verificar se a frase criptografada foi feita ou não pelo usuário.
            if frase[0] == str(usuario):
                print("-> Nenhum arquivo para ser lido.\n")
                while True:
                    x = input("\nDigite '1' para tentar novamente;\nPressione 'Enter' para continuar.\n")
                    if x == "1":
                        novaTela()
                        procurarArqv()
                    else:
                        break
            else:
                if int(frase[2]) == int(usuario) or int(frase[2]) == 0:
                    #Deleta informação inútil da string.
                    del frase[0]
                    del frase[1]
                    x = descriptografarParte2(frase)
                    x = x.split()
                    #O split separou a mensagem descriptografada em espaços, então o elemento
                    #0 é o nome, e o resto a mensagem em sí.
                    remetente = x[0]
                    del x[0]
                    #Ele vai dar join no resto dos elementos, pondo um espaço vazio entre eles.
                    mensagem = ' '.join(map(str, x)) 

                    print("\n=====================================================")
                    print("-> Sua frase foi descriptografada com sucesso:\n\nRemetente:",remetente,"\nMensagem:",mensagem)
                    print("\n=====================================================")

                    arqv.close()
                    nomeArqv = glob("m*.txt")[0]
                    #Ele vai deletar esse arquivo que foi lido.
                    os.remove(nomeArqv)
                    x = input("\n-> Esta mensagem não pode mais ser lida.\nPressione 'Enter' para continuar.")
                else:
                    print("-> Nenhum arquivo para ser lido.\n")
                    while True:
                        x = input("\nDigite '1' para tentar novamente;\nPressione 'Enter' para continuar.\n")
                        if x == "1":
                            novaTela()
                            procurarArqv()
                        else:
                            break   
    except Exception:
        novaTela()
        print("-> Nenhum arquivo para ser lido.\n")

def procurarArqv():
    while True:
        print("-> Nenhum arquivo para ser lido.\n")
        print("\nProcurando...")
        #Função que vai executar descriptografarParte1 a cada 20s
        tempo.enter(20, 1, descriptografarParte1, ())
        tempo.run()
        x = input("\nDigite '1' para tentar novamente;\nPressione 'Enter' para continuar.\n")
        if x == "1":
            novaTela()
            continue
        else:
            break

def listarUsuarios():
    for file in glob("*usuario.txt"):
        #Var arqv pega tudo o que tem dentro do .txt
        arqv = open(file)
        nomeUsuario = arqv.read()
        nomeUsuario = list(nomeUsuario)
        #Até aqui, o list separou tudo por caractere.
        IDUsuario = nomeUsuario[0]
        del nomeUsuario[0]
        #Eu deleto o primeiro elemento, que é o número de ID do usuário.
        nomeUsuario = descriptografarParte2(nomeUsuario)
        #Depois eu quebro a criptografia do resto, e por fim deleto de novo
        #o elemento 0 porque ele ficou como " ", que na criptografia vira um "i".
        nomeUsuario = list(nomeUsuario)
        del nomeUsuario[0]
        nomeUsuario = ''.join(map(str, nomeUsuario))
        print("ID:",IDUsuario,"   Nome:",nomeUsuario)

#=========================================================================================
# Processo de configuração inicial do programa.
if os.path.exists("Diretorio.txt"):
    with open("Diretorio.txt", "r") as diretorio:
        caminho = diretorio.read()
        if caminho == "":
            novaTela()
            print("===========================================\n")
            print("• Copie e cole o caminho para a pasta raíz do Dropbox no seguinte arquivo:\n   Diretorio.txt")
            print("-> Ex.: C:\Program Files\Dropbox")
            x = input("\nPressione 'Enter' para continuar.")
            exit()
        else:
            try:
                os.chdir(caminho)
            except Exception:
                print("-> Erro. Você não inseriu um caminho válido!")
                x = input("\nPressione 'Enter' para continuar.")
                exit()
else:
    diretorio = open("Diretorio.txt", "w")
    novaTela()
    print("===========================================\n")
    print("• Copie e cole o caminho para a pasta raíz do Dropbox no seguinte arquivo:\n   Diretorio.txt")
    print("-> Ex.: C:\Program Files\Dropbox")
    x = input("\nPressione 'Enter' para continuar.")
    exit()

#=========================================================================================
# Registro de usuário no sistema.
novaTela()
while True:
    usuarioFail = 0
    usuario = input("• Defina seu ID de usuário (1-9): ")
    try:
        usuario = int(usuario)
        #Limitei a single-digit pra não "bugar" um negócio em outra parte do código.
        #Anyway, não é como se esse código fosse ser usado por mais de 10 pessoas simultaneamente mesmo lol.
        if usuario < 1 or usuario > 9:
            print("-> Insira um número entre 1 e 9!\n")
            continue
        else:
            for file in glob("*usuario.txt"):
                arqv = open(file, 'r')
                arqv2 = arqv.read()
                arqv2 = arqv2.split()
                if int(arqv2[0]) == int(usuario):
                    usuarioFail = 1
            if usuarioFail == 1:
                print("-> Este usuario já está ocupado!\n")
                continue
            else:
                print("\nPressione 'Enter' para retornar.")
                usuarioNome = input("• Defina seu nome de usuário: ")
                if usuarioNome == "":
                    novaTela()
                    continue
                else:
                    #Aqui se transforma o nome em um só bloco, sem espaços, pra não dar erro lá na frente.
                    usuarioNome = usuarioNome.replace(" ","_")
                    arqvUsuario = open(str(usuario) + "usuario.txt", "w")
                    print(str(usuario),criptografar(usuarioNome), file=arqvUsuario)
                    arqvUsuario.close()
                    break
    except ValueError:
        print("-> Insira um número válido!\n")

#=========================================================================================
# O programa em sí; o menu principal, após as duas etapas acima.    
while True:
    novaTela()
    opc = input("\n===SELECIONE SUA OPÇÃO===\n\n-> '1' Listar usuários na rede;\n-> '2' Criptografar;\n-> '3' Descriptografar.\n")
    try:
        opc = int(opc)
        if opc == 1:
            novaTela()
            print("=====================================================\n • Lista de usuários no sistema:\n")
            listarUsuarios()
            x = input("\nPressione 'Enter' para continuar.")
        elif opc == 2: #Criptografar mensagens.
            while True:
                novaTela()
                print("-> Para qual ID você enviar esta mensagem?\n\n Digite '0' para mensagem pública;\n Pressione 'Enter' para cancelar.\n")
                listarUsuarios()
                destinatario = input("")
                if destinatario == "":
                    break
                elif int(destinatario) > 9 or int(destinatario) < 0:
                    print("-> Selecione um ID válido, de 1 à 9!")
                    continue
                else:
                    if int(destinatario) == int(usuario):
                        print("-> Você não pode enviar uma mensagem para sí mesmo!")
                        x = input("\nPressione 'Enter' para continuar.")
                        continue
                    else:
                        novaTela()
                        while True:
                            msg = criptografar(input("-> Insira sua frase à ser criptografada:\n"))
                            if len(msg) > 128:
                                print("-> Erro. Suja mensagem deve ser igual ou inferior à 128 caracteres!\n")
                                continue
                            else:
                                arqv = open("m" + randomString(30) + ".txt", "w")
                                arqv.write(str(usuario) + "p" + destinatario + "p" + criptografar(usuarioNome) + "p" + msg)
                                arqv.close()
                                print("\n=====================================================\n-> Sua frase foi criptografada com sucesso!")
                                x = input("\nPressione 'Enter' para continuar.")
                                break
                        break    
        elif opc == 3: #Verificar se há mensagens para serem lidas.
            novaTela()
            try:
                nomeArqv = glob("m*.txt")[0]
                if os.path.exists(nomeArqv):
                    descriptografarParte1()
                else:
                    procurarArqv()   
            except Exception:
                procurarArqv()            
        else:
            print("-> Opção inválida! Tente novamente.")
    except ValueError:
        print("-> Opção inválida! Tente novamente.")
        continue
