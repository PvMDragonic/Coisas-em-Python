import sys
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from GUI.Mensagens.menssagem_erro import MsgErro

class PoupancaCadastro:
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
        root.title("Nova Conta Poupança")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.019, rely=0.026, relheight=0.935
                , relwidth=0.959)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.Titulo = ttk.Label(self.TFrame1)
        self.Titulo.place(relx=0.081, rely=0.028, height=42, width=416)
        self.Titulo.configure(background="#d9d9d9")
        self.Titulo.configure(foreground="#000000")
        self.Titulo.configure(font="-family {Yu Mincho} -size 21 -slant italic")
        self.Titulo.configure(relief="flat")
        self.Titulo.configure(anchor='center')
        self.Titulo.configure(justify='left')
        self.Titulo.configure(text='''Cadastro conta poupança''')
        self.Titulo.configure(compound='center')

        self.BotaoCancelar = ttk.Button(self.TFrame1, command=lambda: self.encerrar())
        self.BotaoCancelar.place(relx=0.566, rely=0.831, height=25, width=80)
        self.BotaoCancelar.configure(takefocus="")
        self.BotaoCancelar.configure(text='''Cancelar''')
        self.BotaoCancelar.configure(cursor="hand2")

        self.BotaoConfirmar = ttk.Button(self.TFrame1, command=lambda: self.pegarInputs(self.entryNome, self.entryDataAbertura, self.entryDataVencimento, self.entryNumAgencia, self.entryNumConta, self.entrySaldo, self.entryRendimento))
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
        self.entryNumAgencia.place(relx=0.303, rely=0.443, relheight=0.058, relwidth=0.598)
        self.entryNumAgencia.configure(takefocus="")
        self.entryNumAgencia.configure(cursor="ibeam")

        self.entryNumConta = ttk.Entry(self.TFrame1)
        self.entryNumConta.place(relx=0.303, rely=0.526, relheight=0.058, relwidth=0.598)
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
        self.labelNumAgencia.place(relx=0.04, rely=0.443, height=21, width=116)
        self.labelNumAgencia.configure(background="#d9d9d9")
        self.labelNumAgencia.configure(foreground="#000000")
        self.labelNumAgencia.configure(font="TkDefaultFont")
        self.labelNumAgencia.configure(relief="flat")
        self.labelNumAgencia.configure(anchor='e')
        self.labelNumAgencia.configure(justify='left')
        self.labelNumAgencia.configure(text='''Número da agência:''')

        self.labelNumConta = ttk.Label(self.TFrame1)
        self.labelNumConta.place(relx=0.061, rely=0.526, height=21, width=106)
        self.labelNumConta.configure(background="#d9d9d9")
        self.labelNumConta.configure(foreground="#000000")
        self.labelNumConta.configure(font="TkDefaultFont")
        self.labelNumConta.configure(relief="flat")
        self.labelNumConta.configure(anchor='e')
        self.labelNumConta.configure(justify='left')
        self.labelNumConta.configure(text='''Número da conta:''')

        self.labelSaldo = ttk.Label(self.TFrame1)
        self.labelSaldo.place(relx=0.182, rely=0.609, height=21, width=46)
        self.labelSaldo.configure(background="#d9d9d9")
        self.labelSaldo.configure(foreground="#000000")
        self.labelSaldo.configure(font="TkDefaultFont")
        self.labelSaldo.configure(relief="flat")
        self.labelSaldo.configure(anchor='e')
        self.labelSaldo.configure(justify='left')
        self.labelSaldo.configure(text='''Saldo:''')

        self.entrySaldo = ttk.Entry(self.TFrame1)
        self.entrySaldo.place(relx=0.303, rely=0.609, relheight=0.058, relwidth=0.598)
        self.entrySaldo.configure(takefocus="")
        self.entrySaldo.configure(cursor="ibeam")

        self.entryRendimento = ttk.Entry(self.TFrame1)
        self.entryRendimento.place(relx=0.303, rely=0.693, relheight=0.058, relwidth=0.598)
        self.entryRendimento.configure(takefocus="")
        self.entryRendimento.configure(cursor="ibeam")

        self.labelRendimento = ttk.Label(self.TFrame1)
        self.labelRendimento.place(relx=0.05, rely=0.693, height=21, width=110)
        self.labelRendimento.configure(background="#d9d9d9")
        self.labelRendimento.configure(foreground="#000000")
        self.labelRendimento.configure(font="TkDefaultFont")
        self.labelRendimento.configure(relief="flat")
        self.labelRendimento.configure(anchor='e')
        self.labelRendimento.configure(justify='left')
        self.labelRendimento.configure(text='''Dia do rendimento:''')

        self.labelDataVencimento = ttk.Label(self.TFrame1)
        self.labelDataVencimento.place(relx=0.04, rely=0.36, height=21, width=116)
        self.labelDataVencimento.configure(background="#d9d9d9")
        self.labelDataVencimento.configure(foreground="#000000")
        self.labelDataVencimento.configure(font="TkDefaultFont")
        self.labelDataVencimento.configure(relief="flat")
        self.labelDataVencimento.configure(anchor='e')
        self.labelDataVencimento.configure(justify='left')
        self.labelDataVencimento.configure(text='''Data de vencimento:''')

        self.entryDataVencimento = ttk.Entry(self.TFrame1)
        self.entryDataVencimento.place(relx=0.303, rely=0.36, relheight=0.058, relwidth=0.598)
        self.entryDataVencimento.configure(takefocus="")
        self.entryDataVencimento.configure(cursor="ibeam")

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

    def pegarInputs(self, nome, dataAbertura, dataVencimento, numAgencia, numConta, saldo, rendimento):
        self.sucessoCadastro = False
        erro = MsgErro()
        self.novaPoupanca = []
        nome = nome.get()
        dataAbertura = dataAbertura.get()
        dataVencimento = dataVencimento.get()
        numAgencia = numAgencia.get()
        numConta = numConta.get()
        saldo = saldo.get()
        rendimento = rendimento.get()

        while True:
            if(nome == ""):
                erro.iniciarM("Nome")
                break

            if(dataAbertura != ""):
                dataAbertura = dataAbertura.split("/")
                if(len(dataAbertura) == 3): #Verifica se o usuário botou algo no formato de data, ou seja, 10/10/10.
                    try:
                        datetime.datetime(year=int(dataAbertura[2]),month=int(dataAbertura[1]),day=int(dataAbertura[0])) #Verifica se cada um se adequa nos formatos do datetime
                    except ValueError:
                        erro.iniciarF("Data de abertura")
                        break
                else:
                    erro.iniciarF("Data de abertura")
                    break
            else:
                erro.iniciarF("Data de abertura")
                break

            if(dataVencimento != ""):
                dataVencimento = dataVencimento.split("/")
                if(len(dataVencimento) == 3): #Verifica se o usuário botou algo no formato de data, ou seja, 10/10/10.
                    try:
                        if (datetime.datetime(year=int(dataAbertura[2]),month=int(dataAbertura[1]),day=int(dataAbertura[0])) < datetime.datetime(year=int(dataVencimento[2]),month=int(dataVencimento[1]),day=int(dataVencimento[0]))): #Verifica se cada um se adequa nos formatos do datetime
                            dataAbertura = "/".join(dataAbertura)
                            dataVencimento = "/".join(dataVencimento) #Rejunta tudo numa string de novo
                        else:
                            erro.dataVenc()
                            break    
                    except ValueError:
                        erro.iniciarF("Data de vencimento")
                        break
                else:
                    erro.iniciarF("Data de vencimento")
                    break
            else:
                erro.iniciarF("Data de vencimento")
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

            if(rendimento == ""):
                erro.iniciarM("Rendimento")
                break
            else:
                try:
                    int(rendimento)
                    if(int(rendimento) < 1 or int(rendimento) > 30):
                        erro.iniciarRendimento(rendimento)
                        break
                except ValueError:
                    erro.iniciarRendimento(rendimento)
                    break

            self.novaPoupanca.append(nome)
            self.novaPoupanca.append(dataAbertura)
            self.novaPoupanca.append(dataVencimento)
            self.novaPoupanca.append(numAgencia)
            self.novaPoupanca.append(numConta)
            self.novaPoupanca.append(saldo)
            self.novaPoupanca.append(rendimento)

            self.sucessoCadastro = True
            erro.encerrar()
            self.encerrar()
            break

    def iniciar(self):
        root.mainloop()

    def encerrar(self):
        root.destroy()