#extract_loc.py
import pandas as pd 
import joblib
import time
import sys
import os 
import numpy as np
from tqdm import tqdm
import gmplot
ziptoloc_pd = pd.read_csv("../data/zipToLngLat.txt")


ziptoloc = {}
for val in ziptoloc_pd.values:
	ziptoloc[str(int(val[0]))] = val[1:]

collected_data = {}
if os.path.isfile('../out/collection.dump'):
	collected_data = joblib.load('../out/collection.dump')
tracks = {}
for key in collected_data:
	if "TrackDetail" not in collected_data[key]:
		continue
	zipcodes = []
	lnglat = []
	for step in collected_data[key]['TrackDetail']:
		zipcode = step['EventZIPCode']
		if zipcode is not None:
			zipcodes.append(zipcode)
			if zipcode in ziptoloc:
				lnglat.append(ziptoloc[zipcode])
			else:
				print "key %s with zipcode %s not found" % (key,zipcode)
				
	tracks[key] = np.array(lnglat)


gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
for key in tracks:
	if len(tracks[key]) >0:
		gmap.plot(tracks[key][:,0], tracks[key][:,1], 'cornflowerblue', edge_width=1)
gmap.draw("../out/mymap.html")





