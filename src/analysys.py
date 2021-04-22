import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import fingerprinting as fin
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
import fingerprinting as fin


def reshape_data(feature):
    
    s_f = np.array_split(feature,100)
    sample_point=[]
    for i in range(100):
        sample_point.append(s_f[i][-1])

    return(sample_point)


if __name__ == "__main__":

    model = keras.models.load_model("../data/trained_model")
    test_size = 10
    sites = open("../data/sites",'r')
    

    test_sizeset = list()
    test_featureset = list()
    test_labels = list()
    class_num = 0

    for site in sites:
        site_dataset = list()
        s = site.split()
        if s[0] == "#":
            continue

        for i in range(test_size):
            f = fin.get_feature(domain=s[1],data_name="../data/test/"+str(i)+".pcap",ip=s[2])
            print("domain : "+s[1]+" ("+str(i)+"th)"+" ::f.shape = "+str(len(f)))
            if len(f) < 100:
                print(str(i)+"th capture contain less than 100 of "+s[1])
                continue
            size = [0]
            feature = [0]
            for data in f:
                size.append(size[-1] + abs(data[1]))
                feature.append(size[-1] + data[1])
            sample_size = reshape_data(size)
            sample_feature = reshape_data(feature)

            test_sizeset.append(sample_size)
            test_featureset.append(sample_feature)
            test_labels.append(class_num)

        class_num+=1

    ts = np.array(test_sizeset)
    tf = np.array(test_featureset)
    tl = np.array(test_labels)
    ts.reshape(-1,100)
    tf.reshape(-1,100)
    tl.reshape(-1,len(ts))

    test_loss,test_acc = model.evaluate([ts,tf],tl,verbose=2)
    print('Test loss    :', test_loss)
    print('Test accuracy:', test_acc)
