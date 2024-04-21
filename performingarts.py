from tkinter import *
from tkinter import messagebox
import pymysql

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Performing Arts")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False,False)
        self.loginform()

    def loginform(self):
        Frame_login=Frame(self.root,bg="midnightblue")
        Frame_login.place(x=0,y=0,height=700,width=1350)

        frame_input=Frame(self.root,bg='white')
        frame_input.place(x=450,y=130,height=450,width=350)

        label1=Label(frame_input,text="Admin Login",font=('britannic bold',32,'bold'),fg="black",bg="white")
        label1.place(x=55,y=20)

        label2=Label(frame_input,text="Username",font=('Goudy old style',20,'bold'),fg="royalblue",bg="white")
        label2.place(x=30,y=95)

        self.email_txt=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")
        self.email_txt.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input,text="Password",font=('Goudy old style',20,'bold'),fg="royalblue",bg="white")
        label3.place(x=30,y=195)

        
        self.password=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")
        self.password.place(x=30,y=245,width=270,height=35)

        btn1=Button(frame_input,text="Forgot password?",cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0)
        btn1.place(x=125,y=305)

        btn2=Button(frame_input,text="Login",command=self.login,cursor='hand2',font=('times new roman',15),fg="white",bg="royalblue",bd=0,width=15,height=1)
        btn2.place(x=90,y=340)

        btn3=Button(frame_input,command=self.Register,text="Not Registered?Register",cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0)
        btn3.place(x=110,y=390)

    def login(self):
        if self.email_txt.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='hardikpandya33',database='performing_arts')
                cur=con.cursor()
                cur.execute('select * from register where username=%s and password=%s',(self.email_txt.get(),self.password.get()))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
                    self.loginclear()
                    self.email_txt.focus()
                    
                else:
                    self.homepage()
                    con.close()
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)

    def Register(self):
        Frame_login1=Frame(self.root,bg="midnightblue")
        Frame_login1.place(x=0,y=0,height=700,width=1366)

        frame_input2=Frame(self.root,bg='white')
        frame_input2.place(x=320,y=130,height=450,width=630)

        label1=Label(frame_input2,text="Register",font=('britannic bold',32,'bold'),fg="black",bg="white")
        label1.place(x=45,y=20)

        label2=Label(frame_input2,text="Username",font=('Goudy old style',20,'bold'),fg="royalblue",bg="white")
        label2.place(x=30,y=95)

        self.entry=Entry(frame_input2,font=('times new roman',15,'bold'),bg="lightgray")
        self.entry.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input2,text="Password",font=('Goudy old style',20,'bold'),fg="royalblue",bg="white")
        label3.place(x=30,y=195)

        self.entry2=Entry(frame_input2,font=('times new roman',15,'bold'),bg="lightgray")
        self.entry2.place(x=30,y=245,width=270,height=35)

        label4=Label(frame_input2,text="Email_id",font=('Goudy old style',20,'bold'),fg="royalblue",bg="white")
        label4.place(x=330,y=95)
        
        self.entry3=Entry(frame_input2,font=('times new roman',15,'bold'),bg="lightgray")
        self.entry3.place(x=330,y=145,width=270,height=35)

        label5=Label(frame_input2,text="Confirm password",font=('Goudy old style',20,'bold'),fg="royalblue",bg="white")
        label5.place(x=330,y=195)
        
        self.entry4=Entry(frame_input2,font=('times new roman',15,'bold'),bg="lightgray")
        self.entry4.place(x=330,y=245,width=270,height=35)

        btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="royalblue",bd=0,width=15,height=1)
        btn2.place(x=90,y=340)

        btn3=Button(frame_input2,command=self.loginform,text="Already Registered? Login",cursor="hand2",font=("calibri",10),fg="black",bg="white",bd=0)
        btn3.place(x=110,y=390)

    def register(self):
        if self.entry.get()=="" or self.entry2.get()=="" or self.entry3.get()=="" or self.entry4.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.entry2.get()!=self.entry4.get():
            messagebox.showerror("Error","Password and confirm password should be same",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='hardikpandya33',database='performing_arts')
                cur=con.cursor()
                cur.execute("select * from register where emailid=%s",self.entry3.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,Please try with another email id",parent=self.root)
                    self.regclear()
                    self.entry.focus()
                else:
                    cur.execute("Insert into register values(%s,%s,%s,%s)",(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Successfully Registered",parent=self.root)
                    self.regclear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)

    def regclear(self):
        self.entry.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)

    def loginclear(self):
        self.email_txt.delete(0,END)
        self.password.delete(0,END)
        
    def homepage(self):                   
            Frame_login2=Frame(self.root,bg="white")
            Frame_login2.place(x=0,y=0,height=700,width=1350)

            title=Label(Frame_login2,text="Welcome to \n Institution of Performing Arts  ",bd=10,font=("engravers mt",30,"bold"),fg="black",bg="white")
            title.place(x=5,y=5)

            frame_input=Frame(self.root,bg='white')
            frame_input.place(x=300,y=170,height=500,width=650)

            b=Button(frame_input, text="Manage Students",bd=5,font=("times new roman",25),bg="black",fg="white",width=20,pady=10,cursor='hand2',command=self.student)
            b.place(x=5,y=0,height=85,width=500)
            b1=Button(frame_input, text="Manage Instructors",bd=5,font=("times new roman",25),bg="black",fg="white",width=20,pady=10,cursor='hand2',command=self.Instructor)
            b1.place(x=5,y=100,height=85,width=500)
            b2=Button(frame_input, text="Course",bd=5,font=("times new roman",25),bg="black",fg="white",width=20,pady=10,cursor='hand2',command= self.course)
            b2.place(x=5,y=200,height=85,width=500)
            b5=Button(frame_input, text="Performance details",bd=5,font=("times new roman",25),bg="black",fg="white",width=20,pady=10,cursor='hand2',command=self.performance)
            b5.place(x=5,y=300,height=85,width=500)

            b6=Button(Frame_login2, text="Logout",bd=5,font=("times new roman",14),bg="black",fg="white",width=20,pady=10,cursor='hand2',command=self.loginform)
            b6.place(x=1100,y=630,height=50,width=90)

    def Instructor(self):

            def connect():
                conn = pymysql.connect(host="localhost",user="root",password="hardikpandya33",database="performing_arts")
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS instructor (iid VARCHAR(50) PRIMARY KEY ,iname VARCHAR(50) ,iphno NVARCHAR(50) ,iage VARCHAR(50) ,igender  VARCHAR(50) ,specialization VARCHAR(50) , icity VARCHAR(50))")
                conn.commit()
                conn.close()

            def insert_inst(iid , iname , iphno , iage, igender, specialization, icity):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("INSERT INTO instructor VALUES (%s,%s,%s,%s,%s,%s,%s )" , (iid , iname , iphno , iage, igender, specialization, icity ))
                print(iid , iname , iphno , iage, igender, specialization, icity)
                conn.commit()
                conn.close()

            def view_inst():
                conn = pymysql.connect(host="localhost",user="root",password="hardikpandya33",database="performing_arts")
                cur = conn.cursor()
                cur.execute("SELECT * FROM instructor")
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows

            def delete_inst(iid):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("DELETE FROM instructor WHERE iid=%s ", (iid))
                conn.commit()
                conn.close()

            def update_inst(iname , iphno , iage, igender, specialization, icity,iid):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("UPDATE instructor SET iname=%s,iphno=%s,iage=%s ,igender=%s,specialization=%s , icity=%s WHERE iid=%s ", ( iname , iphno , iage, igender, specialization, icity,iid ))
                conn.commit()
                conn.close()


            def search_inst(iid='' , iname='' , iphno='' , iage='', igender='', specialization='', icity='' ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("SELECT * FROM instructor WHERE iid=%s  OR iname=%s OR iphno=%s OR iage=%s OR igender=%s OR specialization=%s OR icity=%s " , (iid , iname , iphno , iage, igender, specialization, icity))
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows 

            connect()
           
            def get_selected_row(event):
                 global selected_row
                 index = list.curselection()[0]
                 selected_row = list.get(index)
                 e1.delete(0,END)
                 e1.insert(END,selected_row[0])
                 e2.delete(0,END)
                 e2.insert(END,selected_row[1])
                 e3.delete(0,END)
                 e3.insert(END,selected_row[2])
                 e4.delete(0,END)
                 e4.insert(END,selected_row[3])
                 e5.delete(0,END)
                 e5.insert(END,selected_row[4])
                 e6.delete(0,END)
                 e6.insert(END,selected_row[5])
                 e7.delete(0,END)
                 e7.insert(END,selected_row[6])

            def delete_command():
               delete_inst(selected_row[0])
               messagebox.showinfo("Success","Successfully Deleted the field")

            def view_command():
                list.delete(0,END)
                for row in view_inst():
                    list.insert(END,row)

            def search_command():
                list.delete(0,END)
                for row in search_inst(self.iid_text.get(),self.iname_text.get(),self.phno_text.get(),self.age_text.get(),self.gender_text.get(),self.speci_text.get(),self.city_text.get()):
                    list.insert(END,row)

            def add_command():
                 if self.iid_text.get()=="" or self.iname_text.get()=="" or self.phno_text.get()=="" or self.age_text.get()==""  or self.gender_text.get()=="" or self.speci_text.get()=="" or self.city_text.get()=="" :
                        messagebox.showerror("Error","All fields are required")
                 else:
                     insert_inst(self.iid_text.get(),self.iname_text.get(),self.phno_text.get(),self.age_text.get(),self.gender_text.get(),self.speci_text.get(),self.city_text.get())

                     list.delete(0,END)
                     list.insert(END,(self.iid_text.get(),self.iname_text.get(),self.phno_text.get(),self.age_text.get(),self.gender_text.get(),self.speci_text.get(),self.city_text.get()))

            def update_command():
                 update_inst(self.iname_text.get(),self.phno_text.get(),self.age_text.get(),self.gender_text.get(),self.speci_text.get(),self.city_text.get(),self.iid_text.get())
               
                 list.delete(0,END)
                 list.insert(END,(self.iname_text.get(),self.phno_text.get(),self.age_text.get(),self.gender_text.get(),self.speci_text.get(),self.city_text.get(),self.iid_text.get()))
                 messagebox.showinfo("Success","Successfully updated field")


            def clear_command():
                self.iid_text.set("")
                self.iname_text.set("")
                self.phno_text.set("")
                self.gender_text.set("")
                self.age_text.set("")
                self.gender_text.set("")
                self.speci_text.set("")
                self.city_text.set("")
           
            background= Label(self.root,bg='midnightblue')
            background.place(x=0,y=0,height=700,width=1350)

            Manage_Frame=Frame(self.root ,bd=4,bg="white")
            Manage_Frame.place(x=20,y=100,width=450,height=580)

            m_title=Label(self.root ,text="INSTRUCTOR DETAILS",bg='midnightblue',fg="white",font=("georgia",30,"bold"))
            m_title.place(x=15,y=15)

            #---------label-----------
            l1 = Label( Manage_Frame, text='Instructor ID',fg="black",bg="white",font=("times new roman",20,"bold"))
            l1.grid(row=1,column=0,pady=10,padx=20,sticky="w")
            l2 = Label( Manage_Frame, text='Name',fg="black",bg="white",font=("times new roman",20,"bold"))
            l2.grid(row=2,column=0,pady=10,padx=20,sticky="w")
            l3 = Label( Manage_Frame, text='Phone No',fg="black",bg="white",font=("times new roman",20,"bold"))
            l3.grid(row=3,column=0,pady=10,padx=20,sticky="w")
            l4 = Label( Manage_Frame, text='Age',fg="black",bg="white",font=("times new roman",20,"bold"))
            l4.grid(row=4,column=0,pady=10,padx=20,sticky="w")
            l5 = Label( Manage_Frame, text='Gender',fg="black",bg="white",font=("times new roman",20,"bold"))
            l5.grid(row=5,column=0,pady=10,padx=20,sticky="w")
            l6 = Label( Manage_Frame, text='Specialization',fg="black",bg="white",font=("times new roman",20,"bold"))
            l6.grid(row=6,column=0,pady=10,padx=20,sticky="w")
            l7 = Label( Manage_Frame, text='City',fg="black",bg="white",font=("times new roman",20,"bold"))
            l7.grid(row=7,column=0,pady=10,padx=20,sticky="w")

            #------------text entry------------------
            self.iid_text = StringVar()
            e1 = Entry( Manage_Frame, textvariable=self.iid_text,font=('times new roman',15,'bold'),bg="lightgray")
            e1.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            self.iname_text = StringVar()
            e2 = Entry( Manage_Frame, textvariable=self.iname_text,font=('times new roman',15,'bold'),bg="lightgray")
            e2.grid(row=2,column=1,pady=10,padx=20,sticky="w")

            self.phno_text = StringVar()
            e3 = Entry( Manage_Frame, textvariable=self.phno_text,font=('times new roman',15,'bold'),bg="lightgray")
            e3.grid(row=3,column=1,pady=10,padx=20,sticky="w")

            self.age_text = StringVar()
            e4 = Entry( Manage_Frame, textvariable=self.age_text,font=('times new roman',15,'bold'),bg="lightgray")
            e4.grid(row=4,column=1,pady=10,padx=20,sticky="w")

            self.gender_text = StringVar()
            e5 = Entry( Manage_Frame, textvariable=self.gender_text,font=('times new roman',15,'bold'),bg="lightgray")
            e5.grid(row=5,column=1,pady=10,padx=20,sticky="w")

            self.speci_text = StringVar()
            e6 = Entry( Manage_Frame, textvariable=self.speci_text,font=('times new roman',15,'bold'),bg="lightgray")
            e6.grid(row=6,column=1,pady=10,padx=20,sticky="w")

            self.city_text = StringVar()
            e7 = Entry( Manage_Frame, textvariable=self.city_text,font=('times new roman',15,'bold'),bg="lightgray")
            e7.grid(row=7,column=1,pady=10,padx=20,sticky="w")

            #-------------list-----------------------
            list = Listbox(self.root,height=10,width=40,font=("times new roman",20),fg="black",bg="white")
            list.place(x=480,y=100,width=780,height=580)

            sb = Scrollbar(self.root)
            sb.place(x=1260,y=100,width=30,height=580)

            list.bind('<<ListboxSelect>>',get_selected_row)


            #-----------buttons------------------------
            btn_Frame=Frame(self.root,bd=4,bg="white")
            btn_Frame.place(x=20,y=500,width=420)

            b1 = Button(btn_Frame,text='Add',width=12,pady=5,command=add_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b1.grid(row=0,column=0,padx=10,pady=10)

            b2 = Button(btn_Frame,text='Search',width=12,pady=5,command=search_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b2.grid(row=0,column=1,padx=10,pady=10)

            b3 = Button(btn_Frame,text='Delete',width=12,pady=5,command=delete_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b3.grid(row=1,column=0,padx=10,pady=10)

            b4 = Button(btn_Frame,text='View all',width=12,pady=5,command=view_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b4.grid(row=1,column=1,padx=10,pady=10)

            b5 = Button(btn_Frame,text='Clear',width=12,pady=5,command = clear_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b5.grid(row=1,column=2,padx=10,pady=10)

            b6 = Button(btn_Frame,text='Update',width=12,pady=5,command = update_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b6.grid(row=0,column=2,padx=10,pady=10)

            b7 = Button(self.root,text='Back',width=12,pady=5,command = self.homepage,cursor='hand2',font=('times new roman',15),bg="white",fg="midnightblue",bd=0,height=1)
            b7.place(x=1150,y=15)

    def course(self):

            def connect():
                conn = pymysql.connect(host="localhost",user="root",password="hardikpandya33",database="performing_arts")
                cur = conn.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS course (cid VARCHAR(50) PRIMARY KEY ,
                                                                  cname VARCHAR(50) ,
                                                                  form VARCHAR(50) ,
                                                                  level VARCHAR(50) ,
                                                                  duration  VARCHAR(50) ,
                                                                  startdate VARCHAR(50) ,
                                                                  time VARCHAR(50),
                                                                  fees VARCHAR(50) ,
                                                                  iid VARCHAR(50) ,
                                                                  FOREIGN KEY (iid) REFERENCES instructor(iid) )""")
                
                conn.commit()
                conn.close()

            def insert_course(cid , cname , form , level , duration ,startdate , time , fees , iid ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("INSERT INTO course VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (cid , cname , form , level , duration ,startdate, time , fees , iid))
                print(cid , cname , form , level , duration ,startdate , time , fees , iid)
                conn.commit()
                conn.close()

            def view_course():
                conn = pymysql.connect(host="localhost",user="root",password="hardikpandya33",database="performing_arts")
                cur = conn.cursor()
                cur.execute("SELECT * FROM course;")
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows

            def delete_course(cid):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("DELETE FROM course WHERE cid=%s ", (cid))
                conn.commit()
                conn.close()

            def update_course(cname , form , level , duration ,startdate , time , fees ,cid ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("""UPDATE course
                               SET cname=%s , form=%s , level=%s , duration=%s , startdate=%s , time=%s , fees=%s 
                               WHERE cid=%s """, ( cname , form , level , duration ,startdate , time , fees ,cid ))
                conn.commit()
                conn.close()


            def search_course(cid='' , cname='' , form='' , level='' , duration='' , startdate='' ,time='' , fees='' , iid ='' ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("""SELECT * FROM course
                               WHERE cid=%s  OR cname=%s OR form=%s OR
                               level=%s OR duration=%s OR startdate=%s OR
                               time =%s OR fees=%s OR iid=%s""" , (cid , cname , form , level , duration ,startdate , time , fees , iid ))
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows

            def music_course():
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("""SELECT *
                               FROM course 
                               WHERE form = 'music' """)
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows

            def dance_course():
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("""SELECT *
                               FROM course 
                               WHERE form = 'dance' """)
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows

            def drama_course():
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("""SELECT *
                               FROM course 
                               WHERE form = 'drama' """)
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows
            
            connect()

            def get_selected_row(event):
                 global selected_row
                 index = list.curselection()[0]
                 selected_row = list.get(index)
                 e1.delete(0,END)
                 e1.insert(END,selected_row[0])
                 e2.delete(0,END)
                 e2.insert(END,selected_row[1])
                 e3.delete(0,END)
                 e3.insert(END,selected_row[2])
                 e4.delete(0,END)
                 e4.insert(END,selected_row[3])
                 e5.delete(0,END)
                 e5.insert(END,selected_row[4])
                 e6.delete(0,END)
                 e6.insert(END,selected_row[5])
                 e7.delete(0,END)
                 e7.insert(END,selected_row[6])
                 e8.delete(0,END)
                 e8.insert(END,selected_row[7])
                 e9.delete(0,END)
                 e9.insert(END,selected_row[8])


            def delete_command():
               delete_course(selected_row[0])
               messagebox.showinfo("Success","Successfully Deleted the field")

            def view_command():
                list.delete(0,END)
                for row in view_course():
                    list.insert(END,row)

                '''for row in course_bd.view_course():
                    string_data = [str(data) for data in row]
                    list.insert(END, " ".join(string_data))'''

                 
                     
            def search_command():
                list.delete(0,END)
                for row in search_course(self.cid_text.get(),self.cname_text.get(),self.form_text.get(),self.level_text.get(),self.dur_text.get(),self.start_text.get(),self.time_text.get(),self.fee_text.get(),self.iid_text.get()):
                    list.insert(END,row)

            def add_command():
                 if self.cid_text.get()=="" or self.cname_text.get()==""or self.form_text.get()=="" or self.level_text.get()=="" or self.dur_text.get()=="" or self.start_text.get()=="" or self.time_text.get()=="" or self.fee_text.get()=="" or self.iid_text.get()=="" :
                        messagebox.showerror("Error","All fields are required")
                 else:
                     insert_course(self.cid_text.get(),self.cname_text.get(),self.form_text.get(),self.level_text.get(),self.dur_text.get(),self.start_text.get(),self.time_text.get(),self.fee_text.get(),self.iid_text.get())

                     list.delete(0,END)
                     list.insert(END,(self.cid_text.get(),self.cname_text.get(),self.form_text.get(),self.level_text.get(),self.dur_text.get(),self.start_text.get(),self.time_text.get(),self.fee_text.get(),self.iid_text.get()))

            def update_command():
                update_course(self.cname_text.get(),self.form_text.get(),self.level_text.get(),self.dur_text.get(),self.start_text.get(),self.time_text.get(),self.fee_text.get(),self.cid_text.get())
               
                list.delete(0,END)
                list.insert(END,(self.cname_text.get(),self.form_text.get(),self.level_text.get(),self.dur_text.get(),self.start_text.get(),self.time_text.get(),self.fee_text.get(),self.cid_text.get()))

            def clear_command():
                self.cid_text.set("")
                self.cname_text.set("")
                self.form_text.set("")
                self.level_text.set("")
                self.dur_text.set("")
                self.start_text.set("")
                self.time_text.set("")
                self.fee_text.set("")
                self.iid_text.set("")

            def music_command():
                 list.delete(0,END)
                 for row in music_course():
                    list.insert(END,row)

            def dance_command():
                 list.delete(0,END)
                 for row in dance_course():
                    list.insert(END,row)

            def drama_command():
                 list.delete(0,END)
                 for row in drama_course():
                    list.insert(END,row)

            background= Label(self.root,bg='midnightblue')
            background.place(x=0,y=0,height=700,width=1350)

            Manage_Frame=Frame(self.root ,bd=4,bg="white")
            Manage_Frame.place(x=20,y=100,width=450,height=580)

            m_title=Label(self.root ,text="COURSES",bg='midnightblue',fg="white",font=("georgia",30,"bold"))
            m_title.place(x=15,y=15)

            #---------label-----------
            l1 = Label(Manage_Frame, text='Course code',fg="black",bg="white",font=("times new roman",18,"bold"))
            l1.grid(row=1,column=0,pady=10,padx=20,sticky="w")
            l2 = Label(Manage_Frame, text='Name',fg="black",bg="white",font=("times new roman",18,"bold"))
            l2.grid(row=2,column=0,pady=10,padx=20,sticky="w")
            l3 = Label(Manage_Frame, text='Form',fg="black",bg="white",font=("times new roman",18,"bold"))
            l3.grid(row=3,column=0,pady=10,padx=20,sticky="w")
            l4 = Label(Manage_Frame, text='Level',fg="black",bg="white",font=("times new roman",18,"bold"))
            l4.grid(row=4,column=0,pady=10,padx=20,sticky="w")
            l5 = Label(Manage_Frame, text='Duration',fg="black",bg="white",font=("times new roman",18,"bold"))
            l5.grid(row=5,column=0,pady=10,padx=20,sticky="w")
            l6 = Label(Manage_Frame, text='Start date',fg="black",bg="white",font=("times new roman",18,"bold"))
            l6.grid(row=6,column=0,pady=10,padx=20,sticky="w")
            l7 = Label(Manage_Frame, text='Time',fg="black",bg="white",font=("times new roman",18,"bold"))
            l7.grid(row=7,column=0,pady=10,padx=20,sticky="w")
            l8 = Label(Manage_Frame, text='Fees',fg="black",bg="white",font=("times new roman",18,"bold"))
            l8.grid(row=8,column=0,pady=10,padx=20,sticky="w")
            l9 = Label(Manage_Frame, text='Instructor ID',fg="black",bg="white",font=("times new roman",18,"bold"))
            l9.grid(row=9,column=0,pady=10,padx=20,sticky="w")

            self.cid_text = StringVar()
            e1 = Entry(Manage_Frame, textvariable=self.cid_text,font=('times new roman',15,'bold'),bg="lightgray")
            e1.grid(row=1,column=1)

            self.cname_text = StringVar()
            e2 = Entry(Manage_Frame, textvariable=self.cname_text,font=('times new roman',15,'bold'),bg="lightgray")
            e2.grid(row=2,column=1)

            self.form_text = StringVar()
            e3 = Entry(Manage_Frame, textvariable=self.form_text,font=('times new roman',15,'bold'),bg="lightgray")
            e3.grid(row=3,column=1)

            self.level_text = StringVar()
            e4 = Entry(Manage_Frame, textvariable=self.level_text,font=('times new roman',15,'bold'),bg="lightgray")
            e4.grid(row=4,column=1)

            self.dur_text = StringVar()
            e5 = Entry(Manage_Frame, textvariable=self.dur_text,font=('times new roman',15,'bold'),bg="lightgray")
            e5.grid(row=5,column=1)

            self.start_text = StringVar()
            e6 = Entry(Manage_Frame, textvariable=self.start_text,font=('times new roman',15,'bold'),bg="lightgray")
            e6.grid(row=6,column=1)

            self.time_text = StringVar()
            e7 = Entry(Manage_Frame, textvariable=self.time_text,font=('times new roman',15,'bold'),bg="lightgray")
            e7.grid(row=7,column=1)

            self.fee_text = StringVar()
            e8 = Entry(Manage_Frame, textvariable=self.fee_text,font=('times new roman',15,'bold'),bg="lightgray")
            e8.grid(row=8,column=1)

            self.iid_text = StringVar()
            e9 = Entry(Manage_Frame, textvariable=self.iid_text,font=('times new roman',15,'bold'),bg="lightgray")
            e9.grid(row=9,column=1)

            
            #-------------list-----------------------
            list = Listbox(self.root,height=10,width=40,font=("times new roman",18),fg="black",bg="white")
            list.place(x=480,y=100,width=780,height=480)

            sb = Scrollbar(self.root)
            sb.place(x=1260,y=100,width=30,height=480)

            list.bind('<<ListboxSelect>>',get_selected_row)

            #-----------buttons------------------------
            btn_Frame=Frame(self.root,bd=4,bg="white")
            btn_Frame.place(x=25,y=560,width=400)

            b1 = Button(btn_Frame,text='Add',width=12,pady=5,command=add_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b1.grid(row=0,column=0,padx=10,pady=10)

            b2 = Button(btn_Frame,text='Search',width=12,pady=5,command=search_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b2.grid(row=0,column=1,padx=10,pady=10)

            b3 = Button(btn_Frame,text='Delete',width=12,pady=5,command=delete_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b3.grid(row=1,column=0,padx=10,pady=10)

            b4 = Button(btn_Frame,text='View all',width=12,pady=5,command=view_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b4.grid(row=1,column=1,padx=10,pady=10)

            b5 = Button(btn_Frame,text='Clear',width=12,pady=5,command=clear_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b5.grid(row=1,column=2,padx=10,pady=10)

            b6 = Button(btn_Frame,text='Update',width=12,pady=5,command=update_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b6.grid(row=0,column=2,padx=10,pady=10)

            b7=Button(self.root, text="Music",bd=5,font=("times new roman",25),fg="black",bg="white",width=12,pady=10,command=music_command,cursor='hand2')
            b7.place(x=480,y=587)

            b8=Button(self.root, text="Dance",bd=5,font=("times new roman",25),fg="black",bg="white",width=12,pady=10,command=dance_command,cursor='hand2')
            b8.place(x=750,y=587)

            b9=Button(self.root, text="Drama",bd=5,font=("times new roman",25),fg="black",bg="white",width=12,pady=10,command=drama_command,cursor='hand2')
            b9.place(x=1025,y=587)

            b10 = Button(self.root,text='Back',width=12,pady=5,command = self.homepage,cursor='hand2',font=('times new roman',15),bg="white",fg="midnightblue",bd=0,height=1)
            b10.place(x=1150,y=15)

    def student(self):

            def connect():
                conn = pymysql.connect(host="localhost",user="root",password="hardikpandya33",database="performing_arts")
                cur = conn.cursor()
                cur.execute( """  CREATE TABLE IF NOT EXISTS student
                                  (sid VARCHAR(50) PRIMARY KEY ,
                                  sname VARCHAR(50) ,
                                  phno NVARCHAR(50) ,
                                  gender VARCHAR(50) ,
                                  age  VARCHAR(50) ,
                                  city VARCHAR(50) ,
                                  cid varchar(50) , 
                                  INDEX cor_id(cid) ,
                                  FOREIGN KEY (cid) REFERENCES course(cid) ON DELETE CASCADE , 
                                  paymode VARCHAR(50))""")
                conn.commit()
                conn.close()

            def insert_stud(sid , sname , phno , gender , age , city, cid  , paymode ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s )" , (sid , sname , phno , gender , age ,city, cid , paymode))
                print(sid , sname , phno , gender , age ,city, cid , paymode)
                conn.commit()
                conn.close()

            def view_stud():
                conn = pymysql.connect(host="localhost",user="root",password="hardikpandya33",database="performing_arts")
                cur = conn.cursor()
                cur.execute('''SELECT * FROM student;''')
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows

            def delete_stud(sid):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("DELETE FROM student WHERE sid=%s ", (sid,))
                conn.commit()
                conn.close()

            def update_stud(sname , phno , gender , age ,city, cid , paymode , sid ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("UPDATE student SET sname=%s,phno=%s, gender=%s ,age=%s, city=%s, cid=%s ,paymode=%s WHERE sid=%s ", (sname , phno , gender , age ,city, cid , paymode , sid ))
                conn.commit()
                conn.close()


            def search_stud(sid='' , sname='' , phno='' , gender='' , age='' , city='', cid='', paymode='' ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("SELECT * FROM student WHERE sid=%s  OR sname=%s OR phno=%s OR gender=%s OR  age=%s OR city=%s OR cid=%s OR paymode=%s" , (sid , sname , phno , gender , age , city, cid  , paymode))
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows

            connect()

            def get_selected_row(event):
                 global selected_row
                 index = list.curselection()[0]
                 selected_row = list.get(index)
                 e1.delete(0,END)
                 e1.insert(END,selected_row[0])
                 e2.delete(0,END)
                 e2.insert(END,selected_row[1])
                 e3.delete(0,END)
                 e3.insert(END,selected_row[2])
                 e4.delete(0,END)
                 e4.insert(END,selected_row[3])
                 e5.delete(0,END)
                 e5.insert(END,selected_row[4])
                 e6.delete(0,END)
                 e6.insert(END,selected_row[5])
                 e7.delete(0,END)
                 e7.insert(END,selected_row[6])
                 e8.delete(0,END)
                 e8.insert(END,selected_row[7])

            def delete_command():
                delete_stud(selected_row[0])
                messagebox.showinfo("Success","Successfully Deleted the field")

            def view_command():
                 list.delete(0,END)
                 for row in  view_stud():
                    list.insert(END,row)
                     
            def search_command():
                list.delete(0,END)
                for row in search_stud( self.sid_text.get(), self.sname_text.get(), self.phno_text.get(), self.gen_text.get(), self.age_text.get(), self.city_text.get(), self.cid_text.get(), self.paymode_text.get()):
                    list.insert(END,row)

            def add_command():
                 if self.sid_text.get()=="" or self.sname_text.get()=="" or  self.phno_text.get()=="" or  self.gen_text.get()=="" or  self.age_text.get()=="" or  self.city_text.get()=="" or  self.cid_text.get()=="" or  self.paymode_text.get()==""  :
                        messagebox.showerror("Error","All fields are required")
                 else:
                       insert_stud(self.sid_text.get(), self.sname_text.get(), self.phno_text.get(), self.gen_text.get(), self.age_text.get(), self.city_text.get(), self.cid_text.get(), self.paymode_text.get())

                       list.delete(0,END)
                       list.insert(END,(self.sid_text.get(), self.sname_text.get(), self.phno_text.get(), self.gen_text.get(), self.age_text.get(), self.city_text.get(), self.cid_text.get(), self.paymode_text.get()))

            def update_command():
                update_stud(self.sname_text.get(), self.phno_text.get(), self.gen_text.get(), self.age_text.get(), self.city_text.get(), self.cid_text.get(), self.paymode_text.get(),self.sid_text.get())
               
                list.delete(0,END)
                list.insert(END,(self.sname_text.get(), self.phno_text.get(), self.gen_text.get(), self.age_text.get(), self.city_text.get(), self.cid_text.get(), self.paymode_text.get(),self.sid_text.get()))

            def clear_command():
                self.sid_text.set("")
                self.sname_text.set("")
                self.phno_text.set("")
                self.gen_text.set("")
                self.age_text.set("")
                self.city_text.set("")
                self.cid_text.set("")
                self.paymode_text.set("")

            background= Label(self.root,bg='midnightblue')
            background.place(x=0,y=0,height=700,width=1350)

            Manage_Frame=Frame(self.root ,bd=4,bg="white")
            Manage_Frame.place(x=20,y=100,width=450,height=580)

            m_title=Label(self.root ,text="MANAGE STUDENTS",bg='midnightblue',fg="white",font=("georgia",30,"bold"))
            m_title.place(x=15,y=15)

            #---------label-----------
            l1 = Label(Manage_Frame, text='Enrollment No',fg="black",bg="white",font=("times new roman",18,"bold"))
            l1.grid(row=1,column=0,pady=10,padx=20,sticky="w")
            l2 = Label(Manage_Frame, text='Name',fg="black",bg="white",font=("times new roman",18,"bold"))
            l2.grid(row=2,column=0,pady=10,padx=20,sticky="w")
            l3 = Label(Manage_Frame, text='Phone No',fg="black",bg="white",font=("times new roman",18,"bold"))
            l3.grid(row=3,column=0,pady=10,padx=20,sticky="w")
            l4 = Label(Manage_Frame, text='Gender',fg="black",bg="white",font=("times new roman",18,"bold"))
            l4.grid(row=4,column=0,pady=10,padx=20,sticky="w")
            l5 = Label(Manage_Frame, text='Age',fg="black",bg="white",font=("times new roman",18,"bold"))
            l5.grid(row=5,column=0,pady=10,padx=20,sticky="w")
            l6 = Label(Manage_Frame, text='City',fg="black",bg="white",font=("times new roman",18,"bold"))
            l6.grid(row=6,column=0,pady=10,padx=20,sticky="w")
            l7 = Label(Manage_Frame, text='Course code',fg="black",bg="white",font=("times new roman",18,"bold"))
            l7.grid(row=7,column=0,pady=10,padx=20,sticky="w")
            l8 = Label(Manage_Frame, text='Payment Mode',fg="black",bg="white",font=("times new roman",18,"bold"))
            l8.grid(row=8,column=0,pady=10,padx=20,sticky="w")

            #------------text entry------------------
            self.sid_text = StringVar()
            e1 = Entry(Manage_Frame, textvariable= self.sid_text,font=('times new roman',15,'bold'),bg="lightgray")
            e1.grid(row=1,column=1,padx=20,pady=10)

            self.sname_text = StringVar()
            e2 = Entry(Manage_Frame, textvariable= self.sname_text,font=('times new roman',15,'bold'),bg="lightgray")
            e2.grid(row=2,column=1,padx=20,pady=10)

            self.phno_text = StringVar()
            e3 = Entry(Manage_Frame, textvariable= self.phno_text,font=('times new roman',15,'bold'),bg="lightgray")
            e3.grid(row=3,column=1,padx=20,pady=10)

            self.gen_text = StringVar()
            e4 = Entry(Manage_Frame, textvariable= self.gen_text,font=('times new roman',15,'bold'),bg="lightgray")
            e4.grid(row=4,column=1)

            self.age_text = StringVar()
            e5 = Entry(Manage_Frame, textvariable= self.age_text,font=('times new roman',15,'bold'),bg="lightgray")
            e5.grid(row=5,column=1,padx=20,pady=10)

            self.city_text = StringVar()
            e6 = Entry(Manage_Frame, textvariable= self.city_text,font=('times new roman',15,'bold'),bg="lightgray")
            e6.grid(row=6,column=1,padx=20,pady=10)

            self.cid_text = StringVar()
            e7 = Entry(Manage_Frame, textvariable= self.cid_text,font=('times new roman',15,'bold'),bg="lightgray")
            e7.grid(row=7,column=1,padx=20,pady=10)

            self.paymode_text = StringVar()
            e8 = Entry(Manage_Frame, textvariable= self.paymode_text,font=('times new roman',15,'bold'),bg="lightgray")
            e8.grid(row=8,column=1,padx=20,pady=10)

            #-------------list-----------------------

            list = Listbox(self.root,height=10,width=40,font=("times new roman",20),fg="black",bg="white")
            list.place(x=480,y=100,width=780,height=580)

            sb = Scrollbar(self.root)
            sb.place(x=1260,y=100,width=30,height=580)

            list.bind('<<ListboxSelect>>',get_selected_row)

            #-----------buttons------------------------
            btn_Frame=Frame(self.root,bd=4,bg="white")
            btn_Frame.place(x=20,y=550,width=420)

            b1 = Button(btn_Frame,text='Add',width=12,pady=5,command=add_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b1.grid(row=0,column=0,padx=10,pady=10)

            b2 = Button(btn_Frame,text='Search',width=12,pady=5,command=search_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b2.grid(row=0,column=1,padx=10,pady=10)

            b3 = Button(btn_Frame,text='Delete',width=12,pady=5,command=delete_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b3.grid(row=1,column=0,padx=10,pady=10)

            b4 = Button(btn_Frame,text='View all',width=12,pady=5,command=view_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b4.grid(row=1,column=1,padx=10,pady=10)

            b5 = Button(btn_Frame,text='Clear',width=12,pady=5,command = clear_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b5.grid(row=1,column=2,padx=10,pady=10)

            b6 = Button(btn_Frame,text='Update',width=12,pady=5,command=update_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b6.grid(row=0,column=2,padx=10,pady=10)

            b7 = Button(self.root,text='Back',width=12,pady=5,command = self.homepage,cursor='hand2',font=('times new roman',15),bg="white",fg="midnightblue",bd=0,height=1)
            b7.place(x=1150,y=15)


    def performance(self):

            def connect():
                conn = pymysql.connect(host="localhost",user="root",password="hardikpandya33",database="performing_arts")
                cur = conn.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS performance (pid VARCHAR(50) PRIMARY KEY ,
                                                                       pname VARCHAR(50) ,
                                                                       pdate VARCHAR(50) ,
                                                                       time VARCHAR(50),
                                                                       venue VARCHAR(50) ,
                                                                       city VARCHAR(50),
                                                                       no_of_stud VARCHAR(50),
                                                                       iid VARCHAR(50) ,
                                                                       FOREIGN KEY (iid) REFERENCES instructor(iid))""")
                conn.commit()
                conn.close()

            def insert_per(pid , pname , pdate , time , venue , city ,no_of_stud , iid ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("INSERT INTO performance VALUES (%s,%s,%s,%s,%s,%s,%s,%s )" , (pid , pname , pdate , time , venue , city , no_of_stud , iid   ))
                print(pid , pname , pdate , time , venue , city ,no_of_stud , iid  )
                conn.commit()
                conn.close()

            def view_per():
                conn = pymysql.connect(host="localhost",user="root",password="hardikpandya33",database="performing_arts")
                cur = conn.cursor()
                cur.execute('''SELECT * FROM performance;''')
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows

            def delete_per(pid):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("DELETE FROM performance WHERE pid=%s ", (pid,))
                print(pid ,'deleted successfully')
                conn.commit()
                conn.close()

            def update_per(pname , pdate , time , venue , city , no_of_stud , pid ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("""UPDATE performance SET pname=%s , pdate=%s , time=%s , venue=%s , city=%s ,no_of_stud=%s 
                               WHERE pid=%s """, (pname , pdate , time , venue , city ,no_of_stud , pid))
                conn.commit()
                conn.close()


            def search_per(pid='' , pname='' , pdate='' , time='' , venue='' ,  city='' , no_of_stud='' , iid='' ):
                conn = pymysql.connect(host="localhost" , user="root" , password="hardikpandya33" , database="performing_arts")
                cur = conn.cursor()
                cur.execute("""SELECT * FROM performance WHERE pid=%s  OR pname=%s OR pdate=%s
                               OR time=%s OR venue=%s OR city=%s OR no_of_stud=%s OR iid=%s """ , (pid , pname , pdate , time , venue , city , no_of_stud , iid ))
                rows = cur.fetchall()
                conn.commit()
                conn.close()
                return rows

            connect()

            def get_selected_row(event):
                 global selected_row
                 index = list.curselection()[0]
                 selected_row = list.get(index)
                 e1.delete(0,END)
                 e1.insert(END,selected_row[0])
                 e2.delete(0,END)
                 e2.insert(END,selected_row[1])
                 e3.delete(0,END)
                 e3.insert(END,selected_row[2])
                 e4.delete(0,END)
                 e4.insert(END,selected_row[3])
                 e5.delete(0,END)
                 e5.insert(END,selected_row[4])
                 e6.delete(0,END)
                 e6.insert(END,selected_row[5])
                 e7.delete(0,END)
                 e7.insert(END,selected_row[6])
                 e8.delete(0,END)
                 e8.insert(END,selected_row[7])


            def delete_command():
               delete_per(selected_row[0])
               messagebox.showinfo("Success","Successfully Deleted the field")

            def view_command():
                 list.delete(0,END)
                 for row in view_per():
                    list.insert(END,row)
                
                 
            def search_command():
                list.delete(0,END)
                for row in search_per(self.pid_text.get(),self.pname_text.get(),self.date_text.get(),self.time_text.get(),self.venue_text.get(),self.city_text.get(),self.no_stud_text.get(),self.iid_text.get()):
                    list.insert(END,row)

            def add_command():
                if self.pid_text.get()=="" or self.pname_text.get()=="" or self.date_text.get()=="" or self.time_text.get()=="" or self.venue_text.get()=="" or self.city_text.get()=="" or self.no_stud_text.get()=="" or self.iid_text.get()==""  :
                        messagebox.showerror("Error","All fields are required")
                else:
                    insert_per(self.pid_text.get(),self.pname_text.get(),self.date_text.get(),self.time_text.get(),self.venue_text.get(),self.city_text.get(),self.no_stud_text.get(),self.iid_text.get())

                    list.delete(0,END)
                    list.insert(END,(self.pid_text.get(),self.pname_text.get(),self.date_text.get(),self.time_text.get(),self.venue_text.get(),self.city_text.get(),self.no_stud_text.get(),self.iid_text.get()))

            def update_command():
                update_per(self.pname_text.get(),self.date_text.get(),self.time_text.get(),self.venue_text.get(),self.city_text.get(),self.no_stud_text.get(),self.pid_text.get())
      
               
                list.delete(0,END)
                list.insert(END,(self.pname_text.get(),self.date_text.get(),self.time_text.get(),self.venue_text.get(),self.city_text.get(),self.no_stud_text.get(),self.pid_text.get()))

            def clear_command():
                self.pid_text.set("")
                self.pname_text.set("")
                self.date_text.set("")
                self.time_text.set("")
                self.venue_text.set("")
                self.city_text.set("")
                self.no_stud_text.set("")
                self.iid_text.set("")

            background= Label(self.root,bg='midnightblue')
            background.place(x=0,y=0,height=700,width=1350)

            Manage_Frame=Frame(self.root ,bd=4,bg="white")
            Manage_Frame.place(x=20,y=100,width=450,height=580)

            m_title=Label(self.root ,text="PERFORMANCE DETAILS",bg='midnightblue',fg="white",font=("georgia",30,"bold"))
            m_title.place(x=15,y=15)

            #---------label-----------
            l1 = Label( Manage_Frame, text='Pno',fg="black",bg="white",font=("times new roman",18,"bold"))
            l1.grid(row=1,column=0,pady=10,padx=20,sticky="w")
            l2 = Label( Manage_Frame, text='Name',fg="black",bg="white",font=("times new roman",18,"bold"))
            l2.grid(row=2,column=0,pady=10,padx=20,sticky="w")
            l3 = Label( Manage_Frame, text='Date',fg="black",bg="white",font=("times new roman",18,"bold"))
            l3.grid(row=3,column=0,pady=10,padx=20,sticky="w")
            l4 = Label( Manage_Frame, text='Time',fg="black",bg="white",font=("times new roman",18,"bold"))
            l4.grid(row=4,column=0,pady=10,padx=20,sticky="w")
            l5 = Label( Manage_Frame, text='Venue',fg="black",bg="white",font=("times new roman",18,"bold"))
            l5.grid(row=5,column=0,pady=10,padx=20,sticky="w")
            l6 = Label( Manage_Frame, text='City',fg="black",bg="white",font=("times new roman",18,"bold"))
            l6.grid(row=6,column=0,pady=10,padx=20,sticky="w")
            l7 = Label( Manage_Frame, text='Students\n performing',fg="black",bg="white",font=("times new roman",18,"bold"))
            l7.grid(row=7,column=0,pady=10,padx=20,sticky="w")
            l8 = Label( Manage_Frame, text='Instructor ID',fg="black",bg="white",font=("times new roman",18,"bold"))
            l8.grid(row=8,column=0,pady=10,padx=20,sticky="w")


            #------------text entry------------------
            self.pid_text = StringVar()
            e1 = Entry( Manage_Frame, textvariable=self.pid_text,font=('times new roman',15,'bold'),bg="lightgray")
            e1.grid(row=1,column=1)

            self.pname_text = StringVar()
            e2 = Entry( Manage_Frame, textvariable=self.pname_text,font=('times new roman',15,'bold'),bg="lightgray")
            e2.grid(row=2,column=1)

            self.date_text = StringVar()
            e3 = Entry( Manage_Frame, textvariable=self.date_text,font=('times new roman',15,'bold'),bg="lightgray")
            e3.grid(row=3,column=1)

            self.time_text = StringVar()
            e4 = Entry( Manage_Frame, textvariable=self.time_text,font=('times new roman',15,'bold'),bg="lightgray")
            e4.grid(row=4,column=1)

            self.venue_text = StringVar()
            e5 = Entry( Manage_Frame, textvariable=self.venue_text,font=('times new roman',15,'bold'),bg="lightgray")
            e5.grid(row=5,column=1)

            self.city_text = StringVar()
            e6 = Entry( Manage_Frame, textvariable=self.city_text,font=('times new roman',15,'bold'),bg="lightgray")
            e6.grid(row=6,column=1)

            self.no_stud_text = StringVar()
            e7 = Entry( Manage_Frame, textvariable=self.no_stud_text,font=('times new roman',15,'bold'),bg="lightgray")
            e7.grid(row=7,column=1)

            self.iid_text = StringVar()
            e8 = Entry( Manage_Frame, textvariable=self.iid_text,font=('times new roman',15,'bold'),bg="lightgray")
            e8.grid(row=8,column=1)

            #---------list box-----------------------
            list = Listbox(self.root,height=10,width=40,font=("times new roman",18),fg="black",bg="white" )
            list.place(x=480,y=100,width=780,height=580)

            sb = Scrollbar(self.root)
            sb.place(x=1260,y=100,width=30,height=580)

            list.bind('<<ListboxSelect>>',get_selected_row)

            #-----------buttons------------------------
            btn_Frame=Frame(self.root,bd=4,bg="white")
            btn_Frame.place(x=20,y=550,width=420)

            b1 = Button(btn_Frame,text='Add',width=12,pady=5,command=add_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b1.grid(row=0,column=0,padx=10,pady=10)

            b2 = Button(btn_Frame,text='Search',width=12,pady=5,command=search_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b2.grid(row=0,column=1,padx=10,pady=10)

            b3 = Button(btn_Frame,text='Delete',width=12,pady=5,command=delete_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b3.grid(row=1,column=0,padx=10,pady=10)

            b4 = Button(btn_Frame,text='View all',width=12,pady=5,command=view_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b4.grid(row=1,column=1,padx=10,pady=10)

            b5 = Button(btn_Frame,text='Clear',width=12,pady=5,command = clear_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b5.grid(row=1,column=2,padx=10,pady=10)

            b6 = Button(btn_Frame,text='Update',width=12,pady=5,command = update_command,cursor='hand2',font=('times new roman',12),fg="white",bg="midnightblue",bd=0)
            b6.grid(row=0,column=2,padx=10,pady=10)

            b7 = Button(self.root,text='Back',width=12,pady=5,command = self.homepage,cursor='hand2',font=('times new roman',15),bg="white",fg="midnightblue",bd=0,height=1)
            b7.place(x=1150,y=15)
                    
root=Tk()
ob=Login(root)
root.mainloop()
