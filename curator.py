import re
from html.parser import HTMLParser


class DataCurator:
    
    def __init__(self, data):
        self.data = data
        self.htmlParser = HTMLParser()
    
    def basicCleanUp(self):
        curated_data = []
        for tweet in self.data:
            tweet = self.htmlParser.unescape(tweet)
            url_pattern = re.compile("http\S+")
            username_pattern = re.compile("@\S+")
            tweet = re.sub(url_pattern, "", tweet)
            tweet = re.sub(username_pattern, "", tweet)
            hash_tags = re.compile("#\S+")
            tweet = re.sub(hash_tags, "", tweet)
            curated_data.append(tweet)
        self.data = curated_data
        return self
                
    def removeRepeatedPunctuations(self):
        curated_data = []
        patterns = {"!" : "[!]+", "?" : "[?]+", "." : "[.]+", "," : "[,]+", "\"" : "[\"]+", \
         "'" : "[']+", "-" : "[-]+"}
        for text in self.data:
            for key, pattern in patterns.items():
                p = re.compile(pattern)
                text = re.sub(p, key, text)
            curated_data.append(text)
        self.data = curated_data
        return self
    
    def removePunctuationsAndReTweet(self):
        curated_data = []
        patterns = {".": "[.]", ",": "[,]", ":": "[:]", "-":"[\s][\-][\s]", "[": "[\[]", "]": "[\]]", "(": "[(]", ")": "[)]"\
        , "rt":"[\sR][T][\s]", "retweet":"[Rr][Ee][Tt][Ww][Ee][Ee][Tt]"}
        for text in self.data:
            for _, pattern in patterns.items():
                p = re.compile(pattern)
                text = re.sub(p, "", text)
            curated_data.append(text)
        self.data = curated_data
        return self
    
    def expandPunctuatedWords(self):
        curated_data = []
        patterns = {"can not":"[cC][Aa][Nn]['’][t]", "m not":"[Ii][n]['’][t]", " have":"['’][v][e]", " will":"['’][l][l]", " are":"['’][r][e]", \
            " am":"['’][m]", " not":"[n]['’][t]", "Let us":"[lL][Ee][Tt]['][Ss]"}
        for text in self.data:
            for key, pattern in patterns.items():
                p = re.compile(pattern)
                text = re.sub(p, key, text)
            curated_data.append(text)
        self.data = curated_data
        return self
    
    def expandShortHands(self):
        curated_data = []
        patterns = {" you ":"[\s][Uu][\s]", " your ":"[\s]*[Uu][Rr][\s]", " are ":"[^\S][Rr][\s]"}
        for text in self.data:            
            for key, pattern in patterns.items():
                p = re.compile(pattern)
                text = re.sub(p, key, text)
            curated_data.append(text)
        self.data = curated_data
        return self
    
    def build(self):
        return [text.strip() for text in self.data]
