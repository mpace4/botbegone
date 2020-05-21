import tweepy
import datetime
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
outputList = []
rtcount = 0
count = 20
botPoints = 0


# validate username
def validate_username(username: str) -> None:
    """validate if username is valid or not, if not, raise Value Error"""
    if username == "":
        raise ValueError
    try:
        dummy = api.user_timeline(id=username, count=1)
        del dummy
    except tweepy.TweepError:
        raise ValueError


def search(username: str):
    """search and process user information: username, account description,
        tweets, location, folllwing, followers, profile picture"""
    global acctDesc, tweetText, location, following, follwers
    global totaltweets, usercreatedts, count, profile_pic

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


def rtcounter() -> None:
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


def tweetChecker() -> None:
    global botPoints
    num = length = 0
    counter = count - rtcount
    num_compare = 1
    tweetCheckerPoints = 0
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
                tweetCheckerPoints = 5
            elif total >= .35:
                tweetCheckerPoints = 3
            elif total >= .20:
                tweetCheckerPoints = 1
            element = element + 1
            num_compare = num_compare + 1
    tweetCheckerPoints = tweetCheckerPoints / num_compare
    if tweetCheckerPoints < 1:
        tweetCheckerPoints = 0
    outputList.append(f"Tweet checker: {tweetCheckerPoints} out of 5")
    botPoints += tweetCheckerPoints


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


def tweetDateTime() -> None:
    global tweetTime
    global botPoints
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
    tweetDatePoints = 0
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
            if list1min + 5 > list2min or list1min - 5 < list2min:
                matches = matches + 1
    total = matches / pairs
    if total >= .50:
        tweetDatePoints = 5
    elif total >= .35:
        tweetDatePoints = 3
    elif total >= .20:
        tweetDatePoints = 1
    outputList.append(f"Tweet time: {tweetDatePoints} out of 5")
    botPoints += tweetDatePoints


def checkPic() -> None:
    """check if user have default profile picture"""
    global profile_pic, botPoints
    picPoints = 0
    if profile_pic == "http://abs.twimg.com/sticky/default_profile_images/"\
                      "default_profile_normal.png":
        picPoints = 5
    outputList.append(f"Profile picture: {picPoints} out of 5")
    botPoints += picPoints


def checkDate() -> None:
    """Check how new the user is"""
    global usercreatedts, botPoints
    checkDatePoints = 0
    if usercreatedts > (datetime.now() - timedelta(days=7)):
        checkDatePoints = 5
    elif usercreatedts > (datetime.now() - timedelta(days=30)):
        checkDatePoints = 3
    elif usercreatedts > (datetime.now() - timedelta(days=60)):
        checkDatePoints = 1

    outputList.append(f"Check date: {checkDatePoints} out of 5")
    botPoints += checkDatePoints


def checkBio() -> None:
    """Check user bio if it's empty"""
    global botPoints, acctDesc
    bioPoints = 0
    if acctDesc == "":
        bioPoints = 3
    outputList.append(f"Check bio: {bioPoints} out of 3")
    botPoints += bioPoints


def bot_points(username: str) -> list:
    """take a string of username, process the bot points,
        return an output of list"""
    search(username)
    rtcounter()
    tweetChecker()
    checkPic()
    checkDate()
    checkRT()
    checkBio()
    tweetDateTime()
    outputList.append(f"Total bot points: {botPoints}")

    return outputList
