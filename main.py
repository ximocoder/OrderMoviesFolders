#
# App to move movies to different folders depending on year
# ximo.coder@gmail.com
#
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from stat import *


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.directory = ""

    def createWidgets(self):
        self.btnload = tk.Button(self)
        self.btnload["text"] = "Load Directory\n(click me)"
        self.btnload["command"] = self.askdir
        self.btnload.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.QUIT.pack(side="bottom")

        self.GO = tk.Button(self, text="GO", fg="red",
                            command=self.loadtree)

        self.GO.pack(side="bottom")

    def askdir(self):
        """Returns a selected directoryname."""
        res = askdirectory()
        self.directory = res
        print(res)

    def loadtree(self):
        listdir = os.walk(self.directory)
        dirbase = "D:\\Movies_Year\\"
        for x in listdir:
            mode = os.stat(x[0]).st_mode
            if S_ISDIR(mode) and "VIDEOTECA" not in x[0]:  # and ("dvdrip" or "xvid" in x[0].lower()):
                print(x[0])
                dr = self.directory
                if "\\" in x[0]:
                    y = x[0].rsplit("\\", 1)[1]
                else:
                    y = ""
                print("split: " + y)

                if "198" in x[0]:
                    # print(x[0], "D:\\Movies_Year\\" + y)

                    # sh.move(x[0], "D:\\Movies_Year\\1980\\" + y)
                    os.rename(x[0], dirbase + "1980\\" + y)

                if "194" in x[0]:
                    os.rename(x[0], dirbase + "pre1950\\" + y)

                if "195" in x[0]:
                    os.rename(x[0], dirbase + "1950\\" + y)

                if "196" in x[0]:
                    os.rename(x[0], dirbase + "1960\\" + y)

                if "197" in x[0]:
                    os.rename(x[0], dirbase + "1970\\" + y)

                if "198" in x[0]:
                    os.rename(x[0], dirbase + "1980\\" + y)

                if "199" in x[0]:
                    os.rename(x[0], dirbase + "1990\\" + y)

                if "200" in x[0]:
                    os.rename(x[0], dirbase + "2000\\" + y)

                if "2010" in x[0]:
                    os.rename(x[0], dirbase + "2010\\" + y)

                if "2011" in x[0]:
                    os.rename(x[0], dirbase + "2010\\" + y)

                if "2012" in x[0]:
                    os.rename(x[0], dirbase + "2010\\" + y)

                if "2013" in x[0]:
                    os.rename(x[0], dirbase + "2010\\" + y)

                if "2014" in x[0]:
                    os.rename(x[0], dirbase + "2010\\" + y)

                if "2015" in x[0]:
                    os.rename(x[0], dirbase + "2015\\" + y)

                if "2016" in x[0]:
                    os.rename(x[0], dirbase + "2015\\" + y)


        tk.messagebox._show("Done", "Done")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

