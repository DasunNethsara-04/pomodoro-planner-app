import customtkinter as ctk
import requests

def getResponse()->dict[str, str]|requests.RequestException:
    try:
        response: requests.Response = requests.get("https://api-pomodoroplanner.vercel.app/")
        return response.json()
    except requests.RequestException as e:
        return e

root = ctk.CTk()
root.geometry("800x400")
root.title("Pomodoro Planner")

ctk.CTkLabel(root, text=f"{getResponse()['message']}", font=("Arial", 25)).pack()

root.mainloop()