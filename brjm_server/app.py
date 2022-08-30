from distutils.debug import DEBUG
from email.mime import application
from sre_constants import SUCCESS
from unittest import result
from flask import Flask, Response, send_file, request, jsonify
from flask_jwt_extended import *
import bcrypt
import json
import socket
import random, string
from requests import get
import mysqlDB as mDB
from curd import *
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
from secret import *

app = Flask (__name__)


#토큰 SECRET KEY
app.config.update(
    DEBUG = True,
    JWT_SECRET_KEY = BRJM_JWT_SECRET_KEY
)


#메일 모듈
mail = Mail(app)

app.config['MAIL_SERVER'] = BRJM_MAIL_SERVER
app.config['MAIL_PORT'] = BRJM_MAIL_PORT
app.config['MAIL_USERNAME'] = BRJM_MAIL_USERNAME
app.config['MAIL_PASSWORD'] = BRJM_MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = BRJM_USE_TLS
app.config['MAIL_USE_SSL'] = BRJM_USE_SSL
mail = Mail(app)



#JWT 확장 모듈
jwt = JWTManager(app)


#비밀번호 암호화 모듈
bcrypt = Bcrypt(app)
    

#회원가입/이메일 인증
@app.route('/user/register/email', methods = ['POST'])
def EmailVerification():
    received = request.get_json()
    input_email = received['email']
    user_email = []
    user_email.append(input_email)
    
    #인증코드 생성
    verificationCode = ""
    _LENGTH = 6
    string_pool = string.digits
    for i in range(_LENGTH):
        verificationCode += random.choice(string_pool)
    
    #인증코드 메일 전송
    msg = Message("BRJM Email Verification", sender="projbrjm@gmail.com", recipients=user_email)
    msg.body = "BRJM Email Verification Code : " + verificationCode
    mail.send(msg)
    return "Check Email"


#회원가입/비밀번호
@app.route('/user/register/password', methods = ['POST'])
def registerPassword():
    received = request.get_json()
    input_password = received['password']
    user_password = []
    user_password.append(input_password)
    
    return user_password
    
    # #비밀번호 암호화
    # hashed_password = bcrypt.generate_password_hash(user_password)
    # bcrypt.check_password_hash(hashed_password, user_password)
    
    # return hashed_password
    
    
#회원가입/닉네임 & 카테고리
@app.route('/user/register/nickname', methods = ["POST"])
def registerNickname():
    received = request.get_json()
    input_nickname = received['nickname']
    select_query = "SELECT nickname FROM users WHERE nickname = '" + input_nickname + "'"
    db_nickname = loadData(0, select_query)   
    if input_nickname == db_nickname:
        return "Duplicate Nickname"
    else:
        return "Available Nickname"
    
    
#회원가입/회원정보 저장
@app.route('/user/register',methods = ['POST'])
def register():
    received = request.get_json()
    form = ['email', 'hashed_password', 'nickname']
    user_data = []
    for i in form:
        user_data.append(received[i])
    insert_query = "INSERT INTO users (email, hashed_password, nickname) VALUES (%s, %s, %s)"
    insert_values = tuple(user_data)
    result = saveData(insert_query, insert_values)
    return result
    

#로그인
@app.route('/user/login', methods = ['POST'])
def login():
    received = request.get_json()
    input_email = received['email']
    input_password = received['password']
    select_query = "SELECT email, hashed_password FROM users WHERE email = '" + input_email + "'"
    login_data = list(loadData(1, select_query))
    user_data = []
    user_data.append(input_email)
    user_data.append(input_password)
    # if str(login_data[0]) == str(user_data[0]):
    #     if str(login_data[1]) == str(user_data[1]):
    #         return "Login Success"
    #     else:
    #         return "Check Password"
    # else:
    #     return "Check Email or Password"

    
#환경소식
@app.route('/main/news', methods = ['GET'])
def news():
    select_query = "SELECT title, url FROM news"
    data = loadData(1, select_query)
    return jsonify(data), 
    
    
if __name__ == "__main__":
    app.run()