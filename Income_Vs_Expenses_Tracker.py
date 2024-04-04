from customtkinter import *
import customtkinter
import tkinter as tk

class Application_Gui:
    MAIN_FONT = "Cambria"  # This is the type of Font
    PRIMARY_HEADER = 18  # This is the size of the font: Primary Header
    SECONDARY_HEADER = 14  # This is the size of the font: Secondary Header
    TERTIARY_HEADER = 10  # This is the size of the font: Tertiary Header

    test_Array = list(range(10))
    my_dictionary = {}
    continue_To_Next_Page = False
    current_Row_Position = 1
    cols = 4
    list_2D = [[1,2,3],[1,2,3]]

    def __init__(self):
        self.root = CTk()
        self.root.geometry("1000x600")
        self.root.title("Expense Tracker")
        self.root._set_appearance_mode("light")

        self.root.resizable(width=False, height=True)
        self.title = CTkLabel(master=self.root, text="Income and Expense Inputs", font=(self.MAIN_FONT, 28),bg_color="#EBEBEB", text_color="black")
        self.title.pack(padx=10, pady=30)

        self.input_Frame = CTkScrollableFrame(self.root, fg_color="#EBEBEB", border_width=-2, orientation="vertical",width=900, height=320)
        self.input_Frame.pack(padx=50)

        self.input_Frame.columnconfigure(0, weight=1)
        self.input_Frame.columnconfigure(1, weight=1)
        self.input_Frame.columnconfigure(2, weight=1)
        self.input_Frame.columnconfigure(3, weight=1)

        self.btn_Add_Position_In_Row = 1
        self.current_Row_Position = 0
        self.var1 = CTkEntry(master=self.input_Frame, placeholder_text="Date (dd/mm/yy): ", width=300,
                                       text_color="black", fg_color="#EBEBEB")
        self.var1.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.var2 = CTkEntry(master=self.input_Frame, placeholder_text="Type (Income / Expense)", width=300,
                                       text_color="black", fg_color="#EBEBEB")
        self.var2.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.var3 = CTkEntry(master=self.input_Frame, placeholder_text="Category (One Word Description)",
                                       width=300, text_color="black", fg_color="#EBEBEB")
        self.var3.grid(row=0, column=3, sticky=tk.W + tk.E)

        self.var4 = CTkEntry(master=self.input_Frame, placeholder_text="Amounts (R)", width=250,
                                       text_color="black", fg_color="#EBEBEB")
        self.var4.grid(row=0, column=4, sticky=tk.W + tk.E)
        self.temp_Dictionary = {}
        # self.temp_List = [self.var1 , self.var2 , self.var3 ,self.var4]
        # self.temp_Dictionary = {1:self.temp_List[0]}

        # print(type(self.var1))
        self.temp_List = [self.var1, self.var2, self.var3, self.var4]
        # self.temp_Dictionary = {self.current_Row_Position: f"{self.temp_List[0].get()}-{self.temp_List[1].get()}-{self.temp_List[2].get()}-{self.temp_List[3].get()}"}
        def create_New_Row():
            self.current_Row_Position += 1
            self.temp_List = [self.var1, self.var2, self.var3, self.var4]
            self.temp_Dictionary["Row " + str(self.current_Row_Position)] = f"{self.temp_List[0].get()}-{self.temp_List[1].get()}-{self.temp_List[2].get()}-{self.temp_List[3].get()}"

            # self.temp_List = list(range(self.current_Row_Position + 3))

            self.var1 = CTkEntry(master=self.input_Frame, placeholder_text="Date (dd/mm/yy): ", width=300, text_color="black", fg_color="#EBEBEB")
            self.var1.grid(row=self.current_Row_Position, column=1, sticky=tk.W + tk.E)

            self.var2 = CTkEntry(master=self.input_Frame, placeholder_text="Date (dd/mm/yy): ", width=300,text_color="black", fg_color="#EBEBEB")
            self.var2.grid(row=self.current_Row_Position, column=2, sticky=tk.W + tk.E)

            self.var3 = CTkEntry(master=self.input_Frame, placeholder_text="Date (dd/mm/yy): ", width=300,text_color="black", fg_color="#EBEBEB")
            self.var3.grid(row=self.current_Row_Position, column=3, sticky=tk.W + tk.E)

            self.var4 = CTkEntry(master=self.input_Frame, placeholder_text="Date (dd/mm/yy): ", width=250,text_color="black", fg_color="#EBEBEB")
            self.var4.grid(row=self.current_Row_Position, column=4, sticky=tk.W + tk.E)


            self.btn_Add_Position_In_Row += 1
            self.btn_Add_Inputs.grid(row=self.btn_Add_Position_In_Row, column=4, sticky=tk.W + tk.E, pady=10)

        def continue_To_Next_Page():
            self.temp_List = [self.var1, self.var2, self.var3, self.var4]
            self.temp_Dictionary[
                "Row " + str(self.current_Row_Position + 1)] = f"{self.temp_List[0].get()}-{self.temp_List[1].get()}-{self.temp_List[2].get()}-{self.temp_List[3].get()}"

            print("Continue To Next Page")
            print(self.temp_Dictionary)

            return

        # Note Zee, the button's rows should be one more than the current index
        self.btn_Add_Inputs = CTkButton(master=self.input_Frame, text="Add Input", corner_radius=10, bg_color="#EBEBEB",height=40, font=(self.MAIN_FONT, 14), command=create_New_Row)
        # self.btn_Add_Inputs.update()
        self.btn_Add_Inputs.grid(row=self.btn_Add_Position_In_Row, column=4, sticky=tk.W + tk.E, pady=10)

        self.btn_Continue = CTkButton(master=self.root, text="Continue", corner_radius=10, bg_color="#EBEBEB",height=50, width=400, font=(self.MAIN_FONT, 14), command=continue_To_Next_Page)
        self.btn_Continue.pack(pady=60)





        self.root.mainloop()


# Hallo

Application_Gui()
