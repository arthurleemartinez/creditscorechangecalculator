# import modules/packages/libraries
# set your initial personal global variables
# ph = percentage of on-time payments represented as a decimal integer in range 0-1
from typing import Any, Union
# Initialize User Interface
def UI():
    print("This program will ask you a few questions about your financial situation, and calculate important information that MAY help you make more informed financial decisions.")
#card_debt = 687
def cd():
    a = input("How much credit card debt do you currently have (USD)?: ")
    b = int(a)
    return b
def php():
    a = input("Please enter your payment history percentage (omit symbol): ")
    b = float(a)
    c = b / 100
    return c
card_debt = cd()
def cl():
    a = input("Do you have an outstanding car loan? (y/n): ")
    if a == ('Y' or 'y'):
        b = input("How much is left on your car note? (USD)?: ")
    else:
        b = 0
    if b > 0:
        c = int(b)
    else:
        c = 0
    return c
# if you have had card debt in past week use 1 cent so the function will know you have a card
car_loan = 11187
mortgage = 0
ph = php()
personal_loan = 0
new_accounts = 4
# number of inquiries in past year
recent_applications = 4
# represented as number of years
length_credit = .33
# Variable to be used as function component that turns mortgage into boolean
# These functions will turn ints into booleans
def has_mortgage():
    if mortgage > 0:
        hm = True
    else:
        hm = False
    return hm
def has_card():
    if card_debt > 0:
        cd1 = True
    else:
        cd1 = False
    return cd1
def has_car_loan():
    if car_loan > 0:
        car = True
    else:
        car = False
    return car
def has_personal_loan():
    if personal_loan > 0:
        pl = True
    else:
        pl = False
    return pl
# length of credit represented as ratio of itself to 25 years
def credit_ratio():
    ch1 = (length_credit / 25)
    return ch1
# converts payment history into component of new credit score equation
def payment_history():
    ph1 = .35 * ph
    return ph1
# convert total debt to a number between 0 and 1 that will become component of new equation
def amount_owed_convert():
    amounts_owed = (card_debt + car_loan + mortgage + personal_loan) * .30
    return amounts_owed
# Length of credit history (15%): the longer you’ve had credit, the better
def credit_history():
    ch = credit_ratio() * 0.15
    return ch
# how many new accounts you have opened, and many times you have applied for credit.
def new_credit() -> new_accounts:
    global nc
    if (recent_applications + new_accounts) < 3:
        nc = 0.10 * 1
    elif (recent_applications + new_accounts) < 7:
        nc = 0.10 * 0.75
    elif (recent_applications + new_accounts) < 12:
        nc = 0.10 * 0.50
    elif (recent_applications + new_accounts) < 14:
        nc = 0.10 * 0.25
    return nc
# The more types of credit you have, the better.
# needs booleans as function variables for if statement
def credit_types():
    if (has_mortgage() == False) and (has_car_loan() == True) and (has_personal_loan() == True) and (has_card() == True):
        ct = 0.10 * 0.75
    elif (has_mortgage() == True) and (has_car_loan() == False) and (has_personal_loan() == True) and (has_card() == True):
        ct = 0.10 * 0.75
    elif (has_mortgage() == True) and (has_car_loan() == True) and (has_personal_loan() == False) and (has_card() == True):
        ct = 0.10 * 0.75
    elif (has_mortgage() == True) and (has_car_loan() == True) and (has_personal_loan() == True) and (has_card() == False):
        ct = 0.10 * 0.75
    elif (has_mortgage() == False) and (has_car_loan() == False) and (has_personal_loan() == True) and (has_card() == True):
        ct = 0.10 * 0.50
    elif (has_mortgage() == False) and (has_car_loan() == True) and (has_personal_loan() == False) and (has_card() == True):
        ct = 0.10 * 0.50
    elif (has_mortgage() == False) and (has_car_loan() == True) and (has_personal_loan() == True) and (has_card() == False):
        ct = 0.10 * 0.50
    elif (has_mortgage() == True) and (has_car_loan() == False) and (has_personal_loan() == True) and (has_card() == False):
        ct = 0.10 * 0.50
    elif (has_mortgage() == True) and (has_car_loan() == True) and (has_personal_loan() == False) and (has_card() == False):
        ct = 0.10 * 0.50
    elif (has_mortgage() == True) and (has_car_loan() == False) and (has_personal_loan() == False) and (has_card() == True):
        ct = 0.10 * 0.50
    elif (has_mortgage() == False) and (has_car_loan() == False) and (has_personal_loan() == False) and (has_card() == True):
        ct = 0.10 * 0.25
    elif (has_mortgage() == False) and (has_car_loan() == False) and (
        has_personal_loan() == True) and (has_card() == False):
        ct = 0.10 * 0.25
    elif (has_mortgage() == False) and (has_car_loan() == True) and (has_personal_loan() == False) and (has_card() == False):
        ct = 0.10 * 0.25
    elif (has_mortgage() == True) and (has_car_loan() == False) and (has_personal_loan() == False) and (has_card() == False):
        ct = 0.10 * 0.25
    else:
        ct = 0.10 * 1
    return ct
def standard_credit_score():
    score = 300 + (550 * (credit_types() + payment_history() + amount_owed_convert() + credit_history() + new_credit()))
    return score
payment_history()
#def new_credit_score():
#   scs = credit_types() + payment_history() + amount_owed_convert() + credit_history() + new_credit()
