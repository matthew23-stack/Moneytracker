from customtkinter import *
import customtkinter
import tkinter as tk

class Application_Gui:
    MAIN_FONT = "Cambria"  # This is the type of Font
    PRIMARY_HEADER = 18  # This is the size of the font: Primary Header
    SECONDARY_HEADER = 14  # This is the size of the font: Secondary Header
    TERTIARY_HEADER = 10  # This is the size of the font: Tertiary Header
    current_Row_Position = 0 # This variable contains which row the program is currently on

    def __init__(self):
        self.root = CTk()
        self.root.geometry("1000x600")
        self.root.title("Expense Tracker")
        self.root._set_appearance_mode("light")
        self.root.resizable(width=False, height=False)

        # This refers to the main title
        self.title = CTkLabel(master=self.root, text="Income and Expense Inputs", font=(self.MAIN_FONT, 28),bg_color="#EBEBEB", text_color="black")
        self.title.pack(padx=10, pady=50)


        # This refers to the various titles of each column
        self.title_Date = CTkLabel(master=self.root, text="Date", font=(self.MAIN_FONT, 18),bg_color="#EBEBEB", text_color="black")
        self.title_Date.place(x=140,y=108)

        self.title_Date = CTkLabel(master=self.root, text="Type", font=(self.MAIN_FONT, 18),bg_color="#EBEBEB", text_color="black")
        self.title_Date.place(x=350,y=108)

        self.title_Date = CTkLabel(master=self.root, text="Category", font=(self.MAIN_FONT, 18),bg_color="#EBEBEB", text_color="black")
        self.title_Date.place(x=540,y=108)

        self.title_Date = CTkLabel(master=self.root, text="Amount", font=(self.MAIN_FONT, 18),bg_color="#EBEBEB", text_color="black")
        self.title_Date.place(x=775,y=108)


        # This refers to the Frame (which is basically a container that contains the inputs)
        self.input_Frame = CTkScrollableFrame(self.root, fg_color="#EBEBEB", border_width=-2, orientation="vertical",width=900, height=300)
        self.input_Frame.pack(padx=50)

        # This initializes each column
        self.input_Frame.columnconfigure(0, weight=1)
        self.input_Frame.columnconfigure(1, weight=1)
        self.input_Frame.columnconfigure(2, weight=1)
        self.input_Frame.columnconfigure(3, weight=1)

        # This sets the current row to 1
        self.btn_Add_Position_In_Row = 1

        # This sets the first set of input rows
        self.var1 = CTkEntry(master=self.input_Frame, placeholder_text="Date (dd/mm/yy): ", width=300,text_color="black", fg_color="#EBEBEB")
        self.var1.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.var2 = CTkEntry(master=self.input_Frame, placeholder_text="Type (Income / Expense)", width=300,text_color="black", fg_color="#EBEBEB")
        self.var2.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.var3 = CTkEntry(master=self.input_Frame, placeholder_text="Category (One Word Description)",width=300, text_color="black", fg_color="#EBEBEB")
        self.var3.grid(row=0, column=3, sticky=tk.W + tk.E)

        self.var4 = CTkEntry(master=self.input_Frame, placeholder_text="Amounts (R)", width=250,text_color="black", fg_color="#EBEBEB")
        self.var4.grid(row=0, column=4, sticky=tk.W + tk.E)

        # This initializes the main dictionary which all the information would be stored in
        self.temp_Dictionary = {}

        # This puts the var1 to var4 into a list
        self.temp_List = [self.var1, self.var2, self.var3, self.var4]

        # This is the Function which would create a now row
        def create_New_Row():
            self.current_Row_Position += 1

            # This puts the var1 to var4 into a list
            self.temp_List = [self.var1, self.var2, self.var3, self.var4]

            # This puts the list with all current values into the dictionary. The key gets incrimented after the button "Add Input" is clicked.
            # After the button "Add Input" is clicked, the values are stored into the dictionary.
            self.temp_Dictionary["Row " + str(self.current_Row_Position)] = f"{self.temp_List[0].get()}-{self.temp_List[1].get()}-{self.temp_List[2].get()}-{self.temp_List[3].get()}"

            # This sets the first set of input rows
            self.var1 = CTkEntry(master=self.input_Frame, placeholder_text="Date (dd/mm/yy): ", width=300, text_color="black", fg_color="#EBEBEB")
            self.var1.grid(row=self.current_Row_Position, column=1, sticky=tk.W + tk.E)

            self.var2 = CTkEntry(master=self.input_Frame, placeholder_text="Type (Income / Expense): ", width=300,text_color="black", fg_color="#EBEBEB")
            self.var2.grid(row=self.current_Row_Position, column=2, sticky=tk.W + tk.E)

            self.var3 = CTkEntry(master=self.input_Frame, placeholder_text="Category (One Word Description): ", width=300,text_color="black", fg_color="#EBEBEB")
            self.var3.grid(row=self.current_Row_Position, column=3, sticky=tk.W + tk.E)

            self.var4 = CTkEntry(master=self.input_Frame, placeholder_text="Amounts (R): ", width=250,text_color="black", fg_color="#EBEBEB")
            self.var4.grid(row=self.current_Row_Position, column=4, sticky=tk.W + tk.E)

            self.btn_Add_Position_In_Row += 1
            self.btn_Add_Inputs.grid(row=self.btn_Add_Position_In_Row, column=4, sticky=tk.W + tk.E, pady=10)

            # The function (continue_To_Next_Page()) would continue to the Display Information Gui
        def continue_To_Next_Page():
            # This allows the last input row to be retrieved
            self.temp_List = [self.var1, self.var2, self.var3, self.var4]
            self.temp_Dictionary["Row " + str(self.current_Row_Position + 1)] = f"{self.temp_List[0].get()}-{self.temp_List[1].get()}-{self.temp_List[2].get()}-{self.temp_List[3].get()}"

            # This contains the Dictionary with all the values added
            print(self.temp_Dictionary)

            # This will be the code to move to the next GUI
            print("Continue To Next Page")

            return

        # This code initializes the Add Input Button
        self.btn_Add_Inputs = CTkButton(master=self.input_Frame, text="Add Input", corner_radius=10, bg_color="#EBEBEB",height=40, font=(self.MAIN_FONT, 14), command=create_New_Row)
        self.btn_Add_Inputs.grid(row=self.btn_Add_Position_In_Row, column=4, sticky=tk.W + tk.E, pady=10)

        # This code initializes the Continue Button
        self.btn_Continue = CTkButton(master=self.root, text="Continue", corner_radius=10, bg_color="#EBEBEB",height=50, width=400, font=(self.MAIN_FONT, 14), command=continue_To_Next_Page)
        self.btn_Continue.pack(pady=60)

        self.root.mainloop()
Application_Gui()
