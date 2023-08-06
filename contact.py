from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class contact():
    def __init__(self,root):
        self.root=root
        self.root.title("Contact Management System")
        self.root.geometry("1400x750+0+0")

        title = Label(self.root,text="Contact Management System",bd=9,relief=GROOVE,font=("times new roman",50,"bold"), bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #===== variables for data base

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.birth_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        #=====manageframe===

        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=28,y=100,width=450,height=625)

        m_title = Label(Manage_Frame,text="Manage Contact",bg="yellow",fg="black",font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        #==== roll number===

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="blue", fg="white",font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, columnspan=1, pady=10, padx=20,sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, columnspan=1, pady=10, padx=130,sticky="w")

        #=== name====

        lbl_name = Label(Manage_Frame, text="Name: ", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, columnspan=1, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, columnspan=1, pady=10, padx=130, sticky="w")

        #== email ====

        lbl_email = Label(Manage_Frame, text="Email:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, columnspan=1, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, columnspan=1, pady=10, padx=130, sticky="w")

        #== gender ===

        lbl_gender = Label(Manage_Frame, text="Gender:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, columnspan=1, pady=10, padx=20, sticky="w")

        txt_gender = Entry(Manage_Frame,  textvariable=self.gender_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_gender.grid(row=4, columnspan=1, pady=10, padx=130, sticky="w")

       
        #=== contact ==

        lbl_contact = Label(Manage_Frame, text="Contact:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, columnspan=1, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, columnspan=1, pady=10, padx=130, sticky="w")

        #== date of birth===
    
        lbl_dob = Label(Manage_Frame, text="Birth:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, columnspan=1, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame, textvariable=self.birth_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, columnspan=1, pady=10, padx=130, sticky="w")

        #== address ===

        lbl_Address = Label(Manage_Frame, text="Address:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, columnspan=1, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=20, height=3, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_Address.grid(row=7, columnspan=1, pady=10, padx=130, sticky="w")

        #===== button ====

        btn_frame = LabelFrame(Manage_Frame, bd=3, relief=RIDGE,bg="black")
        btn_frame.place(x=15,y=550,width=420)

        Addbtn = Button(btn_frame,text ="Add", width=10, command=self.add_contacts).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)

#=====details frame===

        Details_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Details_Frame.place(x=500,y=100,width=880,height=625)

        lbl_search = Label(Details_Frame,text="Search By",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by, font=("times new roman", 13, "bold"), width= 10, state='readonly')
        combo_search['values'] = ("roll_no", "name", "contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Details_Frame, textvariable=self.search_txt, font=("times new roman", 10, "bold"), width= 20,bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Details_Frame,text ="Search", width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Details_Frame, text="Show All", width=10,pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

#=====Table frame===

        Table_Frame = Frame(Details_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=525)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Contact_table = ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","birth","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config()
        scroll_y.config()

        self.Contact_table.heading("roll",text="Roll NO.")
        self.Contact_table.heading("name", text="Name")
        self.Contact_table.heading("email", text="Email")
        self.Contact_table.heading("gender", text="Gender")
        self.Contact_table.heading("contact", text="Contact")
        self.Contact_table.heading("birth", text="Birth")
        self.Contact_table.heading("Address", text="Address")

        self.Contact_table['show']='headings'
        self.Contact_table.column("roll", width=100)
        self.Contact_table.column("name", width=100)
        self.Contact_table.column("email", width=100)
        self.Contact_table.column("gender", width=100)
        self.Contact_table.column("contact", width=100)
        self.Contact_table.column("birth", width=100)
        self.Contact_table.column("Address", width=150)

        self.Contact_table.pack(fill=BOTH,expand=1)
        self.Contact_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_contacts(self):

        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.contact_var.get()=="":
            messagebox.showerror("error","all fields are required to fill")
        else:
         con = pymysql.connect(host="localhost",user="root",password="",database="contact management")
         cur=con.cursor()
         cur.execute("insert into contact values (%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                         self.name_var.get(),
                                                                                         self.email_var.get(),
                                                                                         self.gender_var.get(),
                                                                                         self.contact_var.get(),
                                                                                         self.birth_var.get(),
                                                                                         self.txt_Address.get('1.0',END)))
         con.commit()
         self.fetch_data()
         self.clear()
         con.close()
         messagebox.showinfo("success","Data has been inserted")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root",password="",database="contact management")
        cur = con.cursor()
        cur.execute("select * from contact")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Contact_table.delete(*self.Contact_table.get_children())
        for row in rows:
            self.Contact_table.insert('', END,values=row)
        con.commit()
        con.close()

    def get_cursor(self,ev):
        cursor_row = self.Contact_table.focus()
        contents = self.Contact_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.birth_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])



    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.birth_var.set("")
        self.txt_Address.delete("1.0",END)

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="contact management")
        cur = con.cursor()
        cur.execute("update students set name=%s, email=%s,gender=%s,contact=%s,birth=%s where roll=%s", (
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.birth_var.get(),
                                                                          self.txt_Address.get('1.0', END),
                                                                          self.Roll_No_var.get()))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success", "Data has been inserted")

    def delete_data(self):

        con = pymysql.connect(host="localhost", user="root",password="",database="contact management")
        cur = con.cursor()
        cur.execute("delete from contact where roll=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):

        con = pymysql.connect(host="localhost", user="root",password="",database="contact management")
        cur = con.cursor()
        cur.execute("select * from contact where" + str(self.search_by.get()) + "like '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Contact_table.delete(*self.Contact_table.get_children())
            for row in rows:
                self.Contact_table.insert('',END, values=row)
            con.commit()
        con.close()





class contact():
    pass
    root = Tk()
    obj= contact(root)
    root.mainloop()