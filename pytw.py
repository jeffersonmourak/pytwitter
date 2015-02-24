from tweepy import OAuthHandler
from SimpleCV import Image, Camera
import easygui, sys, tweepy
import takepic


ckey ='CONSUMER KEY'
#Consumer Key(API Key)
csecret ='CONSUMER SECRET'
#Consumer Secret(API Secret)
atoken = 'ACESS TOKEN'
#Acess Token
asecret = 'ACESS TOKEN SECRET'
#Acess Token Secret
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()

choice = easygui.buttonbox("Entre no seu Twitter","Twitter", ["Enter","Exit","Take a Picture"],"twitter.png")

if choice =="Enter":    
    for tweet in public_tweets:
        print (tweet.text)
        
elif choice =="Take a Picture":
    takepic.take_pic()
    
elif choice =="Exit":
    sys.exit()
