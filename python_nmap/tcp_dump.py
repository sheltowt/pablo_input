
#  PyShark
# pycap

# https://pycap.readthedocs.io/en/latest/
# http://www.secdev.org/projects/scapy/


#use python with tcp dump to grab packets

#!/usr/bin/python
from scapy.all import *
def print_summary(pkt):
    print pkt


sniff(filter="ip",prn=print_summary)
# or it possible to filter with filter parameter...!


#save packets to mongodb





#pull aggregation data from stored packets