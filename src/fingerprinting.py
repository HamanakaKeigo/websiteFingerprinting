import pyshark
import os



    
def get_feature(data_name="../data/test.cap",ip="133.1.138.1"):

    #print(data_name)
    #print(ip)
    if not os.path.isfile(data_name):
        return(False)
    data = pyshark.FileCapture(data_name)
    packets = list()
    feature = [0]

    
    for packet in data:
        
        if "IP" in packet:
            if(packet.ip.src == ip):
                packets.append([packet.sniff_timestamp , int(packet.tcp.len) + int(packet.tcp.hdr_len)])
            elif(packet.ip.dst == ip):
                packets.append([packet.sniff_timestamp , -int(packet.tcp.hdr_len) - int(packet.tcp.len)])
        
    
    spackets = sorted(packets , key=lambda s: s[0])
    
    for p in spackets:
        feature.append(feature[-1]+p[1])
    

    return(feature)
        