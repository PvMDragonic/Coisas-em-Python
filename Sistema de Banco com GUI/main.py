from GUI.Menus.menu_principal import MainMenu
from GUI.Menus.tipo_cadastrar import TipoCadastrar
from GUI.Menus.selecionar_conta import SelecionarConta
from GUI.Menus.cadastros_exibir import CadastrosExibir
from GUI.Menus.pedir_cpf import pedirCPF
from GUI.Mensagens.menssagem_cadastrado import MsgCadastrado
from GUI.Mensagens.menssagem_nao_cadastrado import MsgNaoCadastrado
from GUI.Mensagens.menssagem_sucesso import MsgSucesso
from GUI.Mensagens.menssagem_erro import MsgErro
from GUI.Cadastro.cliente_cadastro import ClienteCadastro
from GUI.Cadastro.corrente_cadastro import CorrenteCadastro
from GUI.Cadastro.especial_cadastro import EspecialCadastro
from GUI.Cadastro.poupanca_cadastro import PoupancaCadastro
from GUI.Exibicao.exibir_corrente import CorrenteExibir
from GUI.Exibicao.exibir_especial import EspecialExibir
from GUI.Exibicao.exibir_poupanca import PoupancaExibir

global continuar
continuar = False
clientesCadastrados = []
contasCorrentes = []
contasEspeciais = []
contasPoupanca = []

def cadastrarCliente():
    naoCadastrado = MsgNaoCadastrado()
    naoCadastrado.iniciar()
    cliente = ClienteCadastro()
    cliente.iniciar(cpf.inputCPF)
    if (cliente.sucessoCadastro == True):
        clientesCadastrados.append(cliente.novoCliente)
        msg = MsgSucesso()
        msg.iniciar()
        global continuar 
        continuar = True

def verificarClientes():
    global continuar 
    continuar = False
    clienteJaCadastrado = False
    if (len(clientesCadastrados) > 0): #Verifica se o CPF já existia no sistema
        for i in range(len(clientesCadastrados)):
            if (clientesCadastrados[i][1] == cpf.inputCPF):
                clienteJaCadastrado = True 
        if (clienteJaCadastrado == False):
            cadastrarCliente()
        else:
            cadastrado = MsgCadastrado()
            cadastrado.iniciar()
            continuar = True
    else:
        cadastrarCliente()

while True:
    menuPrincipal = MainMenu()
    menuPrincipal.iniciar()

    if (menuPrincipal.escolhaMenu == 1): #Escolheu 'Cadastrar' pra cadastrar novo cliente
        while True:
            tipoCadastro = TipoCadastrar()
            tipoCadastro.iniciar()

            if (tipoCadastro.escolhaMenu == 1): #Escolheu 'Corrente' pra nova conta corrente
                if (len(contasCorrentes) < 10):
                    cpf = pedirCPF()
                    cpf.iniciar()
                    if (cpf.inputCPF != None):
                        verificarClientes()
                        if (continuar == True): # Isso aqui é pra caso a pessoa clique 'Cancelar' na hora de cadastrar como cliente.
                            cadastrarCorrente = CorrenteCadastro()
                            cadastrarCorrente.iniciar()
                            if (cadastrarCorrente.sucessoCadastro == True):
                                contasCorrentes.append(cadastrarCorrente.novaCorrente)
                                msg = MsgSucesso()
                                msg.iniciarCorrente()
                    else:
                        continue
                else:
                    erro = MsgErro()
                    erro.maxContas("corrente")
                    continue

            elif (tipoCadastro.escolhaMenu == 2): #Escolheu 'Especial' pra nova conta especial
                if (len(contasEspeciais) < 10):
                    cpf = pedirCPF()
                    cpf.iniciar()
                    if (cpf.inputCPF != None):
                        verificarClientes()
                        if (continuar == True):
                            cadastrarEspecial = EspecialCadastro()
                            cadastrarEspecial.iniciar()
                            if (cadastrarEspecial.sucessoCadastro == True):
                                contasEspeciais.append(cadastrarEspecial.novaEspecial)
                                msg = MsgSucesso()
                                msg.iniciarEspecial()
                    else:
                        continue
                else:
                    erro = MsgErro()
                    erro.maxContas("especial")
                    continue

            elif (tipoCadastro.escolhaMenu == 3): #Escolheu 'Poupanca' pra nova conta poupança
                if (len(contasPoupanca) < 10):
                    cpf = pedirCPF()
                    cpf.iniciar()
                    if (cpf.inputCPF != None):
                        verificarClientes()
                        if (continuar == True):
                            cadastrarPoupanca = PoupancaCadastro()
                            cadastrarPoupanca.iniciar()
                            if (cadastrarPoupanca.sucessoCadastro == True):
                                contasPoupanca.append(cadastrarPoupanca.novaPoupanca)
                                msg = MsgSucesso()
                                msg.iniciarPoupanca()
                    else:
                        continue
                else:
                    erro = MsgErro()
                    erro.maxContas("poupança")
                    continue
            else:
                break

    elif (menuPrincipal.escolhaMenu == 2): #Escolheu 'Exibir' pra mostrar os cadastrados
        if (len(contasCorrentes) == 0 and len(contasEspeciais) == 0 and len(contasPoupanca) == 0):
            erro = MsgErro()
            erro.semContas()
        else:
            while True:
                qualExibir = CadastrosExibir()
                qualExibir.iniciar()

                if (qualExibir.escolhaMenu == 1): #Exibir conta 'Corrente' selecionada
                    if (len(contasCorrentes) == 0):
                        erro = MsgErro()
                        erro.semConta("corrente")
                    else: 
                        dropMenu = SelecionarConta()
                        dropMenu.iniciar(contasCorrentes, qualExibir.escolhaMenu)
                        if (dropMenu.passou == True):
                            corrente = CorrenteExibir()
                            corrente.iniciar(contasCorrentes[dropMenu.escolha][0], contasCorrentes[dropMenu.escolha][1], contasCorrentes[dropMenu.escolha][2], contasCorrentes[dropMenu.escolha][3], contasCorrentes[dropMenu.escolha][4])
                elif (qualExibir.escolhaMenu == 2): #Exibir conta 'Especial' selecionada
                    if (len(contasEspeciais) == 0):
                        erro = MsgErro()
                        erro.semConta("especial")
                    else:
                        dropMenu = SelecionarConta()
                        dropMenu.iniciar(contasEspeciais, qualExibir.escolhaMenu)
                        if (dropMenu.passou == True):
                            especial = EspecialExibir()
                            especial.iniciar(contasEspeciais[dropMenu.escolha][0], contasEspeciais[dropMenu.escolha][1], contasEspeciais[dropMenu.escolha][2], contasEspeciais[dropMenu.escolha][3], contasEspeciais[dropMenu.escolha][4], contasEspeciais[dropMenu.escolha][5], contasEspeciais[dropMenu.escolha][6])
                elif (qualExibir.escolhaMenu == 3): #Exibir conta 'Poupança' selecionada
                    if (len(contasPoupanca) == 0):
                        erro = MsgErro()
                        erro.semConta("poupanca")
                    else:
                        dropMenu = SelecionarConta()
                        dropMenu.iniciar(contasPoupanca, qualExibir.escolhaMenu)
                        if (dropMenu.passou == True):
                            poupanca = PoupancaExibir()
                            poupanca.iniciar(contasPoupanca[dropMenu.escolha][0], contasPoupanca[dropMenu.escolha][1], contasPoupanca[dropMenu.escolha][2], contasPoupanca[dropMenu.escolha][3], contasPoupanca[dropMenu.escolha][4], contasPoupanca[dropMenu.escolha][5], contasPoupanca[dropMenu.escolha][6])
                else:
                    break