# This script parses the json dumped from q1.py (Streaming Data)
import json


def readFile(filename):
    """ This function parse file line by line into list of json objects
    """
    lines = []
    f = open(filename, mode='r', buffering=1024)
    for json_data in f:
        # json_data = json_data.replace('"', '\\"')
        lines.append(json.loads(json_data))
    f.close()
    return lines

def findKeys(datas):
    keys = set()
    for data in datas:
        if isinstance(data, dict):
            for key,_ in data.items():
                keys.add(key)
    return  keys
        
def findTweets(datas):
    tweets = []
    for data in datas:
        if isinstance(data, dict) and 'text' in data.keys():
            tweets.append(data['text'])
        else:
            print('String Data :', data)
    return tweets

def getTweets():
    json_datas = readFile('ipl2017_data_stream.json')
    return findTweets(json_datas)






