import login
import bank
import customer

if __name__ == '__main__':
    while True:
        choice = input('\033[33m<< PYTHON BANK >>\033[m\n\033[33m[1]\033[m Sing Up\n\033[33m[2]\033[m Login \n\033[33m[3]\033[m Exit \nEnter choice: ').strip()
        while choice.isnumeric()==False or int(choice)>3 or int(choice)<1:
            print('\033[31mInvalid choice\033[31m')
            choice = input('\033[33m<< PYTHON BANK >>\033[m\n\033[33m[1]\033[m Sing Up\n\033[33m[2]\033[m Login \n\033[33m[3]\033[m Exit \nEnter choice: ').strip()
        print('-'*40)
        if int(choice)==1:
            emp1 = customer.Customer()
        if int(choice)==2:
            a=login.Login()
            if a[0]:
                print('\033[32mLoged in!\033[m')
                user = a[1]
                import json

                with open('data_base.json', 'r') as r:
                    rjson = json.load(r)
                for c in range(len(rjson['customers'])):
                    if rjson['customers'][c].get('username') == user:
                        valor = rjson['customers'][c].get(f'{user}balance')
                info = bank.Bank(valor, [], [], 0, 0, user)
                bank.Bank.transactions(info)
            else:
                break
        if int(choice)==3:
            break



