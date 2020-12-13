import sys
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from GUI.Mensagens.menssagem_erro import MsgErro

class ClienteCadastro:
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

        root.geometry("516x348+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(3844, 1061)
        root.resizable(1, 1)
        root.title("Novo Cliente")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.019, rely=0.029, relheight=0.934, relwidth=0.959)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.Titulo = ttk.Label(self.TFrame1)
        self.Titulo.place(relx=0.081, rely=0.031, height=29, width=416)
        self.Titulo.configure(background="#d9d9d9")
        self.Titulo.configure(foreground="#000000")
        self.Titulo.configure(font="-family {Yu Mincho} -size 21 -slant italic")
        self.Titulo.configure(relief="flat")
        self.Titulo.configure(anchor='center')
        self.Titulo.configure(justify='left')
        self.Titulo.configure(text='''Cadastro de cliente''')
        self.Titulo.configure(compound='center')

        self.BotaoCancelar = ttk.Button(self.TFrame1, command=lambda: self.encerrar())
        self.BotaoCancelar.place(relx=0.566, rely=0.8, height=25, width=80)
        self.BotaoCancelar.configure(takefocus="")
        self.BotaoCancelar.configure(text='''Cancelar''')
        self.BotaoCancelar.configure(cursor="hand2")

        self.BotaoConfirmar = ttk.Button(self.TFrame1, command=lambda: self.cadastrarCliente(self.entryNome, self.entryCPF, self.entryDataNasc, self.entryEndereco))
        self.BotaoConfirmar.place(relx=0.263, rely=0.8, height=25, width=80)
        self.BotaoConfirmar.configure(takefocus="")
        self.BotaoConfirmar.configure(text='''Confirmar''')
        self.BotaoConfirmar.configure(cursor="hand2")

        self.entryNome = ttk.Entry(self.TFrame1)
        self.entryNome.place(relx=0.242, rely=0.246, relheight=0.065, relwidth=0.638)
        self.entryNome.configure(takefocus="")
        self.entryNome.configure(cursor="ibeam")

        self.entryCPF = ttk.Entry(self.TFrame1)
        self.entryCPF.place(relx=0.242, rely=0.369, relheight=0.065, relwidth=0.638)
        self.entryCPF.configure(takefocus="")
        self.entryCPF.configure(cursor="ibeam")

        self.entryDataNasc = ttk.Entry(self.TFrame1)
        self.entryDataNasc.place(relx=0.242, rely=0.492, relheight=0.065, relwidth=0.638)
        self.entryDataNasc.configure(takefocus="")
        self.entryDataNasc.configure(cursor="ibeam")

        self.entryEndereco = ttk.Entry(self.TFrame1)
        self.entryEndereco.place(relx=0.242, rely=0.615, relheight=0.065, relwidth=0.638)
        self.entryEndereco.configure(takefocus="")
        self.entryEndereco.configure(cursor="ibeam")

        self.labelNome = ttk.Label(self.TFrame1)
        self.labelNome.place(relx=0.061, rely=0.246, height=19, width=76)
        self.labelNome.configure(background="#d9d9d9")
        self.labelNome.configure(foreground="#000000")
        self.labelNome.configure(font="TkDefaultFont")
        self.labelNome.configure(relief="flat")
        self.labelNome.configure(anchor='e')
        self.labelNome.configure(justify='left')
        self.labelNome.configure(text='''Nome:''')

        self.labelCPF = ttk.Label(self.TFrame1)
        self.labelCPF.place(relx=0.061, rely=0.369, height=19, width=76)
        self.labelCPF.configure(background="#d9d9d9")
        self.labelCPF.configure(foreground="#000000")
        self.labelCPF.configure(font="TkDefaultFont")
        self.labelCPF.configure(relief="flat")
        self.labelCPF.configure(anchor='e')
        self.labelCPF.configure(justify='left')
        self.labelCPF.configure(text='''CPF:''')

        self.labelDataNasc = ttk.Label(self.TFrame1)
        self.labelDataNasc.place(relx=0.061, rely=0.492, height=19, width=76)
        self.labelDataNasc.configure(background="#d9d9d9")
        self.labelDataNasc.configure(foreground="#000000")
        self.labelDataNasc.configure(font="TkDefaultFont")
        self.labelDataNasc.configure(relief="flat")
        self.labelDataNasc.configure(anchor='e')
        self.labelDataNasc.configure(justify='left')
        self.labelDataNasc.configure(text='''Data Nasc.:''')

        self.labelEndereco = ttk.Label(self.TFrame1)
        self.labelEndereco.place(relx=0.061, rely=0.615, height=19, width=76)
        self.labelEndereco.configure(background="#d9d9d9")
        self.labelEndereco.configure(foreground="#000000")
        self.labelEndereco.configure(font="TkDefaultFont")
        self.labelEndereco.configure(relief="flat")
        self.labelEndereco.configure(anchor='e')
        self.labelEndereco.configure(justify='left')
        self.labelEndereco.configure(text='''Endereço:''')

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

    def cadastrarCliente(self, nome, cpf, dataNasc, endereco):
        erro = MsgErro()
        self.sucessoCadastro = False
        self.novoCliente = []
        nome = nome.get()
        cpf = cpf.get()
        dataNasc = dataNasc.get()
        endereco = endereco.get()

        while True:
            if(nome == ""):
                erro.iniciarM("Nome")
                break               

            if(len(cpf) != 11):
                erro.iniciarM("CPF")
                break
            else:
                try:
                    int(cpf)
                except ValueError:
                    erro.iniciarM("CPF")
                    break

            if(dataNasc != ""):
                dataNasc = dataNasc.split("/")
                if(len(dataNasc) == 3): #Verifica se o usuário botou algo no formato de data, ou seja, 10/10/10.
                    try:
                        datetime.datetime(year=int(dataNasc[2]),month=int(dataNasc[1]),day=int(dataNasc[0])) #Verifica se cada um se adequa nos formatos do datetime
                        dataNasc = "/".join(dataNasc) #Rejunta tudo numa string de novo
                    except ValueError:
                        erro.iniciarF("Data de nascimento")
                        break
                else:
                    erro.iniciarF("Data de nascimento")
                    break
            else:
                erro.iniciarF("Data de nascimento")
                break

            if(endereco == ""):
                erro.iniciarM("Endereço")
                break
            
            self.novoCliente.append(nome)
            self.novoCliente.append(cpf)
            self.novoCliente.append(dataNasc)
            self.novoCliente.append(endereco)
            self.sucessoCadastro = True
            erro.encerrar()
            self.encerrar()
            break
        
    def iniciar(self, cpf):
        self.entryCPF.insert(0, cpf)
        root.mainloop()

    def encerrar(self):
        root.destroy()