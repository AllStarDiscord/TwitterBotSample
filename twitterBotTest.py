import time
import random
import csv

print('Logging On')

print('Logged In')

with open(r'C:\Users\darkd\Documents\Twitter Bot\celebrityList.csv',encoding="utf8") as f:
    reader = csv.reader(f)
    celebrityList = list(reader)

with open(r'C:\Users\darkd\Documents\Twitter Bot\event1.csv',encoding="utf8") as j:
    reader2 = csv.reader(j)
    event1List = list(reader2)

with open(r'C:\Users\darkd\Documents\Twitter Bot\event2.csv',encoding="utf8") as l:
    reader3 = csv.reader(l)
    event2List = list(reader3)

with open(r'C:\Users\darkd\Documents\Twitter Bot\place.csv',encoding="utf8") as k:
    reader4 = csv.reader(k)
    placeList = list(reader4)

with open(r'C:\Users\darkd\Documents\Twitter Bot\pastEvent.csv',encoding="utf8",newline='') as m:
    reader5 = csv.reader(m)
    pastEventList = list(reader5)

i=0
kList=(1,2,3,4,5)
while i==0:
    k=random.choice(kList)
    place=random.choice(placeList[0])
    celebrity=random.choice(celebrityList[0])
    pastEvent=random.choice(pastEventList[0])
    if celebrity[-1] in {'s','S'}:
        apostrophe = "'"
    else:
        apostrophe = "'s"
    if k==1:
        event=random.choice(event1List[0])
        if event[0] in {'a','e','i','o','u','A','E','I','O','U'}:
            article = 'an'
        else:
            article = 'a'
        tweet='This is like '+article+' '+event+' at '+celebrity+apostrophe+' '+place+'!'
        #api.update_status(tweet)
        print('Tweet Sent: '+'"'+tweet+'"')
    elif k==2:
        tweet="Note to self: Don't "+pastEvent+' at '+celebrity+apostrophe+'.'

        #api.update_status(tweet)
        print('Tweet Sent: '+'"'+tweet+'"')
    elif k==3:
        event2=random.choice(event2List[0])
        tweet='This is like '+event2+' at '+celebrity+apostrophe+' '+place+'!'
        #api.update_status(tweet)
        print('Tweet Sent: '+'"'+tweet+'"')
    elif k==4:
        event=random.choice(event1List[0])
        event2=random.choice(event2List[0])
        if event[0] in {'a','e','i','o','u','A','E','I','O','U'}:
            article = 'an'
        else:
            article = 'a'
        tweet="I haven't seen "+article+' '+event+' like this since '+event2+' at '+celebrity+apostrophe+' '+place+'!'
        #api.update_status(tweet)
        print('Tweet Sent: '+'"'+tweet+'"')
    elif k==5:
        event2=random.choice(event2List[0])
        tweet="Reminds me of "+event2+' at '+celebrity+apostrophe+'.'
        #api.update_status(tweet)
        print('Tweet Sent: '+'"'+tweet+'"')
    time.sleep(5)
