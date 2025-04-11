import json
import random as random
import string
#import hashlib
from shlex import join
from cryptography.fernet import Fernet

# Rahmen
text = 'Welcome in Password Generator Program'
space = " "
stern = "*"


def rahmen():
    lang = len(text)
    sternlang = lang + 6
    for i in range(sternlang):
        print('*', end=' ')


rahmen()
print('\n {1}{1}{1}{1}{2}{2}{2}{2}{2} {0} {2}{2}{2}{2}{2} {1}{1}{1}{1}\n'.format(text, '*', ' '))
rahmen()
username = ''
# Folder Path definieren
path = 'C:\\Users\\Dunya\\PycharmProjects\\test1\\Project'


# function zu registeration ,hier wird ein json datei erstellet ,
# mit der username,zum speicheren nur Username ,masterpassword zum login process,
# (empfehlwerft noch den master password zu encreption), aber leider wegen Zeit Druck konnnte ich nicht .
def user_register_json():
    username = input('\n bitte gebne Sie Ihre User Name \n >>')
    masterpwd = input('\n bitte gebne Sie Ihre Master password \n >>')
    userdata = {'username': username, 'master_pwd': masterpwd}
    file_name = rf".\jsonfile\{username}_data.json"
    with open(file_name, 'w') as file:
        json.dump(userdata, file)
        print(f'registoration done ,file mit usernmae {username}_data.json wird in jsonfile folder erstellet ')



#Hier login Information wird geprüft ,bei Call the user jason file,
# wo steht user name und master password .
def user_login():
    global username
    username = input('\n bitte gebne Sie Ihre User Name \n >>')
    masterpwd = input('\n bitte gebne Sie Ihre Master password\n >>')

    # try:
    filename = f'.\\jsonfile\\{username}_data.json'
    with open(filename, 'r') as file:
        user_data = json.load(file)
        json_master_pw = user_data['master_pwd']
        print(json_master_pw)
        if masterpwd == json_master_pw:
            rahmen()
            print('\n')
            print(f'welcommen {username}')
            print('\n')
            rahmen()
            print('\n')
            user_Choice()
        else:
            print('password stimmet nicht,bitte versuchen Sie nochmal ')
            user_login()
        return username


# Account Information in Json File speicheren,mit der username, 3 option für password ,selbst password,generated password,encrepted password
# Hier wird die Login Information gespeichert ,Account ,User-ID,Website Link(if any) ,und password ,
# hier hat der User 3 Option für seine Password (eigene text Password ,
# Complex password bei password Generator function zu erstellen,oder encrepted Password zu erstellen .
def add_pwd_account():
    print(' bitte geben Sie Ihre login Information \n')
    account = input('Name der Account(bei Program oder website\n')
    userid = input('Ihre User ID bei diesem Account \n')
    website = input('Website link ,bei Internet Account,falls None,geben Sie bitte None\n')
    pass_choice = int(input(
        'bitte wählen Sie ,Was von Password für diese Account möchten Sie ?,\n "1" eigene pasword  ,\n "2" Generated Komplex Password ,\n "3" encrepted Password \n >> '))
    if pass_choice == 1:
        password = input('enter Ihre Password\n >>')
    elif pass_choice == 2:
        password = pdw_new()
    elif pass_choice == 3:
        password = security_pwd()
    else:
        print('sorry falsche Eingabe ,versuchen Sie nochmal')
        add_pwd_account()
    dict_user = {'Account': account, 'User_Id': userid, 'Website': website, 'Password': password, 'encrepted': False}
    print(dict_user)

    filename = f'.\\jsonfile\\{username}_pw_data.json'
    data_json = []
    with open(filename, 'r') as file:
        data_json = json.load(file)
        data_json.append(dict_user)
    with open(filename, 'w') as file:
        data_json = json.dump(data_json, file, indent=4)
        file.close()
        user_Choice()


# password Erstellung :gefragt wird :Length,Gross letter length ,:Digit length,sonderzeichung length
def pdw_new():
    length = len_gl = len_dig = len_sym = 0
    while length < 12:
        length = int(input('\n bitte gebne Sie  die gewünschte Passswordlänger,**min 12 digit** \n >>'))
    while len_gl < 1:
        len_gl = int(input('bitte geben Sie  die min Grosse Buchstaben Zahle in Ihre Password \n >>'))
        if len_gl > length:
            print('falsche Eingabe ,bitte versuchen Sie nochmal')
            pdw_new()
    while len_dig < 1:
        len_dig = int(
            input('bitte geben Sie  die min Digits zahl in Ihre Password ,**Empfehlungwert min 2 digit** \n >>'))
        if len_dig > length:
            print('falsche Eingabe ,bitte versuchen Sie nochmal')
            pdw_new()
    while length > len_sym < 1:
        len_sym = int(
            input('bitte geben Sie  die min besonders Zeichen in Ihre Password ,**Empfehlungwert min 2 digit** \n >>'))
        if len_sym > length:
            print('falsche Eingabe ,bitte versuchen Sie nochmal')
            pdw_new()
    pwd = []
    pwd_gl = []
    pwd_sl = []
    pwd_di = []
    pwd_sym = []
    len_sl = int(length - len_gl - len_sym - len_dig)
    print(len_sl)
    for i in range(len_gl):
        pwd_gl.append(random.choice(string.ascii_uppercase))
    for j in range(len_dig):
        pwd_di.append(random.choice(string.digits))
    for k in range(len_sym):
        pwd_sym.append(random.choice(string.punctuation))
    for l in range(len_sl):
        pwd_sl.append(random.choice(string.ascii_lowercase))

    pwd = pwd_gl + pwd_sl + pwd_di + pwd_sym
    # rearrange the charachter in random way,using shuffel function in randum, und chanege it to string sing join
    random.shuffle(pwd)
    password = ''.join(pwd)
    print(password)
    return password


# Login inforamation Suche ,falls nicht gefunden ,die gesamt user login info wird gedrückt als option
def get_data():
    account_info = input('\n bitte gebne Sie die Account name or User ID für die gewünschte login Information \n>> ')
    user_dict = {}
    filename = f'.\\jsonfile\\{username}_pw_data.json'
    with open(filename, 'r') as file:
        user_dict = json.load(file)
        #print(user_dict)

        # result=list(filter(lambda item: item['Account'] == account_info,user_dict))
        try:
            result = next(item for item in user_dict if item["Account"] == account_info)
            rahmen()
            print('\n')
            print(result)
            print('\n')
            rahmen()
            print('\n')
            user_Choice()
            password = result['Password']
            print(password)
        except:
            info_druck = str(input('diese Information wurde nicht gefounden ,wollen Sie alle Ihre gespeichert  login information drucken,bei ja geben Sie "1" or nein "2"\n>>'))
            if info_druck == 1:
                rahmen()
                print('\n')
                print(user_dict)
                print('\n')
                rahmen()
                user_Choice()
            else:
                user_Choice()
    return password

# Generieren den symmetric Key für die Encreption ,using cryptography.fernet,der Key wird für jede User einmal erstellet
#und mit file von username gespeichert
def key_generator():
    key_file = rf".\key\{username}_key"
    key = Fernet.generate_key()
    with open(key_file, 'wb') as key_file:
        key_file.write(key)
    user_Choice()

# encrepted von Password using the gespeichert generated key in der key file(mit der username)
def security_pwd():
    key_file = rf".\key\{username}_key"
    with open(key_file, 'rb') as key_file:
        key = key_file.read()
    cipher = Fernet(key)
    password = input('enter Ihre Password, zum encryption \n>>')
    new_enc_password = (cipher.encrypt(password.encode()).decode())
    rahmen()
    print('\n')
    print(new_enc_password)
    print('\n')
    password = new_enc_password
    user_Choice()
    return password

# hier kann man über copy von encrepted Pasword ,der original passwpord zu erhalten ,z.b zum test option 3 Ergebnisse ,oder von output von get login information dictionary ,
# zuerst copieren und nacher hier bei option 4 ,der Original password erhalten , leider gabe es nicht der Zeit für decreption  von encrepted gespeicherte Passworde direckt von json datei,leider muss mann händische kopieren
def security_pwd_decreption():
    key_file = rf".\key\{username}_key"
    with open(key_file, 'rb') as key_file:
        key = key_file.read()
    cipher = Fernet(key)
    enc_password = input('enter die encrepted Password bitte \n >> ')
    original_password = (cipher.decrypt(enc_password.encode()).decode())
    rahmen()
    print('\n')
    print(original_password)
    print('\n')
    rahmen()
    password = original_password
    user_Choice()
    return password


###Choice für login oder registeration oder exit
def login_Choice():
    login_choice = int(input('\n Bei neue User bitte zuerst Registeration,bei existing User login,sonsest exit, enter bitte: ,\n "1" Registration,\n "2" login ,\n "3" exit \n >>'))
    if login_choice == 1:
        user_register_json()
    elif login_choice == 2:
        user_login()
    elif login_choice == 3:
        quit()
    else:
        print('falsche Eingabe ,versuchen Sie nochmal')
        login_Choice()

# Nach Login die Option für die User ,damit kommt hier ,neue Komplex password, neue encrepted password ,oder decreption von schon encrepted password
# neue logine Information,und hier hat nochmal der user die option von Komplex oder encrepted password password zu erstellen.
#noch kann der user seine gespeicherte login Information ,leider gabe es nicht der Zeit ,für decreption gespeicherte Passworde , Decreption pass nur bei direckt copy von encrepted Pasword
def user_Choice():
    user_choice = int(input(
        'Was wünchen Sie von Password Manager ,\n "1" neue Komplex Password ,\n "2" generate a neue key für encreption ,\n "3" Password Encreption ,\n "4" Password Decreption ,\n "5"login Information speicheren,\n "6"get login Information ,\n "7" exit \n>>'))
    if user_choice == 1:
        pdw_new()
    elif user_choice == 2:
        key_generator()
    elif user_choice == 3:
        security_pwd()
    elif user_choice == 4:
        security_pwd_decreption()
    elif user_choice == 5:
        add_pwd_account()
    elif user_choice == 6:
        get_data()
    elif user_choice == 7:
        quit()
    else:
        print('falsche Eingabe ,versuchen Sie nochmal')
        user_Choice()

def main():
    login_Choice()

main()



"""""

        

class Password():
    def __init__(self):
    
    def new_pwd:
    
    def add_sec_key:
    def get_sec_key
    
    def security_pwd():
      def hashing(): 
      def encreption():   
    
    def search_pwd:
    def pwd_uses   

class User():
    def __init__(self,user):
        
    def register:
    def login:
        
    def new_user:
    
    def new_json_file
"""""


