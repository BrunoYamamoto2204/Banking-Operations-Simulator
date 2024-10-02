def Login():
    import customer

    while True:
        log=input('''\033[33m<< PYTHON BANK LOGIN >>\033[m
\033[33m[1]\033[m Login
\033[33m[2]\033[m Forgot password 
\033[33m[3]\033[m Forgot useraname
\033[33m[4]\033[m Log out
                
Enter choice: ''').strip()
        while log.isnumeric()==False or int(log)<1 or int(log)>4:
            print('=-'*15)
            print('\033[31mInvalid option!!\033[m')
            log=input('''\033[33m<< PYTHON BANK LOGIN >>\033[m
\033[33m[1]\033[m Login
\033[33m[2]\033[m Forgot password 
\033[33m[3]\033[m Forgot useraname
\033[33m[4]\033[m Log out
                                                
Enter choice: ''').strip()
        print('=-'*15)
        if int(log)==1:
            exist=customer.existing_customers()
            if exist[0]:
                 print('=-'*15)
                 return [True,exist[1]]
            else:
                return [False,None]
        if int(log)==2:
            customer.forgot_pass()
            print('=-'*15)
        if int(log)==3:
            customer.forgot_user()
            print('=-'*15)
        if int(log)==4:
            return [False,None]


