import sys
import tkinter as tk
import tkinter.ttk as ttk

class TipoCadastrar:
    def __init__(self):
        global root
        root = tk.Tk()

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
        root.title("Selecionar Tipo de Conta")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.019, rely=0.029, relheight=0.934, relwidth=0.959)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.182, rely=0.062, height=39, width=306)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {Yu Mincho} -size 21 -slant italic")
        self.TLabel1.configure(relief="ridge")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''TIPO DE CADASTRO''')
        self.TLabel1.configure(compound='center')

        self.BotaoContaPoupanca = ttk.Button(self.TFrame1, command=lambda: self.poupancaClicado())
        self.BotaoContaPoupanca.place(relx=0.667, rely=0.554, height=35, width=116)
        self.BotaoContaPoupanca.configure(takefocus="")
        self.BotaoContaPoupanca.configure(text='''Conta Poupança''')
        self.BotaoContaPoupanca.configure(cursor="hand2")

        self.BotaoContaEspecial = ttk.Button(self.TFrame1, command=lambda: self.especialClicado())
        self.BotaoContaEspecial.place(relx=0.384, rely=0.554, height=35, width=116)
        self.BotaoContaEspecial.configure(takefocus="")
        self.BotaoContaEspecial.configure(text='''Conta Especial''')
        self.BotaoContaEspecial.configure(cursor="hand2")

        self.BotaoContaCorrente = ttk.Button(self.TFrame1, command=lambda: self.correnteClicado())
        self.BotaoContaCorrente.place(relx=0.101, rely=0.554, height=35, width=116)
        self.BotaoContaCorrente.configure(takefocus="")
        self.BotaoContaCorrente.configure(text='''Conta Corrente''')
        self.BotaoContaCorrente.configure(cursor="hand2")

        self.BotaoRetornar = ttk.Button(self.TFrame1, command=lambda: self.retornarClicado())
        self.BotaoRetornar.place(relx=0.424, rely=0.769, height=25, width=80)
        self.BotaoRetornar.configure(takefocus="")
        self.BotaoRetornar.configure(text='''Retornar''')
        self.BotaoRetornar.configure(cursor="hand2")

        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.182, rely=0.215, height=19, width=306)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='center')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Por favor, selecione o tipo de conta que deseja cadastrar:''')

    def correnteClicado(self):
        self.escolhaMenu = 1
        self.encerrar()

    def especialClicado(self):
        self.escolhaMenu = 2
        self.encerrar()

    def poupancaClicado(self):
        self.escolhaMenu = 3
        self.encerrar()

    def retornarClicado(self):
        self.escolhaMenu = 4
        self.encerrar()

    def iniciar(self):
        root.mainloop()

    def encerrar(self):
        root.destroy()