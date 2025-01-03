import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Master Panel")
        
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w,h))
        
        logo = utl.leer_imagen("img/yo.png", (200,200))
        
        label = tk.Label(self.ventana, image=logo, bg="#38b6ff")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        self.ventana.mainloop()