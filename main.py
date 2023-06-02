from email.mime import base
from logging import exception
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import*
from PIL import Image, ImageTk
import time
import sqlite3 as sq
import datetime
import os
import sys


#connect to the salon database
conn = sq.connect('system.db')
c = conn.cursor()


c.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        username TEXT NOT NULL,
        password TEXT NOT NULL
        )
        """)

#activities tables
        #Hair.......................................................

c.execute(""" CREATE TABLE IF NOT EXISTS Hair(
        date TEXT,
        customers TEXT,
        type TEXT,
        amount INTEGER
        )""")

c.execute(""" CREATE TABLE IF NOT EXISTS Hair_Input(
        date TEXT,
        items TEXT,
        type TEXT,
        amount INTEGER
        
        )""")


        #manicure..........................................

c.execute(""" CREATE TABLE IF NOT EXISTS Manicure(
        date TEXT,
        customers TEXT,
        type TEXT,
        amount INTEGER
        )""")

c.execute(""" CREATE TABLE IF NOT EXISTS Manicure_Input(
        date TEXT,
        items TEXT,
        type TEXT,
        amount INTEGER
        
        )""")

        #Training.....................................................

c.execute(""" CREATE TABLE IF NOT EXISTS Training(
        date TEXT,
        customers TEXT,
        type TEXT,
        amount INTEGER
        )""")

c.execute(""" CREATE TABLE IF NOT EXISTS Training_Input(
        date TEXT,
        items TEXT,
        type TEXT,
        amount INTEGER
        
        )""")



        #Fields..........................

c.execute(""" CREATE TABLE IF NOT EXISTS Fields(
        date TEXT,
        customers TEXT,
        type TEXT,
        amount INTEGER
        )""")

c.execute(""" CREATE TABLE IF NOT EXISTS Fields_Input(
        date TEXT,
        items TEXT,
        type TEXT,
        amount INTEGER
        
        )""")




#Customers tables....................................
c.execute(""" CREATE TABLE IF NOT EXISTS Booking(
        name TEXT,
        service TEXT,
        date TEXT,
        time TEXT,
        contact INTEGER
        
        )""")

c.execute(""" CREATE TABLE IF NOT EXISTS Suggestions(
        name TEXT,
        service TEXT,
        date TEXT,
        time TEXT,
        contact INTEGER
        
        )""")


#Students table..................................................
c.execute(""" CREATE TABLE IF NOT EXISTS Students(
        Fname TEXT,
        Lname TEXT,
        contact INTEGER,
        home TEXT,
        parent TEXT
        
        )""")


#Products table.............................................................
c.execute(""" CREATE TABLE IF NOT EXISTS Products(
        number INTEGER,
        type TEXT,
        worth INTEGER
        )""")

#Manicure Products table.............................................................
c.execute(""" CREATE TABLE IF NOT EXISTS Man_Products(
        number INTEGER,
        type TEXT,
        worth INTEGER
        )""")

#Other Products table.............................................................
c.execute(""" CREATE TABLE IF NOT EXISTS Others(
        number INTEGER,
        type TEXT,
        worth INTEGER
        )""")


#create Admin user....................................*****************************

#c.execute(" INSERT INTO Users VALUES(:username, :password)",
#                {'username':'BanixAdmin', 'password':'admin@banix'})
#
#conn.commit()


#Management system  window
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Banix Salon Management System')
        self.config(background= '#0000cd')
        self.display_footer()
        

#********************System Menu************************************
    

        
        self.text = tk.StringVar()

#*****************************************************System layout*******************************
#********************************************************************************************************

#************************************home page*********************

        self.home_canvas = tk.Canvas(self, width=1000, height=800, bg= '#0000cd', bd=5)
        self.home_canvas.pack(fill=BOTH, expand=1)

        self.home_frame = tk.Frame(self.home_canvas, bg= '#0000cd')
        self.home_frame.pack()

        self.home_title = tk.Label(self.home_frame, text='BANIX SALON MANAGEMENT', bg= '#0000cd', fg='#ffffff')
        self.home_title.config(font=('Ubuntu', 50))
        self.home_title.pack()



        self.home_home_sub = tk.Label(self.home_frame, text='your beauty is our pride', bg= '#0000cd', fg='gold')
        self.home_home_sub.pack()
        
        self.home_image = Image.open('images/logo.png')
        self.logo = self.home_image.resize((400, 300))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(self.home_frame, image=self.logo, bd=0)
        self.logo_label.image = self.logo
        self.logo_label.pack()

#Admin Log in form...................
        self.text = 'Log In'
        self.login_form = tk.Frame(self.home_frame, bg= '#0000ff')
        self.login_form.pack(pady=30)

        self.login_legend = tk.Label(self.login_form, text='Admin Log in', bg= '#0000ff', fg='gold')
        self.login_legend.config(font=('Arial', 20))
        self.login_legend.pack(padx=20)

        self.Admin_name = tk.Label(self.login_form, text='User Name', bg= '#0000ff', fg='#ffffff')
        self.Admin_name.pack()
        self.Admin_name_entry = tk.Entry(self.login_form)
        self.Admin_name_entry.pack(pady=5, padx=10)

        self.Admin_passwrd = tk.Label(self.login_form, text='Password', bg= '#0000ff', fg='#ffffff')
        self.Admin_passwrd.pack()
        self.Admin_passwrd_entry = tk.Entry(self.login_form, show="*")
        self.Admin_passwrd_entry.pack(pady=5, padx=10)

        self.login_btn = tk.Button(self.login_form, text=self.text, fg= '#0000ff', bg="gold", width=30, command=self.login)
        self.login_btn.pack(padx=10,pady=10)




#********************Main page******************************************************
# **********************************************************************************

        self.main_canvas = tk.Canvas(self, width=1000, height=800, bd=0, bg='#0000cd')


        admin_panel = tk.Frame(self.main_canvas, bg='#ffffff', width=300, height=800)
        admin_panel.pack(side=LEFT, fill=Y)

        admin_head = tk.Label(admin_panel, text='Admin Panel', bg='#ffffff', fg='#000000')
        admin_head.config(font=('Arial', 20))
        admin_head.pack(pady=10)

        #Generate Report...................................
        gen_report = tk.Button(admin_panel, text='Generate Report', fg='#000000', bg='gold', command=lambda:
            self.Report())
        gen_report.config(font=('Arial', 10))
        gen_report.pack(pady=5)

#**********************Edit Admin*****************************************************

        edit_frame = tk.Frame(admin_panel, bg='#ffffff', highlightthickness=1, highlightbackground='#000000')
        edit_frame.pack(pady=30)

        edit_head = tk.Label(edit_frame, text='Edit Admin', fg='#ffffff', bg='#0000ff')
        edit_head.config(font=('Arial', 15))
        edit_head.pack(fill=X)

        self.edit_name_entry = tk.Entry(edit_frame)
        self.edit_name_entry.insert(0, 'Username')
        self.edit_name_entry.pack(padx=10, pady=5)

        self.new_edit_name_entry = tk.Entry(edit_frame)
        self.new_edit_name_entry.insert(0, 'New Username')
        self.new_edit_name_entry.pack(padx=10, pady=5)


        self.edit_passwrd_entry = tk.Entry(edit_frame)
        self.edit_passwrd_entry.insert(0, 'Password')
        self.edit_passwrd_entry.pack(padx=10, pady=5)

        self.new_edit_passwrd_entry = tk.Entry(edit_frame)
        self.new_edit_passwrd_entry.insert(0, 'New Password')
        self.new_edit_passwrd_entry.pack(padx=10)

        edit_btn = tk.Button(edit_frame, text='Save Edit', bg='#0000ff', fg='#ffffff', command=lambda:
                self.edit_admin())
        edit_btn.pack(pady=10)

#*****************Add Admin user***********************************

        add_frame = tk.Frame(admin_panel, bg='#ffffff', highlightthickness=1, highlightbackground='#000000')
        add_frame.pack(pady=30, padx=30)

        add_head = tk.Label(add_frame, text='Add Admin User', fg='#000000', bg='#00ff00')
        add_head.config(font=('Arial', 15))
        add_head.pack(fill=X)

        self.add_name = tk.Label(add_frame, text='User Name', fg='#000000', bg='#ffffff')
        self.add_name.pack(padx=10, pady=5)
        self.add_name_entry = tk.Entry(add_frame)
        self.add_name_entry.pack(padx=10)

        self.add_passwrd = tk.Label(add_frame, text='Password', fg='#000000', bg='#ffffff')
        self.add_passwrd.pack(padx=10, pady=5)
        self.add_passwrd_entry = tk.Entry(add_frame)
        self.add_passwrd_entry.pack(padx=10)

        edit_btn = tk.Button(add_frame, text='Add User', bg='#00ff00', fg='#000000', command=lambda:
                self.add_admin())
        edit_btn.pack(pady=10)

#******************Log out*****************************
        logout_frame = tk.Frame(admin_panel, bg='#ffffff')
        logout_frame.pack(pady=30)

        logout_btn = tk.Button(logout_frame, text='Log Out', bg='#ff0000', fg='#000000', width=15, height=2, command=lambda:
            self.logout(int(2)))
        logout_btn.pack(side=LEFT)

        power_image = Image.open('images/logout.png')
        power = power_image.resize((50, 50))
        power = ImageTk.PhotoImage(power)
        power_label = tk.Label(logout_frame, image=power, bd=0)
        power_label.image = power
        power_label.pack(side=LEFT, padx=10)


#**********************************Bussiness Panel***********************************************************

        busns_panel = tk.Frame(self.main_canvas, width=700, bg='#0000cd')
        busns_panel.pack(side=LEFT, padx=50)

#bussines  title and logo********************************
        busns_intro = tk.Frame(busns_panel, width=500, bg='#0000cd')
        busns_intro.pack(side=LEFT, pady=30)

        busns_label = tk.Label(busns_intro, text='BANIX SALON', fg='#ffffff', bg='#0000cd')
        busns_label.config(font=('Ubuntu', 50))
        busns_label.pack()

        home_image = Image.open('images/logo.png')
        logo = home_image.resize((300, 200))
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(busns_intro, image=self.logo, bd=0)
        logo_label.image = logo
        logo_label.pack()

        sub_busns = tk.Label(busns_intro, text='your beauty is our pride', bg='#0000cd', fg='gold')
        sub_busns.config(font=('Arial', 18))
        sub_busns.pack(pady=10)
#bussiness address****************************************

        address = tk.Frame(busns_panel, bg='#0000ff', width=100, highlightbackground='#000000', highlightthickness=1)
        address.pack(side=RIGHT)

        address_title = tk.Label(address, text='Address', bg='#000077', fg='#ffffff')
        address_title.config(font=('Arial', 20))
        address_title.pack(fill=X)

        location = tk.Label(address, text='Kabale Municipality', fg='#ffffff', bg='#0000ff')
        location.pack(pady=10)
        location_info = tk.Label(address, text='Lower Kigongi street, plot No.5 2nd floor', fg='#ffffff', bg='#0000ff')
        location_info.pack()

        email = tk.Label(address, text='Email: admin@banixsalon.com', fg='#ffffff', bg='#0000ff')
        email.pack(pady=10)
        website = tk.Label(address, text='website: www.banixsalon.com', fg='#ffffff', bg='#0000ff')
        website.pack()

    
    
        
    
    
#****************************************************************************

#*************************Activities Page*********************************************

#***************************************************************************************
        
        self.activity = tk.Frame(self)
        
        
        self.activity_win = tk.Canvas(self.activity,  bg='#0000cd', width=1000, height=1000, scrollregion=(0, 0, 2000, 2000))
        self.activity_win.pack(side=LEFT ,fill=BOTH, expand=1)
        
        activity_scroll = tk.Scrollbar(self.activity, orient='vertical', command=self.activity_win.yview)
        activity_scroll.pack(side=RIGHT, fill=Y)
        self.activity_win.config(yscrollcommand=activity_scroll.set)

        logo_image = Image.open('images/logo.png')
        small_logo = logo_image.resize((50, 50))
        small_logo = ImageTk.PhotoImage(small_logo)
        small_logo_label = tk.Label(self.activity_win, image=small_logo, bd=0)
        small_logo_label.image = small_logo
        small_logo_label.pack(pady=10)

        activity_title = tk.Label(self.activity_win, text='BANIX SALON', bg='#0000cd', fg='#ffffff')
        activity_title.config(font=('Ubuntu', 30))
        activity_title.pack(padx=30)
#**********************Hair Plaiting**********************************

        hair_frame = tk.Frame(self.activity_win, width=250, bg='#ffffff', highlightbackground='#0000ff', highlightthickness=1)
        hair_frame.pack(side=LEFT, fill=BOTH, expand=1)

        hair_title = tk.Label(hair_frame, text='Hair Plaiting', fg='#000000', bg='#ffffff')
        hair_title.config(font=('Arial', 20))
        hair_title.pack(fill=Y)


#track hair activity log
        hair_track = tk.Frame(hair_frame, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        hair_track.pack(pady=30, padx=30)

        hTrack_ttle = tk.Label(hair_track, text='Activity Log', fg='#ffffff', bg='#0000ff')
        hTrack_ttle.pack(fill=X)

        self.hTrack_date_entry = tk.Entry(hair_track)
        self.hTrack_date_entry.insert(0, 'Date')
        self.hTrack_date_entry.pack(padx=30, pady=10)

        self.hTrack_customers_entry = tk.Entry(hair_track)
        self.hTrack_customers_entry.insert(0, 'No. of customers')
        self.hTrack_customers_entry.pack(padx=30)

        self.hTrack_type_entry = tk.Entry(hair_track)
        self.hTrack_type_entry.insert(0, 'Type plaited')
        self.hTrack_type_entry.pack(padx=30, pady=10)

        self.hTrack_amount_entry = tk.Entry(hair_track)
        self.hTrack_amount_entry.insert(0, 'Amount Paid')
        self.hTrack_amount_entry.pack(padx=30)

        hTrack_btn = tk.Button(hair_track, text='Save Data', fg='#ffffff', bg='#0000ff', command=lambda:
            self.hair_activity())
        hTrack_btn.pack(pady=10)


            #track hair activity input

        hair_input = tk.Frame(hair_frame, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        hair_input.pack(pady=30, padx=30)

        hTrack_ttle = tk.Label(hair_input, text='Daily Input', fg='#000000', bg='#00ff00')
        hTrack_ttle.pack(fill=X)

        self.hTrack_input_date_entry = tk.Entry(hair_input)
        self.hTrack_input_date_entry.insert(0, 'Date')
        self.hTrack_input_date_entry.pack(padx=30, pady=10)

        self.hTrack_items_entry = tk.Entry(hair_input)
        self.hTrack_items_entry.insert(0, 'No. of items')
        self.hTrack_items_entry.pack(padx=30)

        self.hTrack_item_type_entry = tk.Entry(hair_input)
        self.hTrack_item_type_entry.insert(0, 'Type of items')
        self.hTrack_item_type_entry.pack(padx=30, pady=10)

        self.hTrack_paid_amount_entry = tk.Entry(hair_input)
        self.hTrack_paid_amount_entry.insert(0, 'Amount Paid')
        self.hTrack_paid_amount_entry.pack(padx=30)

        hTrack_input_btn = tk.Button(hair_input, text='Save Data', fg='#000000', bg='#00ff00', command=lambda:
                self.Hair_input())
        hTrack_input_btn.pack(pady=10)


#**********************Manicure & Pedicure**********************************

        manicure_frame = tk.Frame(self.activity_win, width=200, height=800, bg='#ffffff', highlightbackground='#0000ff', highlightthickness=1)
        manicure_frame.pack(side=LEFT, fill=BOTH, expand=1)

        mancr_title = tk.Label(manicure_frame, text='Manicure & Pedicure', fg='#000000', bg='#ffffff')
        mancr_title.config(font=('Arial', 20))
        mancr_title.pack(fill=Y)


#track manicure activity log
        mancr_track = tk.Frame(manicure_frame, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        mancr_track.pack(pady=30, padx=30)

        mTrack_ttle = tk.Label(mancr_track, text='Activity Log', fg='#ffffff', bg='#0000ff')
        mTrack_ttle.pack(fill=X)


        self.mTrack_date_entry = tk.Entry(mancr_track)
        self.mTrack_date_entry.insert(0, 'Date')
        self.mTrack_date_entry.pack(padx=30, pady=10)

       
        self.mTrack_customers_entry = tk.Entry(mancr_track)
        self.mTrack_customers_entry.insert(0, 'No. of customers')
        self.mTrack_customers_entry.pack(padx=30)


        self.mTrack_type_entry = tk.Entry(mancr_track)
        self.mTrack_type_entry.insert(0, 'Type of service')
        self.mTrack_type_entry.pack(padx=30, pady=10)

        
        self.mTrack_amount_entry = tk.Entry(mancr_track)
        self.mTrack_amount_entry.insert(0, 'Amount Paid')
        self.mTrack_amount_entry.pack(padx=30)

        mTrack_btn = tk.Button(mancr_track, text='Save Data', fg='#ffffff', bg='#0000ff', command=lambda:
                self.manicure_activity())
        mTrack_btn.pack(pady=10)


            #track manicure activity input

        manicure_input = tk.Frame(manicure_frame, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        manicure_input.pack(pady=30, padx=30)

        mTrack_ttle = tk.Label(manicure_input, text='Daily Input', fg='#000000', bg='#00ff00')
        mTrack_ttle.pack(fill=X)

      
        self.mTrack_input_date_entry = tk.Entry(manicure_input)
        self.mTrack_input_date_entry.insert(0, 'Date')
        self.mTrack_input_date_entry.pack(padx=30, pady=10)

        
        self.mTrack_items_entry = tk.Entry(manicure_input)
        self.mTrack_items_entry.insert(0, 'No. of items')
        self.mTrack_items_entry.pack(padx=30)


        self.mTrack_item_type_entry = tk.Entry(manicure_input)
        self.mTrack_item_type_entry.insert(0, 'Type of items')
        self.mTrack_item_type_entry.pack(padx=30, pady=10)


        self.mTrack_paid_amount_entry = tk.Entry(manicure_input)
        self.mTrack_paid_amount_entry.insert(0, 'Amount Paid')
        self.mTrack_paid_amount_entry.pack(padx=30)

        mTrack_input_btn = tk.Button(manicure_input, text='Save Data', fg='#000000', bg='#00ff00', command=lambda:
                self.Manicure_input())
        mTrack_input_btn.pack(pady=10)


#**********************training**********************************

        training_frame = tk.Frame(self.activity_win, width=200, height=800, bg='#ffffff', highlightbackground='#0000ff', highlightthickness=1)
        training_frame.pack(side=LEFT, fill=BOTH, expand=1)

        train_title = tk.Label(training_frame, text='Training', fg='#000000', bg='#ffffff')
        train_title.config(font=('Arial', 20))
        train_title.pack(fill=Y)


#track training activity log
        train_track = tk.Frame(training_frame, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        train_track.pack(pady=30, padx=30)

        tTrack_ttle = tk.Label(train_track, text='Activity Log', fg='#ffffff', bg='#0000ff')
        tTrack_ttle.pack(fill=X)

        
        self.tTrack_date_entry = tk.Entry(train_track)
        self.tTrack_date_entry.insert(0, 'Date')
        self.tTrack_date_entry.pack(padx=30, pady=10)

       
        self.tTrack_students_entry = tk.Entry(train_track)
        self.tTrack_students_entry.insert(0, 'Students present')
        self.tTrack_students_entry.pack(padx=30)

        
        self.tTrack_type_entry = tk.Entry(train_track)
        self.tTrack_type_entry.insert(0, 'Activity taught')
        self.tTrack_type_entry.pack(padx=30, pady=10)

        self.tTrack_amount_entry = tk.Entry(train_track)
        self.tTrack_amount_entry.insert(0, 'Amount Paid')
        self.tTrack_amount_entry.pack(padx=30)

        tTrack_btn = tk.Button(train_track, text='Save Data', fg='#ffffff', bg='#0000ff', command=lambda:
                self.training_activity())
        tTrack_btn.pack(pady=10)


    #track training activity input

        training_input = tk.Frame(training_frame, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        training_input.pack(pady=30, padx=30)

        tTrack_ttle = tk.Label(training_input, text='Daily Input', fg='#000000', bg='#00ff00')
        tTrack_ttle.pack(fill=X)

        
        self.tTrack_input_date_entry = tk.Entry(training_input)
        self.tTrack_input_date_entry.insert(0, 'Date')
        self.tTrack_input_date_entry.pack(padx=30, pady=10)

      
        self.tTrack_items_entry = tk.Entry(training_input)
        self.tTrack_items_entry.insert(0, 'No. of items')
        self.tTrack_items_entry.pack(padx=30)

        
        self.tTrack_item_type_entry = tk.Entry(training_input)
        self.tTrack_item_type_entry.insert(0, 'Type of items')
        self.tTrack_item_type_entry.pack(padx=30, pady=10)


        self.tTrack_paid_amount_entry = tk.Entry(training_input)
        self.tTrack_paid_amount_entry.insert(0, 'Amount Paid')
        self.tTrack_paid_amount_entry.pack(padx=30)

        tTrack_input_btn = tk.Button(training_input, text='Save Data', fg='#000000', bg='#00ff00', command=lambda:
                self.Training_input())
        tTrack_input_btn.pack(pady=10)


#**********************fields**********************************

        fields_frame = tk.Frame(self.activity_win, width=200, height=800, bg='#ffffff', highlightbackground='#0000ff', highlightthickness=1)
        fields_frame.pack(side=LEFT, fill=BOTH, expand=1)

        fld_title = tk.Label(fields_frame, text='Fields', fg='#000000', bg='#ffffff')
        fld_title.config(font=('Arial', 20))
        fld_title.pack(fill=Y)


#track field activity log
        fld_track = tk.Frame(fields_frame, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        fld_track.pack(pady=30, padx=30)

        fTrack_ttle = tk.Label(fld_track, text='Activity Log', fg='#ffffff', bg='#0000ff')
        fTrack_ttle.pack(fill=X)

      
        self.fTrack_date_entry = tk.Entry(fld_track)
        self.fTrack_date_entry.insert(0, 'Date')
        self.fTrack_date_entry.pack(padx=30, pady=10)

       
        self.fTrack_customers_entry = tk.Entry(fld_track)
        self.fTrack_customers_entry.insert(0, 'No. of customers')
        self.fTrack_customers_entry.pack(padx=30)

        
        self.fTrack_type_entry = tk.Entry(fld_track)
        self.fTrack_type_entry.insert(0, 'Type of service')
        self.fTrack_type_entry.pack(padx=30, pady=10)

        
        self.fTrack_amount_entry = tk.Entry(fld_track)
        self.fTrack_amount_entry.insert(0, 'Amount Paid')
        self.fTrack_amount_entry.pack(padx=30)

        fTrack_btn = tk.Button(fld_track, text='Save Data', fg='#ffffff', bg='#0000ff', command=lambda:
                self.feilds_actvity())
        fTrack_btn.pack(pady=10)


     #track Field activity input

        fields_input = tk.Frame(fields_frame, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        fields_input.pack(pady=30, padx=30)

        fTrack_ttle = tk.Label(fields_input, text='Daily Input', fg='#000000', bg='#00ff00')
        fTrack_ttle.pack(fill=X)


        self.fTrack_input_date_entry = tk.Entry(fields_input)
        self.fTrack_input_date_entry.insert(0, 'Date')
        self.fTrack_input_date_entry.pack(padx=30, pady=10)

        
        self.fTrack_items_entry = tk.Entry(fields_input)
        self.fTrack_items_entry.insert(0, 'No. of items')
        self.fTrack_items_entry.pack(padx=30)

       
        self.fTrack_item_type_entry = tk.Entry(fields_input)
        self.fTrack_item_type_entry.insert(0, 'Type of items')
        self.fTrack_item_type_entry.pack(padx=30, pady=10)

       
        self.fTrack_paid_amount_entry = tk.Entry(fields_input)
        self.fTrack_paid_amount_entry.insert(0, 'Amount Paid')
        self.fTrack_paid_amount_entry.pack(padx=30)

        fTrack_input_btn = tk.Button(fields_input, text='Save Data', fg='#000000', bg='#00ff00', command=lambda:
                self.Fields_input())
        fTrack_input_btn.pack(pady=10)



#********************************Customers Page************************************************************************************
#**********************************************************************************************************************************
        self.cust_frame = tk.Frame(self)

        self.cust_win = tk.Canvas(self.cust_frame, width=1000, height=800, bg='#0000cd', scrollregion=(0, 0, 1000, 1000))
        self.cust_win.pack(fill=BOTH, expand=1)

        y_scroll = tk.Scrollbar(self.cust_frame, orient='vertical', command=self.cust_win.yview)
        y_scroll.pack(side=RIGHT, fill=Y)
        self.cust_win.config(yscrollcommand=y_scroll.set)
        


        logo_image = Image.open('images/logo.png')
        small_logo = logo_image.resize((50, 50))
        small_logo = ImageTk.PhotoImage(small_logo)
        small_logo_label = tk.Label(self.cust_win, image=small_logo, bd=0)
        small_logo_label.image = small_logo
        small_logo_label.pack(pady=10)

        cust_title = tk.Label(self.cust_win, text='BANIX SALON', bg='#0000cd', fg='#ffffff')
        cust_title.config(font=('Ubuntu', 40))
        cust_title.pack(padx=20)
    


        cust_book = tk.Frame(self.cust_win, width=200, bg='#ffffff', highlightbackground='#0000ff', highlightthickness=1)
        cust_book.pack(side=LEFT, fill=BOTH, expand=1)

        book_title = tk.Label(cust_book, text='Customer Booking', fg='#000000', bg='#ffffff')
        book_title.config(font=('Arial', 20))
        book_title.pack(pady=10)


#Add customer booking

        add_book = tk.Frame(cust_book, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        add_book.pack(pady=15, padx=30, expand=1)


        Adbook_ttle = tk.Label(add_book, text='Add Booking', fg='#ffffff', bg='#0000ff')
        Adbook_ttle.pack(fill=X)

        self.Adbook_input_name_entry = tk.Entry(add_book)
        self.Adbook_input_name_entry.insert(0, 'Customer Name')
        self.Adbook_input_name_entry.pack(padx=30, pady=5)

        
        self.Adbook_service_entry = tk.Entry(add_book)
        self.Adbook_service_entry.insert(0, 'Service')
        self.Adbook_service_entry.pack(padx=30, pady=5)

       
        self.Adbook_date_entry = tk.Entry(add_book)
        self.Adbook_date_entry.insert(0, 'Date')
        self.Adbook_date_entry.pack(padx=30, pady=5)


        self.Adbook_time_entry = tk.Entry(add_book)
        self.Adbook_time_entry.insert(0, 'Time')
        self.Adbook_time_entry.pack(padx=30,  pady=5)


        self.Adbook_Contact_entry = tk.Entry(add_book)
        self.Adbook_Contact_entry.insert(0, 'Customer Contact')
        self.Adbook_Contact_entry.pack(padx=30)

        Adbook_input_btn = tk.Button(add_book, text='Save Booking', fg='#ffffff', bg='#0000ff', command=lambda:
            self.book_customer())
        Adbook_input_btn.pack(pady=10)

#edit Customer booking
        edit_book = tk.Frame(cust_book, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        edit_book.pack(pady=15, padx=30, expand=1)

        Edbook_ttle = tk.Label(edit_book, text='Edit Booking', fg='#000000', bg='#00ff00')
        Edbook_ttle.pack(fill=X)

        self.Edbook_input_name_entry = tk.Entry(edit_book)
        self.Edbook_input_name_entry.insert(0, 'Customer Name')
        self.Edbook_input_name_entry.pack(padx=30, pady=5)

        
        self.Edbook_service_entry = tk.Entry(edit_book)
        self.Edbook_service_entry.insert(0, 'Service')
        self.Edbook_service_entry.pack(padx=30, pady=5)

       
        self.Edbook_date_entry = tk.Entry(edit_book)
        self.Edbook_date_entry.insert(0, 'Date')
        self.Edbook_date_entry.pack(padx=30, pady=5)


        self.Edbook_time_entry = tk.Entry(edit_book)
        self.Edbook_time_entry.insert(0, 'Time')
        self.Edbook_time_entry.pack(padx=30,  pady=5)


        self.Edbook_Contact_entry = tk.Entry(edit_book)
        self.Edbook_Contact_entry.insert(0, 'Customer Contact')
        self.Edbook_Contact_entry.pack(padx=30)

        Edbook_input_btn = tk.Button(edit_book, text='Save Edit', fg='#000000', bg='#00ff00', command=lambda:
            self.edit_book_customer())
        Edbook_input_btn.pack(pady=10)




#*******************Customers Dashboard************************8

        cust_dash = tk.Frame(self.cust_win, width=500, bg='#ffffff')
        cust_dash.pack(side=LEFT, fill=BOTH, expand=1)

        cust_dash_title = tk.Label(cust_dash, text='Customers Dashboard', fg='#000000', bg='#ffffff')
        cust_dash_title.config(font=('Arial', 30))
        cust_dash_title.pack(pady=10, padx=30)

#Active bookings
        active_book = tk.Frame(cust_dash, width=400, bg='#00ff00', height=250)
        active_book.pack(pady=10, padx=30, expand=1)

        active_book_title = tk.Label(active_book, text='            Total Bookings         ', fg='#000000', bg='#007700')
        active_book_title.config(font=('Arial', 20))
        active_book_title.pack(fill=X)

        active_book_body = tk.Label(active_book, text=self.count_bookings(), fg='#000000', bg='#00ff00')
        active_book_body.config(font=('Arial', 100))
        active_book_body.pack()

    #Active Suggestions

        pending_book = tk.Frame(cust_dash, width=400, bg='#999999', height=250)
        pending_book.pack(pady=10, padx=30, expand=1)

        pending_book_title = tk.Label(pending_book, text='            Total Suggestions         ', fg='#000000', bg='#808080')
        pending_book_title.config(font=('Arial', 20))
        pending_book_title.pack(fill=X)

        pending_book_body = tk.Label(pending_book, text=self.count_suggestions(), fg='#000000', bg='#999999')
        pending_book_body.config(font=('Arial', 100))
        pending_book_body.pack()
    
    
    
#************************customer suggestions ***********************
        cust_sugst = tk.Frame(self.cust_win, width=200, bg='#ffffff', highlightbackground='#0000ff', highlightthickness=1)
        cust_sugst.pack(side=LEFT, fill=BOTH, expand=1)

        cust_sugst_title = tk.Label(cust_sugst, text='Customer Suggestions', fg='#000000', bg='#ffffff')
        cust_sugst_title.config(font=('Arial', 20))
        cust_sugst_title.pack(pady=10)


#add suggestion
        add_sugst = tk.Frame(cust_sugst, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        add_sugst.pack(pady=15, padx=30, expand=1)

        Adsugst_ttle = tk.Label(add_sugst, text='Add suggestion', fg='#ffffff', bg='#0000ff')
        Adsugst_ttle.pack(fill=X)

        self.Adsugst_input_name_entry = tk.Entry(add_sugst)
        self.Adsugst_input_name_entry.insert(0, 'Customer Name')
        self.Adsugst_input_name_entry.pack(padx=30, pady=5)

        
        self.Adsugst_service_entry = tk.Entry(add_sugst)
        self.Adsugst_service_entry.insert(0, 'Service')
        self.Adsugst_service_entry.pack(padx=30, pady=5)

       
        self.Adsugst_date_entry = tk.Entry(add_sugst)
        self.Adsugst_date_entry.insert(0, 'Date')
        self.Adsugst_date_entry.pack(padx=30, pady=5)


        self.Adsugst_time_entry = tk.Entry(add_sugst)
        self.Adsugst_time_entry.insert(0, 'Time')
        self.Adsugst_time_entry.pack(padx=30,  pady=5)


        self.Adsugst_Contact_entry = tk.Entry(add_sugst)
        self.Adsugst_Contact_entry.insert(0, 'Customer Contact')
        self.Adsugst_Contact_entry.pack(padx=30)

        Adsugst_input_btn = tk.Button(add_sugst, text='Save suggestion', fg='#ffffff', bg='#0000ff', command=lambda:
            self.add_suggestion())
        Adsugst_input_btn.pack(pady=10)

    #edit suggestion
        edit_sugst = tk.Frame(cust_sugst, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        edit_sugst.pack(pady=15, padx=30, expand=1)

        edsugst_ttle = tk.Label(edit_sugst, text='Edit suggestion', fg='#000000', bg='#00ff00')
        edsugst_ttle.pack(fill=X)

        self.edsugst_input_name_entry = tk.Entry(edit_sugst)
        self.edsugst_input_name_entry.insert(0, 'Customer Name')
        self.edsugst_input_name_entry.pack(padx=30, pady=5)

        
        self.edsugst_service_entry = tk.Entry(edit_sugst)
        self.edsugst_service_entry.insert(0, 'Service')
        self.edsugst_service_entry.pack(padx=30, pady=5)

       
        self.edsugst_date_entry = tk.Entry(edit_sugst)
        self.edsugst_date_entry.insert(0, 'Date')
        self.edsugst_date_entry.pack(padx=30, pady=5)


        self.edsugst_time_entry = tk.Entry(edit_sugst)
        self.edsugst_time_entry.insert(0, 'Time')
        self.edsugst_time_entry.pack(padx=30,  pady=5)


        self.edsugst_Contact_entry = tk.Entry(edit_sugst)
        self.edsugst_Contact_entry.insert(0, 'Customer Contact')
        self.edsugst_Contact_entry.pack(padx=30)

        edsugst_input_btn = tk.Button(edit_sugst, text='Save Edit', fg='#000000', bg='#00ff00', command=lambda:
            self.edit_suggestion())
        edsugst_input_btn.pack(pady=10)


#***************Search customer booking******************************8

        cust_search = tk.Frame(self.cust_win, width=100, bg='#ffffff')
        cust_search.pack(side=RIGHT, fill=BOTH, expand=1)
        

        search_title = tk.Label(cust_search, text='Search Customer', bg='#ffffff')
        search_title.config(font=('Arial',15))
        search_title.pack(pady=10)

        search_title = tk.Label(cust_search, text='Search Booking', bg='#ffffff', fg='#0000ff')
        search_title.config(font=('Arial', 10))
        search_title.pack(pady=1)
        #search by date
        by_date = tk.Frame(cust_search, bg='#ffffff')
        by_date.pack(pady=10)

        self.search_date = tk.Entry(by_date)
        self.search_date.insert(5, 'Search by Date')
        self.search_date.pack(padx=5, pady=5)

        search_btn = tk.Button(cust_search, text='search', fg='#000000', bg='gold', command=lambda:
            self.search_booking())
        search_btn.pack(pady=5)

        search_title = tk.Label(cust_search, text='Search Suggestion', bg='#ffffff', fg='#0000ff')
        search_title.config(font=('Arial', 10))
        search_title.pack(pady=1)

        
        #search by date
        by_date = tk.Frame(cust_search, bg='#ffffff')
        by_date.pack(pady=10)

        self.sug_search_date = tk.Entry(by_date)
        self.sug_search_date.insert(5, 'Search by Date')
        self.sug_search_date.pack(padx=5, pady=5)

        search_btn = tk.Button(cust_search, text='search', fg='#000000', bg='gold', command=lambda:
            self.search_suggestion())
        search_btn.pack(pady=5)



        #delete customer booking

        del_book_title = tk.Label(cust_search, text='Delete Customer', bg='#ffffff', fg='#ff0000')
        del_book_title.config(font=('Arial', 15))
        del_book_title.pack(pady=5)

        del_book = tk.Frame(cust_search, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        del_book.pack(pady=10, padx=30, expand=1)

        Dbook_ttle = tk.Label(del_book, text='Delete Booking', fg='#000000', bg='#ff0000')
        Dbook_ttle.pack(fill=X)

        self.Dbook_Contact_entry = tk.Entry(del_book)
        self.Dbook_Contact_entry.insert(0, 'Customer Contact')
        self.Dbook_Contact_entry.pack(padx=30, pady=5)

        Dbook_input_btn = tk.Button(del_book, text='Delete Booking', fg='#000000', bg='#ff0000', command=lambda:
            self.delete_booking())
        Dbook_input_btn.pack(pady=10)

        #delete customer suggestion

        del_sug = tk.Frame(cust_search, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        del_sug.pack(pady=10, padx=30, expand=1)

        Dsug_ttle = tk.Label(del_sug, text='Delete Suggestion', fg='#000000', bg='#ff0000')
        Dsug_ttle.pack(fill=X)


        self.Dsugst_Contact_entry = tk.Entry(del_sug)
        self.Dsugst_Contact_entry.insert(0, 'Customer Contact')
        self.Dsugst_Contact_entry.pack(padx=30, pady=5)

        Dsuggst_input_btn = tk.Button(del_sug, text='Delete suggestion', fg='#000000', bg='#ff0000', command=lambda:
            self.delete_suggestion())
        Dsuggst_input_btn.pack(pady=10)

#******************************************************************************************
#*************************************Students Page****************************************
#*****************************************************************************************


        self.students_frame = tk.Frame(self, bg='#0000cd', width=1000, height=800)
        

        self.students_container = tk.Canvas(self.students_frame, bg='#0000cd')
        self.students_container.pack(fill=BOTH, expand=1)

        logo_image = Image.open('images/logo.png')
        small_logo = logo_image.resize((50, 50))
        small_logo = ImageTk.PhotoImage(small_logo)
        small_logo_label = tk.Label(self.students_container, image=small_logo, bd=0)
        small_logo_label.image = small_logo
        small_logo_label.pack(pady=10)

        stdnt_title = tk.Label(self.students_container, text='BANIX SALON', bg='#0000cd', fg='#ffffff')
        stdnt_title.config(font=('Ubuntu', 40))
        stdnt_title.pack(padx=20)
    


        stdnt_pane = tk.Frame(self.students_container, width=200, bg='#ffffff', highlightbackground='#0000ff', highlightthickness=1)
        stdnt_pane.pack(side=LEFT, fill=BOTH, expand=1)

        stdnt_title = tk.Label(stdnt_pane, text='Students Panel', fg='#000000', bg='#ffffff')
        stdnt_title.config(font=('Arial', 20))
        stdnt_title.pack(pady=20)


#Add student

        add_stdnt = tk.Frame(stdnt_pane, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        add_stdnt.pack(pady=15, padx=30, expand=1)


        Astdnt_ttle = tk.Label(add_stdnt, text='Add Student', fg='#ffffff', bg='#0000ff')
        Astdnt_ttle.pack(fill=X)

        self.Adstdnt_input_Fname_entry = tk.Entry(add_stdnt)
        self.Adstdnt_input_Fname_entry.insert(0, 'First Name')
        self.Adstdnt_input_Fname_entry.pack(padx=30, pady=5)

        
        self.Astdnt_Lname_entry = tk.Entry(add_stdnt)
        self.Astdnt_Lname_entry.insert(0, 'Last Name')
        self.Astdnt_Lname_entry.pack(padx=30, pady=5)

       
        self.Astdnt_tel_entry = tk.Entry(add_stdnt)
        self.Astdnt_tel_entry.insert(0, 'Telephone no')
        self.Astdnt_tel_entry.pack(padx=30, pady=5)


        self.Adstdnt_home_entry = tk.Entry(add_stdnt)
        self.Adstdnt_home_entry.insert(0, 'Home')
        self.Adstdnt_home_entry.pack(padx=30,  pady=5)


        self.Adstdnt_parent_entry = tk.Entry(add_stdnt)
        self.Adstdnt_parent_entry.insert(0, 'Parent/ Guardian')
        self.Adstdnt_parent_entry.pack(padx=30)

        Adstdnt_input_btn = tk.Button(add_stdnt, text='Add Student', fg='#ffffff', bg='#0000ff', command=lambda:
            self.add_student())
        Adstdnt_input_btn.pack(pady=10)


#delete student 

        del_stdnt = tk.Frame(stdnt_pane, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        del_stdnt.pack(pady=15, padx=30, expand=1)

        Dstdnt_ttle = tk.Label(del_stdnt, text='Delete student', fg='#000000', bg='#ff0000')
        Dstdnt_ttle.pack(fill=X)

        self.Dstdnt_input_Fname_entry = tk.Entry(del_stdnt)
        self.Dstdnt_input_Fname_entry.insert(0, 'First name')
        self.Dstdnt_input_Fname_entry.pack(padx=30, pady=5)

       
        self.Dstdnt_Lname_entry = tk.Entry(del_stdnt)
        self.Dstdnt_Lname_entry.insert(0, 'Last Name')
        self.Dstdnt_Lname_entry.pack(padx=30, pady=5)


        self.Dstdnt_tel_entry = tk.Entry(del_stdnt)
        self.Dstdnt_tel_entry.insert(0, 'Telephone')
        self.Dstdnt_tel_entry.pack(padx=30,  pady=5)


        Dstdnt_input_btn = tk.Button(del_stdnt, text='Delete Student', fg='#000000', bg='#ff0000', command=lambda:
            self.remove_student())
        Dstdnt_input_btn.pack(pady=10)


#*******************students Dashboard************************8

        stdnt_dash = tk.Frame(self.students_container, width=500, bg='#ffffff')
        stdnt_dash.pack(side=LEFT, fill=BOTH, expand=1)

        stdnt_dash_title = tk.Label(stdnt_dash, text='Students Dashboard', fg='#000000', bg='#ffffff')
        stdnt_dash_title.config(font=('Arial', 30))
        stdnt_dash_title.pack(pady=10, padx=30)

#Active students
        active_stdnt = tk.Frame(stdnt_dash, width=400, bg='#00ff00', height=250)
        active_stdnt.pack(pady=10, padx=30, expand=1)

        active_stdnt_title = tk.Label(active_stdnt, text='            Total Students         ', fg='#000000', bg='#007700')
        active_stdnt_title.config(font=('Arial', 20))
        active_stdnt_title.pack(fill=X)

        active_stdnt_body = tk.Label(active_stdnt, text=self.count_students(), fg='#000000', bg='#00ff00')
        active_stdnt_body.config(font=('Arial', 100))
        active_stdnt_body.pack()

    #new students

        #new_stdnt = tk.Frame(stdnt_dash, width=400, bg='#00ff00', height=250)
        #new_stdnt.pack(pady=10, padx=30, expand=1)

        #new_stdnt_title = tk.Label(new_stdnt, text='            new stdntings         ', fg='#000000', bg='#007700')
        #new_stdnt_title.config(font=('Arial', 20))
        #new_stdnt_title.pack(fill=X)

        #new_stdnt_body = tk.Label(new_stdnt, text='00', fg='#000000', bg='#00ff00')
        #new_stdnt_body.config(font=('Arial', 100))
        #new_stdnt_body.pack()



#***************************************************************************************************************************************
#**********************************************Products page****************************************************************************
#***************************************************************************************************************************************
        
        self.products_frame = tk.Frame(self, bg='#0000cd', width=1000, height=800)

        self.products_container = tk.Canvas(self.products_frame, bg='#0000cd')
        self.products_container.pack(fill=BOTH, expand=1)

        logo_image = Image.open('images/logo.png')
        small_logo = logo_image.resize((50, 50))
        small_logo = ImageTk.PhotoImage(small_logo)
        small_logo_label = tk.Label(self.products_container, image=small_logo, bd=0)
        small_logo_label.image = small_logo
        small_logo_label.pack(pady=10)

        prdct_title = tk.Label(self.products_container, text='BANIX SALON', bg='#0000cd', fg='#ffffff')
        prdct_title.config(font=('Ubuntu', 40))
        prdct_title.pack(padx=20)
    


        prdct_pane = tk.Frame(self.products_container, width=200, bg='#ffffff', highlightbackground='#0000ff', highlightthickness=1)
        prdct_pane.pack(side=LEFT, fill=BOTH, expand=1)

        prdct_title = tk.Label(prdct_pane, text='Products Manager', fg='#000000', bg='#ffffff')
        prdct_title.config(font=('Arial', 20))
        prdct_title.pack(pady=5)


#Add products

        add_hair_prdct = tk.Frame(prdct_pane, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        add_hair_prdct.pack(pady=7, padx=30, expand=1)


        hair_prdct_ttle = tk.Label(add_hair_prdct, text='Hair Products', fg='#ffffff', bg='#0000ff')
        hair_prdct_ttle.pack(fill=X)

        self.hair_prdct_input_name_entry = tk.Entry(add_hair_prdct)
        self.hair_prdct_input_name_entry.insert(0, 'Number')
        self.hair_prdct_input_name_entry.pack(padx=30, pady=5)

        
        self.hair_prdct_type_entry = tk.Entry(add_hair_prdct)
        self.hair_prdct_type_entry.insert(0, 'Type')
        self.hair_prdct_type_entry.pack(padx=30, pady=5)

       
        self.hair_prdct_worth_entry = tk.Entry(add_hair_prdct)
        self.hair_prdct_worth_entry.insert(0, 'Worth')
        self.hair_prdct_worth_entry.pack(padx=30, pady=5)

        hair_prdct_add_btn = tk.Button(add_hair_prdct, text='Add', fg='#ffffff', bg='#0000ff', command=lambda:
            self.add_Hair_product())
        hair_prdct_add_btn.pack(pady=5)


#***********************************Manicure Products student 

        add_manicure_prdct = tk.Frame(prdct_pane, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        add_manicure_prdct.pack(pady=7, padx=30, expand=1)


        manicure_prdct_ttle = tk.Label(add_manicure_prdct, text='Manicure Products', fg='#000000', bg='#ec9ba4')
        manicure_prdct_ttle.pack(fill=X)

        self.manicure_prdct_number_entry = tk.Entry(add_manicure_prdct)
        self.manicure_prdct_number_entry.insert(0, 'Number')
        self.manicure_prdct_number_entry.pack(padx=30, pady=5)

        
        self.manicure_prdct_type_entry = tk.Entry(add_manicure_prdct)
        self.manicure_prdct_type_entry.insert(0, 'Type')
        self.manicure_prdct_type_entry.pack(padx=30, pady=5)

       
        self.manicure_prdct_worth_entry = tk.Entry(add_manicure_prdct)
        self.manicure_prdct_worth_entry.insert(0, 'Worth')
        self.manicure_prdct_worth_entry.pack(padx=30, pady=5)

        manicure_prdct_input_btn = tk.Button(add_manicure_prdct, text='Add', fg='#000000', bg='#ec9ba4', command=lambda:
            self.add_man_product())
        manicure_prdct_input_btn.pack(pady=5)



#*************************************Others********************************

        add_other_prdct = tk.Frame(prdct_pane, width='150', bg='#ffffff', highlightbackground='#000000', highlightthickness=1)
        add_other_prdct.pack(pady=7, padx=30, expand=1)


        other_prdct_ttle = tk.Label(add_other_prdct, text='Other Products', fg='#000000', bg='#808080')
        other_prdct_ttle.pack(fill=X)

        self.other_prdct_number_entry = tk.Entry(add_other_prdct)
        self.other_prdct_number_entry.insert(0, 'Number')
        self.other_prdct_number_entry.pack(padx=30, pady=5)

        
        self.other_prdct_type_entry = tk.Entry(add_other_prdct)
        self.other_prdct_type_entry.insert(0, 'Type')
        self.other_prdct_type_entry.pack(padx=30, pady=5)

       
        self.other_prdct_worth_entry = tk.Entry(add_other_prdct)
        self.other_prdct_worth_entry.insert(0, 'Worth')
        self.other_prdct_worth_entry.pack(padx=30, pady=5)

        other_prdct_input_btn = tk.Button(add_other_prdct, text='Add', fg='#000000', bg='#808080', command=lambda:
            self.add_others())
        other_prdct_input_btn.pack(pady=5)


#*******************Products Dashboard************************8

        prdct_dash = tk.Frame(self.products_container, width=500, bg='#ffffff')
        prdct_dash.pack(side=LEFT, fill=BOTH, expand=1)

        prdct_dash_title = tk.Label(prdct_dash, text='Products Dashboard', fg='#000000', bg='#ffffff')
        prdct_dash_title.config(font=('Arial', 25))
        prdct_dash_title.pack(pady=10, padx=30)

#Hair Products
        hair_prdct_dash = tk.Frame(prdct_dash, width=400, bg='#0000ff', height=200)
        hair_prdct_dash.pack(pady=10, padx=30, expand=1)

        hair_prdct_title = tk.Label(hair_prdct_dash, text='            Hair Products         ', fg='#000000', bg='#000077')
        hair_prdct_title.config(font=('Arial', 20))
        hair_prdct_title.pack(fill=X)

        hair_prdct_body = tk.Label(hair_prdct_dash, text=self.count_hair_prdcts(), fg='#000000', bg='#0000ff')
        hair_prdct_body.config(font=('Arial', 80))
        hair_prdct_body.pack()

    #Manicure Products

        mancr_prdct_dash = tk.Frame(prdct_dash, width=400, bg='#e0c2cd', height=200)
        mancr_prdct_dash.pack(pady=10, padx=30, expand=1)

        mancr_prdct_title = tk.Label(mancr_prdct_dash, text='            Manicure Products         ', fg='#000000', bg='#ec9ba4')
        mancr_prdct_title.config(font=('Arial', 20))
        mancr_prdct_title.pack(fill=X)

        mancr_prdct_body = tk.Label(mancr_prdct_dash, text=self.count_man_prdcts(), fg='#000000', bg='#e0c2cd')
        mancr_prdct_body.config(font=('Arial', 80))
        mancr_prdct_body.pack()


     #Other Products

        other_prdct_dash = tk.Frame(prdct_dash, width=400, bg='#999999', height=200)
        other_prdct_dash.pack(pady=10, padx=30, expand=1)

        other_prdct_title = tk.Label(other_prdct_dash, text='            Other Products         ', fg='#000000', bg='#808080')
        other_prdct_title.config(font=('Arial', 20))
        other_prdct_title.pack(fill=X)

        other_prdct_body = tk.Label(other_prdct_dash, text=self.count_other_prdcts(), fg='#000000', bg='#999999')
        other_prdct_body.config(font=('Arial', 80))
        other_prdct_body.pack()
    
    
################.................Window layout end.....................................


#Window functionality...................................
    

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    

    
    def system_menu(self):
        self.menu_frame = tk.Frame(self, width=100)
        self.menu_frame.pack()

        self.menu = tk.Menu(self.menu_frame)
        self.menu.config(background='gold', font=('Arial', 15))

        self.menu.add_command(label='Home', command=lambda:
            self.display_home())
        self.menu.add_command(label='Activities', command=lambda:
            self.display_activities_menu())
        self.menu.add_command(label='Customers', command=lambda:
            self.display_customers())
        self.menu.add_command(label='Students', command=lambda:
            self.display_students())
        self.menu.add_command(label='Products', command=lambda:
            self.display_products())
        self.menu.add_command(label='Exit', command=lambda:
            self.destroy())

        self.logout_menu = tk.Menu(self)
        self.logout_menu.config(background='#0000cd')

        self.config(menu=self.menu)

#login........................................................
    def login(self):
        self.text = 'Loging In...'
        admin_username = self.Admin_name_entry.get()
        admin_pass = self.Admin_passwrd_entry.get()
        aunth_name = c.execute("SELECT username FROM Users WHERE username= :username", {'username': admin_username})
        cleaned_auth_name = aunth_name.fetchone()

        aunth_pw = c.execute("SELECT password FROM Users WHERE password= :password", {'password': admin_pass})
        cleaned_auth_pw = aunth_pw.fetchone()
        #print(cleaned_auth_name, cleaned_auth_pw)


        if cleaned_auth_name and cleaned_auth_pw:
                self.home_canvas.pack_forget()
                self.system_menu()
                self.config(menu=self.menu)
                self.main_canvas.pack(fill=BOTH, expand=1)
                
        else:
                logIn_error = 'Invalid Login credentials'
                msg.showerror('Error', logIn_error)

#admin page functions.......................................................................
    def edit_admin(self):
            edname = self.edit_name_entry.get()
            newEdname = self.new_edit_name_entry.get()
            edpass = self.edit_passwrd_entry.get()
            newEdpass = self.new_edit_passwrd_entry.get()
            try:
                c.execute("UPDATE Users SET username= :new_username WHERE username= :username", {'username': edname, 'new_username': newEdname})
                c.execute("UPDATE Users SET password= :new_password WHERE password= :password" , {'password': edpass, 'new_password': newEdpass})
                msg.showinfo('Edit User', 'Successfully Edited Admin!')
            except:
                msg.showerror('Error', 'Error editing admin')

    def add_admin(self):
            new_adUsername = self.add_name_entry.get()
            new_adpasswrd = self.add_passwrd_entry.get()

            try:
                c.execute("INSERT INTO Users VALUES(:username, :password)", {'username':new_adUsername, 'password':new_adpasswrd })
                msg.showinfo('Add User', 'User added successfully!')

            except:
                msg.showerror('Error', 'Error Adding user')


    def logout(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}: {:02d}'.format(mins, secs)
            #print(timer, end='\r')
            time.sleep(1)
            t -= 1
            self.home_canvas.pack(fill=BOTH, expand=1)
            self.config(menu=self.logout_menu)
            self.main_canvas.pack_forget()
            self.activity.pack_forget()
            self.cust_frame.pack_forget()
            self.students_frame.pack_forget()
            self.products_frame.pack_forget()
            self.destroy()


    def close_home(self):
        close_btn = tk.Button(self.home_canvas, text='Close', fg='#000000', bg='#ff0000', command=self.close)
        close_btn.pack(side=RIGHT, padx=10)

    def close(self):
        self.home_canvas.pack_forget()
        self.destroy()
        

    def display_home(self):
        self.home_canvas.pack_forget()
        self.main_canvas.pack(fill=BOTH, expand=1)
        self.activity.pack_forget()
        self.cust_frame.pack_forget()
        self.students_frame.pack_forget()
        self.products_frame.pack_forget()


#activities page functions..........................................................................

    def hair_activity(self):
        HacDate = self.hTrack_date_entry.get()
        HacCust = self.hTrack_customers_entry.get()
        HaTyp = self.hTrack_type_entry.get()
        HaAmnt = self.hTrack_amount_entry.get()

        try:
            c.execute("INSERT INTO Hair VALUES(:date, :customers, :type, :amount)", 
            {'date':HacDate, 'customers':HacCust, 'type':HaTyp, 'amount':HaAmnt})
            msg.showinfo('Success', 'Data successfully added')
        except:
            msg.showerror('Error', 'Error Adding information!')


    def Hair_input(self):
        HiDate = self.hTrack_input_date_entry.get()
        HiItem = self.hTrack_items_entry.get()
        HiTyp = self.hTrack_item_type_entry.get()
        HiAmnt = self.hTrack_paid_amount_entry.get()

        try:
            c.execute("INSERT INTO Hair_Input VALUES(:date, :items, :type, :amount)",
            {'date':HiDate, 'items':HiItem, 'type':HiTyp, 'amount':HiAmnt})
            msg.showinfo('Success', 'Data successfully added')
        except:
            msg.showerror('Error', 'Error Adding information!')

        #manicure.................................................
    def manicure_activity(self):
        manDate = self.mTrack_date_entry.get()
        manCus = self.mTrack_customers_entry.get()
        manTyp = self.mTrack_type_entry.get()
        manAmnt = self.mTrack_amount_entry.get()

        try:
            c.execute("INSERT INTO Manicure VALUES(:date, :customers, :type, :amount)",
            {'date':manDate, 'customers':manCus, 'type':manTyp, 'amount':manAmnt})
            msg.showinfo('Success', 'Data Succesfully Addded!')
        except:
            msg.showerror('Error', 'Error adding information')

    def Manicure_input(self):
        MiDate = self.mTrack_input_date_entry.get()
        MiItems = self.mTrack_items_entry.get()
        MiTyp = self.mTrack_item_type_entry.get()
        MiAmnt = self.mTrack_paid_amount_entry.get()

        try:
            c.execute("INSERT INTO Manicure_Input VALUES(:date, :items, :type, :amount)",
            {'date':MiDate, 'items':MiItems, 'type':MiTyp, 'amount':MiAmnt})
            msg.showinfo('Success', 'Data Succesfully Addded!')

        except:
            msg.showerror('Error', 'Error adding information')

        #Training...............................................................................

    def training_activity(self):
        trDate = self.tTrack_date_entry.get()
        trStdnts = self.tTrack_students_entry.get()
        trActv = self.tTrack_type_entry.get()
        trAmnt = self.tTrack_amount_entry.get()

        try:
            c.execute("INSERT INTO Training VALUES(:date, :customers, :type, :amount)",
            {'date':trDate, 'customers':trStdnts, 'type':trActv, 'amount':trAmnt})
            msg.showinfo('Success', 'Data Succesfully Addded!')

        except:
            msg.showerror('Error', 'Error adding information')

    def Training_input(self):
        triDate = self.tTrack_input_date_entry.get()
        triItems = self.tTrack_items_entry.get()
        triTyp = self.tTrack_item_type_entry.get()
        triAmnt = self.tTrack_paid_amount_entry.get()

        try:
            c.execute("INSERT INTO Training_Input VALUES(:date, :items, :type, :amount)",
            {'date':triDate, 'items':triItems, 'type':triTyp, 'amount':triAmnt})
            msg.showinfo('Success', 'Data Succesfully Addded!')

        except:
            msg.showerror('Error', 'Error adding information')

        #Fields....................................................................................
    def feilds_actvity(self):
        fDate = self.fTrack_date_entry.get()
        fCust = self.fTrack_customers_entry.get()
        fTyp = self.fTrack_type_entry.get()
        fAmnt = self.fTrack_amount_entry.get()

        try:
            c.execute("INSERT INTO Fields VALUES(:date, :customers, :type, :amount)",
            {'date':fDate, 'customers':fCust, 'type':fTyp, 'amount':fAmnt})
            msg.showinfo('Success', 'Data Succesfully Addded!')

        except:
            msg.showerror('Error', 'Error adding information')


    def Fields_input(self):
        fiDate = self.fTrack_input_date_entry.get()
        fiItems = self.fTrack_items_entry.get()
        fiTyp = self.fTrack_item_type_entry.get()
        fiAmnt = self.fTrack_paid_amount_entry.get()

        try:
            c.execute("INSERT INTO Fields_Input VALUES(:date, :items, :type, :amount)",
            {'date':fiDate, 'items':fiItems, 'type':fiTyp, 'amount':fiAmnt})
            msg.showinfo('Success', 'Data Succesfully Addded!')

        except:
            msg.showerror('Error', 'Error adding information')

    def display_activities_menu(self):
        self.activity.pack(fill=BOTH, expand=1)
        self.main_canvas.pack_forget()
        self.cust_frame.pack_forget()
        self.students_frame.pack_forget()
        self.products_frame.pack_forget()


#Customers' page functions...........................................................................

    def display_customers(self):
        self.main_canvas.pack_forget()
        self.activity.pack_forget()
        self.students_frame.pack_forget()
        self.products_frame.pack_forget()
        self.cust_frame.pack( side=LEFT, expand=1, fill=BOTH)


    def book_customer(self):
        cust_name = self.Adbook_input_name_entry.get()
        cust_servc = self.Adbook_service_entry.get()
        cust_date = self.Adbook_date_entry.get()
        cust_time = self.Adbook_time_entry.get()
        cust_contct = self.Adbook_Contact_entry.get()

        try:
            c.execute("INSERT INTO Booking VALUES(:name, :service, :date, :time, :contact)",
            {'name':cust_name, 'service':cust_servc, 'date':cust_date, 'time':cust_time, 'contact':cust_contct})
            msg.showinfo('Success', 'Booking saved successfully!')

        except:
            msg.showerror('Error', 'Error Saving Information!')

    def edit_book_customer(self):
        ed_cus_name = self.Edbook_input_name_entry.get()
        ed_cus_service = self.Edbook_service_entry.get()
        ed_cus_date = self.Edbook_date_entry.get()
        ed_cus_time = self.Edbook_time_entry.get()
        ed_cus_conctct = self.Edbook_Contact_entry.get()

        try:
            c.execute("UPDATE Booking SET service= :edited_service WHERE name= :name",{'name':ed_cus_name, 'edited_service':ed_cus_service})
            c.execute("UPDATE Booking SET date= :edited_date WHERE name= :name",{'name':ed_cus_name, 'edited_date':ed_cus_date})
            c.execute("UPDATE Booking SET time= :edited_time WHERE name= :name",{'name':ed_cus_name, 'edited_time':ed_cus_time})
            c.execute("UPDATE Booking SET contact= :edited_contact WHERE name= :name",{'name':ed_cus_name, 'edited_contact':ed_cus_conctct})
            msg.showinfo('Success', 'Booking Edited Successfully!')

        except:
            msg.showerror('Error', 'Error Editing Booking!')

    def delete_booking(self):
        del_cus = self.Dbook_Contact_entry.get()

        try:
            c.execute("DELETE FROM Booking WHERE contact= :contact", {'contact':del_cus})
            msg.showinfo('Success', 'Booking Successfully deleted!')
        except:
            msg.showerror('Error', 'Error deleting booking!')

        #suggestions..........................................................

    def add_suggestion(self):
        sug_name = self.Adsugst_input_name_entry.get()
        sug_servic = self.Adsugst_service_entry.get()
        sug_date = self.Adsugst_date_entry.get()
        sug_time = self.Adsugst_time_entry.get()
        sug_cont = self.Adsugst_Contact_entry.get()

        try:
            c.execute("INSERT INTO Suggestions VALUES(:name, :service, :date, :time, :contact)",
            {'name':sug_name, 'service':sug_servic, 'date':sug_date, 'time':sug_time, 'contact':sug_cont})
            msg.showinfo('Success', 'Suggestion saved successfully!')
        
        except:
            msg.showerror('Error', 'Error adding Suggestion!')

    def edit_suggestion(self):
        ed_sug_name = self.edsugst_input_name_entry.get()
        ed_servc = self.edsugst_service_entry.get()
        ed_date = self.edsugst_date_entry.get()
        ed_time = self.edsugst_time_entry.get()
        ed_contct = self.edsugst_Contact_entry.get()

        try:
            c.execute("UPDATE Suggestions SET service= :new_service WHERE name= :name", 
            {'name':ed_sug_name, 'new_service':ed_servc})
            c.execute("UPDATE Suggestions SET date= :new_date WHERE name= :name", 
            {'name':ed_sug_name, 'new_date':ed_date})
            c.execute("UPDATE Suggestions SET time= :new_time WHERE name= :name", 
            {'name':ed_sug_name, 'new_time':ed_time})
            c.execute("UPDATE Suggestions SET contact= :new_contact WHERE name= :name", 
            {'name':ed_sug_name, 'new_contact':ed_contct})

            msg.showinfo('Success', 'Suggestion Edited Successfully!')

        except:
            msg.showerror('Error', 'Error editing suggestion!')
                

    def delete_suggestion(self):
        sug_contact = self.Dsugst_Contact_entry.get()

        try:
            c.execute("DELETE FROM Suggestions where contact= :contact", {'contact':sug_contact})
            msg.showinfo('Success', 'Suggestion deleted!')

        except:
            msg.showerror('Error', 'Error deleting suggestion!')

    #Customers dashboard..................................................
    
    def count_bookings(self):
        num = c.execute("SELECT COUNT(*) FROM Booking")
        rslt = num.fetchall()
        return rslt

    def count_suggestions(self):
        sug_num = c.execute("SELECT COUNT(*) FROM Suggestions")
        sug_rslt = sug_num.fetchall()
        return sug_rslt


    #Search customer booking ................................................
    def search_booking(self):
        srch_date = self.search_date.get()

        try:
            srch_rslt = c.execute("SELECT * FROM Booking WHERE date= :date", {'date':srch_date})
            db_rslts = srch_rslt.fetchall()
            if db_rslts:
                msg.showinfo('Result', list(db_rslts))
                
            else:
                msg.showinfo('Result','Sorry, No booking available for your search!')
        except:
            return 'Error processing search'

    def search_suggestion(self):
        sug_srch_date = self.sug_search_date.get()

        try:
            sug_srch_rslt = c.execute("SELECT * FROM Suggestions WHERE date= :date", {'date':sug_srch_date})
            sug_db_rslts = sug_srch_rslt.fetchall()
            if sug_db_rslts:
                msg.showinfo('Result', list(sug_db_rslts))
                
            else:
                msg.showinfo('Result','Sorry, No booking available for your search!')
        except:
            return 'Error processing search'
        
#Students page functions...................................................

    def display_students(self):
        self.main_canvas.pack_forget()
        self.activity.pack_forget()
        self.cust_frame.pack_forget()
        self.products_frame.pack_forget()
        self.students_frame.pack(fill=BOTH, expand=1)

    def add_student(self):
        stdnt_Fname = self.Adstdnt_input_Fname_entry.get()
        stdnt_Lname = self.Astdnt_Lname_entry.get()
        stdnt_tel = self.Astdnt_tel_entry.get()
        stdnt_home = self.Adstdnt_home_entry.get()
        stdnt_par = self.Adstdnt_parent_entry.get()

        try:
            c.execute("INSERT INTO Students VALUES(:Fname, :Lname, :contact, :home, :parent)",
            {'Fname':stdnt_Fname, 'Lname':stdnt_Lname, 'contact':stdnt_tel, 'home':stdnt_home, 'parent':stdnt_par})
            msg.showinfo('Success', 'Student Added successfully!')

        except:
            msg.showerror('Error', 'Error Adding Student!')

    def remove_student(self):
        stdnt_fName = self.Dstdnt_input_Fname_entry.get()
        stdnt_lName = self.Dstdnt_Lname_entry.get()
        stdnt_Tel = self.Dstdnt_tel_entry.get()

        try:
            c.execute("DELETE FROM Students WHERE contact= :contact", {'contact':stdnt_Tel})
            msg.showinfo('Success', 'Student deleted!!')

        except:
            msg.showerror('Error', 'Error deleting student!')


    def count_students(self):
        result = c.execute("SELECT COUNT(*) FROM Students")
        number = result.fetchall()
        return number

#Products page.........................................................................

    def display_products(self):
        self.main_canvas.pack_forget()
        self.activity.pack_forget()
        self.cust_frame.pack_forget()
        self.students_frame.pack_forget()
        self.products_frame.pack(fill=BOTH, expand=1)

    def add_Hair_product(self):
        HpNum  = self.hair_prdct_input_name_entry.get()
        HpTyp = self.hair_prdct_type_entry.get()
        HpWorth = self.hair_prdct_worth_entry.get()

        try:
            c.execute("INSERT INTO Products VALUES(:number, :type, :worth)",
            {'number':HpNum, 'type':HpTyp, 'worth':HpWorth})
            msg.showinfo('Success', 'Product Added!')

        except:
            msg.showerror('Error', 'Error adding product!!')

    def add_man_product(self):
        man_prod_num = self.manicure_prdct_number_entry.get()
        man_prod_typ = self.manicure_prdct_type_entry.get()
        man_prod_worth = self.manicure_prdct_worth_entry.get()

        try:
            c.execute("INSERT INTO Man_Products VALUES(:number, :type, :worth)",
            {'number':man_prod_num, 'type':man_prod_typ, 'worth':man_prod_worth})
            msg.showinfo('Success', 'Product Added!')

        except:
            msg.showerror('Error', 'Error adding product!!')

    def add_others(self):
        other_num = self.other_prdct_number_entry.get()
        other_typ = self.other_prdct_type_entry.get()
        other_worth = self.other_prdct_worth_entry.get()

        try:
            c.execute("INSERT INTO Others VALUES(:number, :type, :worth)",
            {'number':other_num, 'type':other_typ, 'worth':other_worth})
            msg.showinfo('Success', 'Product Added!')

        except:
            msg.showerror('Error', 'Error adding product!!')
    
    
    #Count products........................

    def count_hair_prdcts(self):
        res = c.execute("SELECT COUNT(*) FROM Products")
        result = res.fetchall()
        return result

    def count_man_prdcts(self):
        res = c.execute("SELECT COUNT(*) FROM Man_Products")
        result = res.fetchall()
        return result

    def count_other_prdcts(self):
        res = c.execute("SELECT COUNT(*) FROM Others")
        result = res.fetchall()
        return result


#Generate report....................................................
    def Report(self):

        #Hair Plaiting activity...............
        HPA_report = c.execute("SELECT * FROM Hair")
        HPA_report_result = list(HPA_report.fetchall())

        HPI_report = c.execute("SELECT * FROM Hair_Input")
        HPI_report_result = list(HPI_report.fetchall())

        #Manicure Activity.....................
        MPA_report = c.execute("SELECT * FROM Manicure")
        MPA_report_result = list(MPA_report.fetchall())

        MPI_report = c.execute("SELECT * FROM Manicure_Input")
        MPI_report_result = list(MPI_report.fetchall())


        #Training Activity..........................
        TA_report = c.execute("SELECT * FROM Training")
        TA_report_result = list(TA_report.fetchall())

        TI_report = c.execute("SELECT * FROM Training_Input")
        TI_report_result = list(TI_report.fetchall())


        #Field activity.......................
        FA_report = c.execute("SELECT * FROM Fields")
        FA_report_result = list(FA_report.fetchall())

        FI_report = c.execute("SELECT * FROM Fields_Input")
        FI_report_result = list(FI_report.fetchall())

        #Cutomer Booking.........................
        CB_report = c.execute("SELECT * FROM Booking")
        CB_report_result = list(CB_report.fetchall())

        #Customer Suggestions.....................
        CS_report = c.execute("SELECT * FROM Suggestions")
        CS_report_result = list(CS_report.fetchall())

        #Students......................................
        ST_report = c.execute("SELECT * FROM Students")
        ST_report_result = list(ST_report.fetchall())

        #Hair Products report..............................
        PD_report = c.execute("SELECT * FROM Products")
        PD_report_result = list(PD_report.fetchall())

        #Man products...................
        MPD_report = c.execute("SELECT * FROM Man_Products")
        MPD_report_result = list(MPD_report.fetchall())

        #Other products..................
        OPD_report = c.execute("SELECT * FROM Others")
        OPD_report_result = list(OPD_report.fetchall())

        with open('Report.txt', 'w') as data:
            print('*******************************************Report for ',datetime.datetime.now(), '********************************************************', '\n', '\n', 'Hair Plaiting Results', '\n', HPA_report_result, '\n','\n', 'Hair Plaiting input results', '\n', HPI_report_result, '\n', '\n', 'Manicure and Pedicure results', '\n', MPA_report_result, '\n','\n',
                'Manicure input results', '\n', MPI_report_result, '\n', '\n', 'Training results', '\n', TA_report_result, '\n', '\n', 'Training Input results', '\n', TI_report_result, '\n', '\n', 'Field Results', '\n', FA_report_result, '\n', '\n',
                    'Field input rfesults', '\n', FI_report_result, '\n', '\n', 'Customer Booking results', '\n', CB_report_result, '\n', '\n', 'Customer Suggestions Result', '\n', CS_report_result, '\n', '\n', 'Students Report result', '\n', ST_report_result, '\n', '\n',
                        'Hair Products results', '\n', PD_report_result, '\n', '\n', 'Manicure products results', '\n', MPD_report_result, '\n', '\n', 'Other Products', '\n', OPD_report_result,
                            file=data)
#footer...................
    def display_footer(self):
        self.footer_frame = tk.Frame(self, bg= '#0000cd')
        self.footer_frame.pack(side=BOTTOM,  fill=X)
        footer = tk.Label(self.footer_frame, text='primU developers @copy 2022', bg='#0000cd', fg='#ffffff')
        footer.config(font=('Times New Roman', 10))
        footer.pack()

        
if __name__ == "__main__":
    window = Window()
    window.mainloop()

conn.commit()
