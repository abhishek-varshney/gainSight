import json
from pprint import pprint
from textblob import TextBlob
import difflib


with open('/home/abhishek/hotelReviews/data/json/275856.json') as data_file:    
        data = json.load(data_file)
        nphrases = dict()
        for rev in data["Reviews"]:
            text = (rev["Content"])
            blob = TextBlob(text)
            for sentence in blob.sentences:
                #print sentence.correct()
                #print sentence.noun_phrases
                for phrs in sentence.noun_phrases:
                    if phrs in nphrases:
                        pCnt = nphrases[phrs][0] + 1
                        pPol = (nphrases[phrs][1] + sentence.sentiment.polarity)/pCnt
                        pSub = (nphrases[phrs][2] + sentence.sentiment.subjectivity)/pCnt
                        nphrases[phrs] = [pCnt,pPol,pSub]
                    else:
                        nphrases[phrs] = [1,sentence.sentiment.polarity, sentence.sentiment.subjectivity]
                #print(sentence.sentiment.polarity)
        #pprint(nphrases)
        for keys in nphrases:
            print difflib.get_close_matches(keys,[key for key in nphrases])

