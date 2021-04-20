import pyshark
import os
import numpy as np



    
def get_feature(domain="www.osaka-u.ac.jp",data_name="../data/0.pcap",ip="133.1.138.1"):

    if not os.path.isfile(data_name):
        return(False)
    data = pyshark.FileCapture(data_name)
    packets = list()
    
    print("f1")
    
    for packet in data:
        
        if "TCP" in packet:
            if(packet.ip.src == ip):
                packets.append([packet.sniff_timestamp , int(packet.tcp.len) + int(packet.tcp.hdr_len)])
            elif(packet.ip.dst == ip):
                packets.append([packet.sniff_timestamp , -int(packet.tcp.hdr_len) - int(packet.tcp.len)])
        
    print("f2")
    spackets = sorted(packets , key=lambda s: s[0])
    
    #print(spackets.shape)
    '''
    feature = [0]
    for p in spackets:
        feature.append(feature[-1]+p[1])
    '''
    feature = np.array([spackets])
    

    return(spackets)
        