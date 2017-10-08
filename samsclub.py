'''

Hey there! If you have made it till here we kindly request you to take a step back :)
If we find out who you are, the consequences will not be good.
And stop fiddling with someone else's work. You can't do shit on your own eh?

// MADE BY AMITATTRY
'''

import requests
import datetime
import json
import sys
import random
import time
import os
import io
from tkinter.filedialog import askopenfilename
from colorama import init
from termcolor import colored
from multiprocessing import Queue as queue

code1 = input("Enter PRFTCF TOKEN : ")

def auth(username,password):
    username1 = username
    password1 = password
    headers = {
        'channel':'mobiApp',
        'Content-Type': 'application/json; charset=UTF-8',
        'Cookie': 'JSESSIONID=7C9C88E82A5D29C55A5746102463D1FA.mobileapp-44276360-17-194902890; AB_param=polaris; NSC_JOtjdfbld3vdt1jc5f4jhqb1qpxh1bc=28d4a3da941d735234a97145fd0e60a02666be01b13de845773331aaffeee5613f9439cf; disSL=1; NSC_JOghxlpodanpqiubo0vmh0choujmbcc=28d4a3dace46642c056050bed9939d36d6831290466978d717fd61e3231bd60f7ffce081; TS014ef44d=0103fe0547eb75643c232c44e22905a466ad8ec28366f8b1a8c885a5d47fd8f01300735fac95be3a7e7bc929796ec1cb182a829485bde06dbd988c4c76ea60c9acdb958382f9df849c3c251d3b85681d829b8b0d8f',
        'User-Agent': 'okhttp/3.4.2',
        'X-NewRelic-ID':'XAYAWV9WGwYEUVBWDwE='
        }
    url = 'https://mobility.samsclub.com/jsonsrv/account.jsp'
    data = {'act':'login','class':'profile','prftcf':code1,'p':password1,'u':username1,'ver':'0.9.1'}
    content = json.dumps(data)

    r = requests.post(url,headers=headers,data=content,allow_redirects=True)
    z = r.text
    p = r.headers
    cookies = (p['Set-Cookie'])

    headers1 = {
        'channel':'mobiApp',
        'Content-Type': 'application/json; charset=UTF-8',
        'Cookie' : cookies,
        'User-Agent': 'okhttp/3.8.0'
        }
    
    
    loda = (("%s:%s")%(username1,password1))
    testx = json.loads(z)
    has = str(testx['err'])
    if str(r.status_code) == '412' or has == "cf_token_exception" or str(r.status_code) == '500':
        print('\033[31m',"[",datetime.datetime.now().time(),"] : ",('%s:%s')%(username1,password1),"Email or password is incorrect \r\n",'\033[33m')
        return ("400") 
    elif (str(r.status_code) == '200'):
        data = json.loads(z)
        check = str((data['err']))
        if (check == "We don't recognize your email address. Please try again or click Forgot Email to find your email. Need help? Contact Member Services at 1.888.746.7726."):
            print('\033[31m',"[",datetime.datetime.now().time(),"] : ",('%s:%s')%(username1,password1),"Email or password is incorrect \r\n",'\033[33m')                
            return ("400")
        elif (check == "Your membership card was recently reported lost or stolen. Please contact Member Services at 1-888–746-7726."):
            print('\033[31m',"[",datetime.datetime.now().time(),"] : ",('%s:%s')%(username1,password1),"Email or password is incorrect \r\n",'\033[33m')                
            return ("400")   
        else :
            urlx = 'https://mobility.samsclub.com/jsonsrv/account/myCashRewardSummary.jsp'
            parsing = requests.get(urlx,headers=headers1)
            print (" ")
            last = parsing.text
            data = json.loads(last) 
            s = str(data['s'])
            if (s == '0'):
                balance = data['cashInfo'][0]['dollAmt']
                balancedate = data['cashInfo'][1]['dollAmt']
                balancenext = data['cashInfo'][1]['dollDesc']
                balance1 = 'Available now: %s, Available at %s: %s' % (balance , balancenext ,balancedate )
                if(balance == None):
                    print('\033[31m',"[",datetime.datetime.now().time(),"] : ",('%s:%s')%(username1,password1),"Email or password is incorrect \r\n",'\033[33m')
                    return ("400")
                else : return (balance1 , balancedate)


ux = input("Enter Email id : ")
px = input("Enter Your password : ")

print (auth(ux,px) )
