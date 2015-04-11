from flask import Flask, render_template, send_from_directory,jsonify
import os
import sys
import urllib2
from flask.ext.cors import CORS, cross_origin
from os import listdir
from os.path import isfile, join
import json
from pprint import pprint
from textblob import TextBlob
import difflib
import csv

app = Flask(__name__,template_folder = "/home/abhishek/hotelReviews/src/web1/templates")
app.config['STATIC_FOLDER'] = "/home/abhishek/hotelReviews/src/web1/static"


@app.route("/hotels")
@cross_origin()
def hotels():
    onlyfiles = [ f[0:-5] for f in listdir("/home/abhishek/hotelReviews/data/json") if isfile(join("/home/abhishek/hotelReviews/data/json",f)) ]
    onlyfiles = map(int,onlyfiles)
    onlyfiles.sort()
    return jsonify({"hotels":onlyfiles})

@app.route("/hotelcor/<hid>")
@cross_origin()
def hotelcor(hid):
    with open('/home/abhishek/hotelReviews/data/insights/corbyhotels3000.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[1] == hid:
                return jsonify({"Service":row[2],"Business Service":row[3],"Cleanliness":row[4],"FrontDesk/Checkin":row[5],"value":row[6],"rooms":row[7],"Sleep Quality":row[8]})
    return jsonify({"Result":"NA"})
@app.route("/hotel/<hid>")
@cross_origin()
def hotel(hid):
    with open('/home/abhishek/hotelReviews/data/json/'+hid+'.json') as data_file:    
        data = json.load(data_file)
        nphrases = dict()
        for rev in data["Reviews"]:
            text = (rev["Content"])
            blob = TextBlob(text)
            for sentence in blob.sentences:
                tmpPhr = ""
                #print sentence.correct()
                #print sentence.noun_phrases
                for phrs in sentence.noun_phrases:
                    tmpPhr = phrs
                    if phrs in nphrases:
                        pCnt = nphrases[phrs][0] + 1
                        pPol = (nphrases[phrs][1] + sentence.sentiment.polarity)/pCnt
                        pSub = (nphrases[phrs][2] + sentence.sentiment.subjectivity)/pCnt
                        nphrases[phrs] = [pCnt,pPol,pSub]
                    else:
                        nphrases[phrs] = [1,sentence.sentiment.polarity, sentence.sentiment.subjectivity]
                if tmpPhr != "" and len(nphrases[tmpPhr]) != 4:
                    nphrases[tmpPhr].append([])
                    for value,key in sorted(set(sentence.tags)):
                        if key == "JJ":
                            nphrases[phrs][3].append([value])
                #print(sentence.sentiment.polarity)
        #pprint(nphrases)
        #print nphrases
        simList = []
        for keys in nphrases:
            nrby = difflib.get_close_matches(keys,[key for key in nphrases])
            #nrby.append(str(keys))
            simList.append(nrby)
        snd = dict()
        i = 0
        for data in simList:
            cntL = 0
            polL = 0
            subL = 0
            aLst = []
            #print data
            for items in data:
                #print nphrases[items][0]
                cntL += nphrases[items][0]
                polL += nphrases[items][1]
                subL += nphrases[items][2]
                if len((nphrases[items])) == 4:
                    aLst.extend(nphrases[items][3])
            snd[i]=[cntL,data,polL/cntL,subL/cntL,aLst]
            i += 1
    #print nphrases
    '''
    sortL = [int(k) for k in snd.keys()]
    sortL.sort(reverse=True)
    if len(sortL) >= 10:
        sortL = sortL[:10]
    sortL = map(str,sortL)
    
    return jsonify({k: snd[k] for k in sortL})
    '''
    return jsonify(snd)

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=5000)
