import sys
import tkinter as tk
import tkinter.ttk as ttk

class MainMenu:
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
        root.title("Menu Principal")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.019, rely=0.029, relheight=0.934, relwidth=0.959)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.192, rely=0.062, height=39, width=306)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {Yu Mincho} -size 21 -slant italic")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''SISTEMA DE BANCO''')
        self.TLabel1.configure(compound='center')
        self.TLabel1.configure(cursor="fleur")

        self.BotaoEncerrar = ttk.Button(self.TFrame1, command=lambda: self.encerrarClicado())
        self.BotaoEncerrar.place(relx=0.384, rely=0.708, height=35, width=116)
        self.BotaoEncerrar.configure(takefocus="")
        self.BotaoEncerrar.configure(text='''Encerrar''')
        self.BotaoEncerrar.configure(cursor="hand2")

        self.BotaoExibir = ttk.Button(self.TFrame1, command=lambda: self.exibirClicado())
        self.BotaoExibir.place(relx=0.384, rely=0.554, height=35, width=116)
        self.BotaoExibir.configure(takefocus="")
        self.BotaoExibir.configure(text='''Exibir''')
        self.BotaoExibir.configure(cursor="hand2")

        self.BotaoCadastrar = ttk.Button(self.TFrame1, command=lambda: self.cadastrarClicado())
        self.BotaoCadastrar.place(relx=0.384, rely=0.4, height=35, width=116)
        self.BotaoCadastrar.configure(takefocus="")
        self.BotaoCadastrar.configure(text='''Cadastrar''')
        self.BotaoCadastrar.configure(cursor="hand2")

    def cadastrarClicado(self):
        self.escolhaMenu = 1
        self.encerrar()

    def exibirClicado(self):
        self.escolhaMenu = 2
        self.encerrar()

    def encerrarClicado(self):
        exit()

    def iniciar(self):
        root.mainloop()

    def encerrar(self):
        root.destroy()