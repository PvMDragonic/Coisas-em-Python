import sys
import tkinter as tk
import tkinter.ttk as ttk

class MsgErro:
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

        root.geometry("516x173+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(3844, 1061)
        root.resizable(1, 1)
        root.title("ERRO")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.012, rely=0.058, relheight=0.89, relwidth=0.973)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.BotaoOk = ttk.Button(self.TFrame1, command=lambda: self.encerrar())
        self.BotaoOk.place(relx=0.42, rely=0.753, height=25, width=80)
        self.BotaoOk.configure(takefocus="")
        self.BotaoOk.configure(text='''OK''')
        self.BotaoOk.configure(cursor="hand2")

        self.label = ttk.Label(self.TFrame1)
        self.label.place(relx=0.022, rely=0.195, height=39, width=477)
        self.label.configure(text=" ")
        self.label.configure(background="#f0f0f0")
        self.label.configure(foreground="#000000")
        self.label.configure(font="-family {Yu Gothic} -size 12")
        self.label.configure(relief="flat")
        self.label.configure(anchor='center')
        self.label.configure(justify='left')

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

    def iniciarM(self, whatFailed):
        self.label.configure(text="Erro! " + whatFailed + " inválido inserido!")
        root.mainloop()

    def iniciarF(self, whatFailed):
        self.label.configure(text="Erro! " + whatFailed + " inválida inserida!")
        root.mainloop()

    def semConta(self, conta):
        self.label.configure(background="#d9d9d9")
        self.label.configure(text="Não há conta(s) do tipo " + conta + " para ser(rem) exibida(s).")
        root.mainloop()

    def semContas(self):
        self.label.configure(background="#d9d9d9")
        self.label.configure(text="Não há nenhuma conta para ser exibida.")
        root.mainloop()

    def semUsuario(self):
        self.label.configure(text="Você não selecionou um usuário válido!")
        root.mainloop()

    def dataVenc(self):
        self.label.configure(text="Erro! A data de vencimento é anterior a de abertura.")
        root.mainloop()

    def maxContas(self, qualTipo):
        self.label.configure(text="Não estamos abrindo contas do tipo " + qualTipo + " neste momento.")
        root.mainloop()

    def iniciarRendimento(self, num):
        self.label.configure(text="Erro! " + num + " não é um número válido para mês no calendário fiscal.")
        root.mainloop()

    def encerrar(self):
        root.update() # Isso aqui que arruma o spam de warnings. O que, ou porque, eu já não sei. But it works!
        root.destroy()