from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
tweets = []
#Variables that contains the user credentials to access Twitter API
access_token = "144826144-fRTezjoG4fnVCgxymQ5XvIEOhuoB8MNX6bBzPXjr"
access_token_secret = "XcsomBu7jln5lP1j4lb4j2pjkooUChNQRmTIRaJbF6HIx"
consumer_key = "qZlLHeRDuswGWNRiE7oyH1sks"
consumer_secret = "LxYquxhs75BB3hfi3LnCl4iEIp5elcL5qbw0Azv9iFyKDPiTBW"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):


    def on_data(self, data):
        #print data
        tweet = json.loads(data)

        if 'text' in tweet:
            createdAt = tweet['created_at']
            tweetId =  tweet['id']
            userId = tweet['user']['id']
            userName = tweet['user']['name']
            tweetText = tweet['text']

        else:
            createdAt = " "
            tweetId = " "
            userId = " "
            userName = " "
            tweetText = " "

        with open('tweets.csv', 'a') as f:

            from csv import writer
            csv = writer(f)
            row = [createdAt,tweetId,userId,userName,tweetText]
            values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
            csv.writerow(values)

        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.userstream(track=['@barackobama, @HillaryClinton, @jimwebbUSA, @realDonalTrump, @Berniesanders, @jebBush']) # or f.write('...\n')

