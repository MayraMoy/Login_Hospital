import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.forms_maestro import MasterPanel
from forms.login.from_login_designe import FormLoginDesigner
from persistence.model import Auth_User
import util.enconding_decoding as end_dec
class FormLogin(FormLoginDesigner):

    def verificar(self):
        user_db: Auth_User = self.auth_repository.getUserByUserName(self.usuario.get()) 

    def isUser(self, user: Auth_User):
        status: bool = True
        if (user == None):
            status = False
            messagebox.showerror(message="El usuario no existe por favor registrese", title="Mensaje")
        return status

    def isPassword(self, password: str, user: Auth_User):
        b_password = end_dec.decrypt(user.password)
        if(password == b_password):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")

    def __init__(self):
        super().__init__()