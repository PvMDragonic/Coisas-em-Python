import sys
import tkinter as tk
import tkinter.ttk as ttk
from GUI.Mensagens.menssagem_erro import MsgErro

class SelecionarConta:
    def __init__(self):
        global root
        root = tk.Tk()
        self.passou = False

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

        root.geometry("407x250+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(3844, 1061)
        root.resizable(1, 1)
        root.title("Selecionar Conta")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.027, rely=0.04, relheight=0.936, relwidth=0.956)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.Titulo = ttk.Label(self.TFrame1)
        self.Titulo.place(relx=0.103, rely=0.043, height=41, width=317)
        self.Titulo.configure(background="#d9d9d9")
        self.Titulo.configure(foreground="#000000")
        self.Titulo.configure(font="-family {Yu Mincho} -size 21 -slant italic")
        self.Titulo.configure(relief="flat")
        self.Titulo.configure(anchor='center')
        self.Titulo.configure(justify='left')
        self.Titulo.configure(text='''SELECIONE A CONTA''')
        self.Titulo.configure(compound='center')

        self.BotaoCancelar = ttk.Button(self.TFrame1, command=lambda: self.encerrar())
        self.BotaoCancelar.place(relx=0.566, rely=0.799, height=25, width=80)
        self.BotaoCancelar.configure(takefocus="")
        self.BotaoCancelar.configure(text='''Cancelar''')
        self.BotaoCancelar.configure(cursor="hand2")

        self.BotaoConfirmar = ttk.Button(self.TFrame1, command=lambda: self.selecionarConta(self.TCombobox1))
        self.BotaoConfirmar.place(relx=0.216, rely=0.812, height=25, width=85)
        self.BotaoConfirmar.configure(takefocus="")
        self.BotaoConfirmar.configure(text='''Confirmar''')
        self.BotaoConfirmar.configure(cursor="hand2")

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

    def selecionarConta(self, conta):
        global tipoExibir
        if (conta.get() == " "):
            erro = MsgErro()
            erro.semUsuario()
        else:
            global cadastrados
            for i in range(len(cadastrados)):
                    if (cadastrados[i] == conta.get()):
                        self.escolha = i
            self.passou = True
            self.encerrar()         

    def iniciar(self, arrayConta, opc):
        global tipoExibir
        tipoExibir = opc # Pra saber qual tipo de conta o usuário escolheu.
        global todosUsuarios
        todosUsuarios = arrayConta
        global cadastrados 
        cadastrados = []
        for i in range(len(arrayConta)):
            cadastrados.append(arrayConta[i][0])
        self.TCombobox1 = ttk.Combobox(self.TFrame1, value = cadastrados, state = "readonly")
        self.TCombobox1.place(relx=0.308, rely=0.47, relheight=0.09, relwidth=0.368)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.set(" ")
        root.mainloop()

    def encerrar(self):
        root.destroy()