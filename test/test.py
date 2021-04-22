import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pyshark
import math
import time
import sys
from subprocess import PIPE
import subprocess

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


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

    option = Options()                          # オプションを用意
    option.add_argument('--headless')  

    driver = webdriver.Chrome(options = option)
    p = subprocess.Popen(['tcpdump','-w', '../data/test.pcap'], stdout=subprocess.PIPE)

    driver.get("https://www.osaka-u.ac.jp/ja")

    p.kill()
    driver.delete_all_cookies()
    driver.quit()
