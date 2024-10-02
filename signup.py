def add_database():
    import json

    list_customers = {
        "customers": [
            {   
                "firstname": "Joao",
                "lastname": "Silva",
                "username": "joaosilva",
                "account_number":'653080591964',
                "joaosilvapassword": "pass123",
                'joaosilvabalance': 1000
            },
            {
                "firstname": "Maria",
                "lastname": "Santos",
                "username": "mariasantos",
                "account_number": "793052631861",
                "mariasantospassword": "pass321",
                'mariasantosbalance': 1000
            }
        ]
    }
  
    with open('data_base.json','w') as data:
        json.dump(list_customers,data,indent=4)
    print('\033[32mDatabase created successfully!\033[m')

class Signup:
    def new_user(self): 
        fname=input('First Name: ').strip()
        lname=input('Last Name: ').strip()
        username=input('Username: ').strip()
        passwords=self.password()

        from random import randint 
        number=''
        for c in range(0,12):
            ram_number=randint(0,9)
            number+=str(ram_number)
        
        self.add_customers(fname, lname, username, number, passwords[1])
        result = [fname, lname, username, number, passwords[1]]
        return result
 
    def value_password(self,password):
        contl=0
        contu=0
        contd=0
        contsc=0
        for c in str(password):
            if c.islower():
                contl+=1
            if c.isupper():
                contu+=1
            if c.isdigit():
                contd+=1
            if c in ('!','@','?','#','$','%','-','&','*','=','_'):
                contsc+=1
        if contu<1 or  contl<1 or contd<1 or contsc<1 or len(password)<6 or len(password)>12:
            return False 
        else:
            return True 
        
    def password(self):
        import os 
        import hashlib
        import base64

        while True:    
            while True:
                passwords=input('\033[34mEnter a password: \033[m').strip()
                if self.value_password(passwords):
                    break 
                else: 
                    print('\033[31mInvalid password! \033[m')
            salt=os.urandom(64)
            passwordhash=hashlib.pbkdf2_hmac('sha256',passwords.encode('utf-8'),salt,100000)
            #Confirm
            confpassword=input('\033[34mConfirm your password: \033[m').strip()
            confpasswordhash=hashlib.pbkdf2_hmac('sha256',confpassword.encode('utf-8'),salt,100000)
            if confpasswordhash==passwordhash:
                print('\033[32mAccount created successfully!\033[m')
                passwordhash_base64= base64.b64encode(passwordhash).decode('utf-8')
                return [passwordhash_base64,passwords]
            else:
                print('\033[31mPasswords not match!\033[m')
            continue
    
    def add_customers(self,fname,lname,user,account_number,password):
        import json     
        with open('data_base.json','r') as dr:
            customers=json.load(dr) #json p/ Python 
        new_customer = {
            "firstname": fname,
            "lastname": lname,
            "username": user,
            "account_number": account_number,
            f"{user}password": password,
            f'{user}balance': 1000
        }
        customers['customers'].append(new_customer)
        with open('data_base.json','w') as sc:
            json.dump(customers,sc,indent=4)  #Python p/ json
        return [fname,lname,user,account_number,password]
        
if __name__ == "__main__":
    add_database()  #1
    signup = Signup()  #2
    signup.new_user()  #3


