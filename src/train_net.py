import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, concatenate, Dense, Flatten
import numpy as np
import matplotlib.pyplot as plt

import fingerprinting as fin


def reshape_data(feature):

    s_f = np.array_split(feature,100)
    sample_point=[]
    for i in range(100):
        sample_point.append(s_f[i][-1])

    return(sample_point)



if __name__ == "__main__":

    sites = open("../data/sites",'r')
    train_size = 30
    
    train_sizeset = list()
    train_featureset = list()
    train_labels = list()
    class_num = 0

    for site in sites:
        site_dataset = list()
        s = site.split()
        if s[0] == "#":
            continue

        for i in range(train_size):
            f = fin.get_feature(domain=s[1],data_name="../data/train/"+str(i)+".pcap",ip=s[2])
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

            train_sizeset.append(sample_size)
            train_featureset.append(sample_feature)
            train_labels.append(class_num)

        class_num+=1

    #print(type(train_sizeset[0][0]))
    

    ###build neural net###
    
    #class_num=3
    input1 = Input(shape=(100,))
    input2 = Input(shape=(100,))

    x1 = Flatten(input_shape=(100,))
    x1 = Dense(1,activation='linear')(input1)
    x1 = Model(inputs=input1, outputs=x1)
    x2 = Flatten(input_shape=(100,))
    x2 = Dense(1,activation='linear')(input2)
    x2 = Model(inputs=input2, outputs=x2)

    combined = concatenate([x1.output,x2.output])

    y = Dense(8,activation="relu")(combined)
    y = Dense(class_num,activation="softmax")(y)

    model = Model(inputs=[input1,input2],outputs=y)
    model.compile(optimizer='adam', 
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])
    model.summary()
    

    ts = np.array(train_sizeset)
    tf = np.array(train_featureset)
    tl = np.array(train_labels)
    ts.reshape(-1,100)
    tf.reshape(-1,100)
    tl.reshape(-1,len(ts))

    #print(ts)
    #print("ts : "+str(ts.shape)+" tf : "+str(tf.shape)+" tl : "+str(tl.shape))
    model.fit([ts,tf], tl, epochs=50)
    model.save("../data/trained_model")
    #model.summary()
        