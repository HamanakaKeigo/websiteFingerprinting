import matplotlib.pyplot as plt
import sys
import fingerprinting as fin
import numpy as np
import os

if __name__ == "__main__":
    Train_dataset = {}

    with open("../data/sites",'r') as f:
        sites = f.readlines()
        for site in sites:
            s = site.split()
            if s[0] == "#":
                continue

            
            Train_dataset[s[0]] = list()
            packets_set = list()

            test_epoch=10
            for i in range(test_epoch):
                if not os.path.isfile("../data/train/"+str(i)+".pcap"):
                    break
                packets_data = fin.get_feature(domain=s[1],data_name="../data/train/"+str(i)+".pcap",ip=s[2])

                #packets_set.append(packets_data)
                Train_dataset[s[0]].append(packets_data)
            #print(len(packets_set[0]))

            graph = plt.figure()
            ax = graph.add_subplot(111)

            s = site.split()
            for i in range(test_epoch):
                feature = [0]
                for j in range(len(Train_dataset[s[0]][i])):
                    feature.append(feature[-1]+int(Train_dataset[s[0]][i][j][1]))
                x = list(range(len(feature)))
                ax.plot(x,feature)
            #plt.show()

            plt.savefig("../data/train/"+str(s[1])+".png")

            
        
        '''
        s_f = np.array_split(feature,100)
        s_x = np.array_split(x,100)
        sample_point = []
        sample_x=[]

        for j in range(100):
            sample_point.append(s_f[i][-1])
            sample_x.append(s_x[i][-1])

        ax.plot(sample_x,sample_point,marker="*")
        #ax.plot(sample_x,sample_point)

        plt.savefig("../data/"+s[1]+"/data"+str(num)+".png")
        '''

    