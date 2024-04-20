# registered logins
registered_logins = ['opcjusz', 't4cs', 'admin']

# registered passcodes
registered_passcodes = {'opcjusz': 'realpass :0', 't4cs': 'teafourceees', 'admin': 'notadminpass69_12!@0.'}

print('Hello! Welcome to The Fully Working Login Screen!')
print('For any help, contact TFWLS@gmail.com') 
print('Please input your login.')

login_var = input()
if login_var in registered_logins:
    print("Welcome back " + login_var + '!')
    print('Please input your passcode')
    
    passcode_var = input()

    if passcode_var == registered_passcodes[login_var]:
        print('Welcome to TFWLS ' + login_var + '!')
    else:
        print("Wrong Passcode, contact support for a reset.")
else:
    print("Seems you haven't registered.... Or you forgot the login :)")

