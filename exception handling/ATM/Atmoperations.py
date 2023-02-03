#operations in the Atm
from AtmExceptions import DepositError
from AtmExceptions import WithdrawError,InSuffFundError
bal=500

def Deposit():
        try:
            n=int(input("Enter how much amount u want to deposit: "))
            if(n<=0):
                raise DepositError
            else:
                global bal
                bal=bal+n
        except DepositError:
            print("Don't Enter negative amt and zero")
        except ValueError:
            print("Don't Enter ALphanums,strs,symbols") 
        else:
            print("Your Account Balance= ",bal)
def Withdraw():
    try:
        n=int(input("Enter how much amount you want to withdraw: "))
        global bal
        if(n<=0):
                raise WithdrawError
        if((n+500)>bal):
		        raise InSuffFundError
        else:
            bal=bal-n
    except WithdrawError:
        print("Don't Enter negative amt and zero")
    except InSuffFundError:
        print("Don't withdraw the amount below the minimum balance")
    except ValueError:
        print("Don't Enter ALphanums,strs,symbols") 
    else:
        print("Your Account Balance= ",bal)
def Bal():
    global bal
    print("Your Account Balance= ",bal)
