"""
Programming Assignments:
* OOPS - Create a BankAccount class with deposit, withdraw, and check_balance. Handle insufficient balance with exceptions.
"""
import os


class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance in BankAccount."""
    pass

class BankAccount:
     """
    A simple BankAccount class to perform basic banking operations.

    Attributes:
        account_holder (str): Name of the account holder.
        balance (float): Current account balance.
    """
     
     def __init__(self, account_holder, initial_balance=0):
         """
        Initializes a new BankAccount instance.
        Args:
            account_holder (str): Name of the account holder.
            initial_balance (float, optional): Initial balance. Defaults to 0.
        """
         self.account_holder = account_holder
         self.balance = initial_balance



     def deposit(self, amount):
            """
        Deposits money into the account.
        
        Args:
            amount (float): Amount to deposit.
        """
            if amount > 0:
                self.balance += amount
                self._write_output(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
            else:
                self._write_output("Deposit amount must be positive.")



     def withdraw(self, amount):
          """
        Withdraws money from the account if sufficient balance exists.
        
        Args:
            amount (float): Amount to withdraw.
        
        Raises:
            InsufficientBalanceError: If balance is not enough.
        """
          if amount > self.balance:
              raise InsufficientBalanceError("Insufficient balance for this withdrawal.")
          elif amount <= 0:
              self._write_output("Withdrawal amount must be positive.")
          else:
              self.balance -= amount
              self._write_output(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")



     def check_balance(self):
           """
        Returns the current balance of the account.
        
        Returns:
            float: Current balance.
        """
           self._write_output(f"Checked balance: {self.balance:.2f}")
           return self.balance
     

     def _write_output(self, message):
      """
      Writes messages to an output file in the ./code/output folder.
      """
      folder_path = "./code/output"
      if not os.path.exists(folder_path):
          os.makedirs(folder_path)  # create folder if it doesn't exist
      with open(f"{folder_path}/bank_account_output.txt", "a") as file:
          file.write(message + "\n")




account = BankAccount("Yash Fating", 1000)
account.deposit(100000)
try:
    account.withdraw(500)
    account.withdraw(2000)
except InsufficientBalanceError as e:
    print(e)   
  
           
print(f"Final balance: {account.check_balance():.2f}")
            
