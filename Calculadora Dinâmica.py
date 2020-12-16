def verificarConta(ligma):
    # Essa parte vai, caso a conta seja escrita toda junta, tratar de separar ela.
    if len(ligma) == 1:
        # Vai separar a conta caractere-por-caractere
        ligma = list(ligma[0])
        for i in range(len(ligma)):
            if ligma[i] == "+":
                ligma[i] = " + "
            elif ligma[i] == "-":
                ligma[i] = " - "
            elif ligma[i] == "*":
                ligma[i] = " * "
            elif ligma[i] == "/":
                ligma[i] = " / "
            elif ligma[i] == "^":
                ligma[i] = " ^ "
        ligma = "".join(ligma)
        ligma = ligma.split()
    # Essa parte vai verificar se o input foi só uma única coisa, mas sem ser conta. Ex.: "asdasda", "55555"
    if len(ligma) > 1:
        verificarErros(ligma)
    else:
        # Caso venha pra cá, ele vai ver se o input único é num ou letra; se for num ele repete o input, senão mensagem de erro.
        try:
            ligma[0] = float(ligma[0])
            print("Sua resposta é: ",ligma[0])
        except Exception:
            print("Sua resposta é: calculo invalido!")

def verificarErros(ligma):
    # Essa parte vai verificar se, no lugar onde deveria ter um símbolo matemático, há um número.
    falha = 0
    for i in range(len(ligma)):
        if (i+1)%2 == 0: # Seleciona só os slots ímpares da array. Ex.: [5, -, 5] ele seleciona o -.
            try:
                ligma[i] = float(ligma[i]) # Caso não seja um número, ele vai travar aqui e puxar pro except ali embaixo.
                falha = falha + 1
            except ValueError:
                continue # Continue faz voltar pro inicio do Loop, onde ele avança pro próximo elemento.               
    if falha == 0:
        concatenarConta(ligma)
    else:
        print("Sua resposta é: calculo invalido!") 

def concatenarConta(ligma):
    try: # Esse try é pra ver se não tem não-números em posição que é pra ter números.
        while True: # Vai fazer todas as potenciações, que vem primeiro.
            if "^" in ligma:
                for i in range(len(ligma)):
                    if ligma[i] == "^":
                        ligma[i] = float(ligma[i-1]) ** float(ligma[i+1])
                        del ligma[i-1]
                        del ligma[i]
                        break
            else:
                break
        while True: # Vai fazer todos os calculos de divisão e multiplicação, que vem em seguida.
            if "/" in ligma or "*" in ligma:
                for i in range(len(ligma)):
                    if ligma[i] == "/":
                        ligma[i] = float(ligma[i-1]) / float(ligma[i+1])
                        del ligma[i-1]
                        del ligma[i]
                        break
                    elif ligma[i] == "*":
                        ligma[i] = float(ligma[i-1]) * float(ligma[i+1])
                        del ligma[i-1]
                        del ligma[i]
                        break
            else:
                break
        while True: # Quando acabarem as divs e mults, vai passar por todas as adições e subtrações.
            if "+" in ligma or "-" in ligma:
                for i in range(len(ligma)):
                    if ligma[i] == "+":
                        ligma[i] = float(ligma[i-1]) + float(ligma[i+1])
                        del ligma[i-1]
                        del ligma[i]
                        break
                    elif ligma[i] == "-":
                        ligma[i] = float(ligma[i-1]) - float(ligma[i+1])
                        del ligma[i-1]
                        del ligma[i]
                        break
            else:
                break
        print("Sua resposta é: ",ligma[0])
    except Exception:
        print("Sua resposta é: calculo invalido!")
            
print("===============================\n Bém-vindo(a) a Calculadora Tunada!\n\n Digite sua operação no seguinte formato:\n 5 + 5 - 2 / 2 * 5\n===============================")
while True:
    verificarConta(list(map(str, input("-> Insira sua conta: ").split())))