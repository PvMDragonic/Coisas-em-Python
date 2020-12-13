import sys
import tkinter as tk
import tkinter.ttk as ttk
from GUI.Mensagens.menssagem_erro import MsgErro

class pedirCPF:
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

        root.geometry("391x173+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(3844, 1061)
        root.resizable(1, 1)
        root.title("Verificar Registro de Usuário")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1MsgCadastrado = ttk.Frame(root)
        self.TFrame1MsgCadastrado.place(relx=0.013, rely=0.046, relheight=0.913, relwidth=0.974)
        self.TFrame1MsgCadastrado.configure(relief='groove')
        self.TFrame1MsgCadastrado.configure(borderwidth="2")
        self.TFrame1MsgCadastrado.configure(relief="groove")

        self.BotaoConfirmar = ttk.Button(self.TFrame1MsgCadastrado, command=lambda: self.receberCPF(self.TEntry1))
        self.BotaoConfirmar.place(relx=0.276, rely=0.759, height=25, width=67)
        self.BotaoConfirmar.configure(takefocus="")
        self.BotaoConfirmar.configure(text='''Confirmar''')
        self.BotaoConfirmar.configure(cursor="hand2")

        self.labelMsg = ttk.Label(self.TFrame1MsgCadastrado)
        self.labelMsg.place(relx=0.021, rely=0.19, height=30, width=365)
        self.labelMsg.configure(background="#d9d9d9")
        self.labelMsg.configure(foreground="#000000")
        self.labelMsg.configure(font="-family {Yu Gothic} -size 12")
        self.labelMsg.configure(relief="flat")
        self.labelMsg.configure(anchor='n')
        self.labelMsg.configure(justify='left')
        self.labelMsg.configure(text='''Por favor, insira seu CFP:''')

        self.BotaoCancelar = ttk.Button(self.TFrame1MsgCadastrado, command=lambda: self.encerrar())
        self.BotaoCancelar.place(relx=0.53, rely=0.759, height=25, width=68)
        self.BotaoCancelar.configure(takefocus="")
        self.BotaoCancelar.configure(text='''Cancelar''')
        self.BotaoCancelar.configure(cursor="hand2")

        self.TEntry1 = ttk.Entry(self.TFrame1MsgCadastrado)
        self.TEntry1.place(relx=0.328, rely=0.38, relheight=0.133, relwidth=0.331)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)
        
    def receberCPF(self, cpfInput):
        erro = MsgErro()
        try:
            int(cpfInput.get())
            if (len(cpfInput.get()) == 11):
                self.inputCPF = cpfInput.get()
                erro.encerrar()
                self.retornar()
            else:
                erro.iniciarM("CPF")
        except ValueError:
            erro.iniciarM("CPF")

    def retornar(self):
        root.destroy()

    def iniciar(self):
        root.mainloop()

    def encerrar(self):
        self.inputCPF = None
        root.destroy()