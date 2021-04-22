import time
import subprocess
import sys
from subprocess import PIPE

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":

    args = sys.argv 
    if len(args) < 3 or (args[2] != ("test" or "train" or "valid")):
        print("input like below")
        print("python .py [epoch] [test or train or valid]")
    #python .py [epoch] [test or train or valid] 
    test_epoch = int(args[1])
    option = Options()                          # オプションを用意
    option.add_argument('--headless')  

    with open("../data/sites",'r') as f:
        sites = f.readlines()
        
        
        for i in range(test_epoch):
            print(str(i) + " times")
            driver = webdriver.Chrome(options = option)
            p = subprocess.Popen(['tcpdump','-w', '../data/'+args[2]+'/'+str(i)+'.pcap'], stdout=subprocess.PIPE)

            for site in sites:
                s = site.split()
                if s[0] == "#":
                    continue
                driver.get(s[0])
                #time.sleep(0.2)

            p.kill()
            driver.delete_all_cookies()
            driver.quit()
        
        