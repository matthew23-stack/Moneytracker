from customtkinter import *
import customtkinter
import tkinter as tk

# Create Framework
# Fill Framework with single line inputs
# Follow same tutorial as buttons but use inputs instead of buttons
# Take each value and store it in either a list of dict

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
    array_2d = [[0 for _ in range(4)] for _ in range(current_Row_Position)]

    def __init__(self):
        self.root = CTk()
        self.root.geometry("1000x600")
        self.root.title("Expense Tracker")
        self.root._set_appearance_mode("light")

        self.root.resizable(width=False,height=True)

        # self.main_Title = CTkLabel(master=self.root, text="Expenses Tracker", font=("Cambria",18), bg_color="transparent")
        # self.main_Title.pack(padx=10, pady=30)

        self.title = CTkLabel(master=self.root, text="Income and Expense Inputs", font=(self.MAIN_FONT,28),bg_color="#EBEBEB",text_color="black")
        self.title.pack(padx=10, pady=30)

        self.input_Frame = CTkScrollableFrame(self.root,fg_color="#EBEBEB",border_width=-2,orientation="vertical", width=900, height=320)
        self.input_Frame.pack(padx=50)

        self.input_Frame.columnconfigure(0, weight=1)
        self.input_Frame.columnconfigure(1, weight=1)
        self.input_Frame.columnconfigure(2, weight=1)
        self.input_Frame.columnconfigure(3, weight=1)


        # DR = Date Row,
        # TR = Type Row
        # CR = Category Row
        # AR = Amounts Row
        self.variable_Keys = ["DR" , "TR" , "CR" , "AR"]
        self.btn_Add_Position_In_Row = 1
        self.current_Row_Position = 0

        self.random = list(range(5))

        self.array_2d[0][0] = CTkEntry(master=self.input_Frame,placeholder_text="Date (dd/mm/yy): ", width=300, text_color="black", fg_color="#EBEBEB")
        self.array_2d[0][0].grid(row=0, column=1, sticky=tk.W + tk.E)


        self.array_2d[0][1] = CTkEntry(master=self.input_Frame,
                                                                                              placeholder_text="Type (Income / Expense)",
                                                                                              width=300,
                                                                                              text_color="black",
                                                                                              fg_color="#EBEBEB")
        self.array_2d[0][1].grid(row=0, column=2,
                                                                                        sticky=tk.W + tk.E)

        self.array_2d[0][2] = CTkEntry(master=self.input_Frame,
                                                                                              placeholder_text="Category (One Word Description)",
                                                                                              width=300,
                                                                                              text_color="black",
                                                                                              fg_color="#EBEBEB")
        self.array_2d[0][2].grid(row=0, column=3,
                                                                                        sticky=tk.W + tk.E)

        self.array_2d[0][3] = CTkEntry(master=self.input_Frame,
                                                                                              placeholder_text="Amounts (R)",
                                                                                              width=250,
                                                                                              text_color="black",
                                                                                              fg_color="#EBEBEB")
        self.array_2d[0][3].grid(row=0, column=4,
                                                                                        sticky=tk.W + tk.E)

        def create_New_Row():
            self.current_Row_Position += 1

            self.random[4] = CTkEntry(master=self.input_Frame,placeholder_text="Date (dd/mm/yy): ", width=300,text_color="black", fg_color="#EBEBEB")
            self.random[4].grid(row=self.current_Row_Position, column=1, sticky=tk.W + tk.E)

            self.my_dictionary[self.variable_Keys[1] + str(self.current_Row_Position)] = CTkEntry(master=self.input_Frame,placeholder_text="Type (Income / Expense)", width=300,text_color="black", fg_color="#EBEBEB")
            self.my_dictionary[self.variable_Keys[1] + str(self.current_Row_Position)].grid(row=self.current_Row_Position, column=2, sticky=tk.W + tk.E)

            self.my_dictionary[self.variable_Keys[2] + str(self.current_Row_Position)] = CTkEntry(master=self.input_Frame,placeholder_text="Category (One Word Description)",width=300, text_color="black", fg_color="#EBEBEB")
            self.my_dictionary[self.variable_Keys[2] + str(self.current_Row_Position)].grid(row=self.current_Row_Position, column=3, sticky=tk.W + tk.E)

            self.my_dictionary[self.variable_Keys[3] + str(self.current_Row_Position)] = CTkEntry(master=self.input_Frame,placeholder_text="Amounts (R)", width=250,text_color="black", fg_color="#EBEBEB")
            self.my_dictionary[self.variable_Keys[3] + str(self.current_Row_Position)].grid(row=self.current_Row_Position, column=4, sticky=tk.W + tk.E)


            self.btn_Add_Position_In_Row += 1
            self.btn_Add_Inputs.grid(row=self.btn_Add_Position_In_Row, column=4, sticky=tk.W + tk.E, pady=10)

            print(self.btn_Add_Position_In_Row)
        def continue_To_Next_Page():
            print("Continue To Next Page")

            # other_Dictionary = {1 : self.var1.get()}
            print(self.array_2d[0][0].get())
            print(self.array_2d[0][1].get())
            print(self.array_2d[0][2].get())
            print(self.array_2d[0][3].get())

            return

        # Note Zee, the button's rows should be one more than the current index
        self.btn_Add_Inputs = CTkButton(master=self.input_Frame, text="Add Input",corner_radius=10, bg_color="#EBEBEB", height=40, font=(self.MAIN_FONT,14),command=create_New_Row)
        self.btn_Add_Inputs.update()
        self.btn_Add_Inputs.grid(row=self.btn_Add_Position_In_Row, column=4, sticky=tk.W + tk.E,pady=10)



        self.btn_Continue = CTkButton(master=self.root, text="Continue", corner_radius=10, bg_color="#EBEBEB", height=50, width=400 , font=(self.MAIN_FONT, 14),command=continue_To_Next_Page)
        self.btn_Continue.pack(pady=60)

        self.root.mainloop()



#Hallo

Application_Gui()