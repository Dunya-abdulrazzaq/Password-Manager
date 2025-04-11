import json
import random as random
import string
import hashlib
from shlex import join
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip

# Rahmen
text = 'Welcome in Password Generator Programm'
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
username: str = ''


root = tk.Tk()


def window(title, size: int):
    root.title(title)
    root.geometry(f'{size[0]}x{size[1]}')
    root.minsize(size[0], size[1])
    label_welcom = ttk.Label(master=root, text='Welcom to the Password Manger \n', font=('Calibri', 18),
                             background='black', foreground='green')
    label_welcom.place(relx=0.2, rely=0.0, anchor='nw')
    root.mainloop()


# Hashin Function zu secure das master Password (to perform a Integritety Check using sha256 Algorithm)
def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()


# function zu registeration ,hier wird ein json datei erstellet ,
# mit der username,zum speicheren nur Username ,masterpassword zum login process,
def user_register_json():
    def button_next():
        label_login.place_forget()
        label_name.place_forget()
        label_m_pw.place_forget()
        name_e.place_forget()
        master_pw_e.place_forget()
        button_next.destroy()
        button_exit.destroy()
        root.quit()

    label_login = ttk.Label(master=root,
                            text='\n Bitte geben Sie Ihre gewünschte Login Name und Master Password\n Zum Registerieren  ',
                            font=('Calibri', 15), foreground='green')
    label_login.place(relx=0.0, rely=0.2)
    label_name = ttk.Label(master=root, text='Login Name :', font=('Calibri', 15))
    label_name.place(relx=0.0, rely=0.5)
    label_m_pw = ttk.Label(master=root, text='Master Password :', font=('Calibri', 15))
    label_m_pw.place(relx=0.0, rely=0.6)
    name_e = ttk.Entry(master=root, textvariable=tk.StringVar, font=('Calibri', 15))
    name_e.place(relx=0.3, rely=0.5)
    master_pw_e = ttk.Entry(master=root, textvariable=tk.StringVar, font=('Calibri', 15), show="*")
    master_pw_e.place(relx=0.3, rely=0.6)
    button_next = ttk.Button(master=root, text='  Next  ', command=button_next)
    button_next.place(relx=0.4, rely=0.8)
    button_exit = ttk.Button(master=root, text='  exit  ', command=root.destroy)
    button_exit.place(relx=0.6, rely=0.8)

    window('User Registeration', (600, 300))

    username = name_e.get()
    masterpwd_un = master_pw_e.get()
    masterpwd = hash_password(masterpwd_un)
    print(masterpwd)
    userdata = {'username': username, 'master_pwd': masterpwd}
    file_name = rf".\jsonfile\{username}_data.json"

    with open(file_name, 'w') as file:
        json.dump(userdata, file)
        file.close()
        messagebox.showinfo(title='Registration Done',
                            message=f'Registration done ,file mit Username {username}_data.json wird in jsonfile folder erstellet,bitte login Sie jetzt mit Ihre Username & Master Password ')
        messagebox.showinfo(title='Registration Done', command=user_login())


# Hier login Information wird geprüft ,bei Call the user jason file,
# wo steht user name und master password .
def user_login():
    def button_next():
        label_login.place_forget()
        label_name.place_forget()
        label_m_pw.place_forget()
        name_e.place_forget()
        master_pw_e.place_forget()
        button_next.destroy()
        button_exit.destroy()
        root.quit()

    label_login = ttk.Label(master=root, text='\n Bitte geben Sie Ihre Login Name und Master Password ',
                            font=('Calibri', 15), foreground='green')
    label_login.place(relx=0.0, rely=0.2)
    label_name = ttk.Label(master=root, text='Login Name :', font=('Calibri', 15))
    label_name.place(relx=0.0, rely=0.5)
    label_m_pw = ttk.Label(master=root, text='Master Password :', font=('Calibri', 15))
    label_m_pw.place(relx=0.0, rely=0.6)
    name_e = ttk.Entry(master=root, textvariable=tk.StringVar, font=('Calibri', 15))
    name_e.place(relx=0.3, rely=0.5)
    master_pw_e = ttk.Entry(master=root, textvariable=tk.StringVar, font=('Calibri', 15), show="*")
    master_pw_e.place(relx=0.3, rely=0.6)
    button_next = ttk.Button(master=root, text='  Next  ', command=button_next)
    button_next.place(relx=0.4, rely=0.8)
    button_exit = ttk.Button(master=root, text='  exit  ', command=root.destroy)
    button_exit.place(relx=0.6, rely=0.8)

    window('Login Information', (600, 300))

    global username
    username = name_e.get()
    masterpwd_un = master_pw_e.get()
    masterpwd = hash_password(masterpwd_un)  # hashing the enterd Password

    try:
        filename = f'.\\jsonfile\\{username}_data.json'
        with open(filename, 'r') as file:
            user_data = json.load(file)
            json_master_pw = user_data['master_pwd']
            if masterpwd == json_master_pw:  # vergleich enterd Password(gehashed) mit gespeichert Password(gehasht)

                rahmen()
                print('\n')
                print(f'welcommen {username}')
                print('\n')
                rahmen()
                print('\n')
                user_Choice()
            else:
                messagebox.showerror(title='Error', message='Password stimmt nicht,bitte versuchen Sie nochmal ')
                user_login()
            return username
    except:
        messagebox.showerror(title='Error', message='Falsche Username ,bitte versuchen Sie nochmal')
        user_login()


# Account Information in Json File speicheren,mit der username, 3 option für password ,selbst password,generated password,encrepted password
# Hier wird die Login Information gespeichert ,Account ,User-ID,Website Link(if any) ,und password ,
# hier hat der User 3 Option für seine Password (eigene text Password ,
# Complex password bei password Generator function zu erstellen,oder encrepted Password zu erstellen .

def add_pwd_account():


    def bu_next():
        e_enc.place_forget()
        e_userid.place_forget()
        e_web.place_forget()
        e_account.place_forget()
        e_pw.place_forget()
        ueser_id.place_forget()
        label_pw.place_forget()
        label_enc.place_forget()
        label_web.place_forget()
        label_txt.place_forget()
        account_name.place_forget()
        button_next.place_forget()
        button_exit.place_forget()
        radio_pw1.place_forget()
        radio_pw2.place_forget()
        radio_pw3.place_forget()
        root.quit()
        return

    label_txt = ttk.Label(master=root,text=f' hallo {username.title()},bitte geben Sie Ihre Login Account Information ',
                          font=('Calibri', 15), foreground='green')
    label_txt.place(relx=0.0, rely=0.2)
    account_name = ttk.Label(master=root, text='Account Name :', font=('Calibri', 15))
    account_name.place(relx=0.0, rely=0.3)
    ueser_id = ttk.Label(master=root, text=' User ID :', font=('Calibri', 15))
    ueser_id.place(relx=0.0, rely=0.4)
    label_web = ttk.Label(master=root, text=' Websit Adresse :', font=('Calibri', 15))
    label_web.place(relx=0.0, rely=0.5)
    label_pw = ttk.Label(master=root, text=' Password :', font=('Calibri', 15))
    label_pw.place(relx=0.0, rely=0.6)
    label_enc = ttk.Label(master=root, text=' Encrepted Password(True/False) :', font=('Calibri', 14))
    label_enc.place(relx=0.0, rely=0.8)
    account_var = tk.StringVar()
    e_account = ttk.Entry(master=root, font=('Calibri', 15), textvariable=account_var)
    e_account.place(relx=0.3, rely=0.3)
    userid_var = tk.StringVar()
    e_userid = ttk.Entry(master=root, font=('Calibri', 15), textvariable=userid_var)
    e_userid.place(relx=0.3, rely=0.4)
    web_var = tk.StringVar()
    e_web = ttk.Entry(master=root, font=('Calibri', 15), textvariable=web_var)
    e_web.place(relx=0.3, rely=0.5, width=500)
    password_var = tk.StringVar()
    e_pw = ttk.Entry(master=root, font=('Calibri', 15), textvariable=password_var)
    e_pw.place(relx=0.3, rely=0.6)
    enc_var = tk.StringVar()
    radio_account_ch = tk.IntVar()
    radio_pw1 = tk.Radiobutton(master=root, text=' eigene pasword', font=('Calibri', 14), variable=radio_account_ch,
                               value=1)
    radio_pw1.place(relx=0.2, rely=0.7)
    radio_pw2 = tk.Radiobutton(master=root, text='Generated Komplex Password', font=('Calibri', 14),
                               variable=radio_account_ch, value=2)
    radio_pw2.place(relx=0.4, rely=0.7)
    radio_pw3 = tk.Radiobutton(master=root, text='encrepted Password', font=('Calibri', 14), variable=radio_account_ch,
                               value=3)

    radio_pw3.place(relx=0.7, rely=0.7)
    e_enc = ttk.Entry(master=root, font=('Calibri', 15), textvariable=enc_var)
    e_enc.place(relx=0.3, rely=0.8)
    print(radio_account_ch)
    button_next = ttk.Button(master=root, text=' Next  ', command=bu_next)
    button_next.place(relx=0.4, rely=0.9)
    button_exit = ttk.Button(master=root, text=' Exit  ', command=root.destroy)
    button_exit.place(relx=0.55, rely=0.9)
    window('User Login  Information ', (900, 600))
    account = e_account.get()
    userid = e_userid.get()
    website = e_web.get()
    pass_choice = radio_account_ch.get()
    if pass_choice == 1:
        password = e_pw.get()
        enc = 'False'
        dict_user = {'Account': account, 'User_Id': userid, 'Website': website, 'Password': password,
                     'encrepted': enc}
        print(dict_user)
        filename = f'.\\jsonfile\\{username}_pw_data.json'
        data_json = []
        with open(filename, 'r') as file:
            data_json = json.load(file)
            data_json.append(dict_user)
        with open(filename, 'w') as file:
            data_json = json.dump(data_json, file, indent=4)
            file.close()
        messagebox.showinfo(message=f'den Login Info für den Account {account}  wurde erfolgreich gespeichert ')
        bu_next()
        user_Choice()

    elif pass_choice == 2:
        enc = 'False'
        pdw_new()
        password = pyperclip.paste()
        dict_user = {'Account': account, 'User_Id': userid, 'Website': website, 'Password': password,
                     'encrepted': enc}
        print(dict_user)
        filename = f'.\\jsonfile\\{username}_pw_data.json'
        data_json = []
        with open(filename, 'r') as file:
            data_json = json.load(file)
            data_json.append(dict_user)
        with open(filename, 'w') as file:
            data_json = json.dump(data_json, file, indent=4)
            file.close()
        messagebox.showinfo(message=f'den Login Info für den Account {account}  wurde erfolgreich gespeichert ')
        bu_next()
        user_Choice()
        # print(password)
    else:
        pass_choice == 3
        enc = 'True'
        security_pwd()
        password = pyperclip.paste()
        dict_user = {'Account': account, 'User_Id': userid, 'Website': website, 'Password': password,  'encrepted': enc}
        print(dict_user)
        filename = f'.\\jsonfile\\{username}_pw_data.json'
        data_json = []
        with open(filename, 'r') as file:
            data_json = json.load(file)
            data_json.append(dict_user)
        with open(filename, 'w') as file:
            data_json = json.dump(data_json, file, indent=4)
            file.close()
        messagebox.showinfo(message=f'den Login Info für den Account {account}  wurde erfolgreich gespeichert ')
        bu_next()
        user_Choice()

    return


# password Erstellung :gefragt wird :Length,Gross letter length ,:Digit length,sonderzeichung length
def pdw_new():
    def button_next():
        label_pw.place_forget()
        label_pw_l.place_forget()
        label_pw_d.place_forget()
        label_pw_sz.place_forget()
        label_pw_gl.place_forget()
        lang_e.place_forget()
        gl_e.place_forget()
        d_e.place_forget()
        sz_e.place_forget()
        button_generate.destroy()
        button_exit.destroy()
        button_next.destroy()
        label_pw_gen.place_forget()
        label_gen.place_forget()
        #root.quit()
        ask= messagebox.askquestion(message='ein Kopie von Ihre Passwoprd wurde im Clipboard,hinzugefüt,wollen Sie fortsetzen \n ')
        if ask=='yes':
            user_Choice()
        elif ask== 'no':
            root.destroy()
        return password

    def pw_gen():
        length = len_gl = len_dig = len_sym = 0
        while length < 12:
            length = int(lang_e.get())

        while len_gl < 1:
            len_gl = int(gl_e.get())

            if len_gl > length:
                messagebox.showerror(title='Error', message='Falsche Eingabe ,bitte versuchen Sie nochmal ')

                pdw_new()
        while len_dig < 1:
            len_dig = int(d_e.get())

            if len_dig > length:
                messagebox.showerror(title='Error', message='Falsche Eingabe ,bitte versuchen Sie nochmal ')
                pdw_new()
        while length > len_sym < 1:
            len_sym = int(sz_e.get())


            if len_sym > length:
                messagebox.showerror(title='Error', message='Falsche Eingabe ,bitte versuchen Sie nochmal ')
                pdw_new()
        pwd = []
        pwd_gl = []
        pwd_sl = []
        pwd_di = []
        pwd_sym = []
        len_sl = int(length - len_gl - len_sym - len_dig)

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
        password_var.set(password)
        label_pw_gen["state"] = "readonly"
        pyperclip.copy(password)

        return password

    length = len_gl = len_dig = len_sym = tk.IntVar

    label_pw = ttk.Label(master=root,
                         text=f'\n{username.title()},geben Sie bitte die folgende Angabe  für Ihre gewünschte Password ,\n nach Angabe drücken Sie auf ""Generate Password""\n  Button,wird Ihre Password dort angezeigt ',
                         font=('Calibri', 14), foreground='green')
    label_pw.place(relx=0.0, rely=0.2)
    label_pw_l = ttk.Label(master=root, text='Gewünchte Länge(min 12)  :', font=('Calibri', 15))
    label_pw_l.place(relx=0.0, rely=0.4)
    label_pw_gl = ttk.Label(master=root, text=' Zahle den grosse Buchstaben-GB (< 12) :', font=('Calibri', 15))
    label_pw_gl.place(relx=0.0, rely=0.5)
    label_pw_d = ttk.Label(master=root, text=' Zahle den Digits-D (< (12-Gb)) :', font=('Calibri', 15))
    label_pw_d.place(relx=0.0, rely=0.6)
    label_pw_sz = ttk.Label(master=root, text=' Zahle den Sonder Zeichen-SZ (<(12-GB-D)) :', font=('Calibri', 15))
    label_pw_sz.place(relx=0.0, rely=0.7)
    lang_e = ttk.Entry(master=root, font=('Calibri', 15))
    lang_e.place(relx=0.6, rely=0.4, width=60)
    gl_e = ttk.Entry(master=root, font=('Calibri', 15))
    gl_e.place(relx=0.6, rely=0.5, width=60)
    d_e = ttk.Entry(master=root, font=('Calibri', 15))
    d_e.place(relx=0.6, rely=0.6, width=60)
    sz_e = ttk.Entry(master=root, font=('Calibri', 15))
    sz_e.place(relx=0.6, rely=0.7, width=60)
    label_gen = ttk.Label(master=root, text=' Generated Password :', font=('Calibri', 15))
    label_gen.place(relx=0.0, rely=0.8)
    password_var = tk.StringVar()
    label_pw_gen = ttk.Entry(master=root, font=('Calibri', 15), textvariable=password_var)
    label_pw_gen.place(relx=0.4, rely=0.8)
    button_generate = ttk.Button(master=root, text='  Generate Password  ', command=pw_gen)
    button_generate.place(relx=0.3, rely=0.9)
    button_next = ttk.Button(master=root, text=' Next  ', command=button_next)
    button_next.place(relx=0.5, rely=0.9)
    button_exit = ttk.Button(master=root, text=' Exit  ', command=root.destroy)
    button_exit.place(relx=0.65, rely=0.9)
    password = password_var.get()
    window('Password Generator', (600, 600))
    print(password)
    return password


def get_data_info(result, result_len):

    def next_():
        e_enc.place_forget()
        e_userid.place_forget()
        e_web.place_forget()
        e_account.place_forget()
        e_pw.place_forget()
        ueser_id.place_forget()
        label_pw.place_forget()
        label_enc.place_forget()
        label_web.place_forget()
        label_txt.place_forget()
        account_name.place_forget()
        button_next.place_forget()
        button_exit.place_forget()
        messagebox.showinfo(message='ein Kopie von diese Passwoprd wurde im Clipboard,hinzugefüt')
        root.quit()
        return

    account = result['Account']
    label_txt = ttk.Label(master=root,text=f' hallo {username.title()},diese sind die Login Information für  {account} Account \n,es gibt {result_len} Ergebnisse für diese Account,**nutzen Sie Bitte Next Button',
                          font=('Calibri', 15), foreground='green')
    label_txt.place(relx=0.0, rely=0.2)
    account_name = ttk.Label(master=root, text='Account Name :', font=('Calibri', 15))
    account_name.place(relx=0.0, rely=0.4)
    ueser_id = ttk.Label(master=root, text=' User ID :', font=('Calibri', 15))
    ueser_id.place(relx=0.0, rely=0.5)
    label_web = ttk.Label(master=root, text=' Websit Adresse :', font=('Calibri', 15))
    label_web.place(relx=0.0, rely=0.6)
    label_pw = ttk.Label(master=root, text=' Password :', font=('Calibri', 15))
    label_pw.place(relx=0.0, rely=0.7)
    label_enc = ttk.Label(master=root, text=' Encrepted Password(True/False) :', font=('Calibri', 14))
    label_enc.place(relx=0.0, rely=0.8)
    account_var = tk.StringVar()
    e_account = ttk.Entry(master=root, font=('Calibri', 15), textvariable=account_var)
    e_account.place(relx=0.3, rely=0.4)
    userid_var = tk.StringVar()
    e_userid = ttk.Entry(master=root, font=('Calibri', 15), textvariable=userid_var)
    e_userid.place(relx=0.3, rely=0.5)
    web_var = tk.StringVar()
    e_web = ttk.Entry(master=root, font=('Calibri', 15), textvariable=web_var)
    e_web.place(relx=0.3, rely=0.6, width=500)
    password_var = tk.StringVar()
    e_pw = ttk.Entry(master=root, font=('Calibri', 15), textvariable=password_var)
    e_pw.place(relx=0.3, rely=0.7, width=500)
    enc_var = tk.StringVar()
    e_enc = ttk.Entry(master=root, font=('Calibri', 15), textvariable=enc_var)
    e_enc.place(relx=0.3, rely=0.8)
    button_next = ttk.Button(master=root, text=' Next  ', command=next_)
    button_next.place(relx=0.4, rely=0.9)
    #button_show = ttk.Button(master=root, text='Show Info  ', command=button_show)
    #button_show.place(relx=0.5, rely=0.9)
    button_exit = ttk.Button(master=root, text=' Exit  ', command=root.destroy)
    button_exit.place(relx=0.6, rely=0.9)

    web_var.set(result['Website'])
    password_var.set(result['Password'])
    password = result['Password']
    pyperclip.copy(password)
    account_var.set(result['Account'])
    userid_var.set(result['User_Id'])
    enc_var.set(result['encrepted'])

    window('User Login  Information ', (800, 600))
    return


# Login inforamation Suche ,falls nicht gefunden ,die gesamt user login info wird gedrückt als option
def get_data():
    def butt_next():
        account_info = e_account.get()
        label_suche.place_forget()
        label_account.place_forget()
        e_account.place_forget()
        button_exit.destroy()
        button_next.destroy()
        user_dict = {}
        filename = f'.\\jsonfile\\{username}_pw_data.json'
        with open(filename, 'r') as file:
            user_dict = json.load(file)
            result_list = list(filter(lambda item: item['Account'] == account_info, user_dict))
            # result = next(item for item in user_dict if item["Account"] == account_info)
            result_len = len(result_list)
            if result_len != 0:
                print(list(result_list))
                print(result_len)
                for result in result_list:
                    print(result)
                    get_data_info(result, result_len)
            else:
                messagebox.showerror(title='Account Suche Error', message='keine Account mit dieser Name gefunden')

            user_Choice()

    label_suche = ttk.Label(master=root, text='\n Bitte geben Sie die Account Name ,die suchen wollen ',
                            font=('Calibri', 15), foreground='green')
    label_suche.place(relx=0.0, rely=0.2)
    label_account = ttk.Label(master=root, text=' Account Name :', font=('Calibri', 15))
    label_account.place(relx=0.0, rely=0.5)
    e_account = ttk.Entry(master=root, font=('Calibri', 15))
    e_account.place(relx=0.3, rely=0.5)
    button_next = ttk.Button(master=root, text=' Next  ', command=butt_next)
    button_next.place(relx=0.4, rely=0.75)
    button_exit = ttk.Button(master=root, text=' Exit  ', command=root.destroy)
    button_exit.place(relx=0.55, rely=0.75)

    window('Suche Account Information ', (500, 200))


# Generieren den symmetric Key für die Encreption ,using cryptography.fernet,der Key wird für jede User einmal erstellet
# und mit file von username gespeichert
def key_generator():
    key_file = rf".\key\{username}_key"
    key = Fernet.generate_key()
    with open(key_file, 'wb') as key_file:
        key_file.write(key)
        messagebox.showinfo(title='neue Key', message='ein neue encreption Key wurde erstellet')

    user_Choice()


# encrepted von Password using the gespeichert generated key in der key file(mit der username)
def security_pwd():
    def button_next():
        label_enc_txt.place_forget()
        label_pw.place_forget()
        label_enc_pw.place_forget()
        pwd_e.place_forget()
        e_pw_enc.place_forget()
        button_next.destroy()
        button_enc.destroy()
        button_exit.destroy()
        ask = messagebox.askquestion(message='ein Kopie von Ihre Passwoprd wurde im Clipboard,hinzugefüt,wollen Sie fortsetzen \n ')
        if ask == 'yes':
            user_Choice()
        elif ask == 'no':
            root.destroy()
        return

    def button_enc():
        key_file = rf".\key\{username}_key"
        with open(key_file, 'rb') as key_file:
            key = key_file.read()
        cipher = Fernet(key)
        password = pwd_e.get()
        new_enc_password = (cipher.encrypt(password.encode()).decode())
        enc_e_var.set(new_enc_password)
        password = new_enc_password
        pyperclip.copy(password)
        return password

    label_enc_txt = ttk.Label(master=root,text='\n Bitte geben Sie das Password,was Sie verschlüsseln möchten(Encryption)',font=('Calibri', 15), foreground='green')
    label_enc_txt.place(relx=0.0, rely=0.2)
    label_pw = ttk.Label(master=root, text='Password :', font=('Calibri', 15))
    label_pw.place(relx=0.0, rely=0.5)
    label_enc_pw = ttk.Label(master=root, text='Encrepted  Password :', font=('Calibri', 15))
    label_enc_pw.place(relx=0.0, rely=0.6)
    pwd_e = ttk.Entry(master=root, textvariable=tk.StringVar, font=('Calibri', 15))
    pwd_e.place(relx=0.25, rely=0.5)
    enc_e_var = tk.StringVar()
    e_pw_enc = ttk.Entry(master=root, textvariable=enc_e_var, font=('Calibri', 15))
    e_pw_enc.place(relx=0.25, rely=0.6, width=550)
    button_enc = ttk.Button(master=root, text='  encreypt  ', command=button_enc)
    button_enc.place(relx=0.4, rely=0.8)
    button_next = ttk.Button(master=root, text='  Next  ', command=button_next)
    button_next.place(relx=0.5, rely=0.8)
    button_exit = ttk.Button(master=root, text='  Exit  ', command=root.destroy)
    button_exit.place(relx=0.6, rely=0.8)

    window('Password Encreption ', (800, 300))
    passw = enc_e_var.get()
    return str(passw)


# hier kann man über copy von encrepted Pasword ,der original passwpord zu erhalten ,z.b zum test option 3 Ergebnisse ,oder von output von get login information dictionary ,
# zuerst copieren und nacher hier bei option 4 ,der Original password erhalten , leider gabe es nicht der Zeit für decreption  von encrepted gespeicherte Passworde direckt von json datei,leider muss mann händische kopieren
def security_pwd_decreption():
    def button_next():
        label_enc_txt.place_forget()
        label_pw.place_forget()
        label_dec_pw.place_forget()
        pwd_e.place_forget()
        e_pw_dec.place_forget()
        button_next.destroy()
        button_exit.destroy()
        button_dec.destroy()
        root.quit()
        user_Choice()

    def button_dec():
        key_file = rf".\key\{username}_key"
        with open(key_file, 'rb') as key_file:
            key = key_file.read()
        cipher = Fernet(key)
        enc_password = pwd_e.get()
        original_password = (cipher.decrypt(enc_password.encode()).decode())
        dec_e_var.set(original_password)

    label_enc_txt = ttk.Label(master=root, text='\n Bitte geben Sie Ihre verschlüsselte  Password,um zu entschlüsseln (Decryption)  ',
                              font=('Calibri', 15), foreground='green')
    label_enc_txt.place(relx=0.0, rely=0.2)
    label_pw = ttk.Label(master=root, text='Encrepted Password :', font=('Calibri', 15))
    label_pw.place(relx=0.0, rely=0.5)
    label_dec_pw = ttk.Label(master=root, text='Decrepted  Password :', font=('Calibri', 15))
    label_dec_pw.place(relx=0.0, rely=0.6)
    pwd_e = ttk.Entry(master=root, textvariable=tk.StringVar, font=('Calibri', 15))
    pwd_e.place(relx=0.25, rely=0.5, width=600)
    dec_e_var = tk.StringVar()
    e_pw_dec = ttk.Entry(master=root, textvariable=dec_e_var, font=('Calibri', 15))
    e_pw_dec.place(relx=0.25, rely=0.6, )
    button_dec = ttk.Button(master=root, text='  decreypt ', command=button_dec)
    button_dec.place(relx=0.4, rely=0.8)
    button_next = ttk.Button(master=root, text='  Next ', command=button_next)
    button_next.place(relx=0.5, rely=0.8)
    button_exit = ttk.Button(master=root, text='  Exit ', command=root.destroy)
    button_exit.place(relx=0.6, rely=0.8)

    window('Password Decreption ', (800, 300))
    return


###Choice für login oder registeration oder exit
def login_Choice():
    def buttom_ok():
        radio_opt1.place_forget()
        radio_opt2.place_forget()
        radio_opt3.place_forget()
        label_option.place_forget()
        button_ok.destroy()
        root.quit()

    label_option = ttk.Label(master=root,
                             text='\n Bitte wählen Sie ein Login  Option : \n **(bei Neue User wählen  Sie sich bitte:Registration)',
                             font=('Calibri', 15), foreground='green')
    label_option.place(relx=0.0, rely=0.2)
    radio_choice = tk.IntVar()
    radio_opt1 = tk.Radiobutton(master=root, text='Registration', font=('Calibri', 14), variable=radio_choice, value=1)
    radio_opt2 = tk.Radiobutton(master=root, text='login', font=('Calibri', 14), variable=radio_choice, value=2)
    radio_opt3 = tk.Radiobutton(master=root, text='exit', font=('Calibri', 14), variable=radio_choice, value=3)
    radio_opt1.place(relx=0.0, rely=0.5)
    radio_opt2.place(relx=0.0, rely=0.6)
    radio_opt3.place(relx=0.0, rely=0.7)
    button_ok = ttk.Button(master=root, text='Next', command=buttom_ok)
    button_ok.place(relx=0.4, rely=0.9)

    window('Welcom to Password Manager', (600, 300))
    login_choice = radio_choice.get()

    if login_choice == 1:
        user_register_json()
    elif login_choice == 2:
        user_login()
    elif login_choice == 3:
        root.destroy()


# Nach Login die Option für die User ,damit kommt hier ,neue Komplex password, neue encrepted password ,oder decreption von schon encrepted password
# neue logine Information,und hier hat nochmal der user die option von Komplex oder encrepted password password zu erstellen.
# noch kann der user seine gespeicherte login Information
def user_Choice():
    def button_ok_ch():
        radio_ch1.place_forget()
        radio_ch2.place_forget()
        radio_ch3.place_forget()
        radio_ch4.place_forget()
        radio_ch5.place_forget()
        radio_ch6.place_forget()
        radio_ch7.place_forget()
        label_u_option.destroy()
        button_ok_ch.destroy()
        button_exit.destroy()
        root.quit()

    label_u_welcom = ttk.Label(master=root, text=f'\n Welcome {username.title()}', font=('Calibri', 16),
                               foreground='red')
    label_u_welcom.place(relx=0.3, rely=0.1, anchor='nw')
    label_u_option = ttk.Label(master=root, text='\n Was wünchen Sie von dem Password Manager ,\n',
                               font=('Calibri', 15), foreground='green')
    label_u_option.place(relx=0.0, rely=0.2)
    radio_user_ch = tk.IntVar()
    radio_ch1 = tk.Radiobutton(master=root, text=' neues Komplex Password ', font=('Calibri', 14),
                               variable=radio_user_ch,
                               value=1)
    radio_ch2 = tk.Radiobutton(master=root, text='generate ein neue key für Encreption', font=('Calibri', 14),
                               variable=radio_user_ch, value=2)
    radio_ch3 = tk.Radiobutton(master=root, text='Password Encreption', font=('Calibri', 14), variable=radio_user_ch,
                               value=3)
    radio_ch4 = tk.Radiobutton(master=root, text='Password Decreption', font=('Calibri', 14), variable=radio_user_ch,
                               value=4)
    radio_ch5 = tk.Radiobutton(master=root, text='Login Information Speichern', font=('Calibri', 14),
                               variable=radio_user_ch, value=5)
    radio_ch6 = tk.Radiobutton(master=root, text='get Login Information', font=('Calibri', 14), variable=radio_user_ch,
                               value=6)
    radio_ch7 = tk.Radiobutton(master=root, text='exit', font=('Calibri', 14), variable=radio_user_ch, value=7)
    radio_ch1.place(relx=0.0, rely=0.3)
    radio_ch2.place(relx=0.0, rely=0.4)
    radio_ch3.place(relx=0.0, rely=0.5)
    radio_ch4.place(relx=0.0, rely=0.6)
    radio_ch5.place(relx=0.0, rely=0.7)
    radio_ch6.place(relx=0.0, rely=0.8)
    radio_ch7.place(relx=0.0, rely=0.9)
    button_ok_ch = ttk.Button(master=root, text='Next', command=button_ok_ch)
    button_ok_ch.place(relx=0.4, rely=0.95)
    button_exit = ttk.Button(master=root, text='Exit Programm ', command=root.destroy)
    button_exit.place(relx=0.6, rely=0.95)
    window('User Choice', (600, 500))
    user_choice = radio_user_ch.get()
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
        root.destroy()


def main():
    login_Choice()


main()

