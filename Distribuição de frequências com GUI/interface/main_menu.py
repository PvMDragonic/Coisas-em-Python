import sys
import tkinter as tk
import tkinter.ttk as ttk

class mainScreen:
    def __init__(self):
        self.blink_status = 1

        global root
        root = tk.Tk()

        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        X = int(root.winfo_screenwidth()/2 - windowWidth/2)
        Y = int(root.winfo_screenheight()/3 - windowHeight/2)
        X = int(X * 0.9)
        Y = int(Y * 0.9)

        root.geometry("443x261+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(1370, 749)
        root.resizable(1, 1)
        root.title("Main Menu")
        root.configure(background="#d9d9d9")

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Yu Mincho Light} -size 21 -slant italic"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])    

        self.Canvas1 = tk.Canvas(root)
        self.Canvas1.place(relx=0.018, rely=0.023, relheight=0.95
                , relwidth=0.964)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.GetClassWindow = ttk.Entry(self.Canvas1)
        self.GetClassWindow.place(relx=0.328, rely=0.349, relheight=0.081, relwidth=0.6)
        self.GetClassWindow.configure(takefocus="")
        self.GetClassWindow.configure(cursor="ibeam")

        self.GetNumsWindow = ttk.Entry(self.Canvas1)
        self.GetNumsWindow.place(relx=0.328, rely=0.543, relheight=0.081, relwidth=0.6)
        self.GetNumsWindow.configure(takefocus="")
        self.GetNumsWindow.configure(cursor="ibeam")

        self.Confirm = ttk.Button(self.Canvas1, command=lambda: self.getInputs(self.GetNumsWindow, self.GetClassWindow))
        self.Confirm.place(relx=0.281, rely=0.775, height=25, width=76)
        self.Confirm.configure(takefocus="")
        self.Confirm.configure(text='''Confirm''')
        self.Confirm.configure(cursor="hand2")

        self.Close = ttk.Button(self.Canvas1, command=lambda: sys.exit(1))
        self.Close.place(relx=0.539, rely=0.775, height=26, width=76)
        self.Close.configure(takefocus="")
        self.Close.configure(text='''Close''')
        self.Close.configure(cursor="hand2")

        self.TitleMenu = tk.Message(self.Canvas1)
        self.TitleMenu.place(relx=0.08, rely=0.078, relheight=0.128, relwidth=0.82)
        self.TitleMenu.configure(background="#d9d9d9")
        self.TitleMenu.configure(font=font11)
        self.TitleMenu.configure(foreground="#000000")
        self.TitleMenu.configure(highlightbackground="#d9d9d9")
        self.TitleMenu.configure(highlightcolor="black")
        self.TitleMenu.configure(text='''Statistics Calculator 5000''')
        self.TitleMenu.configure(width=350)

        self.Classes = ttk.Label(self.Canvas1)
        self.Classes.place(relx=0.070, rely=0.349, height=21, width=105)
        self.Classes.configure(background="#d9d9d9")
        self.Classes.configure(foreground="#000000")
        self.Classes.configure(font="TkDefaultFont")
        self.Classes.configure(relief="flat")
        self.Classes.configure(anchor='w')
        self.Classes.configure(justify='left')
        self.Classes.configure(text='''How many classes:''')

        self.version = ttk.Label(self.Canvas1)
        self.version.place(relx=0.867, rely=0.899, height=21, width=47)
        self.version.configure(background="#d9d9d9")
        self.version.configure(foreground="#000000")
        self.version.configure(font="-family {Segoe UI} -size 7")
        self.version.configure(relief="flat")
        self.version.configure(anchor='e')
        self.version.configure(justify='right')
        self.version.configure(text='''ver. 1.0.0.''')
        self.version.configure(cursor="fleur")

        self.Numeros = ttk.Label(self.Canvas1)
        self.Numeros.place(relx=0.047, rely=0.543, height=20, width=116)
        self.Numeros.configure(background="#d9d9d9")
        self.Numeros.configure(foreground="#000000")
        self.Numeros.configure(font="TkDefaultFont")
        self.Numeros.configure(relief="flat")
        self.Numeros.configure(anchor='w')
        self.Numeros.configure(justify='left')
        self.Numeros.configure(text='''Insert your numbers:''')
    
    def startInterface(self):
        root.mainloop()

    def closeInterface(self):
        root.destroy()

    def getInputs(self, entryNums, entryClass):
        inputClasses = True
        inputNums = True

        testNumsInput = list(map(str, entryNums.get().split()))
        try:
            int(entryClass.get())
        except ValueError:
            inputClasses = False
    
        x = 0
        while (inputNums == True and x < len(testNumsInput)): # Roda por todos os nums da array e, se um não for número, pausa e retorna falso.
            try:
                testNumsInput[x] = int(testNumsInput[x])
                x += 1
            except ValueError:
                inputNums = False

        if(inputClasses == False or int(entryClass.get()) <= 0): # Caso os dois inputs sejam válidos, ele faz a ação.
            self.piscaClasse()
        else:
            if(entryNums.get() != ""):
                if(testNumsInput[1:] != testNumsInput[:-1]): # Verifica se, no input de números, eles são todos iguais.
                    if(inputNums == False):
                        self.piscaNum()
                    else:
                        self.classInput = int(entryClass.get())
                        self.numInput = testNumsInput
                        self.closeInterface()
                else:
                    self.piscaNum()
            else:
                self.piscaNum()

    def piscaClasse2(self):
        if(self.blink_status < 6):
            self.blink_status += self.blink_status
            self.Classes.configure(background="#d9d9d9")
        else:
            self.blink_status = 0
        root.after(200, self.piscaClasse)

    def piscaClasse(self):
        if self.blink_status >= 1:
            self.Classes.configure(background="#9D5545")
            root.after(200, self.piscaClasse2)
        elif self.blink_status == 0:
            self.Classes.configure(background="#d9d9d9")
            self.blink_status = 1

    def piscaNum2(self):
        if(self.blink_status < 6):
            self.blink_status += self.blink_status
            self.Numeros.configure(background="#d9d9d9")
        else:
            self.blink_status = 0
        root.after(200, self.piscaNum)

    def piscaNum(self):
        if self.blink_status >= 1:
            self.Numeros.configure(background="#9D5545")
            root.after(200, self.piscaNum2)
        elif self.blink_status == 0:
            self.Numeros.configure(background="#d9d9d9")
            self.blink_status = 1