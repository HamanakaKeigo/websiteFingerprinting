import pyshark

for i in range(10):
    data = pyshark.FileCapture("../data/test_data/"+str(i)+".pcap")
    print(data[0])