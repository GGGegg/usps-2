# read pickle file which saved the result
# The format of results in pickle file will be a list of orderedDict
# One should modify the file_des to correctly run the code
import pickle
import os

file_des = os.path.join(os.path.dirname(__file__) , "origin_0000000_0096669.pkl")

print os.path.dirname(__file__)

tracking_dict_list = []

with open(file_des, "rb") as f:

    while 1:
        try:
            tracking_dict_list.append(pickle.load(f))
        except EOFError:
            break

print len(tracking_dict_list), tracking_dict_list[100]