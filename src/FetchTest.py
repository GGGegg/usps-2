from FetchWriteContinuData import fetchContinuData
import config as cfg
import os
# The purpose is to fetch data from USPS API
# The first para is CIA (channel application id) + Service Type Code + Mailer ID
# The second and third para are the range of serial number
# The fourth para is the file location one want to save the result

file_des = os.path.join(os.path.dirname(__file__) , "origin_8000000_8999999.pkl")

fetchContinuData(cfg.tracking_prefix, 8000000, 8999999 , file_des)
