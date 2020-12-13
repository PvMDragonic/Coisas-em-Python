import sys
import tkinter as tk
import tkinter.ttk as ttk

class MsgNaoCadastrado:
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
        root.title("Usuário não-registrado")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1MsgNaoCadastrado = ttk.Frame(root)
        self.TFrame1MsgNaoCadastrado.place(relx=0.013, rely=0.046, relheight=0.913, relwidth=0.974)
        self.TFrame1MsgNaoCadastrado.configure(relief='groove')
        self.TFrame1MsgNaoCadastrado.configure(borderwidth="2")
        self.TFrame1MsgNaoCadastrado.configure(relief="groove")

        self.BotaoOkMsgNaoCadastrado = ttk.Button(self.TFrame1MsgNaoCadastrado, command=lambda: self.encerrar())
        self.BotaoOkMsgNaoCadastrado.place(relx=0.409, rely=0.759, height=25, width=80)
        self.BotaoOkMsgNaoCadastrado.configure(takefocus="")
        self.BotaoOkMsgNaoCadastrado.configure(text='''OK''')
        self.BotaoOkMsgNaoCadastrado.configure(cursor="hand2")

        self.labelMsgNaoCadastrado = ttk.Label(self.TFrame1MsgNaoCadastrado)
        self.labelMsgNaoCadastrado.place(relx=0.022, rely=0.196, height=30, width=433)
        self.labelMsgNaoCadastrado.configure(background="#d9d9d9")
        self.labelMsgNaoCadastrado.configure(foreground="#000000")
        self.labelMsgNaoCadastrado.configure(font="-family {Yu Gothic} -size 12")
        self.labelMsgNaoCadastrado.configure(relief="flat")
        self.labelMsgNaoCadastrado.configure(anchor='n')
        self.labelMsgNaoCadastrado.configure(justify='left')
        self.labelMsgNaoCadastrado.configure(text='''Você não está registrado em nosso sistema.''')

        self.labelMsgNaoCadastrado2 = ttk.Label(self.TFrame1MsgNaoCadastrado)
        self.labelMsgNaoCadastrado2.place(relx=0.181, rely=0.38, height=30, width=283)
        self.labelMsgNaoCadastrado2.configure(background="#d9d9d9")
        self.labelMsgNaoCadastrado2.configure(foreground="#000000")
        self.labelMsgNaoCadastrado2.configure(font="-family {Yu Gothic} -size 12")
        self.labelMsgNaoCadastrado2.configure(relief="flat")
        self.labelMsgNaoCadastrado2.configure(anchor='n')
        self.labelMsgNaoCadastrado2.configure(justify='left')
        self.labelMsgNaoCadastrado2.configure(text='''Por favor, insira seus dados a seguir.''')

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

    def iniciar(self):
        root.mainloop()

    def encerrar(self):
        root.destroy()