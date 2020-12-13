import sys
import tkinter as tk
import tkinter.ttk as ttk

class results:
    def __init__(self):
        global root  

        root = tk.Tk()

        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        X = int(root.winfo_screenwidth()/2 - windowWidth/2)
        Y = int(root.winfo_screenheight()/6 - windowHeight/2)
        X = int(X * 0.9)
        Y = int(Y * 0.9)

        root.geometry("1135x615+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(3844, 1061)
        root.resizable(1, 1)
        root.title("Results Screen")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Yu Mincho} -size 24 -slant italic"
        font11 = "-family {Segoe UI} -size 13 -underline 1"
        font12 = "-family {Segoe UI} -size 10"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

        self.TFrame1 = ttk.Frame(root)
        self.TFrame1.place(relx=0.011, rely=0.008, relheight=0.984, relwidth=0.974)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")

        self.titleResults = ttk.Label(self.TFrame1)
        self.titleResults.place(relx=0.453, rely=0.033, height=48, width=110)
        self.titleResults.configure(background="#d9d9d9")
        self.titleResults.configure(foreground="#000000")
        self.titleResults.configure(font=font10)
        self.titleResults.configure(relief="flat")
        self.titleResults.configure(anchor='w')
        self.titleResults.configure(justify='left')
        self.titleResults.configure(text='''Results''')

        self.nameClasses = ttk.Label(self.TFrame1)
        self.nameClasses.place(relx=0.036, rely=0.104, height=36, width=127)
        self.nameClasses.configure(background="#d9d9d9")
        self.nameClasses.configure(foreground="#000000")
        self.nameClasses.configure(font=font11)
        self.nameClasses.configure(relief="flat")
        self.nameClasses.configure(anchor='w')
        self.nameClasses.configure(justify='left')
        self.nameClasses.configure(text='''Classes:''')

        self.nameFrequency = ttk.Label(self.TFrame1)
        self.nameFrequency.place(relx=0.516, rely=0.106, height=37, width=184)
        self.nameFrequency.configure(background="#d9d9d9")
        self.nameFrequency.configure(foreground="#000000")
        self.nameFrequency.configure(font=font11)
        self.nameFrequency.configure(relief="flat")
        self.nameFrequency.configure(anchor='w')
        self.nameFrequency.configure(justify='left')
        self.nameFrequency.configure(text='''Frequencies:''')

        self.nameRelFrequency = ttk.Label(self.TFrame1)
        self.nameRelFrequency.place(relx=0.036, rely=0.491, height=35, width=221)
        self.nameRelFrequency.configure(background="#d9d9d9")
        self.nameRelFrequency.configure(foreground="#000000")
        self.nameRelFrequency.configure(font=font11)
        self.nameRelFrequency.configure(relief="flat")
        self.nameRelFrequency.configure(anchor='w')
        self.nameRelFrequency.configure(justify='left')
        self.nameRelFrequency.configure(text='''Relative Frequencies:''')

        self.nameCumulativeFreq = ttk.Label(self.TFrame1)
        self.nameCumulativeFreq.place(relx=0.52, rely=0.491, height=37, width=221)
        self.nameCumulativeFreq.configure(background="#d9d9d9")
        self.nameCumulativeFreq.configure(foreground="#000000")
        self.nameCumulativeFreq.configure(font=font11)
        self.nameCumulativeFreq.configure(relief="flat")
        self.nameCumulativeFreq.configure(anchor='w')
        self.nameCumulativeFreq.configure(justify='left')
        self.nameCumulativeFreq.configure(text='''Cumulative Freq:''')

        self.TSubFrame1 = ttk.Frame(self.TFrame1)
        self.TSubFrame1.place(relx=0.036, rely=0.158, relheight=0.308, relwidth=0.457)
        self.TSubFrame1.configure(relief='groove')
        self.TSubFrame1.configure(borderwidth="2")
        self.TSubFrame1.configure(relief="groove")

        self.labelShowClass = ttk.Label(self.TSubFrame1)
        self.labelShowClass.place(relx=0.022, rely=0.056, height=164, width=488)
        self.labelShowClass.configure(background="#d9d9d9")
        self.labelShowClass.configure(foreground="#000000")
        self.labelShowClass.configure(font=font12)
        self.labelShowClass.configure(relief="flat")
        self.labelShowClass.configure(anchor='nw')
        self.labelShowClass.configure(justify='left')

        self.TSubFrame2 = ttk.Frame(self.TFrame1)
        self.TSubFrame2.place(relx=0.516, rely=0.158, relheight=0.308, relwidth=0.456)
        self.TSubFrame2.configure(relief='groove')
        self.TSubFrame2.configure(borderwidth="2")
        self.TSubFrame2.configure(relief="groove")

        self.labelShowFreq = ttk.Label(self.TSubFrame2)
        self.labelShowFreq.place(relx=0.02, rely=0.056, height=164, width=488)
        self.labelShowFreq.configure(background="#d9d9d9")
        self.labelShowFreq.configure(foreground="#000000")
        self.labelShowFreq.configure(font=font12)
        self.labelShowFreq.configure(relief="flat")
        self.labelShowFreq.configure(anchor='nw')
        self.labelShowFreq.configure(justify='left')

        self.TSubFrame3 = ttk.Frame(self.TFrame1)
        self.TSubFrame3.place(relx=0.036, rely=0.545, relheight=0.307, relwidth=0.457)
        self.TSubFrame3.configure(relief='groove')
        self.TSubFrame3.configure(borderwidth="2")
        self.TSubFrame3.configure(relief="groove")
        self.TSubFrame3.configure(cursor="fleur")

        self.labelShowRelFreq = ttk.Label(self.TSubFrame3)
        self.labelShowRelFreq.place(relx=0.02, rely=0.056, height=159, width=488)
        self.labelShowRelFreq.configure(background="#d9d9d9")
        self.labelShowRelFreq.configure(foreground="#000000")
        self.labelShowRelFreq.configure(font=font12)
        self.labelShowRelFreq.configure(relief="flat")
        self.labelShowRelFreq.configure(anchor='nw')
        self.labelShowRelFreq.configure(justify='left')

        self.TSubFrame4 = ttk.Frame(self.TFrame1)
        self.TSubFrame4.place(relx=0.52, rely=0.545, relheight=0.303, relwidth=0.457)
        self.TSubFrame4.configure(relief='groove')
        self.TSubFrame4.configure(borderwidth="2")
        self.TSubFrame4.configure(relief="groove")

        self.labelShowCumuFreq = ttk.Label(self.TSubFrame4)
        self.labelShowCumuFreq.place(relx=0.02, rely=0.056, height=159, width=485)
        self.labelShowCumuFreq.configure(background="#d9d9d9")
        self.labelShowCumuFreq.configure(foreground="#000000")
        self.labelShowCumuFreq.configure(font=font12)
        self.labelShowCumuFreq.configure(relief="flat")
        self.labelShowCumuFreq.configure(anchor='nw')
        self.labelShowCumuFreq.configure(justify='left')

        self.Return = ttk.Button(self.TFrame1, command=lambda: self.closeInterface())
        self.Return.place(relx=0.412, rely=0.908, height=31, width=79)
        self.Return.configure(takefocus="")
        self.Return.configure(text='''Return''')
        self.Return.configure(cursor="hand2")

        self.Close = ttk.Button(self.TFrame1, command=lambda: sys.exit(1))
        self.Close.place(relx=0.533, rely=0.908, height=31, width=79)
        self.Close.configure(takefocus="")
        self.Close.configure(text='''Close''')
        self.Close.configure(cursor="hand2")

    def recieveClasses(self, classes):
        formatedClasses = ""
        for x in range(len(classes)):
            formatedClasses += "Class " + str(x+1) + ": " + str(classes[x]) + "\n"
        self.labelShowClass.configure(text=formatedClasses)

    def recieveFrequencies(self, frequencies):
        formatedFreqs = ""
        for x in range(len(frequencies)-1):
            formatedFreqs += "Class " + str(x+1) + ": " + str(frequencies[x]) + "\n"

        formatedFreqs += "Total: " + str(frequencies[-1])
        self.labelShowFreq.configure(text=formatedFreqs)

    def recieveRelativeFreqs(self, relFrequencies):
        formatedRelFreqs = ""
        for x in range(len(relFrequencies)-1):
            formatedRelFreqs += "Class " + str(x+1) + ": " + str(relFrequencies[x]) + "\n"
        self.labelShowRelFreq.configure(text=formatedRelFreqs)

    def recieveCumulativeFreqs(self, CumuFrequencies):
        formatedCumuFreqs = ""
        for x in range(len(CumuFrequencies)-1):
            formatedCumuFreqs += "Class " + str(x+1) + ": " + str(CumuFrequencies[x]) + "\n"
        self.labelShowCumuFreq.configure(text=formatedCumuFreqs)

    def startInterface(self):
        global root
        root.mainloop()

    def closeInterface(self):
        global root
        root.destroy()