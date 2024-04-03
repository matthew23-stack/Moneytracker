# importing required modules
import tkinter
import customtkinter
from IPython.utils import frame

customtkinter.set_appearance_mode("system")  # can set light or dark
customtkinter.set_default_color_theme("green")  # themes: blue,dark-blue or green

app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("600x440")
app.title('Login')

def save():
    print("Make login credentials")
def button_function():
    app.destroy()
    w = customtkinter.CTk()
    w.geometry('1200x720')
    w.title('Welcome')
    l1=customtkinter.CTkLabel(master=w, text='Home Page',font=('century gothic', 60))
    l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    w.mainloop()


l2 = customtkinter.CTkLabel(master=app, text="Log into your Account", font=('century gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=app, width=220, placeholder_text="Username")
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=app, width=220, placeholder_text="Password")
entry2.place(x=50, y=165)

l2 = customtkinter.CTkButton(master=app, text="Forgot password", font=('century gothic', 12))
l2.place(x=125, y=195)

button1 = customtkinter.CTkButton(master=app, width=220, text='Login', corner_radius=6,command=save)
button1.place(x=50, y=240)


app.mainloop()
