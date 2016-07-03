#
# App to move movies to different folders depending on year
# ximo.coder@gmail.com
#
import os
import shutil as sh
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
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Load Directory\n(click me)"
        self.hi_there["command"] = self.askdir
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.QUIT.pack(side="bottom")

        self.GO = tk.Button(self, text="GO", fg="red",
                            command=self.loadtree)

        self.GO.pack(side="bottom")

    def say_hi(self):
        print("hola shurmanos!")
        dir = askdirectory()

    def askdir(self):
        """Returns a selected directoryname."""
        res = askdirectory()
        self.directory = res
        print(res)

    def loadtree(self):
        listdir = os.walk(self.directory)
        dirbase = "D:\\MoviesSD_Year\\"
        for x in listdir:
            mode = os.stat(x[0]).st_mode
            if S_ISDIR(mode) and "VIDEOTECA" not in x[0] and ("dvdrip" or "xvid" in x[0].lower()):
                # print(x)
                y = x[0].split(self.directory, 1)[1]
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


                    # if "2010" in x[0] or "2011" in x[0] or "2012" in x[0] or "2013" or "2014" in x[0] \
                    #         and "VIDEOTECA" not in x[0]:
                    #     y = x[0].split(self.directory, 1)[1]
                    #     print("split: " + y)
                    #     try:
                    #         os.rename(x[0], "D:\\Movies_Year\\2010\\" + y)
                    #     except:
                    #         tk.messagebox._show("ERROR", x[0])
                    #
                    # if "2015" in x[0] or "2016" in x[0]:
                    #     y = x[0].split(self.directory, 1)[1]
                    #     print("split: " + y)
                    #     try:
                    #         os.rename(x[0], "D:\\Movies_Year\\2015\\" + y)
                    #     except:
                    #         tk.messagebox._show("ERROR", x[0])

        tk.messagebox._show("Done", "Done")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

# class TkFileDialogExample:
#     def __init__(self):
#         index = 0
#
#     def main(self):
#         root = Tk()
#         directory = self.askdirectory()
#         Label(root, text=directory).pack()
#         root.mainloop()
#     if __name__ == "__main__":
#         main()
#
#     def askdirectory(self):
#         """Returns a selected directoryname."""
#         return tkinter.filedialog(**self.dir_opt)
