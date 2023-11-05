# Importing all packages
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image
import os

import mysql.connector
from tkinter.filedialog import askopenfilename, asksaveasfilename
import mysql.connector as sk
from model import *
# from send_sms import *
print('GUI SYSTEM STARTED...')
# ---------------------------------------------------------------------------------


def LogIn():
    username = box1.get()

    u = 1

    if len(username) == 0:
        u = 0
        messagebox.showinfo("Error", "You must enter something Sir")

    if u:
        password = box2.get()

        if len(password):
            query = "SELECT * FROM THEGREAT"

            sql.execute(query)

            data = sql.fetchall()

            g = 0
            b = 0

            for i in data:
                if i[0] == username:
                    g = 1
                if i[1] == password:
                    b = 1

            if g and b:
                messagebox.showinfo('Hello Sir', 'Welcome to the System')
            else:
                messagebox.showinfo('Sorry', 'Wrong Username or Password')

            global y
            y = True
        else:
            messagebox.showinfo("Error", "You must enter a password Sir!!")


def OpenFile():
    username = box1.get()
    if y:
        try:
            a = askopenfilename()
            print(a)
            value, classes = main(a)
            messagebox.showinfo(
                "your report", ("Predicted Label is ", value, "\nPredicted Class is ", classes))

            query = 'UPDATE THEGREAT SET PREDICT = "%s" WHERE USERNAME = "%s"' % (
                value, username)

            sql.execute(query)
            # print(query)
            connection.commit()

            image = Image.open(a)
            # plotting image
            file = image.convert('RGB')
            plt.imshow(np.array(file))
            plt.title(f'your report is label : {value} class : {classes}')
            plt.show()
            # print(image)
            print('Thanks for using the system !')
            # fn, text = os.path.splitext(a) #fn stands for filename
        except Exception as error:
            print("File not selected ! Exiting..., Please try again")

    else:
        messagebox.showinfo("Hello Sir", "You need to Login first")


x = 0
y = False


def Signup():
    username = box1.get()
    password = box2.get()

    u = 1

    if len(username) == 0 or len(password) == 0:
        u = 0
        messagebox.showinfo("Error", "You must enter something Sir")

    if u:
        query1 = "SELECT * FROM THEGREAT"
        sql.execute(query1)

        data = sql.fetchall()

        z = 1

        for i in data:
            if i[0] == username:
                messagebox.showinfo(
                    "Sorry Sir", "This  username is already registered, try a new one")
                z = 0

        if z:
            query = "INSERT INTO THEGREAT (USERNAME, PASSWORD) VALUES('%s', '%s')" % (
                username, password)
            messagebox.showinfo(
                "signed up", ("Hi ", username, "\n Now you can login with your credentials !"))
            sql.execute(query)
            connection.commit()


# -----------------------------------------------------------------------------------------


connection = sk.connect(
    host="localhost",
    user="root",
    password="kamwalibai",
    database="batch_db_new"
)

sql = connection.cursor()

root = Tk()

root.geometry('700x400')
root.title("Aishwarya")
root.configure(bg='lightgreen')


label1 = Label(root, text="Diabetic Retinopathy Detection", font=('Arial', 30))
label1.grid(padx=30, pady=30, row=0, column=0, sticky='W')

label2 = Label(root, text="Enter your username: ", font=('Arial', 20))
label2.grid(padx=10, pady=10, row=1, column=0, sticky='W')

label3 = Label(root, text="Enter your password: ", font=('Arial', 20))
label3.grid(padx=10, pady=20, row=2, column=0, sticky='W')

box1 = Entry(root)
box1.grid(row=1, column=1)

box2 = Entry(root, show='*')
box2.grid(row=2, column=1)

button3 = Button(root, text="Signup", command=Signup)
button3.grid(padx=10, pady=20, row=3, column=1)

button1 = Button(root, text="LogIn", command=LogIn)
button1.grid(padx=10, pady=20, row=3, column=2)

button2 = Button(root, text="Upload Image", command=OpenFile)
button2.grid(padx=10, pady=20, row=2, column=3)


root.mainloop()
