import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

import fingerprinting as fin


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

    sites = open("../data/sites",'r')
    mnist = tf.keras.datasets.mnist
    (train_data, train_teacher_labels), (test_data, test_teacher_labels) = mnist.load_data()
    train_data, test_data = train_data / 255.0, test_data / 255.0

    print(train_data.shape)
    print(train_teacher_labels.shape)

    for site in sites:
        s = site.split()
        feature = fin.get_feature(data_name=s[0],ip=s[1])
        sample_point,sample_x = reshape_data(feature)

        #print(sample_point)

        train_setX1 = np.arange(100)
        train_setX2 = np.arange(100)
        train_setX2 = np.sqrt(train_setX2)
        train_setX = np.stack([train_setX1,train_setX2])

        train_labels = np.array([1,2])
        print(train_setX.shape)
        print(train_labels.shape)
        ###build neural net###

        model = keras.models.Sequential([
            keras.layers.Flatten(input_shape=(10,)),
            keras.layers.Dense(8, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])

        model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

        model.fit(train_setX, train_labels, epochs=5)
        #model.summary()
        