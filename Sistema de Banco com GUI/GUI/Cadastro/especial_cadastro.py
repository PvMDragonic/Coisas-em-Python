import sys
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from GUI.Mensagens.menssagem_erro import MsgErro

class EspecialCadastro:
    def __init__(self):
        global root
        root = tk.Tk()
        self.sucessoCadastro = False

        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        X = int(root.winfo_screenwidth()/2 - windowWidth/2)
        Y = int(root.winfo_screenheight()/3 - windowHeight/2)
        X = int(X * 0.9)
        Y = int(Y * 0.9)

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

        root.geometry("516x386+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(3844, 1061)
        root.resizable(1, 1)
        root.title("Nova Conta Especial")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.019, rely=0.026, relheight=0.935, relwidth=0.959)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.Titulo = ttk.Label(self.TFrame1)
        self.Titulo.place(relx=0.081, rely=0.03, height=32, width=416)
        self.Titulo.configure(background="#d9d9d9")
        self.Titulo.configure(foreground="#000000")
        self.Titulo.configure(font="-family {Yu Mincho} -size 21 -slant italic")
        self.Titulo.configure(relief="flat")
        self.Titulo.configure(anchor='center')
        self.Titulo.configure(justify='left')
        self.Titulo.configure(text='''Cadastro conta especial''')
        self.Titulo.configure(compound='center')

        self.BotaoCancelar = ttk.Button(self.TFrame1, command=lambda: self.encerrar())
        self.BotaoCancelar.place(relx=0.566, rely=0.831, height=25, width=80)
        self.BotaoCancelar.configure(takefocus="")
        self.BotaoCancelar.configure(text='''Cancelar''')
        self.BotaoCancelar.configure(cursor="hand2")

        self.BotaoConfirmar = ttk.Button(self.TFrame1, command=lambda: self.pegarInputs(self.entryNome, self.entryDataAbertura, self.entryNumAgencia, self.entryNumConta, self.entrySaldo, self.entryLimite, self.entryTaxaJuros))
        self.BotaoConfirmar.place(relx=0.263, rely=0.831, height=28, width=80)
        self.BotaoConfirmar.configure(takefocus="")
        self.BotaoConfirmar.configure(text='''Confirmar''')
        self.BotaoConfirmar.configure(cursor="hand2")

        self.entryNome = ttk.Entry(self.TFrame1)
        self.entryNome.place(relx=0.303, rely=0.194, relheight=0.058, relwidth=0.598)
        self.entryNome.configure(takefocus="")
        self.entryNome.configure(cursor="ibeam")

        self.entryDataAbertura = ttk.Entry(self.TFrame1)
        self.entryDataAbertura.place(relx=0.303, rely=0.277, relheight=0.058, relwidth=0.598)
        self.entryDataAbertura.configure(takefocus="")
        self.entryDataAbertura.configure(cursor="ibeam")

        self.entryNumAgencia = ttk.Entry(self.TFrame1)
        self.entryNumAgencia.place(relx=0.303, rely=0.36, relheight=0.058, relwidth=0.598)
        self.entryNumAgencia.configure(takefocus="")
        self.entryNumAgencia.configure(cursor="ibeam")

        self.entryNumConta = ttk.Entry(self.TFrame1)
        self.entryNumConta.place(relx=0.303, rely=0.443, relheight=0.058, relwidth=0.598)
        self.entryNumConta.configure(takefocus="")
        self.entryNumConta.configure(cursor="ibeam")

        self.labelNome = ttk.Label(self.TFrame1)
        self.labelNome.place(relx=0.081, rely=0.194, height=21, width=96)
        self.labelNome.configure(background="#d9d9d9")
        self.labelNome.configure(foreground="#000000")
        self.labelNome.configure(font="TkDefaultFont")
        self.labelNome.configure(relief="flat")
        self.labelNome.configure(anchor='e')
        self.labelNome.configure(justify='left')
        self.labelNome.configure(text='''Nome do titular:''')

        self.labelDataAbertura = ttk.Label(self.TFrame1)
        self.labelDataAbertura.place(relx=0.081, rely=0.277, height=21, width=96)

        self.labelDataAbertura.configure(background="#d9d9d9")
        self.labelDataAbertura.configure(foreground="#000000")
        self.labelDataAbertura.configure(font="TkDefaultFont")
        self.labelDataAbertura.configure(relief="flat")
        self.labelDataAbertura.configure(anchor='e')
        self.labelDataAbertura.configure(justify='left')
        self.labelDataAbertura.configure(text='''Data de abertura:''')

        self.labelNumAgencia = ttk.Label(self.TFrame1)
        self.labelNumAgencia.place(relx=0.04, rely=0.36, height=21, width=116)
        self.labelNumAgencia.configure(background="#d9d9d9")
        self.labelNumAgencia.configure(foreground="#000000")
        self.labelNumAgencia.configure(font="TkDefaultFont")
        self.labelNumAgencia.configure(relief="flat")
        self.labelNumAgencia.configure(anchor='e')
        self.labelNumAgencia.configure(justify='left')
        self.labelNumAgencia.configure(text='''Número da agência:''')

        self.labelNumConta = ttk.Label(self.TFrame1)
        self.labelNumConta.place(relx=0.061, rely=0.443, height=21, width=106)
        self.labelNumConta.configure(background="#d9d9d9")
        self.labelNumConta.configure(foreground="#000000")
        self.labelNumConta.configure(font="TkDefaultFont")
        self.labelNumConta.configure(relief="flat")
        self.labelNumConta.configure(anchor='e')
        self.labelNumConta.configure(justify='left')
        self.labelNumConta.configure(text='''Número da conta:''')

        self.labelSaldo = ttk.Label(self.TFrame1)
        self.labelSaldo.place(relx=0.182, rely=0.526, height=21, width=46)
        self.labelSaldo.configure(background="#d9d9d9")
        self.labelSaldo.configure(foreground="#000000")
        self.labelSaldo.configure(font="TkDefaultFont")
        self.labelSaldo.configure(relief="flat")
        self.labelSaldo.configure(anchor='e')
        self.labelSaldo.configure(justify='left')
        self.labelSaldo.configure(text='''Saldo:''')

        self.entrySaldo = ttk.Entry(self.TFrame1)
        self.entrySaldo.place(relx=0.303, rely=0.526, relheight=0.058, relwidth=0.598)
        self.entrySaldo.configure(takefocus="")
        self.entrySaldo.configure(cursor="ibeam")

        self.labelLimiteSaque = ttk.Label(self.TFrame1)
        self.labelLimiteSaque.place(relx=0.081, rely=0.609, height=21, width=96)
        self.labelLimiteSaque.configure(background="#d9d9d9")
        self.labelLimiteSaque.configure(foreground="#000000")
        self.labelLimiteSaque.configure(font="TkDefaultFont")
        self.labelLimiteSaque.configure(relief="flat")
        self.labelLimiteSaque.configure(anchor='e')
        self.labelLimiteSaque.configure(justify='left')
        self.labelLimiteSaque.configure(text='''Limite de saque:''')

        self.entryLimite = ttk.Entry(self.TFrame1)
        self.entryLimite.place(relx=0.303, rely=0.609, relheight=0.058, relwidth=0.598)
        self.entryLimite.configure(takefocus="")
        self.entryLimite.configure(cursor="ibeam")

        self.entryTaxaJuros = ttk.Entry(self.TFrame1)
        self.entryTaxaJuros.place(relx=0.303, rely=0.693, relheight=0.058, relwidth=0.598)
        self.entryTaxaJuros.configure(takefocus="")
        self.entryTaxaJuros.configure(cursor="ibeam")

        self.labelTaxaJuros = ttk.Label(self.TFrame1)
        self.labelTaxaJuros.place(relx=0.081, rely=0.693, height=21, width=96)
        self.labelTaxaJuros.configure(background="#d9d9d9")
        self.labelTaxaJuros.configure(foreground="#000000")
        self.labelTaxaJuros.configure(font="TkDefaultFont")
        self.labelTaxaJuros.configure(relief="flat")
        self.labelTaxaJuros.configure(anchor='e')
        self.labelTaxaJuros.configure(justify='left')
        self.labelTaxaJuros.configure(text='''Taxa de juros:''')

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

    def pegarInputs(self, nome, data, numAgencia, numConta, saldo, limite, taxaJuros):
        self.sucessoCadastro = False
        erro = MsgErro()
        self.novaEspecial = []
        nome = nome.get()
        data = data.get()
        numAgencia = numAgencia.get()
        numConta = numConta.get()
        saldo = saldo.get()
        limite = limite.get()
        taxaJuros = taxaJuros.get()

        while True:
            if(nome == ""):
                erro.iniciarM("Nome")
                break

            if(data != ""):
                data = data.split("/")
                if(len(data) == 3): #Verifica se o usuário botou algo no formato de data, ou seja, 10/10/10.
                    try:
                        datetime.datetime(year=int(data[2]),month=int(data[1]),day=int(data[0])) #Verifica se cada um se adequa nos formatos do datetime
                        data = "/".join(data) #Rejunta tudo numa string de novo
                    except ValueError:
                        erro.iniciarF("Data de abertura")
                        break
                else:
                    erro.iniciarF("Data de abertura")
                    break
            else:
                erro.iniciarF("Data de abertura")
                break

            if(numAgencia == ""):
                erro.iniciarM("Número da agência")
                break
            else:
                try:
                    int(numAgencia)
                except ValueError:
                    erro.iniciarM("Número da agência")
                    break

            if(numConta == ""):
                erro.iniciarM("Número da conta")
                break
            else:
                try:
                    int(numConta)
                except ValueError:
                    erro.iniciarM("Número da conta")
                    break

            if(saldo == ""):
                erro.iniciarM("Saldo")
                break
            else:
                try:
                    float(saldo)
                except ValueError:
                    erro.iniciarM("Saldo")
                    break

            if(limite == ""):
                erro.iniciarM("Limite")
                break
            else:
                try:
                    float(limite)
                except ValueError:
                    erro.iniciarM("Limite")
                    break

            if(taxaJuros == ""):
                erro.iniciarF("Taxa de Juros")
                break
            else:
                try:
                    float(taxaJuros)
                except ValueError:
                    erro.iniciarF("Taxa de Juros")
                    break

            self.novaEspecial.append(nome)
            self.novaEspecial.append(data)
            self.novaEspecial.append(numAgencia)
            self.novaEspecial.append(numConta)
            self.novaEspecial.append(saldo)
            self.novaEspecial.append(limite)
            self.novaEspecial.append(taxaJuros)

            self.sucessoCadastro = True
            erro.encerrar()
            self.encerrar()
            break

    def iniciar(self):
        root.mainloop()

    def encerrar(self):
        root.destroy()