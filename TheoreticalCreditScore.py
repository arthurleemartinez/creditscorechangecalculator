# import modules/packages/libraries
from math import *
# set your initial personal global variables
# ph = percentage of on-time payments represented as a decimal integer in range 0-1
ph = 1
# if you have had card debt in past 2 weeks use 1 cent so the function will know you have a card
card_debt  = 687
car_loan = 11187
mortgage = 0
personal_loan = 0
new_accounts = 4
# number of inquiries in past year
recent_applications = 4
# represented as number of years
length_credit = .33

# variable to be used as function component that turns mortgage into boolean
def has_mortgage(mortgage):
    if mortgage > 0:
        hm = True
    else:
        hm = False
    return hm

def has_card(card_debt):
    if card_debt > 0:
        cd1 = True
    else:
        cd1 = False
    return cd1

def has_car_loan(car_loan):
    if car_loan > 0:
        car = True
    else:
        car = False
    return car

def has_personal_loan(personal_loan):
   if personal_loan > 0:
        pl = True
    else:
        pl = False
    return pl
#_________________________________________________________________________________________
# length of credit represented as ratio of itself to 25 years
def credit_ratio(length_credit):
    ch1 = (length_credit / 25)
    return ch1
  
# converts paymnent history into component of new credit score equation
def payment_history(ph):
    ph1 = .35 * ph
    return ph1

# convert total debt to a number between 0 and 1 that will become component of new equation
def amount_owed_convert(card_debt, car_loan, mortage, personal_loan):
    anmounts_owed = (card_debt + car_loan + mortage + personal_loan) * .30  
    return amounts_owed

# Length of credit history (15%): the longer you’ve had credit, the better
def credit_history(length_credit):
    ch = credit_ratio(length_credit) * 0.15
    return ch 

# how many new accounts you have opened, and many times you have applied for credit.
def new_credit(recent_applications, new_accounts): 
    if (recent_applications + new_acounts) < 3:
        nc = 0.10 * 1
    elif (recent_applications + new_acounts) < 7:
        nc = 0.10 * 0.75
    elif (recent_applications + new_acounts) < 12:
        nc = 0.10 * 0.50 
    elif (recent_applications + new_acounts) < 14:
        nc = 0.10 * 0.25
    return nc
    
# The more types of credit you have, the better.
# needs booleans as function variables for if statement
def credit_types(has_car_loan(car_loan), has_personal_loan(personal_loan), has_card(card_debt), has_mortgage(mortgage)):
    if (has_mortgage(mortgage) == True) and (has_car_loan(car_loan) == True) and (has_personal_loan(personal_loan) == True) and (has_card(card_debt) == True):
        ct = 0.10 * 1
    elif (has_mortgage(mortgage) == False) and (has_car_loan(car_loan) == True) and (has_personal_loan(personal_loan) == True) and (has_card(card_debt) == True):
        ct = 0.10 * 0.75
    elif (has_mortgage(mortgage) == True) and (has_car_loan(car_loan) == False) and (has_personal_loan(personal_loan) == True) and (has_card(card_debt) == True):
        ct = 0.10 * 0.75
    elif (has_mortgage(mortgage) == True) and (has_car_loan(car_loan) == True) and (has_personal_loan(personal_loan) == False) and (has_card(card_debt) == True):
        ct = 0.10 * 0.75
    elif (has_mortgage(mortgage) == True) and (has_car_loan(car_loan) == True) and (has_personal_loan(personal_loan) == True) and (has_card(card_debt) == False):
        ct = 0.10 * 0.75
   
    elif (has_mortgage(mortgage) == False) and (has_car_loan(car_loan) == False) and (has_personal_loan(personal_loan) == True) and (has_card(card_debt) == True):
        ct = 0.10 * 0.50
    elif (has_mortgage(mortgage) == False) and (has_car_loan(car_loan) == True) and (has_personal_loan(personal_loan) == False) and (has_card(card_debt) == True):
        ct = 0.10 * 0.50
    elif (has_mortgage(mortgage) == False) and (has_car_loan(car_loan) == True) and (has_personal_loan(personal_loan) == True) and (has_card(card_debt) == False):
        ct = 0.10 * 0.50
    elif (has_mortgage(mortgage) == True) and (has_car_loan(car_loan) == False) and (has_personal_loan(personal_loan) == True) and (has_card(card_debt) == False):
        ct = 0.10 * 0.50
    elif (has_mortgage(mortgage) == True) and (has_car_loan(car_loan) == False) and (has_personal_loan(personal_loan) == False) and (has_card(card_debt) == True):
        ct = 0.10 * 0.50
    elif (has_mortgage(mortgage) == True) and (has_car_loan(car_loan) == False) and (has_personal_loan(personal_loan) == False) and (has_card(card_debt) == True):
        ct = 0.10 * 0.50
    
    elif (has_mortgage(mortgage) == False) and (has_car_loan(car_loan) == False) and (has_personal_loan(personal_loan) == False) and (has_card(card_debt) == True):
        ct = 0.10 * 0.25
    elif (has_mortgage(mortgage) == False) and (has_car_loan(car_loan) == False) and (has_personal_loan(personal_loan) == True) and (has_card(card_debt) == False):
        ct = 0.10 * 0.25    
    elif (has_mortgage(mortgage) == False) and (has_car_loan(car_loan) == True) and (has_personal_loan(personal_loan) == False) and (has_card(card_debt) == False):
        ct = 0.10 * 0.25
    elif (has_mortgage(mortgage) == True) and (has_car_loan(car_loan) == False) and (has_personal_loan(personal_loan) == False) and (has_card(card_debt) == False):
        ct = 0.10 * 0.25    
    return ct
     
# def new_credit_score(payment_history(ph), amounts_owed, credit_history(length_credit), new_credit(recent_applications, new_accounts)):
    #new_score = 300 + 
    #return new_score

# alexa play despacito
def standard_credit_score(credit_types(car_loan, personal_loan, card_debt, mortgage) + payment_history(ph), amount_owed_convert(card_debt, car_loan, mortage, personal_loan), credit_history(length_credit), new_credit(recent_applications, new_accounts)):
    score = 300 + (550 * (credit_types(car_loan, personal_loan, card_debt, mortgage) + payment_history(ph) + amount_owed_convert(card_debt, car_loan, mortage, personal_loan) + credit_history(length_credit) + new_credit(recent_applications, new_accounts)))
    return score
