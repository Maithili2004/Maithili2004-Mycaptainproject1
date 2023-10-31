from django.shortcuts import render
import mysql.connector as sql

em = ''
pwd = ''

def login_action(request):
    global em,pwd
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",passwd="mysql123",database="website")
        cursor=m.cursor()
        d=request.POST
        for k,v in d.items():
            if k == "email":
                em = v
            if k == "password":
                    pwd = v
        c= "select * from users where email ='{}' and password ='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
             return render(request,'error.html')
        else
             return render(request,"welcome.html") 
    
     return render(request,'login_page.html')     
    