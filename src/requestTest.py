from XMLGetter import sendRequest
from GenCheckDigit import gen_check_digit


tracking_dict = sendRequest("9405510200883557547244")
if 'TrackDetail' in tracking_dict.keys():
    print "success!"