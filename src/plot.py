import matplotlib.pyplot as plt
import sys
import fingerprinting as fin
import numpy as np
import os

if __name__ == "__main__":
    args = sys.argv
    sites = open("../data/sites",'r')

    for site in sites:
        s = site.split()
        num=1
        while os.path.isfile("../data/"+s[0]+"/data"+str(num)+".cap"):

            feature = fin.get_feature(data_name="../data/"+s[0]+"/data"+str(num)+".cap",ip=s[1])

            x = list(range(len(feature)))
            s_f = np.array_split(feature,100)
            s_x = np.array_split(x,100)
            sample_point = []
            sample_x=[]

            
            for i in range(100):
                sample_point.append(s_f[i][-1])
                sample_x.append(s_x[i][-1])

            #print(feature)
            
            graph = plt.figure()
            ax = graph.add_subplot(111)

            ax.plot(x,feature)

            ax.plot(sample_x,sample_point,marker="*")
            #ax.plot(sample_x,sample_point)

            plt.savefig("../data/"+s[0]+"/data"+str(num)+".png")
            plt.show()
            num+=1