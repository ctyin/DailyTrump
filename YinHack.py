import smtplib
from email.mime.text import MIMEText
from time import sleep
import random

verbs = ['is',"gonna be",'love',"build","stop","scam","create","rig"]
adverbs = ["bigly","absolutely",'super','really','very','totally','good']
adjectives = ["huge","big league","corrupt","rigged",'WRONG!','crooked','corrupt']
nouns = ["winning",'ISIS','Russia','scams',"China","Mexico","wall","corruption","polls","Mexicans","emails","nukes",'global warming']
people = ['Hillary','Donald J. Drumpf','media','Ted Cruz','Ivanka','Melania','Obama',"bad hombres", "the blacks"]

def select_structure(x):
    n = nouns[random.randint(0,len(nouns)-1)]
    v1 = verbs[random.randint(0,len(verbs)-1)]
    adj = adjectives[random.randint(0,len(adjectives)-1)]
    p = people[random.randint(0,len(people)-1)]
    avphrase = ("%s, %s %s")%(adj, adverbs[random.randint(0,len(adverbs)-1)], adj)
    for mult in range(random.randint(0,1)):
        avphrase += (", %s %s")%(adverbs[random.randint(0,len(adverbs)-1)],adj)
    return{
        1:("%s %s %s. ")%(n.title(),v1,avphrase), #it's gonna be huge (really huge)
        2:("The %s %s %s the %s for %s. ")%(adj,p,v1,n,p), #the crooked media rigged the polls for Hillary
        3:("If %s wasn't my %s I might %s them. ")%(p,n,v1), #if ivanka wasn't my daughter i might be dating her
        4:("%s had a %s %s. %s will %s %s about this. ")%(p.title(),adj,n,people[random.randint(0,len(people)-1)],v1,n) #I've had a flawless campaign. you'll be writing books about this campaign
    }.get(x,("%s %s %s")%(n.capitalize(),v1,avphrase))

def create_message(sentences):
    a = ""
    for i in range(sentences):
        a += select_structure(random.randint(1,4))
    return a

def send_infinite(receiver,sentences):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('dankmaomemes@gmail.com', "allhailTheChairman")
    
    for i in range(0,999): 
        msg = MIMEText(create_message(sentences))
        msg['Subject'] = create_message(1)
        server.sendmail("dankmaomemes@gmail.com", receiver, msg.as_string())
        sleep(1) 

def send(receiver,sentences):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('username', "password") #enter your own info lmfao
    msg = MIMEText(create_message(sentences))
    msg['Subject'] = 'Your Daily Trump'
    server.sendmail("dankmaomemes@gmail.com", receiver, msg.as_string())    

def sendMemes(receiver,sentences):
    inp = raw_input("Become a spam bot? Y/N: ") #infinite loop until error
    if inp.upper()=='Y':
        try:
            send_infinite(receiver,sentences) 
        except:
            send_infinite(receiver,sentences)
    else:
        send(receiver,sentences)