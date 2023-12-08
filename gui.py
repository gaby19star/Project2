import tkinter as tk
from tkinter import ttk
from accounts import SavingsAccount, accounts_list


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ATM")
        self.account_number_label = None
        self.account_number_entry = None
        self.name_entry_label = None
        self.name_entry = None
        self.amount_entry_label = None
        self.amount_entry = None
        self.deposit_button = None
        self.deposit_saving_button = None
        self.withdraw_button = None
        self.withdraw_saving_button = None
        self.output_text = None

        self.create_widgets()
        self.accounts = {account.account_number: account for account in accounts_list}

    def create_widgets(self):
        # Welcome Label
        welcome_label = ttk.Label(self, text="Welcome to CompSci ATM", font=("Helvetica", 16))
        welcome_label.grid(row=0, columnspan=2, pady=10)

        # Account Number Label
        self.account_number_label = ttk.Label(self, text="Enter Account Number:")
        self.account_number_label.grid(row=1, column=0, pady=5)

        # Account Number Entry
        self.account_number_entry = ttk.Entry(self)
        self.account_number_entry.grid(row=1, column=1, pady=5)

        # Name Label
        self.name_entry_label = ttk.Label(self, text="Enter Your Name:")
        self.name_entry_label.grid(row=2, column=0, pady=5)

        # Name Entry
        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(row=2, column=1, pady=5)

        # Amount Label
        self.amount_entry_label = ttk.Label(self, text="Enter Amount:")
        self.amount_entry_label.grid(row=3, column=0, pady=5)

        # Amount Entry
        self.amount_entry = ttk.Entry(self)
        self.amount_entry.grid(row=3, column=1, pady=5)

        self.deposit_button = ttk.Button(self, text="Deposit (Regular)", command=self.deposit_regular)
        self.deposit_button.grid(row=4, column=0, pady=5)

        self.deposit_saving_button = ttk.Button(self, text="Deposit (Saving)", command=self.deposit_saving)
        self.deposit_saving_button.grid(row=4, column=1, pady=5)

        self.withdraw_button = ttk.Button(self, text="Withdraw (Regular)", command=self.withdraw_regular)
        self.withdraw_button.grid(row=5, column=0, pady=5)

        self.withdraw_saving_button = ttk.Button(self, text="Withdraw (Saving)", command=self.withdraw_saving)
        self.withdraw_saving_button.grid(row=5, column=1, pady=5)

        # Output Text
        self.output_text = tk.Text(self, height=10, width=70, state=tk.DISABLED)
        self.output_text.grid(row=6, columnspan=2, padx=10, pady=10)

        self.exit_button = ttk.Button(self, text="Exit", command=self.quit)
        self.exit_button.grid(row=7, column=1, pady=10, sticky="e")

    def clear_input_boxes(self):
        self.account_number_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def deposit_regular(self):
        account_number = self.get_account_number()

        amount = self.get_amount()

        if account_number not in self.accounts:
            self.output_text.insert(tk.END, "Error: Account not found.\n")
            return

        if not isinstance(self.accounts[account_number], SavingsAccount):
            self.accounts[account_number].deposit(amount)
            self.print_output(self.accounts[account_number])
            self.clear_input_boxes()  # Clear input boxes after processing
        else:
            self.output_text.insert(tk.END, "Error: Not a Regular Account.\n")


    def withdraw_regular(self):
        account_number = self.get_account_number()
        amount = self.get_amount()

        if account_number not in self.accounts:
            self.output_text.insert(tk.END, "Error: Account not found.\n")

        if not isinstance(self.accounts[account_number], SavingsAccount):
            self.accounts[account_number].withdraw(amount)
            self.print_output(self.accounts[account_number])
            self.clear_input_boxes()
        else:
            self.output_text.insert(tk.END, "Error: Not a Regular Account.\n")

    def get_account_number(self):
        account_number = self.account_number_entry.get()
        if not account_number:
            self.output_text.insert(tk.END, "Error: Please enter an account number.\n")
        return account_number

    def deposit_saving(self):
        account_number = self.get_account_number()
        amount = self.get_amount()

        if account_number not in self.accounts:
            self.output_text.insert(tk.END, "Error: Account not found.\n")
            return

        if isinstance(self.accounts[account_number], SavingsAccount):
            self.accounts[account_number].deposit(amount)
            self.print_output(self.accounts[account_number])
            self.clear_input_boxes()  # Clear input boxes after processing
        else:
            self.output_text.insert(tk.END, "Error: Not a SavingsAccount.\n")

    def withdraw_saving(self):
        account_number = self.get_account_number()
        amount = self.get_amount()

        if account_number not in self.accounts:
            self.output_text.insert(tk.END, "Error: Account not found.\n")
            return

        if isinstance(self.accounts[account_number], SavingsAccount):
            self.accounts[account_number].withdraw(amount)
            self.print_output(self.accounts[account_number])
            self.clear_input_boxes()  # Clear input boxes after processing
        else:
            self.output_text.insert(tk.END, "Error: Not a SavingsAccount.\n")

    def get_name(self):
        name = self.name_entry.get()
        if not name:
            self.output_text.insert(tk.END, "Error: Please enter a name.\n")
        return name

    def get_amount(self):
        amount_str = self.amount_entry.get()

        if not amount_str:
            self.output_text.insert(tk.END, "Error: Please enter an amount.\n")
            return 0

        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Error: Amount must be greater than 0.")
            return amount
        except ValueError:
            self.output_text.insert(tk.END, "Error: Please enter a valid number.\n")
            return 0

    def print_output(self, account):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, str(account) + "\n")
        self.output_text.config(state=tk.DISABLED)

        # Schedule the clear_output function after 60 seconds
        self.after(5000, self.clear_output)

    def clear_output(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    app = Application()
    app.mainloop()