import sys
import tkinter as tk
import tkinter.ttk as ttk

class CadastrosExibir:
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
        root.title("Selecionar Tipo a Exibir")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.019, rely=0.029, relheight=0.934, relwidth=0.959)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.labelTitulo = ttk.Label(self.TFrame1)
        self.labelTitulo.place(relx=0.141, rely=0.062, height=39, width=346)
        self.labelTitulo.configure(background="#d9d9d9")
        self.labelTitulo.configure(foreground="#000000")
        self.labelTitulo.configure(font="-family {Yu Mincho} -size 21 -slant italic")
        self.labelTitulo.configure(relief="flat")
        self.labelTitulo.configure(anchor='center')
        self.labelTitulo.configure(justify='left')
        self.labelTitulo.configure(text='''SELECIONE QUAL TIPO''')
        self.labelTitulo.configure(compound='center')

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

        self.labelSubtitulo = ttk.Label(self.TFrame1)
        self.labelSubtitulo.place(relx=0.162, rely=0.185, height=19, width=326)
        self.labelSubtitulo.configure(background="#d9d9d9")
        self.labelSubtitulo.configure(foreground="#000000")
        self.labelSubtitulo.configure(font="TkDefaultFont")
        self.labelSubtitulo.configure(relief="flat")
        self.labelSubtitulo.configure(anchor='center')
        self.labelSubtitulo.configure(justify='left')
        self.labelSubtitulo.configure(text='''Por favor, selecione qual tipo de contas devem ser exibidas:''')

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

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