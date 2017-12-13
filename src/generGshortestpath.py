from collections import defaultdict
from heapq import *
import networkx as nx
from cityCount import  city_counter
from roadSegmentCount import count_to_pandas
from roadSegmentCountView import extracttrips
from roadSegmentCountView import roadSegmentCount
from roadSegmentCount import get_distance
import pandas as pd
import numpy as np
import joblib
from evaluation import score
rawdata = joblib.load("../out/collection.dump")
trips = extracttrips(rawdata)
from sklearn.model_selection import train_test_split
train,test = train_test_split(trips,test_size=0.2,random_state=42)
data2=roadSegmentCount(train)
# data3=count_to_pandas(data2)
# data3.to_csv("../out/graph.csv",index=None)



def GenerG(data3):
    Gcity=nx.Graph()
    for i in data3.index:
        Gcity.add_edge( data3['departure'][i],data3['destination'][i],weight=data3['distance'][i])
    return Gcity

def GenerWeightedG(data3):
    Gcity=nx.Graph()
    for i in data3.index:
        Gcity.add_edge( data3['departure'][i],data3['destination'][i],weight=data3['weighted_distance'][i])
    return Gcity
def zipcodeToLL(zipcodes):
    ziptoloc_pd = pd.read_csv("../data/zipToLngLat.txt")
    ziptoloc = {}
    for val in ziptoloc_pd.values:
        ziptoloc[str(int(val[0]))] = val[1:]
    ll = []
    for i in zipcodes:
        if i in ziptoloc:
            ll.append(ziptoloc[i])
    return ll

def drawGraph(true,sp,wsp):
    import gmplot
    import numpy as np
    truth_path = np.array(zipcodeToLL(true))
    sp_path = np.array(zipcodeToLL(sp))
    wsp_path = np.array(zipcodeToLL(wsp))
    gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

    gmap.plot(truth_path[:,0], truth_path[:,1], 'cornflowerblue', edge_width=5)
    gmap.plot(sp_path[:,0], sp_path[:,1], 'green', edge_width=1)
    gmap.plot(wsp_path[:,0], wsp_path[:,1], 'red', edge_width=1)
    gmap.draw("../out/compare.html")

data3=pd.read_csv("../out/graph.csv" )
G=GenerG(data3)
WG = GenerWeightedG(data3)
result = []
weighted_result = []
log_result = []
valid_trips = []
sp = []
wsp = []
lsp = []
for i in range(len(test)):
    t = test[i]
    if len(t)>1:
        if  (G.has_node(t[0])) & (G.has_node(t[-1])):
            try:
                Shortest_path =nx.dijkstra_path(G,t[0],t[-1])
                sp.append(Shortest_path)
                # length =nx.dijkstra_path_length(G,t[0],t[-1])
                s = score(t,Shortest_path)
                result.append(s)
                shortest_path= nx.dijkstra_path(WG,t[0],t[-1])
                wsp.append(shortest_path)
                wScore = score(t, shortest_path)
                weighted_result.append(wScore)
                valid_trips.append(t)
            except :
                continue
# its for compare ground truth with our two approach
# it will generate one google map with three links
# try more and take 5 good result and 5 bad result for the report
# drawGraph(valid_trips[200],sp[200],wsp[200])
result = np.array(result)
weighted_result = np.array(weighted_result)
print(result.mean())
print(weighted_result.mean())
