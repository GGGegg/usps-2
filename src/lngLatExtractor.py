# given a list of tracking events, extract the longtitude and latitude for the events
# reference : https://gist.github.com/erichurst/7882666
# The code is depended on the source data format
import os

def searchLngLat(eventZipCode):
    '''
    Extract the zip code in orderedDict record, and use file named zipToLngLat.txt to transfer it to Lng and Lat
    '''
    localDes = os.path.join(os.path.dirname(__file__), "zipToLngLat.txt")

    if 'zipLngLatTable' not in globals():
        alist = [line.rstrip().split(',') for line in open(localDes)]
        zipLngLatTable = {}

        for line in alist:
            zipLngLatTable[line[0]] = line[1:]

    return zipLngLatTable.get(eventZipCode)

def extractLngLatTraj(trajList):
    '''
    extract the lng and lat from event zip code
    if there is no zip code in field, use the last zip code(means the package didn't move )
    '''
    trajTimeLngLat = []
    eventZipCode = "00000"

    for i in range(len(trajList)):

        if trajList[i]["EventZIPCode"] is not None:
            eventZipCode = trajList[i]["EventZIPCode"]
        lngLat = searchLngLat(eventZipCode)

        if lngLat is None:
            print "Didn't find correct lnglat for zip code: " + eventZipCode
        trajTimeLngLat.append([trajList[i]["EventDate"], trajList[i]["EventTime"], lngLat])

    return trajTimeLngLat