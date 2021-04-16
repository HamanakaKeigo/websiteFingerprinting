import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pyshark
import math


def reshape_data(feature):
    x = list(range(len(feature)))

    s_f = np.array_split(feature,100)
    s_x = np.array_split(x,100)

    sample_point=[]
    sample_x=[]
    for i in range(100):
        sample_point.append(s_f[i][-1])
        sample_x.append(s_x[i][-1])

    return(sample_point,sample_x)



if __name__ == "__main__":

    #print(sample_point)
    data = pyshark.FileCapture("../data/test.cap")

    #print(dir(data[0].tcp))
    #print(data[0].sniff_timestamp)

    sample_point = []
    sample_x = []
    packet_size = list()
    feature = [0]

    #print("type=" + data[1].sniff_timestamp)

    
    time=data[0].sniff_timestamp 
    for packet in data:
        #print(float(packet.sniff_timestamp) - float(time))
        if "TCP" in packet:
            if packet.ip.src == "133.1.138.1":
                packet_size.append([packet.sniff_timestamp , int(packet.tcp.len) + int(packet.tcp.hdr_len)])
            elif packet.ip.dst == "133.1.138.1":
                packet_size.append([packet.sniff_timestamp , -int(packet.tcp.len) - int(packet.tcp.hdr_len)])
        time = packet.sniff_timestamp
    spackets = sorted(packet_size , key=lambda s: s[0])
    graph = plt.figure()
    ax = graph.add_subplot(111)
    
    
    for p in spackets:
        feature.append(feature[-1]+p[1])
    x = list(range(len(feature)))
    
    ax.plot(x,feature)
    plt.show()
    #ax.plot(sample_x,sample_point,marker="*")
    '''
    train_setX1 = np.arange(100)
    train_setX2 = np.arange(100)
    train_setX2 = np.sqrt(train_setX2)
    train_setX = np.stack([train_setX1,train_setX2])

    train_labels = np.array([1,2])
    print(train_setX.shape)
    print(train_labels.shape)
    ###build neural net###

    model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=(100,)),
        keras.layers.Dense(8, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', 
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

    model.fit(train_setX, train_labels, epochs=5)
    #model.summary()
    '''