import customtkinter as ctk
from util import *

util: Util = Util()

class Application(ctk.CTk):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("800x400")
        self.title("Pomodoro Planner")
        ctk.CTkLabel(self, text=f"{util.getResponse('api/author')['message']}", font=("Arial", 25)).pack()


if __name__ == "__main__":
    app:Application = Application()
    app.mainloop()