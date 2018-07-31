from sys import argv, executable
from os import execl
# Initialize User Interface
print("This program will ask you a few questions about your financial situation, and calculate important information that MAY help you make more informed financial decisions.")
cla = input("Do you have an outstanding car loan? (y/n): ")
pla = input("Do you currently have an outstanding personal loan? (y/n): ")
#card_debt = 687
cda = input("How much credit card debt do you currently have (USD)?: ")
cda_num = int(cda)
# ph = percentage of on-time payments represented as a decimal integer in range 0-1
def php():
    a = input("Please enter your payment history percentage (omit symbol): ")
    if type(a) == int or float:
        phpb = float(a)
    else:
        php()
    phpc = phpb / 100
    return phpc
card_debt = int(cda)
ph = php()
ph_percentage = ph * 100
# function that turns the existence of a personal loan into a number value
def pl():
    if not pla != (not (not 'y' and not 'Y')):
        plb = int(input("How much do you still owe on that personal loan (USD)? "))
    elif pla == ('n' or 'N'):
        plb: int = 0
    else:
        print("You entered an incorrect answer. You will now be prompted again." )
        pl()
    return plb
personal_loan = pl()
def get_clb():
    if cla == ("y" or "Y"):
        # car_loan = 11187
        car_loan_balance = int(input("How much is left on your car note? (USD)?: "))
    else:
        car_loan_balance = 0
    return car_loan_balance
def restart_program():
    #Restarts the current program. Note: this function does not return. Any cleanup action (like
    #saving data) must be done before calling this function.
    python = executable
    execl(python, python, *argv)
def confirmation():
    print("Reviewing and displaying your information...")
    if personal_loan > 0:
        print("Your personal loan balances are %s") % personal_loan
    else:
        pass
    print(("Car loan balances: %d") % car_loan)
    print(("Mortgage balance: %d") % mortgage)
    print(("Credit card debt: %d") % cda_num)
    print(("Personal loan balances: %d") % personal_loan)
    print(("Your on-time payment percentage: %d") % ph_percentage)
    confirmation_answer = input("Is this information correct? (Answer y or n)")
    if confirmation_answer == "y" or "Y":
        boolean_answer = True
    else:
        boolean_answer = False
    if boolean_answer is False:
        print("Restarting shell..")
        restart_program()
    else:
        print('Your information will now be used to calculate certain information about your credit profile.')
    return boolean_answer
def user_interface():
    return confirmation()


def cl():
    if cla == ('Y' or 'y'):
        clb = get_clb()
    else:
        clb = 0
    if clb > 0:
        clc = int(clb)
    else:
        clc = 0
    return clc
car_loan = cl()
# if you have had card debt in past week use 1 cent so the function will know you have a card

mortgage = 0
#personal_loan = 0
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
        pl1 = True
    else:
        pl1 = False
    return pl1
# length of credit represented as ratio of itself to 25 years
def credit_ratio():
    ch1 = (length_credit / 25)
    return ch1
# converts payment history into component of new credit score equation
def payment_history():
    if ph > 0.99:
        ph1 = 0.35 * ph
    elif ph >= 0.98:
        ph1 = 0.35 * ph * 0.75
    elif ph >= 0.90:
        ph1 = 0.35 * ph * 0.50:
    elif ph < 0.90:
        ph1 = 0.35 * ph * 0.25:
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
# This function will generate your first estimated credit score
def standard_credit_score():
    score = 300 + (550 * (credit_types() + payment_history() + amount_owed_convert() + credit_history() + new_credit()))
    removal1 = 550/payment_history()
    return score
    
# Call functions to implement program
user_interface()
print("Your estimated credit score is %d" % standard_credit_score())
#def new_credit_score():
#   scs = credit_types() + payment_history() + amount_owed_convert() + credit_history() + new_credit()
