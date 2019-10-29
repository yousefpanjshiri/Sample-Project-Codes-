# -------------------------------------------------------------------------------
# Final Project: Banking Application
# Name: Yousef Panjshiri
# Python Version:  3.7.3
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Comments to grader: 
#-------------------------------------------------------------------------------
from tkinter import *
from Yousef_Panjshiri_CLASS import Saving, Checking, Account, Bank
from Yousef_Panjshiri_UTILITY import createAccountNo

class MyFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.bank = Bank()
        self.welcome()
 
    def clear_frame(self): #clears the previous frame
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        root.destroy()

    def logout(self):
        del self.account
        self.welcome()
        
    def welcome(self): #welcome screen
        self.clear_frame()
        
        welcome_label = Label(self, text = 'Welcome to 209 Banking!')
        self.b1  = Button(self, text = "Existing User", \
                     command=self.existing_account_widget)
        self.b2  = Button(self, text = "New User", \
                     command=self.new_account_widget)
        self.b3  = Button(self, text = "Exit Application", \
                     command=self.exit_application)
        

        #layout  manager for label, b1, b2 and b3
        welcome_label.grid(row=0, column=0)
        self.b1.grid(row=1, column=0)
        self.b2.grid(row=2, column=0)
        self.b3.grid(row=3, column=0)

        
        
        
    def new_account_widget(self):
        
        self.clear_frame()
        # ********************* create widgets *********************
        label_fname = Label(self, text = "First name: ")
        self.entry_fname = Entry(self, width=15)
        label_lname = Label(self, text = "Last name: ")
        self.entry_lname = Entry(self, width=15)


        label_line1 = Label(self, text= "Address line1: ")
        self.entry_line1 = Entry(self, width = 15)

        label_line2 = Label(self, text= "Address line2: ")
        self.entry_line2 = Entry(self, width = 15)

        label_type = Label(self, text="Account Type: ")
        self.entry_accounttype = Entry(self, width = 15)

        label_username = Label(self, text = "Username: ")
        self.entry_username = Entry(self, width=15)
        label_pin = Label(self, text = "Pin: ")
        self.entry_pin = Entry(self, width=15)

        
        button_create  = Button(self, text = "Create account", \
                                command=self.create_account_button_click)
        button_main_menu  = Button(self, text = "Main Menu", \
                                command=self.welcome)

        # ********************* Layout Widgets *********************
        #name
        label_fname.grid(row=0, column = 0)
        self.entry_fname.grid(row=0, column = 1)
        label_lname.grid(row = 1, column = 0)
        self.entry_lname.grid(row = 1, column = 1)
        #address
        label_line1.grid(row = 2, column = 0)
        self.entry_line1.grid(row = 2, column = 1)
        label_line2.grid(row = 3, column = 0)
        self.entry_line2.grid(row = 3, column = 1)
        #account type
        label_type.grid(row=4, column = 0)
        self.entry_accounttype.grid(row=4, column =1)
        #login info
        label_username.grid(row=5, column = 0)
        self.entry_username.grid(row=5, column = 1)
        label_pin.grid(row=6, column = 0)
        self.entry_pin.grid(row=6, column = 1)

        
        #button
        button_create.grid(row = 7, column = 0)
        button_main_menu.grid(row = 7, column = 1)

 

    #Create account object
    def create_account_button_click(self):
        
        cfname= self.entry_fname.get()
        clname= self.entry_lname.get()

        cline1= self.entry_line1.get()
        cline2= self.entry_line2.get()

        t = self.entry_accounttype.get().lower()
        u = self.entry_username.get()
        p = self.entry_pin.get()

        self.clear_frame()
        label_accountno = Label(self, text = "Your account no: ")
        self.accountno  = StringVar(self, '') #create StringVar object
        label_final_accountno  = Label(self, \
                                       textvariable=self.accountno) #associate self.result with this label


        s = createAccountNo()
        self.accountno.set(s) #setting

        

        #create account object for each type of account

        if t.lower() == 'saving': #creating saving object
            d = {'fname':cfname, 'lname':clname,\
                 'line1':cline1, 'line2':cline2, 'accountno':s,\
                 'balance':0, 'acctype':t,'username':u, 'pin':p}
            self.account= Saving(**d)
 
        elif t.lower() == 'checking':
                 z = {'fname': cfname, 'lname': clname,\
                      'line1':cline1, 'line2':cline2, 'accountno':s,\
                      'balance':0, 'acctype':t,'username':u, 'pin':p}
                 self.account= Checking(**z)
            #same as saving

        self.bank.display() #for printing purpose
        self.button_next  = Button(self, text = "Please Login Again", command=self.existing_account_widget)
        label_accountno.grid(column=0, columnspan = 2)
        label_final_accountno.grid(column=0, columnspan = 2)
        self.button_next.grid(column = 0, columnspan = 2 )
 

    def existing_account_widget(self):
        self.clear_frame()
        label_euser=Label(self, text="Username")
        self.entry_label_euser=Entry(self, width=15)
        label_epin=Label(self, text="PIN")
        self.entry_label_epin=Entry(self, width=15)
        button_login=Button(self, text="Login", command=self.login_button_click)
        button_mainMen=Button(self, text="Main Menu", command=self.welcome)

        #layout manager
        label_euser.grid(row=0, column=0)
        self.entry_label_euser.grid(row=0, column=1)
        label_epin.grid(row=1, column=0)
        self.entry_label_epin.grid(row=1, column=1)
        button_login.grid(row=2, column=1)
        button_mainMen.grid(row=3, column=1)
        #your code here step4 in spec
        #login widget
        #username, pin: label and entry
        #login, main menu: buttons

    def login_button_click(self):
        u = self.entry_label_euser.get()
        p = self.entry_label_epin.get()
        if (self.bank.login_validity(u, p)):
            self.account = self.bank.load_account(u, p) #returns account object
            self.existing_user_options()
        else:
            self.existing_account_widget()
            

    def existing_user_options(self):
        self.clear_frame()
        deposit_button  = Button(self, text = "Deposit", \
                                      command=self.deposit_interface)
        deposit_button.grid()
        width_button = Button(self, text = "Withdraw", \
                                   command=self.withdraw_interface)
        width_button.grid()
        summary_button = Button(self, text = "Summary", \
                                command=self.summary_interface)
        summary_button.grid()
        logout_button = Button(self, text = "Logout", \
                                    command=self.logout)
        logout_button.grid()
        exit_button = Button(self, text = "Exit Application", \
                                  command=self.exit_application)
        exit_button.grid()
        #withdraw, summary, logout and exit application
        #button step 5 in spec
        
    def summary_interface(self):
        self.clear_frame()
        label_account_num = Label(self, text = "Account Number ")
        self.entry_account_num = Entry(self, width = 15)
        button_options = Button (self, text = "Options", command = self.existing_user_options)
        next_button = Button (self, text = "Next", command = self.summary)
        label_account_num.grid(row=0, column=0) 
        self.entry_account_num.grid(row=0, column=1)
        button_options.grid(row=1, column=0)
        next_button.grid(row=1, column=1)
        #create label and entry for Account Number
        #button: Options: command = existing_user_options method
        #button: Next: command = summary method
        
    
    def summary(self):
        accno = self.entry_account_num.get() #obtains account no from user
        name, address, acctype, balance = self.account.summary(accno)
        
        self.clear_frame()
        self.info_label = Label(self, text = "Accout Information")
        self.name_label = Label(self, text = name)
        self.address_label = Label(self, text = address)
        self.acctype_label = Label(self, text = acctype)
        self.balance_label = Label(self, text = str(balance))
        self.info_label.pack()
        self.name_label.pack()
        self.address_label.pack()
        self.acctype_label.pack()
        self.balance_label.pack()
        

        self.button_options  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.button_options.pack()
        
    def deposit_interface(self):
        self.clear_frame()
        label_dep_amount = Label(self, text = "Amount to deposit ")
        self.entry_dep_amount = Entry(self, width = 15)
        label_account_num = Label(self, text = "Account Number ")
        self.entry_account_num = Entry(self, width = 15)
        next_button = Button(self, text = "Next", command=self.deposit)
        options_button = Button(self, text = "Options", \
                                     command=self.existing_user_options)
        label_dep_amount.grid(row=0, column=0)
        self.entry_dep_amount.grid(row=0, column=1)
        label_account_num.grid(row=1, column=0)
        self.entry_account_num.grid(row=1, column=1)
        next_button.grid(row=2, column=0)
        options_button.grid(row=2, column=1)
        #step 6 in spec
        #Next button will call deposit, please see summary interface function 

    #Deposit method
    def deposit(self):
        d = self.entry_dep_amount.get()
        accno = self.entry_account_num.get()
        self.account.deposit(d, accno)
        self.check_balance(accno)

        
    def withdraw_interface(self):
        self.clear_frame()
        label_with_amount = Label(self, text = "Amount to withdraw ")
        self.entry_with_amount = Entry(self, width = 15)
        label_account_num = Label(self, text = "Account Number ")
        self.entry_account_num = Entry(self, width = 15)
        next_button = Button(self, text = "Next", command=self.withdraw)
        options_button = Button(self, text = "Options", \
                                     command=self.existing_user_options)
        label_with_amount.grid(row=0, column=0)
        self.entry_with_amount.grid(row=0, column=1)
        label_account_num.grid(row=1, column=0)
        self.entry_account_num.grid(row=1, column=1)
        next_button.grid(row=2, column=0)
        options_button.grid(row=2, column=1)
        #same as depost interface, see step 7 in spec

    #Withdraw method
    def withdraw(self):
        w = self.entry_with_amount.get()
        accno = self.entry_account_num.get()
        self.account.withdraw(w, accno)
        self.check_balance(accno)

        
    def check_balance(self, accno):

        self.clear_frame()
        label_balance = Label(self, text = 'Current balance: ' + \
                              str(self.account.getBalance(accno)))
        label_balance.grid()
        
        self.options_button  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.options_button.grid()


             
#driver
root = Tk()
frame = MyFrame(root)
frame.pack()
root.mainloop()
