import tweets as twt
from curator import DataCurator

tweets = twt.getTweets()

dc = DataCurator(tweets)
clean_data = dc.basicCleanUp().removeRepeatedPunctuations().removePunctuationsAndReTweet()\
            .expandPunctuatedWords().expandShortHands().build()

f = open('cleaned_data.txt', 'w', 1024)            
for tweet in clean_data:
    f.write("%s\n" % (tweet))
f.close()
