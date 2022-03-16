import mysql.connector
db=mysql.connecter.connect(host="192.168.1.39",user="User",passwd="123456",database="Calorify1")
cusor1=db.cursor()
cursor2=db.cursor()
cursor.execute("SELECT Food name FROM Calorify1")
result1=mycursor.fetchall()


import tkinter
import os


def Register():
    global face
    face=tkinter.Tk()
    face.geometry("300x300")
    face.title("Calorify")
    face.configure(bg="white")
    
    global uname_entry
    global pword_entry
    global password
    global username
    username=tkinter.StringVar()
    password=tkinter.StringVar()
    

    reg_lbl=tkinter.Label(face, text="Registeration Page").grid(row=0,column=1)
    name_label=tkinter.Label(face,text="Name *").grid(row=1,column=0)
    name=tkinter.Entry(face, width=20).grid(row=1,column=1)
    age_label=tkinter.Label(face, text="Age *").grid(row=2,column=0)
    age1=tkinter.Entry(face, width=4).grid(row=2, column=1)
    weight_label=tkinter.Label(face, text="Weight(in Kg's) ").grid(row=3,column=0)
    weight_label=tkinter.Entry(face, width=20).grid(row=3, column=1)
    uname_label=tkinter.Label(face, text="Username *").grid(row=4,column=0)
    uname_entry=tkinter.Entry(face, textvariable=username, width=20)
    uname_entry.grid(row=4,column=1)
    pword_label=tkinter.Label(face, text="Password *").grid(row=5,column=0)
    pword_entry=tkinter.Entry(face, textvariable=password, width=20)
    pword_entry.grid(row=5, column=1)
    pconfrm_label=tkinter.Label(face, text="Confirm Password *").grid(row=6, column=0)
    pconfrm=tkinter.Entry(face, width=20).grid(row=6, column=1)
    cnfrm_btn=tkinter.Button(face, text="Submit", command=add).grid(row=7, column=1)
    
def add():
    username_info=uname_entry.get()
    password_info=pword_entry.get()
    file=open(username_info,"a")
    file.write(username_info+'\n')
    file.write(password_info)
    

    uname_entry.delete(0, tkinter.END)
    pword_entry.delete(0, tkinter.END)
    Finally=tkinter.Label(face, text="Registration succesful",fg="green").grid(row=9, column=1)



def LOGIN():
    global screen2
    screen2=tkinter.Toplevel(screen)
    screen2.title("Calorify")
    screen2.geometry("300x150")
    lgn=tkinter.Label(screen2, text="Login Page")
    info=tkinter.Label(screen2, text="Please enter details below to login").pack()
    
    global username_verify
    global password_verify
    username_verify=tkinter.StringVar()
    password_verify=tkinter.StringVar()
    
    global uname_lgnentry
    global pword_lgnentry
    
    uname_lgn=tkinter.Label(screen2, text="Username *").pack()
    uname_lgnentry=tkinter.Entry(screen2,textvariable=username_verify, width=20)
    uname_lgnentry.pack()
    pname_lgn=tkinter.Label(screen2, text="Password *").pack()
    pname_lgnentry=tkinter.Entry(screen2,textvariable=password_verify, width=20)
    pname_lgnentry.pack()
    lgn_btn=tkinter.Button(screen2, text="Login", command=ok).pack()
        
def ok():
    uname1=username_verify.get()
    pword1=password_verify.get()
    uname_lgnentry.delete(0, tkinter.END)
    uname_lgnentry.delete(0, tkinter.END)
    
    list_of_files=os.listdir()
    if uname1 in list_of_files:
        file1=open(uname1,'r')
        verify=file1.read().splitlines()
        if pword1 in verify:
            print("sucess")
        else:
            print("Username and password do not match")
    else:
        print("Username incorrect")
def begin():
    global Height_entry
    global Age_entry
    global Weight_entry
    global tkt
    scrn=tkinter.Tk()
    scrn.geometry("300x300")
    scrn.title("Calorify")
    scrn.configure(bg="white")
    begin_label=tkinter.Label(face,text="Personal Details").grid(row=0,column=1)
    Age_label=tkinter.Label(face,text="Age :").grid(row=1,column=0)
    Age_entry=tkinter.Entry(face,width=20).grid(row=1,column=1)
    Gender_entry=tkinter.Label(face,text="Gender").grid(row=2,colum=0)
    Gender_entry=tkinter.Entry(face,width=20).grid(row=2,column=1)
    Weight_label=tkinter.Label(face,text="Weight(in Kg's):").grid(row=3,column=0)
    Weight_entry=tkinter.Entry(face,width=20).grid(row=3,column=1)
    Height_label=tkinter.Label(face,text="Height(in m's):").grid(row=4,column=0)
    Height_entry=tkinter.Entry(face,width=20).grid(row=4,column=1)
    bmi_btn=tkinter.Button(face,text="Calculate BMI",command=BMI).grid(row=5,column=1)
    tkt="Your age is",Age_entry,"your gender is",Gender_entry,"and your BMI is",bmi,"."
    
def BMI():
    bmi=Weight_entry/(height_entry**2)
    
    pf=tkinter.Tk()
    pf.geometry("300x300")
    pf.title("Calorify")
    pf.configure(bg="white")
    pf2_label=tkinter.Label(face,text=tkt).grid(row=2,column=0)
    start=tkinter.Button(face,text="Enter Calorie caculator",command=bs).grid(row=3,column=1)
    
def bs():
    global selection
    cap=tkinter.Tk()
    cap.geometry("900x900")
    cap.title("Calorify")
    cap.configure(bg="white")
    cap_Inst=tkinter.Label(face,text="Please select your food items from the dropdown list").grid(row=0,column=1)
    cap_inst=tkinter.Label(face,text="All calorific values are for 100 grams").grid(row=1,column=1)
    clicked=StringVar()
    clicked.set("Select Food Item")
    selection=tkinter.OptionsMenu(face,clicked,'Bottle Gourd','Alchohol','Aloo Parantha','Apple','Banana','Beans','Beer','Bitter Gourd','Black Tea','Boiled Egg','Boiled Rice','Bread','Brinjal','Broccoli','Butter','Butter Chicken', 'Butter Naan','Cabbage','Cappucino','Capsicum','Cauliflower','Cereal/Oats with Milk', 'Cheese','Cherries ','Chicken Curry','Chicken Tikka Masala','Cold Drink','Cooked Chicken','Cooked Pork','Crab','Cream','Curd','Dal/Lentils','Drumsticks','Egg','Flavoured Milk ','French Beans','Fried Chicken','Fried Egg''Fried Fish','Fried Potato','Fried Rice','Fruit Juice','Ghee','Grapes','Green Peas','Green Tea','Guava','Idly','Kidney Beans','Lady\'s Finger','Lemon','Litchi','Mango','Masala Dosa','Mashed Potato','Meat','Melon','Milk Tea','Milkshake','Mixed Veggies','Mushrooms','Mutton Biryani','Naan','Omelette','Orange','Palak Paneer','Paneer','Papas','Parantha','Pav','Peach','Pear','Pickle','Plain Dosa','Plain MIlk','Pomegranate','Pomfret','Prawns','Pumpkin','Puri','Radish','Ragi','Ridge Gourd', 'Roti', 'Salad', 'Salmon', 'Sambar', 'Scrambled Egg','Soda','Soup', 'Soya Beans','Spinach', 'Sprouts','Squid', 'Strawberry', 'Sugar', 'Sweet Potato', 'Tandoori Chicken', 'Tender Cocnut','Tomato','Vegetable Curry','Vegetable Rice', 'Vermicelli', 'Watermelon', 'Whole Milk','Zucchini')
    food_submit=tkinter.Button(face,text="Add food item",command=cal).grid(row=3,column=0)
    final_submit=tkinter.Button(face,text="Get total calorie intake",command=gp).grid(row=3,column=1)

def cal():
    global calsum
    calsum=0
    for selection in result1:
        cursor2.execute("SELECT calorie valuescol FROM Calorify1 WHERE Food name= selection")
        result2=cursor2.selectone
        calsum+=selection
    
def gp():
    thend="Your total calorie intake for today is :",calsum
    final_face=tkinter.Tk()
    final_face.geometry("900x900")
    final_face.title("Calorify")
    final_face.configure(bg="white")
    final_label-tkinter.Label(face,text=thend).grid(row==1,column=0)
    thanx=tkinter.Label(face,text="Thank you for using Calorify").grid(row=2,column=1)
    
    


     

screen=tkinter.Tk()
screen.geometry("300x150")
screen.title("Calorify")
Label_header=tkinter.Label(screen, text="Calorify",font=20).pack()
Label_subheader=tkinter.Label(screen, text="Your Calorie Tracker",font=13).pack()
login_btn=tkinter.Button(screen, text="Login", command=LOGIN).pack()
rgister_btn=tkinter.Button(screen,text="Register", command=Register).pack()    
