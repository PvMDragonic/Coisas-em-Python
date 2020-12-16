while True:
    while True:
        try:
            numero = float(input("Insira seu número: "))
            break
        except ValueError:
            print("Número inválido inserido!")
    while True:
        try:
            porcentagem = float(input("Insira qual a porcentagem desse número que deseja receber: "))
        except ValueError:
            print("Número inválido inserido!")
            continue
        if (porcentagem == 0):
            print("Zero não é um valor para porcentagem válido.")
            continue
        else:
            break

    resultado = (porcentagem * numero) / 100
    print("Seu resultado é: ", resultado, "\n\n\n")
