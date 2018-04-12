from nltk.corpus import sentiwordnet as swn 
from nltk import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords 
import numpy as np


def decision(val):
    if val == 0:
        return 'positive'
    elif val == 1:
        return 'negetive'
    else:
        return 'neutral'


def readFile(filename):
    """ This function parse file line by line into list of json objects
    """
    lines = []
    f = open(filename, mode='r', buffering=1024)
    for text in f:
        lines.append(text)
    f.close()
    return lines


stop = stopwords.words('english')
tag_map = {'NN':'n', 'VB':'v', 'JJ':'a', 'RB':'r'}
nltk_tags = tag_map.keys()
# https://www.daniweb.com/programming/threads/509027/sentiment-analysis-using-sentiwordnet-in-python
data = readFile('cleaned_data.txt')
scores = np.zeros(len(data));indx = -1
for tweet in data:
    indx += 1
    tokens = word_tokenize(tweet)  
    score = np.array([0., 0., 0.])
    for word, tag in pos_tag(tokens):
        word = word.lower()
        key = tag[:2];sen_set = None
        if word not in stop and key in nltk_tags:
            polarity_list = list(swn.senti_synsets(word, tag_map[key]))
            if len(polarity_list) > 0:
                sen_set = polarity_list[0]
        if sen_set:
            score += np.array([sen_set.pos_score(), sen_set.neg_score(), sen_set.obj_score()]) 
    max_indx = np.argmax(score)
    if score[max_indx] == 0:
        scores[indx] = 2
    else:
        scores[indx] = max_indx

vfunc = np.vectorize(decision)
results = vfunc(scores)
for indx in range(len(scores)):
    print(data[indx], '---' , results[indx])
