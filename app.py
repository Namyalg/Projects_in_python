#!/usr/bin/env python3
import requests
import json
import time
from sys import argv
from flask import Flask
import requests
from flask_cors import CORS

token = ''
sess_id = ''
sess_name = ''
companyId = '2461'
teamId = '2462'
sub_id = ''
teamIds = '2462'
planId = '2467'

import random
import string

def get_random_string(length):
        letters = "abcdefghijklmnopqrstuvwxyz"
        result_str = ''.join(random.choice(letters) for i in range(length))
        return(result_str + "@mail.com")


def auth():
    auth_url = 'https://cloudlabs.nuvepro.com/v1/users/login'
    body = {'username': 'remoapiadmin@nuvelabs.com', 'password' : 'RemoAdmin@321'}
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(auth_url, data=body, headers=headers)
    p = (r.json())
    return(p["token"] , p["sessid"] , p["session_name"])

#------------------------------------------------------------------------------------------------------------------------------------#
def login(token, cook, userName):
    login_url = 'https://cloudlabs.nuvepro.com/v1/users'
    body = {'userName': userName, 'password' : 'come123$', 'firstName' : 'remouser' , 'lastName': 'poc' , 'companyId' : companyId, 'teamId' : teamId}
    header = {'Content-type': 'application/x-www-form-urlencoded', 'X-CSRF-Token' : token}
    w = requests.post(login_url, headers=header, data=body, cookies=cook)
    s = w.json()
    return(s)

#--------------------------------------------------------------------------------------------------------------------------------------#
def add(token, cook, userName):
    
    cook = {sess_name : sess_id}
    add_users_url = 'https://cloudlabs.nuvepro.com/v1/users/addUserIntoTeams'
    header = {'Content-type': 'application/x-www-form-urlencoded', 'X-CSRF-Token' : token}
    add_body = {'userName' : userName , 'companyId' : companyId , 'teamIds' : teamIds}
    add_details = requests.post(add_users_url, headers=header, data=add_body, cookies=cook)
    return(add_details.json())
#-------------------------------------------------------------------------------------------------------------------------------------#

def createsub(token, cook, userName):
    sub_url = 'https://cloudlabs.nuvepro.com/v1/subscriptions'
    header = {'Content-type': 'application/x-www-form-urlencoded', 'X-CSRF-Token' : token}
    body = {'userName' : userName , 'planId' : planId , 'companyId' : companyId, 'teamId' : teamId}
    create_sub = requests.post(sub_url, headers=header, data=body, cookies=cook)
    create_sub = create_sub.json()
    return(create_sub['subscriptionId'])

#----------------------------------------------------------------------------------------------------------------------------------------#

def launch(token, cook, sub_id):
    launch_url = 'https://cloudlabs.nuvepro.com/v1/subscriptions/launch'
    header = {'Content-type': 'application/x-www-form-urlencoded', 'X-CSRF-Token' : token}
    body = {'subscriptionId' : sub_id}
    launch_lab = requests.post(launch_url, headers=header, data=body, cookies=cook)
    p = launch_lab.json()
    pre = 0
    while pre != 1:
        if 'userAccess' not in p:
            time.sleep(60)
            launch_lab = requests.post(launch_url, headers=header, data=body, cookies=cook)
            p = launch_lab.json()
        else:
            pre = 1
            info = dict()
            p = launch_lab.json()
            p = (p['userAccess'])
            #return(json.loads(p))
            one = (json.loads(p)[1]['value'])
            #return(one)
            two = (json.loads(p)[5]['value'])
            info["one"] = one
            info["two"] = two
            return(info)

token, sess_id, sess_name = auth()
cook = {sess_name : sess_id}

#--------------------------------------------------------------------------------------------------------------------------------------#

def info():
    userName = get_random_string(10)
    login(token, cook , userName)
    add(token, cook, userName)
    sub_id = createsub(token, cook, userName)
    time.sleep(3)
    return(sub_id)


app = Flask(__name__)
CORS(app)

@app.route("/")

def main():
    sub_id = info()
    url = launch(token, cook, sub_id)
    return(url)

if __name__ == "__main__":
    app.run()
    print(main())
