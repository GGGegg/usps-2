import collections
import numpy as np
import joblib

def city_counter(collected_data):
# collected_data = {}
# if os.path.isfile('../out/collection.dump'):
#     collected_data = joblib.load('../out/collection.dump')
    city_count = dict()

    for key in collected_data:
        if "TrackDetail" not in collected_data[key]:
            continue
        test = []
        for step in collected_data[key]['TrackDetail']:
            if (type(step) == collections.OrderedDict) & ("EventCity" in step):
                if step['EventCity'] == None:
                    continue
                # test.append(step['EventCity'].strip('On its way to').split(' ')[0])
                test.append(step['EventCity'].strip('On its way to'))
        if None in test:
            test = test.remove(None)
        test= np.unique(test)

        for i in range(len(test)):
            if test[i] in city_count.keys():
                city_count[test[i]] += 1
            else:
                city_count[test[i]] = 1
    return city_count
