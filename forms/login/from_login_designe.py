import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class FormLoginDesigner:
    def verificar(self):
        pass
    
    def userRegister(self):
        pass

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio se sesion")
        self.ventana.geometry("800x600")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
        
        logo = utl.leer_imagen("img/hospital.png", (200,200))
        
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="#38b6ff")
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg="#38b6ff")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame_forms = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_forms.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        frame_forms_top = tk.Frame(frame_forms, height=50, bd=0, relief=tk.SOLID, bg="black")
        frame_forms_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_forms_top, text="Inicio se sesion", font=("Times", 30), fg="#666a88", bg="#fcfcfc", pady=40)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        frame_forms_fill = tk.Frame(frame_forms, height=50, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_forms_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        etiqueta_usuario = tk.Label(frame_forms_fill, text="Usuario",  font=("Times", 14), fg="#666a88", bg="#fcfcfc", pady=10, anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_forms_fill, font=("Times", 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)
        
        etiqueta_contraseña = tk.Label(frame_forms_fill, text="Contraseña",  font=("Times", 14), fg="#666a88", bg="#fcfcfc", pady=10, anchor="w")
        etiqueta_contraseña.pack(fill=tk.X, padx=20, pady=15)
        self.contraseña = ttk.Entry(frame_forms_fill, font=("Times", 14))
        self.contraseña.pack(fill=tk.X, padx=20, pady=10)
        self.contraseña.config(show="*")
        
        inicio = tk.Button(frame_forms_fill, text="Iniciar sesion", font=("Times", 15, BOLD), bg="#38b6ff", bd="0", fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)
        inicio.bind("<Return>", (lambda event: self.verificar()))
        
        inicio = tk.Button(frame_forms_fill, text="Registrar Usuario", font=("Times", 15, BOLD), bg="#fff", bd="0", fg="#38b6ff", command=self.userRegister)
        inicio.pack(fill=tk.X, padx=20,pady=20)
        inicio.bind("<Return>", (lambda event: self.userRegister()))
        
        self.ventana.mainloop()