from Tkinter import *
import tkMessageBox
reg=Tk()
from bankfxn import Fxn
fxn=Fxn()
class ui():
    uname_e=None
    pass_e=None
    nam_e=None
    ema_e=None
    pass_e=None
    addu=None
    amtt=None
    typt=None
    namt=None
    csvx=None
    def loginf(self):
        #global pass_w
       # global name_w
        log=Toplevel()
        #log.geometry('1800x1080')
        w,h=log.winfo_screenwidth(),log.winfo_screenheight()
        reg.overrideredirect(1)
        log.geometry("%dx%d+0+0"%(w,h))
        log.title("Login page",)
        log.configure(background='mint cream')
        log.title("Login page")
        Label(log,text="Login Page",height=2,width=600,bg='mint cream',font=("Arial",18)).pack()
        Label(log,text="",height=2,width=600,bg='mint cream').pack()
        Label(log,text="Name:",height=2,width=600,bg='mint cream',font=(18)).pack()
        name_w=Entry(log)
        name_w.pack()
        Label(log,text="",height=2,width=600,bg='mint cream').pack()
        Label(log,text="Password",height=2,width=600,bg='mint cream',font=(18)).pack()
        Label(log,text="",height=2,width=600,bg='mint cream').pack()
        pass_w=Entry(log,show='*')
        pass_w.pack()
        Label(log,text="",height=2,width=600,bg='mint cream').pack()
        Button(log,text="Login",height=2,width=10,bg='cornsilk2',command=self.go_to_afterlogin,font=("Arial",18)).pack()
        Label(log,text="",height=2,width=600,bg='mint cream').pack()
        Button(log,text="Exit",height=2,width=10,command=log.destroy,bg='cornsilk2',font=("Arial",18)).pack()
        self.uname_e=name_w
        self.pass_e=pass_w
        log.mainloop()
    def go_to_afterlogin(self):
        name_input1=self.uname_e.get()
        pass_input1=self.pass_e.get()
        yes=fxn.conn(name_input1,pass_input1)
        if yes is True:
            self.dashboard()
    def addmoney(self):
        #global ad_d
        add=Toplevel()
        #add.geometry('1800x1080')
        w,h=add.winfo_screenwidth(),add.winfo_screenheight()
        add.overrideredirect(1)
        add.geometry("%dx%d+0+0"%(w,h))
        add.title('Add money')
        add.configure(background='mint cream')
        Label(add,text="Enter the amount",height=2,width=600,font=(18),bg='cornsilk2').pack()
        Label(add,text="",height=2,width=600,bg='mint cream',font=(18)).pack()
        ad_d=Entry(add)
        ad_d.pack()
        Label(add,text="",height=2,width=600,bg='mint cream').pack()
        Button(add,text="Add money",height=2,width=10,command=self.add_m,font=(18),bg='cornsilk2').pack()
        Label(add,text="",height=2,width=600,bg='mint cream').pack()
        Button(add,text="Exit",height=2,width=10,command=add.destroy,font=(18),bg='cornsilk2').pack()
        self.addu=ad_d
        add.mainloop()
    def add_m(self):
        add_ip=self.addu.get()
        name_input2=self.uname_e.get()
        fxn.add_money(add_ip,name_input2)
    def transfer(self):
##        global amt
##        global nam
##        global typ_tra
        tra=Toplevel()
        #tra.geometry('1800x1080')
        w,h=tra.winfo_screenwidth(),tra.winfo_screenheight()
        tra.overrideredirect(1)
        tra.geometry("%dx%d+0+0"%(w,h))
        tra.title("Transfer section")
        tra.configure(background='mint cream')
        Label(tra,text="Transfer",height=2,width=600,bg='cornsilk2',font=("Arial",20)).pack()
        Label(tra,text="",height=2,width=600,bg='mint cream').pack()
        Label(tra,text="Amount to be transferred",height=2,width=600,bg='mint cream',font=(18)).pack()
        amt=Entry(tra)
        amt.pack()
        Label(tra,text="",height=2,width=600,bg='mint cream').pack()
        Label(tra,text="Name to whom the amount is to be transferred",height=2,width=600,bg='mint cream',font=(18)).pack()
        Label(tra,text="",height=2,width=600,bg='mint cream').pack()
        nam=Entry(tra)
        nam.pack()
        Label(tra,text="Type of transfer",height=2,width=600,bg='mint cream',font=(18)).pack()
        typ_tra=Entry(tra)
        typ_tra.pack()
        Label(tra,text="",height=2,width=600,bg='mint cream',font=(18)).pack()
        Button(tra,text="Transfer",height=2,width=10,bg='cornsilk2',command=self.tran_to).pack()
       # tkMessageBox.showinfo("Status","successfull Transfer")
        Label(tra,text="",height=2,width=600,bg='mint cream').pack()
        Button(tra,text="Exit",height=2,width=10,command=tra.destroy,bg='cornsilk2',font=(18)).pack()
        self.amtt=amt
        self.namt=nam
        self.typt=typ_tra
        tra.mainloop()
    def tran_to(self):
        na_m=self.uname_e.get()
        na=self.namt.get()
        ty=self.typt.get()
        am=self.amtt.get()
        fxn.tran(na_m,na,ty,am)
    def dashboard(self):
        dash=Toplevel()
        #dash.geometry('1800x1080')
        w,h=dash.winfo_screenwidth(),dash.winfo_screenheight()
        dash.overrideredirect(1)
        dash.geometry("%dx%d+0+0"%(w,h))
        dash.title("Dashboard")
        dash.configure(background='mint cream')
        Label(dash,text="Welcome to our Bank",height=2,width=600,font=("Arial",21),bg="cornsilk2").pack()
        Label(dash,text="",height=2,width=600,bg='mint cream').pack()
        Button(dash,text="Add",height=2,width=10,command=self.addmoney,bg='cornsilk2',font=(18)).pack()
        Label(dash,text="",height=2,width=600,bg='mint cream').pack()
        Button(dash,text="Transfer",height=2,width=10,command=self.transfer,bg='cornsilk2',font=(18)).pack()
        Label(dash,text="",height=2,width=700,bg='mint cream').pack()
        Button(dash,text="View passbook",height=2,width=20,bg='cornsilk2',command=self.passb,font=(18)).pack()
        Label(dash,text="",height=2,width=600,bg='mint cream').pack()
        Button(dash,text="Exit",height=2,width=10,command=dash.destroy,bg='cornsilk2',font=(18)).pack()
        dash.mainloop()
    def mynofriend(self):
        nou=Toplevel()
        nou.attributes("-fullscreen", True)
        w,h=nou.winfo_screenwidth(),nou.winfo_screenheight()
        nou.overrideredirect(1)
        nou.geometry("%dx%d+0+0"%(w,h))
        nou.title("Login page")
        nou.configure(background='mint cream')
        Label(nou,text="Registration Page",height=2,width=600,bg='cornsilk2',font=("Arial",20)).pack()
        Label(nou,text="",height=2,width=600,bg='mint cream',font=('Arial',10)).pack()
        Label(nou,text="Name",height=3,width=50,font=18,bg='cornsilk2').pack()
        Label(nou,text="",height=2,width=600,bg='mint cream',font=18).pack()
        name=Entry(nou)
        name.pack()
        Label(nou,text="",height=2,width=600,bg='mint cream').pack()
        Label(nou,text="Password",height=3,width=50,bg='cornsilk2',font=(18)).pack()
        Label(nou,text="",height=2,width=600,bg='mint cream').pack()
        password=Entry(nou,width=20)
        password.pack()
        Label(nou,text="",height=2,width=600,bg='mint cream',font=(18)).pack()
        Label(nou,text="Email",height=3,width=50,font=(18),bg='cornsilk2').pack()
        Label(nou,text="",height=2,width=600,bg='mint cream',font=(18)).pack()
        email=Entry(nou)
        email.pack()
        Label(nou,text="",height=2,width=600,bg='mint cream',font=(18)).pack()
        Button(nou,text="Register",height=2,width=10,bg='cornsilk2',command=self.reg_name,font=("Arial",18)).pack()
        Label(nou,text="",height=2,width=600,bg='mint cream',font=(18)).pack()
        Button(nou,text="Exit",height=2,width=10,command=nou.destroy,bg='cornsilk2',font=("Arial",18)).pack()
        self.nam_e=name
        self.ema_e=email
        self.pass_e=password
        nou.mainloop()
    def reg_name(self):
        nam_ip=self.nam_e.get()
        email_ip=self.ema_e.get()
        pass_ip=self.pass_e.get()
        fxn.dbconnection(nam_ip,email_ip,pass_ip)
    def passb(self):
        
        #nam=name_w.get()
        pa=Toplevel()
        pa.geometry('800x800')
        nam=self.uname_e.get()
    ##    w,h=pa.winfo_screenwidth(),pa.winfo_screenheight()
    ##    pa.overrideredirect(1)
    ##    pa.geometry("%dx%d+0+0"%(w,h))
        pa.title("Passbook")
        pa.configure(background='mint cream')
        #Label(pa,text="Passbook",height=2,width=600,bg='cornsilk2',font=(12)).pack()
        Label(pa,text="",height=2,width=600,bg='mint cream').pack()
        listbox=Listbox(pa,width=25,height=20)
        listbox.pack()
        Label(pa,text="Id Sender Recevier Amount Type",bg='cornsilk').pack()
        #listbox.insert(END,"ID Sender Recevier Amount Type")
        tb=fxn.pass_b(nam)
        
        for i in range(len(tb)):
            listbox.insert(END,tb[i])
        
    ##        Label(pa,text=(tb[i][0],tb[i][1],tb[i][2],tb[i][3],tb[i][4]),width=300,height=1,bg='cornsilk').pack()
    ##    Label(pa,text="",height=2,width=600,bg='mint cream').pack()
        Button(pa,text="Export to CSV file",width=15,height=2,bg='cornsilk2',command=self.csv).pack()
        Label(pa,text="",bg='mint cream',height=2,width=10).pack()
        Button(pa,text="Exit",height=2,width=10,command=pa.destroy,bg='cornsilk2').pack()
        tx=[]
        for i in range(len(tb)):
            tx.append(list(tb[i]))
        self.csvx=tx
        #print tx
        pa.mainloop()
        
    def csv(self):
        cdx=self.csvx
        fxn.csv_file(cdx)
        
mainfxn=ui()
reg.title("Registration Form")
w,h=reg.winfo_screenwidth(),reg.winfo_screenheight()
reg.overrideredirect(1)
reg.geometry("%dx%d+0+0"%(w,h))
reg.configure(background='mint cream')
Label(reg,text="Welcome to ZZZ bank",height=2,width=20,bg='cornsilk2',font=("Arial",20)).pack()
Label(reg,text="",bg='mint cream',height=2,width=10).pack()
Button(reg,text="Login",height=2,width=20,bg='cornsilk2',font=(10),command=mainfxn.loginf).pack()
Label(reg,text="",bg='mint cream',height=2,width=10).pack()
Button(reg,text="press for new registration:",height=2,width=30,command=mainfxn.mynofriend,bg='cornsilk2',font=(10)).pack()
Label(reg,text="",bg='mint cream',height=2,width=10).pack()
Button(reg,text="Exit",height=2,width=10,command=reg.destroy,bg='cornsilk2',font=(10)).pack()
reg.mainloop()


    
