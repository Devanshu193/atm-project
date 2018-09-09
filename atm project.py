print("wlcome to bank")
restart="y"
chances=3    # 1. maximum chance for use atm card
balance=100000
while chances>=0:
    pin=int(input('please enter your 4 digit pin:'))
    if pin == (1234):
        print("you entered you pin correctly\n")
        while restart not in ['n','NO','no','N']:
            print('please press 1 for your balance enquiry\n')  # 2.option for further process
            print('please press 2 for make withdrawl\n')
            print('please press 3 to deposit\n')
            print('please press 4 to return card\n')
            option=int(input('what would you like to choose?'))
            if option==1:
                print('your balance is  ',balance, '\n'  )
                restart=input('would you like to go back?')
                if restart in ('n','NO','no','N'):
                    print("Thank You")
                    break
            elif option==2:
                    option2=('y')
                    withdrawl=float(input("how much would you like to withdraw?\n for other enter1:"))
                    if withdrwal in [1000, 2000, 3000, 4000, 5000]:
                        balance=balance-withdrawl
                        print("\n your balance is now ", balance)
                        restart=input('would you like to go back?')
                        if restart in ('n','NO','no','N'):
                            print('thank you')
                            break
                    elif withdrawl!=[1000, 2000, 3000, 4000, 5000]:
                            print('invalid amount,please re try\n')
                            restart= ('y')
                    elif withdrawl==1:
                            withdrawl= float(input('pleaseenter desired amount:'))
            elif option==3:
                       deposit_in =float(input('how much would you like to deposit?'))
                       balance= balance+deposit_in
                       print("\n your balance is now ", balance)
                       restart = input('would you like to go back?')
                       if restart in ('n', 'NO', 'no', 'N'):
                                print('Thank You')
                                break
            elif option==4:
                print('please wait while you card is returned\n')
                print('thank you for your service')
                break
    else:
        print('please enter a correct number\n')

