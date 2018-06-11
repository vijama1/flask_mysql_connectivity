#!usr/bin/python3

#importing necessary packages
from flask import Flask,render_template,request
import mysql.connector as mysql
app=Flask(__name__)
login_data=[]
register_data=[]
# page="<h1>Flask is fun to learn</h1>"
# post_login="<h1>Welcome</h1>"

#creating an app for home page
@app.route('/')
def webpage():
    return render_template('store_sql.html')

#creating an app for result page
@app.route('/result',methods=['POST'])
def result():
    result=request.form
    for data in result.items():
        register_data.append(data)
    name=register_data[0]
    user_name=name[1]
    mobile=register_data[1]
    user_mobile=int(mobile[1])
    email=register_data[2]
    user_email=email[1]
    password=register_data[3]
    user_password=password[1]
    conn=mysql.connect(user='root',password='password',database='flask',host='localhost')
    if conn.is_connected():
        print("Connected")
        curs=conn.cursor()
        #query='INSERT INTO cgi_info VALUES("%s","%d","%s","%s")'%(name,number,email,password))
        out = curs.execute('insert into user_registration values("%s","%d","%s","%s")'%(user_name,user_mobile,user_email,user_password))
        conn.commit()
        return render_template('login.html')
@app.route('/result',methods=['POST'])
def login():
    return render_template('login.html')




if __name__=="__main__":
    app.run(debug=True,port=9999)
