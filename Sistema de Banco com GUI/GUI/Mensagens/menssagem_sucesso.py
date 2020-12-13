import sys
import tkinter as tk
import tkinter.ttk as ttk

class MsgSucesso:
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

        root.geometry("464x173+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(3844, 1061)
        root.resizable(1, 1)
        root.title("Usuário registrado")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.013, rely=0.046, relheight=0.913, relwidth=0.974)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.BotaoOk = ttk.Button(self.TFrame1, command=lambda: self.encerrar())
        self.BotaoOk.place(relx=0.409, rely=0.759, height=25, width=80)
        self.BotaoOk.configure(takefocus="")
        self.BotaoOk.configure(text='''OK''')
        self.BotaoOk.configure(cursor="hand2")

        self.label = ttk.Label(self.TFrame1)
        self.label.place(relx=0.022, rely=0.253, height=30, width=433)
        self.label.configure(background="#d9d9d9")
        self.label.configure(foreground="#000000")
        self.label.configure(font="-family {Yu Gothic} -size 12")
        self.label.configure(relief="flat")
        self.label.configure(anchor='n')
        self.label.configure(justify='left')
        self.label.configure(text='''Você foi registrado com sucesso em nosso sistema.''')

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

    def iniciar(self):
        root.mainloop()

    def iniciarCorrente(self):
        self.label.configure(text="Nova conta corrente registrada com sucesso.")
        root.mainloop()

    def iniciarEspecial(self):
        self.label.configure(text="Nova conta especial registrada com sucesso.")
        root.mainloop()

    def iniciarPoupanca(self):
        self.label.configure(text="Nova conta poupança registrada com sucesso.")
        root.mainloop()

    def encerrar(self):
        root.destroy()