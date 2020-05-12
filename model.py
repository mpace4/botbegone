import tweepy
import datetime
import view
from datetime import *
from datetime import timedelta

consumer_key = "m5XWyiFCftLbilaFKzuq6ykVU"
consumer_secret = "odau6ZII3wakrKfmk6r0GVUum8QfIGOvAjGQE0OB7P94XX4FNh"
access_token = "55760344-QZlzNLv9hYxEG6u89JMpB5sul4RL383GlHhmLZYsb"
access_token_secret = "Ax7yPGwUckJKY5MZZRbYexFj0OZY2Ux0LcHZTSB1sHB4k"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweetTime = []
tweetText = []
rtcount = 0
count = 20
username = ""
botPoints = 0
checkDatePoints = 0
picPoints = 0
tweetCheckerPoints = 0
RTPoints = 0
tweetDatePoints = 0
bioPoints = 0

def search():
    global username, acctDesc, tweetText, location, following, follwers
    global totaltweets, usercreatedts, count, profile_pic
    
    username = view.twitter_username_input()
    
    try: # check for invalid username
        dummy = api.user_timeline(id=username, count=1)
    except tweepy.TweepError:
        print("Incorrect username")
        username = view.twitter_username_input()
    
    for tweet in api.user_timeline(id=username, count=count):
        totaltweets = tweet.user.statuses_count
        if totaltweets < count:
            count = totaltweets
        
        tweetTime.append(tweet.created_at)
        tweetText.append(tweet.text)
    
    acctDesc = tweet.user.description
    location = tweet.user.location
    following = tweet.user.friends_count
    followers = tweet.user.followers_count
    usercreatedts = tweet.user.created_at
    print(acctDesc)
    profile_pic = tweet.user.profile_image_url
        
def rtcounter()-> None:
    global rtcount
    num = 0
    counter = count
    while (num < counter):
        if len(tweetText[num]) > 2:
            if tweetText[num][:2] == "RT":
                tweetText.remove(tweetText[num])
                rtcount = rtcount + 1
                counter = counter - 1
                num = num - 2
        num = num + 1
        
def tweetChecker()->None:
    global botPoints, tweetCheckerPoints
    num = 0
    counter = count - rtcount
    length = 0
    num_compare = 0
    while (num < counter - 1):
        first_list = tweetText[num]
        first_list = [word.strip(",.()/*-+`~!@#$%^&*;=<>?")
                 for word in first_list.lower().split(" ")]
        set1 = set(first_list)
        num = num + 1
        element = num

        while(element < counter):
            sec_list = tweetText[element]
            sec_list = [word.strip(",.()/*-+`~!@#$%^&*;=<>?")
                 for word in sec_list.lower().split(" ")]
            set2 = set(sec_list)
            intersection = set1 & set2
            length = len(set1) + len(set2)
            total = (len(intersection) * 2) / length 
            if total >= .50:
                botPoints = botPoints + 5
                tweetCheckerPoints = 5
            elif total >= .35:
                botPoints = botPoints + 3
                tweetCheckerPoints = 3
            elif total >= .20:
                botPoints = botPoints + 1
                tweetCheckerPoints = 1
            element = element + 1
            num_compare = num_compare + 1
    botPoints = botPoints / num_compare
    tweetCheckerPoints = tweetCheckerPoints / num_compare
    if botPoints < 1:
        botPoints = 0
   

def checkRT():
    global botPoints, RTPoints
    rtNum = rtcount / count
    if rtNum >= .60:
        botPoints = botPoints + 5
        RTPoints = 5
    elif rtNum >= .45:
        botPoints = botPoints + 3
        RTPoints = 3
    elif rtNum >= .30:
        botPoints = botPoints + 1
        RTPoints = 1


def tweetDateTime()-> None:
    global tweetTime
    global botPoints, tweetDatePoints
    tweetElem = count - 1
    pairs = tweetElem
    num = 0
    monthstart = 5
    monthend = 7
    daystart = 8
    dayend = 10
    hourstart = 11
    hourend = 13
    minstart = 14
    minend = 16
    matches = 0
    while (num < tweetElem):
        list1 = str(tweetTime[num])
        list2 = str(tweetTime[num + 1])
        list1month = list1[monthstart:monthend]
        list2month = list2[monthstart:monthend]
        list1day = list1[daystart:dayend]
        list2day = list2[daystart:dayend]
        list1hour = list1[hourstart:hourend]
        list2hour = list2[hourstart:hourend]
        list1min = int(list1[minstart:minend])
        list2min = int(list2[minstart:minend])
        num = num + 1
        
        if list1month != list2month or list1day != list2day:
            if list1hour == list2hour:
               matches = matches + 1
        elif list1day == list2day or list1hour != list2hour:
            if list1min + 5 > list2min or list1min - 5 < list2min :
                matches = matches + 1
    total = matches / pairs
    if total >= .50:
        botPoints = botPoints + 5
        tweetDatePoints = 5
    elif total >= .35:
        botPoints = botPoints + 3
        tweetDatePoints = 3
    elif total >= .20:
        botPoints = botPoints + 1
        tweetDatePoints = 1


def checkPic():
    global profile_pic, botPoints, picPoints
    
    if profile_pic == "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png":
        botPoints = botPoints + 5
        picPoints = 5
        print(picPoints)

def checkDate():
    global usercreatedts, botPoints, checkDatePoints
    current_date = datetime.now()
        
    if usercreatedts > (datetime.now() - timedelta(days = 7)):
        botPoints = botPoints + 5
        checkDatePoints = 5
    elif usercreatedts > (datetime.now() - timedelta(days = 30)):
        botPoints = botPoints + 3
        checkDatePoints = 3
    elif usercreatedts > (datetime.now() - timedelta(days = 60)):
        botPoints = botPoints + 1
        checkDatePoints = 1
        
def checkBio():
    global botPoints, acctDesc, picPoints, bioPoints
    if acctDesc == "":
        botPoints = botPoints + 3
        bioPoints = 3
        
    
def main():
    mainList = []
    search()
    rtcounter()
    tweetChecker()
    checkPic()
    checkDate()
    checkRT()
    checkBio()
    tweetDateTime()
    print(picPoints)
    mainList = [f"tweet time: {tweetDatePoints} out of 5",f"check date: {checkDatePoints} out of 5", 
                f"profile picture: {picPoints} out of 5", f"tweet checker: {tweetCheckerPoints} out of 5",
                f"check bio: {bioPoints} out of 3", f"total bot points: {botPoints}"]
    view.display_output(mainList)
    #print("bot points: " + str(botPoints))

    
