
import json
from pprint import pprint
from scipy.stats.stats import pearsonr 


with open('/home/abhishek/hotelReviews/data/json/275856.json') as data_file:    
        data = json.load(data_file)
        param = "Rooms"
        #pprint(data)
        serviceList = []
        overallList = []
        for rev in data["Reviews"]:
            if param in rev["Ratings"] and int(rev["Ratings"][param]) != -1 and rev["Ratings"][param] != "-":
                try:
                    int(rev["Ratings"][param])
                    print int(rev["Ratings"][param])
                    serviceList.append(int(rev["Ratings"][param]))
                    overallList.append(int(rev["Ratings"]["Overall"]))
                except:
                    pass
        print overallList
        print serviceList
        print pearsonr(serviceList,overallList)
        #print serviceList
        #print overallList

