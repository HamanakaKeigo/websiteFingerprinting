import matplotlib.pyplot as plt
import sys
import fingerprinting as fin
import numpy as np
import os

if __name__ == "__main__":
    test_epoch = 10

    with open("../data/sites",'r') as f:
        sites = f.readlines()
        for site in sites:
            s = site.split()
            Train_dataset = {s[0]:numpy.empty(test_epoch,)}


        for i in rage(test_eopch):
        #while os.path.isfile("../data/test_data/"+str(num)+".pcap"):
            for site in sites:
                numpy.empty()
                s = site.split()
                feature = fin.get_feature(domain=s[1],data_name="../data/test_data/"+str(i)+".pcap",ip=s[1])

                Train_dataset[s[0]].append(feature)
                

        graph = plt.figure()
        ax = graph.add_subplot(111)

        for site in sites:
            s = site.split()
            for i in range(test_epoch):
                x = list(range(len(Train_dataset[s[0]])))
                ax.plot(x,Train_dataset[s[0]])
        '''
        s_f = np.array_split(feature,100)
        s_x = np.array_split(x,100)
        sample_point = []
        sample_x=[]

        for j in range(100):
            sample_point.append(s_f[i][-1])
            sample_x.append(s_x[i][-1])
        '''

        

        

        ax.plot(sample_x,sample_point,marker="*")
        #ax.plot(sample_x,sample_point)

        plt.savefig("../data/"+s[1]+"/data"+str(num)+".png")
        plt.show()