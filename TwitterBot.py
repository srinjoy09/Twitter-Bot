import tweepy
from tkinter import *
from tkinter import messagebox

access_token = '1440625789-fj09Hk0zjatMv8W3eFEC04i265s4D5GvtBDdtBt'
access_token_secret = '4TRmSLcXy0zEIuHAOytmzFkL1evmTJPs35Lx0CY9eTaDx'
consumer_key = 'UG51ck5uDIda51UX8VdXX5sG9'
consumer_secret = 's9YNuQg5ZAVVwyktgR6mEgPzZIvYI8P7V3HJ6tyiQfjxacYXPt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()

root = Tk()

label0 = Label(root, background='black', foreground='white', width=100, text='TWITTER BOT')

label1 = Label( root, background='black', foreground='white', anchor=CENTER, text="Search")
E1 = Entry(root, fg='blue', bd =5)

label2 = Label( root, background='black', foreground='white', anchor=CENTER, text="Number of Tweets")
E2 = Entry(root, fg='blue', bd =5)

label3 = Label( root, background='black', foreground='white', anchor=CENTER, text="Response")
E3 = Entry(root, fg='blue', bd =5)

label4 = Label( root, background='black', foreground='white', anchor=CENTER, text="Reply?")
E4 = Entry(root, fg='blue', bd =5)

label5 = Label( root, background='black', foreground='white', anchor=CENTER, text="Retweet?")
E5 = Entry(root, fg='blue', bd =5)

label6 = Label( root, background='black', foreground='white', anchor=CENTER, text="Favorite?")
E6 = Entry(root, fg='blue', bd =5)

label7 = Label( root, background='black', foreground='white', anchor=CENTER, text="Follow?")
E7 = Entry(root, fg='blue', bd =5)


def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()


def getE4():
    return E4.get()

def getE5():
    return E5.get()

def getE6():
    return E6.get()

def getE7():
    return E7.get()

def name_print():	
	messagebox.showinfo('NAME',user.name)

def d_tweet():
	search = getE1()+ " -filter:retweets"
	n=getE2()
	n=int(n)
	for tweet in tweepy.Cursor(api.search, search).items(n):
		print(f"{tweet.user.name} said: {tweet.text}")

def mainFunction():
    getE1()
    search = getE1()
    
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    
    getE3()
    phrase = getE3()
    
    getE4()
    reply = getE4()
    
    getE5()
    retweet = getE5()
    
    getE6()
    favorite = getE6()

    getE7()
    follow = getE7()

    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' + str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print ("Replied with " + phrase)
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break


    if retweet == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Retweet
                tweet.retweet()
                print('Retweeted the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if favorite == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Favorite
                tweet.favorite()
                print('Favorited the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if follow == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Follow
                tweet.user.follow()
                print('Followed the user')
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break       
            
submit = Button(root, width=25, background='black', foreground='white', text ="Submit", command = mainFunction)
p_name = Button(root, width=25, background='black', foreground='white', text ="Display Name", command = name_print)
tweet_d = Button(root, width=25, background='black', foreground='white', text ="Display Tweets", command = d_tweet)
label0.pack()
label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
submit.pack(side =BOTTOM)
p_name.pack(side=BOTTOM)
tweet_d.pack(side=BOTTOM)
root.mainloop()