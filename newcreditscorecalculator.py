# future user interface variable functions 

# currentScore = input("What is your current FICO score?")
# currentCarNote = input("What is your current Car Note Balance?")
# currentCardBalances = input("What's your current cumulative credit card balance?")
# monthsPassed = int(input("How many months have passed or will pass before your new score date?"))
# carPaymentMonthly = int(input("What is your current car payment per month?"))
# newCreditCardPayments = int(input("How much have you paid or intend to pay towards your credit card bills?"))
# numberOfInquiries = int(input("How many inquiries will you make in the next 2 years?"))

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
newCreditCardPayments = 76
levelOfDebt = newDebt(oldDebt)

def newDebt(oldDebt):
    z = monthsPassed * carPaymentMonthly
    zz = currentCardBalance - newCreditCardPayments 
    return zz
    
# this will be a percentage converted to a range of 0-1
newPaymentHistory = 1 

def ncscalculator(currentScore, newDebt): 
  cc = currentScore
  b = newPaymentHistory
  n = newCreditHistoryLength
  l = levelOfDebt
  ch = newCreditCardHistoryLength
  in = numberOfInquiries
  # Payment history counts 35% of your score
  bb = b * 0.35
  #Level of debt counts 30% of your score
  ll = l * 0.30 
  #Length of credit history is 15% of your score
  chch = ch * 0.15
  #Inquiries and mix of credit are 10% each
  inin = in * 0.10
  # payment history is out of 1
  paymentHistory = 1
  newScore = cc * (0.1 + (bb + ll + chch + inin))
  
print newDebt(oldDebt)
print ncscalculator(625, newDebt): 
  
  

