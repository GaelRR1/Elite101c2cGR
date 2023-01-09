from datetime import date
import random
# constant values

date = date.today()
scenario_sh = ['show','put']
scenario_tr=['transfer','send']
scenario_cr=['create']

tck = 0 #talk check

#classes and functions
def revis(sc):
  for wo in sc:
    if tck != 1:
      if wo in answer:
        return True




class aaccount:
  def __init__(self,owner,date,funds,code):
    self.owner = owner
    self.date = date
    self.funds = funds
    self.code = code

  def show_account(self):
    print("\n******")
    print("*Owner = "+self.owner)
    print("*Creation = "+self.date)
    print("*Funds = $ "+str(self.funds))
    print("code = "+str(self.code))

  def transfer(self,codit,amount):
      if codit == True:
        self.funds -= amount
      else:
        self.funds += amount
class add_account(aaccount):
  def __init__(self):
    self.owner = input("What is the owner? ")
    self.date = str(date)
    self.funds = int(input("What are the funds of the account?  "))
    self.code = str(random.randint(000,999))

#introduction for give context to user
a1 = aaccount('Mike','2020-11-20',100000,673)
a2 = aaccount('Bobby','2019-05-15',500000,893)
acc_ls = [a1,a2]   
print("""
########################################################
#     Welcome to GR corporated                         #
#                                                      #
# Thank you for contacting the accounts support chat   #
########################################################
""")

h = input("Hello, how are you? ")

print("\nGreat, thanks for contacting.\nRevising this access account you posess admin accces.") 
g = 0

while g == 0:
  answer = input("We can <show> the present accounts and their information ,<transfer> funds ,and <create> an account.For understanding us better can you use the words between < >. \nIf you want to end our chat write end.")
  if revis(scenario_sh) and revis(scenario_tr) and revis(scenario_cr):
    print("\nI don't understand can you specify 1 thing.\n ")
  elif revis(scenario_sh):
    for a in acc_ls:
      a.show_account()
  elif revis(scenario_tr):
    print("For transfering is needed some information.")
    codetk = input("\nWrite the code were taking funds. ")
    codegv = input("\nWrite the code to give funds. ")
    amount_to = int(input("\nWhat is amount to transfer."))
    tk_check = 0
    gv_check = 0
    for a in acc_ls:
      if a.code == codetk:
       a.transfer(True,amount_to)
       tk_check +=1
      elif a.code == codegv:
       a.transfer(False,amount_to)
       gv_check += 1
    if tk_check == 0:
      print("\nTake account not founded")
    if gv_check == 0:
      print("\n give account not founded")
      print("""
    This is the new values""")
    for a in acc_ls:
      a.show_account()
      
  elif revis(scenario_cr):
    print("We need some information to create your account")
    a = random.randint(0,200)
    a = add_account()
    acc_ls.append(a)
  else:
    print("\nMaybe what you want is off limits, or please rephrase it.\n")
  if 'end' in answer:
    g +=1
    break
  else:
    print("\nWhat is next?")