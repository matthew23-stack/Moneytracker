import datetime
import collections 
import csv

class IncomeExpenseTracker:

    def __init__(self):
        self.balance = 0
        self.income_transactions = []
        self.expense_transactions = []

    def add_income(self, amount, category):
        self.balance += amount
        self.income_transactions.append((amount, category))

    def add_expense(self, amount, category):
        self.balance -= amount
        self.expense_transactions.append((amount, category))

    def save_income_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Amount', 'Category'])
            writer.writerows(self.income_transactions)

    def save_expenses_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Amount', 'Category'])
            writer.writerows(self.expense_transactions)

    def view_balance(self):
        print(f"Current Balance: ${self.balance}")

mydict = {  }

def add():
    type_of_transaction = IncomeExpenseTracker()

    global date
    mydict[date]["Income"] = []
    mydict[date]["Expense"] = []

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Save Income Transactions to CSV")
        print("4. Save Expense Transactions to CSV")
        print("5. View Current Balance")
        print("6. Exit")

        choice = input("Enter your choice: ")
    
        # select which choice you want add
        if choice == '1':
            type_of_transactioni = "Income"
            category = input("Enter a category name for Income: ")
            amount = float(input("Enter the Amount: "))
            type_of_transaction.add_income(amount, category)
            #mydict[date][type_of_transaction] = []
            
            print("Income added successfully!")
            mydict[date][type_of_transactioni].append( (category, amount) )
            
            
        elif choice == '2':
            type_of_transactione = "Expense"
            category = input("Enter a category name for Expense: ")
            amount = float(input("Enter the Amount: "))
            type_of_transaction.add_expense(amount, category)
            #mydict[date][type_of_transaction] = []

            print("Expense added successfully!")
            mydict[date][type_of_transactione].append( (category, amount) )

    
        elif choice == '3':
            filename = input("Enter filename to save income transactions (e.g., income.csv): ")
            type_of_transaction.save_income_to_csv(filename)
            print(f"Income transactions saved to {filename}")

        elif choice == '4':
            filename = input("Enter filename to save expense transactions (e.g., expenses.csv): ")
            type_of_transaction.save_expenses_to_csv(filename)
            print(f"Expense transactions saved to {filename}")

        elif choice == '5':
            type_of_transaction.view_balance()


        elif  choice == '6':
            print("Taking you back to main menu...") 
            break         
        else:
            print("Invalid Input")
            break


    saveToFile()


def saveToFile():
    pass

def Alllist():
    select = input("List all Expenses (all) or  List by Date (d)? ")
    if select.lower() == "all":
        print(mydict)
    elif select.lower() == "d":
        #list all transactions of a particular day
        key = input("Enter the date (dd/mm/yyyy) you want to see the transactions: ")
        try:
            print(mydict[key])
        except KeyError:
            print("No Transactions on that Day!")
    else:
        pass   # do nothing

def  update():
    pass

def  delit():
    print(mydict)
    while True:
        select = input("Enter a date(dd/mm/yyyy), TYPE('Income' / 'Expense') and Category you want to remove a transaction for separated by comma : ")
        select = select.split(", ")
        print(select[0] + "\n" + select[1] +"\n" +select[2])
        for t in mydict[select[0]][select[1]]:
            if  t[0] == select[2]:
                mydict[select[0]][select[1]].remove(t)
        print(f'Transaction Removed from {select[0]} on {select[1]}: ')
        
        conti = input("\nDo you wish to continue removing more items? Y/N : ")
        if conti.lower() != 'y':
            break
        select = input("Enter a date, TYPE and Category you want to remove a transaction for separated by comma : ")
    
def balance():
    print(mydict)
    while True:
        checkDate = input("Enter the month and year(mm/yyyy) your summary or exit to return to menu: ")
        if checkDate =='exit':
            break
        else:
            mydates = list(mydict.keys())
            totalIncome = 0
            totalExpense = 0
            for i in mydates:
                if i[3:] == checkDate:
                    for  j in mydict[i]['Income']:
                        totalIncome += float(j[1])
                    for k in mydict[i]['Expense']:
                        totalExpense += float(k[1])
            
            net_balance = totalIncome - totalExpense
            print(f'\nSummary for {checkDate}:\n Incomes:{totalIncome}\n Expenses:{totalExpense}\n Net Balance:{net_balance}\n')
    
while True:
    print("1. Add ")
    print("2. List Income and Expense ")
    print("3. Update ")
    print("4. Delete ")
    print("5. Check Monthly Balances ")
    print("6. Exit ")

    choice = input("Enter your choice: ")

    if choice == "1":
        # add new transaction to the selected day
        date = input("Enter a date in format dd/mm/yyyy: ")
        mydict[date] = {}
        add()

    elif choice == "2":
        Alllist()
        
    elif choice == "3":
        #update existing transaction
        print(mydict)
        update()

    elif choice == "4":
        #delete existing transaction
        delit()

    elif choice == '5':
        #show balance of specific month 
        balance()

    elif choice == '6':
        break
    else:
        break