# future user interface variable functions 

# currentScore = input("What is your current FICO score?")
# currentCarNote = input("What is your current Car Note Balance?")
# currentCardBalances = input("What's your current cumulative credit card balance?")
# monthsPassed = int(input("How many months have passed or will pass before your new score date?"))
# carPaymentMonthly = int(input("What is your current car payment per month?"))
# newCreditCardPayments = int(input("How much have you paid or intend to pay towards your credit card bills?"))
# numberOfInquiries = int(input("How many inquiries will you make in the next 2 years?"))

# global variables start here
belowAverage = 0.25
average = .50
good = .75
excellent = 1

currentDebt = currentCarNote + currentCardBalances
newCreditHistoryLength = currentCreditHistoryLength + monthsPassed
oldDebt = currentCarNote + currentCardBalance
newCarNote = currentCarNote - carPaymentMonthly 
monthsPassed = 24
numberOfInquiries = 0
currentScore = 625
monthsPassed = 24
currentCarNote = 11126
currentCardBalance = 687
b = newPaymentHistory
l = levelOfDebt
# this is a integer in a range of 0-1 based on percentage of max credit score you have
zeroOne = (cc - 300) / 850
newCreditCardPayments = 76
levelOfDebt = newDebt(oldDebt)
# this will be a percentage converted to a range of 0-1
newPaymentHistory = 1 

def newDebt(oldDebt):
    z = monthsPassed * carPaymentMonthly
    zz = currentCardBalance - newCreditCardPayments + (currentCarNote - z)
    return zz

def changeLetter(b, levelOfDebt, newCreditCardHistoryLength, ine):
    if newPaymentHistory > 0.99:
        bR = 1
    elif newPaymentHistory > 0.90:
        bR = .75 
    elif levelOfDebt >    

# this will be a percentage converted to a range of 0-1
newPaymentHistory = 1 
# this is a function that takes variables and calculates a new theoretical score
def ncscalculator(currentScore, newDebt): 
    cc = currentScore
    n = newCreditHistoryLength
    ch = newCreditCardHistoryLength
    ine = numberOfInquiries
    # Payment history counts 35% of your score
    bb = bR * 0.35
    #Level of debt counts 30% of your score
    ll = l * 0.30 
    #Length of credit history is 15% of your score
    chch = ch * 0.15
    #Inquiries and mix of credit are 10% each
    inin = ine * 0.10
    # payment history is out of 1
    newPaymentHistory = 1
    nscomponent = 0.1 + (bb + ll + chch + inin)
    # this is a variable that gets your number out 1 to multiple by 550 to add to 300 to get newScore
    ns = zeroOne * nscomponent
    newScore = (ns * 550) + 300
print newDebt(oldDebt)
print ncscalculator(625, newDebt(oldDebt)) 
