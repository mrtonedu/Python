import random
from tkinter import *
from tkinter import messagebox
from random import randint
mypass=Tk()
mypass.geometry('550x400')
mypass.minsize(550,400)
mypass.maxsize(550, 400)

mypass.title("Password Manager")
mypass.config(padx=20,pady=20,bg="#101A65")
canvas=Canvas(height=200, width=200)
logo_img=PhotoImage(file="./source/download.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


def generate():
    letters = ("QWERTYUIOPASDFGHJKLZXCVBNM")
    lowletters = ("qwertyuiopasdfghjklzxcvbnm")
    numbers = "1234567890"
    symbols = "!@#$%^&*_"

    def glet():
        gletter = randint(0, 25)
        return str(letters[gletter])

    def gllet():
        glletter = randint(0, 25)
        return (lowletters[glletter])

    def gnum():
        gnumber = randint(0, 9)
        return str(numbers[gnumber])

    def gsym():
        gsymbols = randint(0, 8)
        return (symbols[gsymbols])

    def allgen():
        password = ""
        for i in range(1, 9):
            radio = randint(1, 4)
            if radio == 1:
                a = glet()
                password = f"{password}{a}"
            elif radio == 2:
                a = gnum()
                password = f"{password}{a}"
            elif radio == 3:
                a = gsym()
                password = f"{password}{a}"
            elif radio == 4:
                a = gllet()
                password = f"{password}{a}"

        return password

    password = allgen()
    password_entry.delete(0,END)
    password_entry.insert(0,password)



    password_entry.delete(0,END)
    password_entry.insert(0,password)

def save():
    web=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    message=f"------------------------------------------------------------------\nWebsite:{web}\nUsername:{email}\nPassword:{password}\n"
    if len(web)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS",message="Please make sure you haven't left any fields empty.")
    else:
        messagebox.showinfo(title="Title",message=f"These are the details entered:\nWebsite:{web}\nUsername:{email}\nPassword:{password}")

    with open("./source/password.txt",'a') as data_file:
        data_file.write(message)
        website_entry.delete(0,END)
        email_entry.delete(0,END)
        password_entry.delete(0,END)


#Labels
website_label=Label(text="Website",bg="#101A65",fg="#FAFAFA",font=("Helvetica",14))
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username",bg="#101A65",fg="#FAFAFA",font=(("Helvetica",14)))
email_label.grid(row=2,column=0)
password_label=Label(text="Password",bg="#101A65",fg="#FAFAFA",font=(("Helvetica",14)))
password_label.grid(row=3,column=0)


#Entries
website_entry=Entry(width=30,font=("Consolas",9,'bold'))
website_entry.focus()
website_entry.grid(row=1,column=1)
email_entry=Entry(width=30,font=("Consolas",9,'bold'))
email_entry.insert(0,"someone@gmail.com")
email_entry.grid(row=2,column=1)
password_entry=Entry(width=30,font=("Consolas",9,'bold'))
password_entry.grid(row=3,column=1)


#Buttons
generate_password_button=Button(text="Generate\nPassword",command=generate,width=9,height=3,bg="#F88B01",fg="#FAFAFA",font=("Helvetica",12,'bold'))
generate_password_button.grid(row=4,column=1,sticky='w')
add_button=Button(text="Add",command=save,width=9,height=3,bg="#F88B01",fg="#FAFAFA",font=("Helvetica",12,'bold'))
add_button.grid(row=4,column=1,sticky='e')


mypass.mainloop()