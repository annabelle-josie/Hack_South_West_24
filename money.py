"""
USED TO CONTROL INVEST AND SELL BUTTONS

"""

'''THE VARIABLE 'MONEY' IS THE AMOUNT OF MONEY IN THE USER'S ACCOUNT, 
THE VARIABLE 'STOCKACCOUNT' IS THE TOTAL AMOUNT OF STOCK IN EACH COMPANY, 
THE VARIABLE 'STOCKTOREMOVE' IS THE AMOUNT OF STOCKS THAT ARE WANTED TO BE REMOVED FROM THE ACCOUNT, 
THE VARIABLE 'MONEYTOREMOVE' IS THE AMOUNT OF MONEY THE USER HAS CHOSEN TO REMOVE FROM THEIR ACCOUNT.'''
from v2 import companies
user_money = 1000

def addMoney(money, stockAccount):
    # Add money from stock to hand
    # Money = user's money
    # stockAccount = stock worth
    """adds money to users main account and lowers the stock in company"""
    money += stockAccount
    return money, stockAccount


def removeMoney(money, stockAccount):
    # Add money from stock to hand
    # Money = user's money
    # stockAccount = stock worth
    """removes money to users main account and adds to user stock in company"""
    money -= stockAccount
    return money, stockAccount
