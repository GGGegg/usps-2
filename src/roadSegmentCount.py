import collections
import numpy as np
import joblib


def road_segment_counter(collected_data):

    count = dict()

    for key in collected_data:
        if "TrackDetail" not in collected_data[key]:
            continue
        test = []
        # for step in collected_data[key]['TrackDetail']:
        #     if (type(step) == collections.OrderedDict) & ("EventCity" in step):
        #         if step['EventCity'] == None:
        #             continue
        #         test.append(step['EventCity'].strip('On its way to').split(' ')[0])
        for step in collected_data[key]['TrackDetail']:
            if (type(step) == collections.OrderedDict) & ("EventZIPCode" in step):
                if step['EventZIPCode'] == None:
                    continue
                test.append(step['EventZIPCode'])
        if None in test:
            test = test.remove(None)
        test= np.unique(test)
        for i in range(len(test)-1):
            if test[i] in count.keys():
                count[test[i], test[i + 1]] += 1
            else:
                count[test[i], test[i + 1]] = 1

    return count
def count_to_pandas(count):
    pf = pd.DataFrame()
    pf[0]= count.keys()
    pf[1]= count.values()
    departure = []
    destination = []
    for i in range(pf.shape[0]):
        departure.append(pf[0][i][0])
        destination.append(pf[0][i][1])

    pf['departure']=pd.DataFrame(departure)
    pf['destination'] = pd.DataFrame(destination)

    for i in range(pf.shape[0]):
        pf['distance'][i] = get_distance(pf['departure'][i],pf['destination'][i])

    distance  = []
    for i in range(pf.shape[0]):
        distance.append(get_distance(pf['departure'][i],pf['destination'][i]))
    pf['distance'] = pd.DataFrame(distance)
    pf = pf[pf['distance']!=0]
    return pf

def get_distance(departure,destination):
    from math import radians,cos,sin,asin,sqrt
    ziptoloc_pd = pd.read_csv("../data/zipToLngLat.txt")
    ziptoloc = {}
    for val in ziptoloc_pd.values:
        ziptoloc[str(int(val[0]))] = val[1:]
    if (departure in ziptoloc.keys()) and (destination in ziptoloc.keys()):
        [lon1,lat1] = ziptoloc[departure]
        [lon2,lat2] = ziptoloc[destination]
        lon1,lat1,lon2,lat2 = map(radians,[lon1,lat1,lon2,lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371
    else:
        c=0
        r = 6371
    return c * r * 1000
