import mysql.connector as con
from Tkinter import *
import tkMessageBox
import csv
db=con.connect()
db=con.connect(host="localhost",user="root",password="root",database="mydb")
cur=db.cursor()
class Fxn():
    def conn(self,name,password):
##        name_input1=self.uname_e.get()
##        pass_input1=self.pass_e.get()
        q="select name from login"
        cur.execute(q)
        qc=cur.fetchall()
        for i in range(len(qc)):
            q1="select * from login where name='"+name+"' and password='"+password+"'"
            cur.execute(q1)
            c=cur.fetchall()
            if(len(c)>0):
                flag=1
            else:
                flag=0
        if(flag==1):
            tkMessageBox.showinfo("information","successfull login")
            return True
            
        elif(flag==0):
            tkMessageBox.showinfo("information","Unsuccessfull login")
       
        db.commit()
    def add_money(self,add_ip,name_input2):
##        add_ip=self.addu.get()
##        name_input2=self.uname_e.get()
        fet_mo="select balance from login where name='"+name_input2+"'"
        cur.execute(fet_mo)
        fetc_mo=cur.fetchone()
        amt=int(fetc_mo[0])+int(add_ip)
        amt=str(amt)
        quee="update login set balance='"+amt+"' where name='"+name_input2+"'"
        cur.execute(quee)
        db.commit()
        
        
    def tran(self,na_m,na,ty,am):
##        am=amt.get()    
##        na=nam.get()        ## name to who it is to be transferred
##        ty=typ_tra.get()
##        na_m=name_w.get()   ##name of the user login
##        na_m=self.uname_e.get()
##        na=self.namt.get()
##        ty=self.typt.get()
##        am=self.amtt.get()
        gg='insert into transfer(id, sender, recevier, amount, type) values(%s,%s,%s,%s,%s)'
        e=[0,na_m,na,am,ty]
        cur.execute(gg,e)
        db.commit()

        fet_mo="select balance from login where name='"+na_m+"'"
        cur.execute(fet_mo)
        fetc_mo=cur.fetchone()
        amt2=int(fetc_mo[0])-int(am)
        amt2=str(amt2)
        quee="update login set balance='"+amt2+"' where name='"+na_m+"'"
        cur.execute(quee)
        db.commit()

        fetv="select balance from login where name='"+na+"'"
        cur.execute(fetv)
        fet=cur.fetchone()
        #print fet
        amt3=int(fet[0])+int(am)
        amt3=str(amt3)
        quee2="update login set balance='"+amt3+"' where name='"+na+"'"
        cur.execute(quee2)
        db.commit()
    def dbconnection(self,nam_ip,email_ip,pass_ip):
##        nam_ip=self.nam_e.get()
##        email_ip=self.ema_e.get()
##        pass_ip=self.pass_e.get()
##        nam_ip=self.mynofriend(name)
##        pass_ip=self.mynofriend(password)
##        email_ip=self.mynofriend(email)
        inser_db="insert into login(id, name, email, password, balance) values(%s,%s,%s,%s,%s)"
        #inser_d=[0,nam_ip(name),email_ip(email),pass_ip(password),0]
        inser_d=[0,nam_ip,email_ip,pass_ip,0]
        cur.execute(inser_db,inser_d)
        db.commit()
        db.close()
    def pass_b(self,nam):
        t="select * from transfer where sender='"+nam+"'"
        cur.execute(t)
        tb=cur.fetchall()
        db.commit()
        return tb
    def csv_file(self,cdx):
        with open('Passbook.csv', 'ab') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
                            
            spamwriter.writerow(['TRans_id','Sender','Receiver','Amount','Type'])
            for i in cdx:
                spamwriter.writerow(i)
        
