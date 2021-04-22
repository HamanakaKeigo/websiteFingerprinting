import pyshark
import os
import numpy as np



    
def get_feature(domain="www.osaka-u.ac.jp",data_name="../data/0.pcap",ip="133.1.138.1"):

    if not os.path.isfile(data_name):
        print("file not found in")
        return(False)
    data = pyshark.FileCapture(data_name)
    packets = list()
    
    for packet in data:
        
        if "TCP" in packet:
            if(packet.ip.src == ip):
                packets.append([packet.sniff_timestamp , int(packet.tcp.len) + int(packet.tcp.hdr_len)])
            elif(packet.ip.dst == ip):
                packets.append([packet.sniff_timestamp , -int(packet.tcp.hdr_len) - int(packet.tcp.len)])
        
    spackets = sorted(packets , key=lambda s: s[0])
    
    #print(spackets.shape)
    '''
    feature = [0]
    for p in spackets:
        feature.append(feature[-1]+p[1])
    '''
    feature = np.array([spackets])
    

    return(spackets)
        
def getall_feature(target="train",epoch = 1):

    site_data = list()
    packets_dataset = {}
    with open("../data/sites",'r') as f:
        sites = f.readlines()
        for site in sites:
            s = site.split()
            if s[0] == "#":
                continue
            site_data.append(s)
            packets_dataset[s[0]] = list()

    
    for i in range(epoch):
        data = pyshark.FileCapture("../data/"+target+"/"+str(i)+".pcap")
        epoch_set = list()
        for packet in data:
            if "TCP" in packet:
                for i in range(len(site_data)):
                    if(packet.ip.src == site_data[i][2]):
                        packets_dataset[site_data[i][0]].append([packet.sniff_timestamp , int(packet.tcp.len) + int(packet.tcp.hdr_len)])
                        break
                    elif(packet.ip.dst == site_data[i][2]):
                        packets_dataset[site_data[i][0]].append([packet.sniff_timestamp , -int(packet.tcp.hdr_len) - int(packet.tcp.len)])
                        break

        for i in range(len(site_data)):
            for j in range(epoch):
                packets_dataset[site_data[i][0]][j] = sorted(packets_dataset[site_data[i][0]][j] , key=lambda s: s[0])


        