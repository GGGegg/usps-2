import joblib
rawdata = joblib.load("../out/collection.dump")

import collections
import numpy as np
# import matplotlib.pyplot as plt


def extracttrips(rawdata, zipsize=None, by='EventZIPCode'):
    trips = []
    for key in rawdata:
        if "TrackDetail" not in rawdata[key]:
            continue
        zipcodes = []
        for step in rawdata[key]['TrackDetail']:

            if type(step) == collections.OrderedDict:

                zipcode = step[by]
                if zipcode is not None:
                    if zipsize is None:
                        zipcodes.append(str(zipcode))
                    else:
                        zipcodes.append(str(zipcode)[:zipsize])
        uniquetrip = np.unique(zipcodes)
        trips.append(uniquetrip)
    return trips
def roadSegmentCount(trips):
    trips = extracttrips(rawdata)
    # tripslength = [len(x) for x in trips]
    import pandas as pd
    links = []
    for val in trips:
        links.extend([(val[i],val[i+1]) for i in range(len(val)-1)])
    linksrate = pd.Series(links).value_counts()
    linksrate = dict(linksrate)
    # print '# link with more than 1 occur:', (linksrate>1).sum()
    return linksrate