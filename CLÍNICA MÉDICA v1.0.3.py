#Sistema de gerenciamento para uma clínica médica fictícia.

import datetime
import os

listaMedicos = []
listaPacientes = []
erroLogin = 0

# Função pra encaixar os horários em formato de hora;
# Serve também pra verificar se o input == hora válida.
def hora(entrada):  
    entrada = datetime.datetime.strptime(entrada, '%H:%M')
    entrada = str(entrada)
    entrada = entrada.split()
    entrada.pop(0)
    entrada = entrada[0]
    return entrada

#Spamma linhas vazias x50.
def novaTela():
    for i in range(50):
        print(" ")

#Transforma string, em formato de horas (ex.: 7:30), em um número inteiro (ex.: 730).
def converterHoras(hora):
    hora = hora.split(":")
    hora[0] = hora[0] + hora[1]
    hora = hora[0]
    hora = int(hora)
    return hora

#Cadastro dos médicos.
def cadastroMed():
    novaTela()
    medicos = [None] * 5
    print("======== LISTA DE CADASTRO ========")

    while True:
        nomePac = input("• Insira seu nome: ")
        nomePac = nomePac.split()
        if len(nomePac) < 2:
            print("-> Erro. Você não inseriu um nome válido! Tente novamente.\n")
            continue
        else:
            nomePac = ' '.join(nomePac)
            medicos[0] = nomePac
            break

    print(" ")
    print("• Selecione sua área de especialização:")
    print("\n'1' Clínico Geral;\n'2' Pediatra;\n'3' Ginecologista;\n'4' Cardiologista;\n'5' Ortopedista;\n'6' Fisioterapeuta;\n'7' Gastroenterologista.\n")
    while True:
        medicos[1] = input("")
        if medicos[1] == "1":
            medicos[1] = "Clínico Geral"
            break
        elif medicos[1] == "2":
            medicos[1] = "Pediatra"
            break
        elif medicos[1] == "3":
            medicos[1] = "Ginecologista"
            break
        elif medicos[1] == "4":
            medicos[1] = "Cardiologista"
            break
        elif medicos[1] == "5":
            medicos[1] = "Ortopedista"
            break
        elif medicos[1] == "6":
            medicos[1] = "Fisioterapeuta"
            break
        elif medicos[1] == "7":
            medicos[1] = "Gastroenterologista"
            break
        else:
            print("-> Erro. Você não selecionou uma especialização válida! Tente novamente.\n")
            continue

    print("\n• Insira seu horário de atendimento:\n")
    while True:
        entrada = input("DEFINA SEU HORÁRIO DE ENTRADA (ex.: 7:30)\n")
        try:
            hora(entrada)
            
            # Isso aqui adiciona um 0 a mais no final, no caso de, quando der input na hora, o usuário só digitar '12:0' ou '14:3'.
            testeEntrada = entrada.split(":")
            if len(testeEntrada[1]) == 1:
                testeEntrada[1] = testeEntrada[1] + "0"
            entrada = testeEntrada[0]+":"+testeEntrada[1]

            medicos[2] = entrada
            break
        except ValueError:
            print("-> Erro. Você não inseriu uma hora válida; utilize o formato de 24 horas! Tente novamente.\n")
            continue

    while True:
        entrada = input("DEFINA SEU HORÁRIO DE SAÍDA (ex.: 18:30)\n")
        try:
            hora(entrada)

            testeEntrada = entrada.split(":")
            if len(testeEntrada[1]) == 1:
                testeEntrada[1] = testeEntrada[1] + "0"
            entrada = testeEntrada[0]+":"+testeEntrada[1]

            #Vai transformar, por exemplo, 7:30 em 730
            horaSaida = converterHoras(entrada)           
            horaEntrada = converterHoras(medicos[2])

            if horaSaida < horaEntrada or horaSaida == horaEntrada:
                print("-> Erro. Você não pode definir um horário de saída inferior/igual ao de entrada! Tente novamente.\n")
                continue
            else:
                medicos[3] = entrada
                break
        except ValueError:
            print("-> Erro. Você não inseriu uma hora válida; utilize o formato de 24 horas! Tente novamente.\n")
            continue
    while True:
        ocupado = 0
        if medicos[4] == None:
            sala = input("\n• Defina sua sala de atendimento:\n")
            if sala == "":
                print("-> Erro. Você não inseriu um número válido para sua sala! Tente novamente.")
                continue
            else:
                try:
                    sala = int(sala)
                    if sala <= 0:
                        print("-> Erro. Você não inseriu um número válido para sua sala! Tente novamente.\n")
                        continue
                    else:
                        if len(listaMedicos) > 0:
                            for aaa in range(len(listaMedicos)):
                                if sala == int(listaMedicos[aaa][4]):
                                    HORA1 = converterHoras(medicos[2])
                                    HORA2 = converterHoras(medicos[3])
                                    HORA3 = converterHoras(listaMedicos[aaa][2])
                                    HORA4 = converterHoras(listaMedicos[aaa][3])

                                    if (HORA1 >= HORA3 and HORA2 <= HORA4) or ((HORA1 >= HORA3 and HORA1 <= HORA4) and HORA2 >= HORA3) or ((HORA2 <= HORA4 and HORA2 >= HORA3) and HORA1 <= HORA3):
                                        print("-> Erro. Esta sala não está disponível! Tente novamente.")
                                        ocupado = 1
                                    #Eu não faço ideia do porque eu tive que fazer assim. Antes eu tinha um *continue*
                                    #nesse if de cima, e ali no if de baixo a ação medicos[4] = sala tava solta.
                                    #
                                    #A ideia era que, se chegasse no HORA1 >= HORA3 and HORA2 <= HORA4, o *continue* faria
                                    #o código voltar pro inicio do loop, e só caso não batesse na condicional,
                                    #chegasse no medicos[4] = sala. Mas isso não funcionava, então rip usei mais uma
                                    #variável. *BRUH*
                            if ocupado != 1:
                                medicos[4] = sala
                                break
                        else:
                            medicos[4] = sala
                            break
                except ValueError:
                    print("-> Erro. Sua sala precisa ser um número! Tente novamente.")
                    continue
        else:
            break 

    listaMedicos.append(medicos)
    arqv = open("Medicos Registrados.txt", "a")
    for element in medicos:
        print(element, file=arqv)
    arqv.close()
    novaTela()

#Deletar cadastro de médicos.
def deletarMed():
    if not listaMedicos:
        novaTela()
        print("==================================================\n")
        print("• Nenhum médico registrado. Não há o que deletar, *duh*.\n")
        opc = input("-> Pressione 'Enter' para retornar.\n")
        novaTela()
        retorno = ""
    else:
        retorno2 = "1"
        while True:
            if retorno2 != "":
                novaTela()
                contador = 0
                print("==================================================")
                print("• Pressione 'Enter' para cancelar.\n")
                for c in range(len(listaMedicos)):
                    print("'",c+1,"'  ",listaMedicos[c])
                    contador = contador + 1

                deletar = input("\n• Selecione qual você deseja deletar:\n")
                if deletar == "":
                    novaTela()
                    retorno2 == ""
                    break
                else:
                    try:
                        deletar = int(deletar)
                        if deletar > contador or deletar < 0:
                            print("-> Erro. Você não selecionou uma opção válida! Tente novamente.\n")
                        else:
                            confirmar = input("Você tem certeza que deseja deletar este médico do registro?\n   '1' SIM        '2' NÃO\n")
                            if confirmar == "1":
                                del listaMedicos[int(deletar)-1]

                                with open('Medicos Registrados.txt', 'w') as arqv:
                                    for row in listaMedicos:
                                        for item in row:
                                            arqv.write("%s\n" %item)  
                                arqv.close()

                                novaTela()
                                retorno2 = ""
                    except ValueError:
                        print("-> Erro. Você não selecionou um médico válido para deletar! Tente novamente.")
                
            else:
                break

#Registro dos médicos, pra saber quem faz o que e em qual horário.
def med():
    retorno = "0"
    while True:
        if retorno != "":
            novaTela()
            while True:
                if not listaMedicos:
                    print("==================================================")
                    print("-> Nenhum médico registrado!")
                else:
                    print("==================================================")
                    for c in range(len(listaMedicos)):
                        print("Médico:",'{:15}'.format(listaMedicos[c][0])," Especialização:",'{:20}'.format(listaMedicos[c][1])," Hora de entrada:",'{:7}'.format(listaMedicos[c][2])," Hora de saída:",'{:7}'.format(listaMedicos[c][3])," Sala:",listaMedicos[c][4])

                print("\n==================================================")
                retorno = input("• Pressione 'Enter' para retornar;\n\n• Digite '1' para cadastrar novo médico;\n• Digite '2' para deletar um médico.\n")
                if retorno == "":
                    novaTela()
                    break
                elif retorno == "1":
                    cadastroMed()
                elif retorno == "2":
                    deletarMed()
                else:
                    print("-> Erro. Você selecionou uma opção inválida! Tente novamente.\n")
        else:
            break

#Registro dos pacientes, pra saber quem tem hora marcada quando e com quem.
def cadastroPac():
    novaTela()
    pacientes = [None] * 4
    print("======== LISTA DE CADASTRO ========")

    while True:
        nomePac = input("• Insira seu nome: ")
        nomePac = nomePac.split()
        if len(nomePac) < 2:
            print("-> Erro. Você não inseriu um nome válido! Tente novamente.\n")
            continue
        else:
            nomePac = ' '.join(nomePac)
            pacientes[0] = nomePac
            break
    while True:
        pacientes[1] = input("\n• Insira seu número de telefone: ")
        try:
            pacientes[1] = int(pacientes[1])
            if len(str(pacientes[1])) <= 10 or len(str(pacientes[1])) > 11:
                print("-> Erro. Você não inseriu um número válido! Tente novamente.")
            else:    
                break
        except ValueError:
            print("-> Erro. Você não inseriu um número válido! Tente novamente.")
            continue

    print("\n• Selecione o médico especializado que você necessita:\n")
    while True:
        contador = 0
        for h in range(len(listaMedicos)):
            print("'",h+1,"'  ",listaMedicos[h][1]," -  Dr(a).",listaMedicos[h][0],"\n")
            contador = contador + 1
        while True:
            pacientes[2] = input("")
            try:
                pacientes[2] = int(pacientes[2])
                if int(pacientes[2]) < 0 or int(pacientes[2]) > contador:
                    print("-> Erro. Você não selecionou um médico disponível! Tente novamente.")
                    continue
                else:
                    break
            except ValueError:
                print("-> Erro. Você não selecionou um médico disponível! Tente novamente.")
                continue
        break

    while True:
        diasAteConsulta = input("\n• Para daqui quantos dias você deseja marcar sua consulta: ")
        try:
            diasAteConsulta = int(diasAteConsulta)
            if diasAteConsulta <= 0:
                print("-> Erro. Você não pode marcar uma consulta para este dia! Tente novamente.")
                continue
            else:
                break
        except ValueError:
            print("-> Erro. Você não inseriu um número válido! Tente novamente.")

    medicoEscolhido = int(pacientes[2])-1
    print("\n• O",listaMedicos[medicoEscolhido][1],"está disponível entre",listaMedicos[medicoEscolhido][2],"e",listaMedicos[medicoEscolhido][3])
    while True:
        entrada = input("Para qual horário você deseja sua consulta? (ex.: 7:30)\n")            
        try:
            hora(entrada)

            testeEntrada = entrada.split(":")
            if len(testeEntrada[1]) == 1:
                testeEntrada[1] = testeEntrada[1] + "0"
            entrada = testeEntrada[0]+":"+testeEntrada[1]

            horaPaciente = converterHoras(entrada)

            horaMinMedico = converterHoras(listaMedicos[medicoEscolhido][2])
            horaMaxMedico = converterHoras(listaMedicos[medicoEscolhido][3])

            if horaPaciente < horaMinMedico or horaPaciente > horaMaxMedico:
                print("-> Erro. O",listaMedicos[medicoEscolhido][1],"não está disponível para este horário! Tente novamente.\n")
                continue
            else:
                pacientes[3] = entrada
            break
        except ValueError:
            print("-> Erro. Você não inseriu uma hora válida! Tente novamente.\n")
            continue

    pacientes[2] = listaMedicos[medicoEscolhido][1]

    #Vai transformar em data completa, ex.: '2019-10-16 09:00:00'
    dataIncompleta = str(pacientes[3])
    dataIncompleta = hora(dataIncompleta)

    dataCompleta = date.today()
    dataCompleta += datetime.timedelta(days=int(diasAteConsulta))
    dataCompleta = str(dataCompleta)
    dataCompleta = dataCompleta + " " + dataIncompleta

    pacientes[3] = dataCompleta 

    novaTela()
    print("==================================================\n")
    print("• Consulta agendada com sucesso!\n  PACIENTE:",pacientes[0],"\n  MÉDICO:",pacientes[2],"\n  DATA:",pacientes[3],"\n  CONSULTÓRIO:",listaMedicos[medicoEscolhido][4],"\n")

    listaPacientes.append(pacientes)
    arqv = open("Pacientes Registrados.txt", "a")
    for element in pacientes:
        print(element, file=arqv)
    arqv.close()

    opc = input("-> Pressione 'Enter' para retornar.\n")
    if opc == "":
        novaTela()
    else:
        novaTela()

#Deletar consultas de pacientes.
def deletarPac():
    if not listaPacientes:
        novaTela()
        print("==================================================\n")
        print("• Nenhuma consulta registrada. Não há o que deletar, *duh*.\n")
        opc = input("-> Pressione 'Enter' para retornar.\n")
        if opc == "":
            novaTela()
            retorno = ""
        else:
            novaTela()
            retorno = ""
    else:
        retorno2 = "1"
        while True:
            if retorno2 != "":
                novaTela()
                contador = 0
                print("==================================================")
                print("• Pressione 'Enter' para cancelar.\n")
                for c in range(len(listaPacientes)):
                    print("'",c+1,"'  ",listaPacientes[c])
                    contador = contador + 1
                deletar = input("\n• Selecione qual você deseja deletar:\n")
                try:
                    deletar = int(deletar)
                    if deletar == "":
                        novaTela()
                        break
                    else:
                        if deletar > contador or deletar < 0:
                            print("-> Erro. Você não selecionou uma opção válida! Tente novamente.\n")
                        else:
                            confirmar = input("Você tem certeza que deseja deletar esta consulta do registro?\n   '1' SIM        '2' NÃO\n")
                            if confirmar == "1":
                                del listaPacientes[int(deletar)-1]

                                with open('Pacientes Registrados.txt', 'w') as arqv:
                                    for row in listaPacientes:
                                        for item in row:
                                            arqv.write("%s\n" %item)  
                                arqv.close()
                            
                                novaTela()
                                retorno2 = ""
                            else:
                                print("")
                except ValueError:
                    print("-> Erro. Você não selecionou uma consulta válida para deletar! Tente novamente.")               
            else:
                break

#Registro dos pacientes, pra saber quem tem consulta marcada.
def pac():
    retorno = "0"
    while True:
        if retorno != "":
            novaTela()
            while True:
                if not listaMedicos:
                    print("==================================================\n")
                    print("• Consultas indisponíveis por falta de médico!\n")
                    opc = input("-> Pressione 'Enter' para retornar.\n")
                    if opc == "":
                        novaTela()
                        retorno = ""
                        break
                    else:
                        novaTela()
                        retorno = ""
                        break
                else:
                    print("==================================================")
                    if not listaPacientes:
                        print("-> Nenhum paciente com hora marcada!")
                    else:
                        for c in range(len(listaPacientes)):
                            print("Paciente:",'{:15}'.format(listaPacientes[c][0])," Telefone:",listaPacientes[c][1],"   Médico:",'{:20}'.format(listaPacientes[c][2])," Data marcada:",listaPacientes[c][3])

                    print("\n==================================================")
                    retorno = input("• Pressione 'Enter' para retornar;\n• Digite '1' para cadastrar uma consulta;\n• Digite '2' para cancelar uma consulta.\n")
                    if retorno == "":
                        novaTela()
                        break
                    elif retorno == "1":
                        cadastroPac()
                    elif retorno == "2":
                        deletarPac()
                    else:
                        print("-> Erro. Você selecionou uma opção inválida! Tente novamente.\n")
        else:
            break

#Vai abrir os .txt e retirar o que tá lá.
def lerArquivoTxt():
    if os.path.exists("Medicos Registrados.txt"):
        txt = []
        contadorTxt = 0
        #Vai ler linha-por-linha do .txt
        with open("Medicos Registrados.txt", "r") as inputfile:
            for line in inputfile:
                txt.append(line)
        #Como cada linha pula pra outra, a string fica com "\n"
        #Daí isso daqui é pra retirar o \n de cada elemento.
        txt = [s.replace('\n', '') for s in txt]
        #Vai fazer um loop por todos os elementos importados do .txt
        for e in range(int(len(txt)/5)):
            txtTemp = [None] * 5
            txtTemp[0] = txt[0+contadorTxt]
            txtTemp[1] = txt[1+contadorTxt]
            txtTemp[2] = txt[2+contadorTxt]
            txtTemp[3] = txt[3+contadorTxt]
            txtTemp[4] = txt[4+contadorTxt]
            contadorTxt = contadorTxt + 5
            listaMedicos.append(txtTemp)
        inputfile.close()

    if os.path.exists("Pacientes Registrados.txt"):
        txt = []
        contadorTxt = 0
        with open("Pacientes Registrados.txt", "r") as inputfile:
            for line in inputfile:
                txt.append(line)
        txt = [s.replace('\n', '') for s in txt]
        for e in range(int(len(txt)/4)):
            txtTemp = [None] * 4
            txtTemp[0] = txt[0+contadorTxt]
            txtTemp[1] = txt[1+contadorTxt]
            txtTemp[2] = txt[2+contadorTxt]
            txtTemp[3] = txt[3+contadorTxt]
            contadorTxt = contadorTxt + 4
            listaPacientes.append(txtTemp)
        inputfile.close()

while True:
    lerArquivoTxt()
    senhaMedicos = input("• Por favor, insira a senha para acessar o sistema: ")
    if senhaMedicos == "556691":
        erroLogin = 0
        novaTela()
        while True:
            retorno = "0"
            medOuPac = input("Bém-vindo(a), usuário(a). Você fez login com sucesso!\n\n• '1' Registro de Médicos;\n• '2' Registro de Pacientes.\n")
            if medOuPac == "":
                print("-> Erro. Você selecionou uma opção inválida! Tente novamente.\n\n")
                continue
            elif medOuPac == "1":
                med()
            elif medOuPac == "2":
                pac()
            else:
                print("-> Erro. Você selecionou uma opção inválida! Tente novamente.\n\n")
    else:
        if erroLogin < 2:
            print("-> Erro. A senha inserida está incorreta! Tente novamente. (",int(erroLogin)+1,"/ 3 )\n")
            erroLogin = erroLogin + 1
            continue
        else:
            print("-> Você errou a senha vezes demais!")
            exit()
