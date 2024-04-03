#importing required modules
import tkinter
import customtkinter


customtkinter.set_appearance_mode("System") # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green") # Themes: blue(default), dark-blue, green


app = customtkinter.CTk() #creating cutstom tkinter window
app.geometry("600x440")
app.title('Login')




def button_function():
    app.destroy()      # destroy current window and creating new one 
    w = customtkinter.CTk()
    w = geometry("1288x720")
    w.title('Welcome')
    li =customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic' ,60))
    li.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    w.mainloop()
    