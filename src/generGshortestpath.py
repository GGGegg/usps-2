from collections import defaultdict
from heapq import *
import networkx as nx
from cityCount import  city_counter
from roadSegmentCount import count_to_pandas
from roadSegmentCountView import extracttrips
from roadSegmentCountView import roadSegmentCount
import pickle
import pprint
import joblib
from evaluation import score
rawdata = joblib.load("../out/collection.dump")
# pkl_file = open("D:\\17fall\\DS504\\project2 USPS\\collection.dump","rb")
# ori_data = pickle.load(pkl_file)
# pprint.pprint(ori_data)
trips = extracttrips(rawdata)
data1=city_counter(rawdata)
data2=roadSegmentCount(trips)
data3=count_to_pandas(data2)


def GenerG(data3):
    Gcity=nx.Graph()
    for i in data3.index:
        Gcity.add_edge( data3['departure'][i],data3['destination'][i],weight=data3['distance'][i])
    return Gcity

G=GenerG(data3)

Shortest_path =nx.dijkstra_path(G,0,4)
length =nx.dijkstra_path_length(G,0,4)
score = score(['25301', '25302', '25314', '91405'],Shortest_path)
print('length = ',length)
print('The shortest path is ',Shortest_path)