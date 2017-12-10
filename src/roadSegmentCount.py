import collections
import numpy as np
import joblib

def road_segment_counter(collected_data):

    count = dict()

    for key in collected_data:
        if "TrackDetail" not in collected_data[key]:
            continue
        test = []
        for step in collected_data[key]['TrackDetail']:
            if (type(step) == collections.OrderedDict) & ("EventCity" in step):
                if step['EventCity'] == None:
                    continue
                test.append(step['EventCity'].strip('On its way to').split(' ')[0])
        if None in test:
            test = test.remove(None)
        test= np.unique(test)
        for i in range(len(test)-1):
            if test[i] in count.keys():
                count[test[i], test[i + 1]] += 1
            else:
                count[test[i], test[i + 1]] = 1

    return count
