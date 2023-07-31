print("Welcome to OUR ATM ")
pin=6969
balance = 1000000

while True:
    user_pin=int(input("Enter the PIN: "))
    if user_pin==pin:
        print("please select the desired option")
        print('''
        1)      Balance
        2)      Withdraw
        3)      Deposit
        4)      Quit
        ''')
        try:
            Option=int(input("Enter option: "))
        except Exception as e:
            print("Error:",e)
            print("Enter 1,2,3 or 4 only")
        if Option==1:
            print("Balance is ₹",balance)
        elif Option==2:
            print("Balance is ₹",balance)
            Withdraw=float(input("Enter withdraw amount ₹ "))
            if Withdraw>0 and Withdraw<=balance:
                balance=(balance-Withdraw)
                print("Forward balance is ₹",balance)
            elif Withdraw>balance:
                print("Insufficient funds!")
            else:
                print("None withdraw made")
        elif Option==3:
            print("Balance is ₹",balance)
            Deposit=float(input("Enter deposit amount ₹"))
            if Deposit>0:
                balance=(balance+Deposit)
                print("Forward balance is ₹ ",balance)
            else:
                print("None deposit made")
        elif Option==4:
            exit()
        else:
            print("ERROR!!!")
    else:
        print("Invalid pin, please try it again")