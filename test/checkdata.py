import pyshark

for i in range(10):
    data = pyshark.FileCapture("../data/test_data/"+str(i)+".pcap")
    num=0

    for packet in data:

        if packet.eth.type == 2048:
            if(packet.ip.src == "104.244.42.193" or packet.ip.dst == "104.244.42.193"):
                num += 1

    print(num)