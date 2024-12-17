import customtkinter as ctk
from util import *

util: Util = Util()

class Application(ctk.CTk):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.geometry("800x400")
        self.title(util.getResponse("api/info")["app_name"])

        ctk.CTkLabel(self, text=f"{util.getResponse('api/info')['app_name']}", font=("Calibri", 25)).pack()


if __name__ == "__main__":
    app:Application = Application()
    app.mainloop()