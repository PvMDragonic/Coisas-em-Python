import sys
import tkinter as tk
import tkinter.ttk as ttk

class CorrenteExibir:
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

        root.geometry("428x272+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(3844, 1061)
        root.resizable(1, 1)
        root.title("Exibindo usuário")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1Exibir = ttk.Frame(root)
        self.TFrame1Exibir.place(relx=0.014, rely=0.026, relheight=0.949, relwidth=0.974)
        self.TFrame1Exibir.configure(relief='groove')
        self.TFrame1Exibir.configure(borderwidth="2")
        self.TFrame1Exibir.configure(relief="groove")

        self.BotaoRetornar = ttk.Button(self.TFrame1Exibir, command=lambda: self.encerrar())
        self.BotaoRetornar.place(relx=0.398, rely=0.81, height=25, width=74)
        self.BotaoRetornar.configure(takefocus="")
        self.BotaoRetornar.configure(text='''Retornar''')
        self.BotaoRetornar.configure(compound='center')
        self.BotaoRetornar.configure(cursor="hand2")

        self.labelTitular = ttk.Label(self.TFrame1Exibir)
        self.labelTitular.place(relx=0.156, rely=0.058, height=49, width=131)
        self.labelTitular.configure(background="#d9d9d9")
        self.labelTitular.configure(foreground="#000000")
        self.labelTitular.configure(font="-family {Yu Gothic} -size 12")
        self.labelTitular.configure(relief="flat")
        self.labelTitular.configure(anchor='n')
        self.labelTitular.configure(justify='left')
        self.labelTitular.configure(text='''Nome do titular:''')

        self.labelDataAbert = ttk.Label(self.TFrame1Exibir)
        self.labelDataAbert.place(relx=0.132, rely=0.194, height=35, width=141)
        self.labelDataAbert.configure(background="#d9d9d9")
        self.labelDataAbert.configure(foreground="#000000")
        self.labelDataAbert.configure(font="-family {Yu Gothic} -size 12")
        self.labelDataAbert.configure(relief="flat")
        self.labelDataAbert.configure(anchor='n')
        self.labelDataAbert.configure(justify='left')
        self.labelDataAbert.configure(text='''Data de abertura:''')

        self.labelNumAgencia = ttk.Label(self.TFrame1Exibir)
        self.labelNumAgencia.place(relx=0.084, rely=0.333, height=34, width=161)
        self.labelNumAgencia.configure(background="#d9d9d9")
        self.labelNumAgencia.configure(foreground="#000000")
        self.labelNumAgencia.configure(font="-family {Yu Gothic} -size 12")
        self.labelNumAgencia.configure(relief="flat")
        self.labelNumAgencia.configure(anchor='n')
        self.labelNumAgencia.configure(justify='left')
        self.labelNumAgencia.configure(text='''Número da agência:''')

        self.labelNumConta = ttk.Label(self.TFrame1Exibir)
        self.labelNumConta.place(relx=0.125, rely=0.473, height=35, width=149)
        self.labelNumConta.configure(background="#d9d9d9")
        self.labelNumConta.configure(foreground="#000000")
        self.labelNumConta.configure(font="-family {Yu Gothic} -size 12")
        self.labelNumConta.configure(relief="flat")
        self.labelNumConta.configure(anchor='n')
        self.labelNumConta.configure(justify='left')
        self.labelNumConta.configure(text='''Número da conta:''')

        self.labelSaldo = ttk.Label(self.TFrame1Exibir)
        self.labelSaldo.place(relx=0.156, rely=0.601, height=35, width=131)
        self.labelSaldo.configure(background="#d9d9d9")
        self.labelSaldo.configure(foreground="#000000")
        self.labelSaldo.configure(font="-family {Yu Gothic} -size 12")
        self.labelSaldo.configure(relief="flat")
        self.labelSaldo.configure(anchor='e')
        self.labelSaldo.configure(justify='left')
        self.labelSaldo.configure(text='''Saldo:''')

        self.ExibirNome = ttk.Label(self.TFrame1Exibir)
        self.ExibirNome.place(relx=0.487, rely=0.074, height=19, width=200)
        self.ExibirNome.configure(background="#d9d9d9")
        self.ExibirNome.configure(foreground="#000000")
        self.ExibirNome.configure(font="TkDefaultFont")
        self.ExibirNome.configure(relief="flat")
        self.ExibirNome.configure(anchor='w')
        self.ExibirNome.configure(justify='left')
        self.ExibirNome.configure(text='''Tlabel''')

        self.ExibirDataAbert = ttk.Label(self.TFrame1Exibir)
        self.ExibirDataAbert.place(relx=0.487, rely=0.209, height=19, width=166)
        self.ExibirDataAbert.configure(background="#d9d9d9")
        self.ExibirDataAbert.configure(foreground="#000000")
        self.ExibirDataAbert.configure(font="TkDefaultFont")
        self.ExibirDataAbert.configure(relief="flat")
        self.ExibirDataAbert.configure(anchor='w')
        self.ExibirDataAbert.configure(justify='left')
        self.ExibirDataAbert.configure(text='''Tlabel''')

        self.ExibirNumAgencia = ttk.Label(self.TFrame1Exibir)
        self.ExibirNumAgencia.place(relx=0.487, rely=0.349, height=19, width=182)
        self.ExibirNumAgencia.configure(background="#d9d9d9")
        self.ExibirNumAgencia.configure(foreground="#000000")
        self.ExibirNumAgencia.configure(font="TkDefaultFont")
        self.ExibirNumAgencia.configure(relief="flat")
        self.ExibirNumAgencia.configure(anchor='w')
        self.ExibirNumAgencia.configure(justify='left')
        self.ExibirNumAgencia.configure(text='''Tlabel''')

        self.ExibirNumConta = ttk.Label(self.TFrame1Exibir)
        self.ExibirNumConta.place(relx=0.487, rely=0.481, height=21, width=182)
        self.ExibirNumConta.configure(background="#d9d9d9")
        self.ExibirNumConta.configure(foreground="#000000")
        self.ExibirNumConta.configure(font="TkDefaultFont")
        self.ExibirNumConta.configure(relief="flat")
        self.ExibirNumConta.configure(anchor='w')
        self.ExibirNumConta.configure(justify='left')
        self.ExibirNumConta.configure(text='''Tlabel''')

        self.ExibirSaldo = ttk.Label(self.TFrame1Exibir)
        self.ExibirSaldo.place(relx=0.487, rely=0.632, height=20, width=200)
        self.ExibirSaldo.configure(background="#d9d9d9")
        self.ExibirSaldo.configure(foreground="#000000")
        self.ExibirSaldo.configure(font="TkDefaultFont")
        self.ExibirSaldo.configure(relief="flat")
        self.ExibirSaldo.configure(anchor='w')
        self.ExibirSaldo.configure(justify='left')
        self.ExibirSaldo.configure(text='''Tlabel''')

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

    def iniciar(self, nome, dataAbert, numAgencia, numConta, saldo):
        self.ExibirNome.configure(text=nome)
        self.ExibirDataAbert.configure(text=dataAbert)
        self.ExibirNumAgencia.configure(text=numAgencia)
        self.ExibirNumConta.configure(text=numConta)
        self.ExibirSaldo.configure(text=saldo)    
        root.mainloop()

    def encerrar(self):
        root.destroy()