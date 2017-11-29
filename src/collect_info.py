from GenRandomTra import gen_valid_tra
from XMLGetter import sendRequest
import joblib
import time
import sys
import os 
from tqdm import tqdm
num_try = int(sys.argv[1])

collected_data = {}
if os.path.isfile('../out/collection.dump'):
	collected_data = joblib.load('../out/collection.dump')
try:
	for i in tqdm(range(num_try)):
		track_number = gen_valid_tra()
		if track_number not in collected_data:
			res = sendRequest(track_number)	
			collected_data[track_number] = res
			
except (Exception),x:
	print x
finally:
	joblib.dump(collected_data,filename="../out/collection.dump")




