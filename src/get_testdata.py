import time
import subprocess
from subprocess import PIPE

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":

    test_epoch = 10

    with open("../data/sites",'r') as f:
        sites = f.readlines()
        driver = webdriver.Safari()

        for i in range(test_epoch):
            p = subprocess.Popen(['tcpdump','-w', '../data/test_data/'+str(i)+'.pcap'], stdout=subprocess.PIPE)

            for site in sites:
                s = site.split()
                driver.get(s[0])
                #time.sleep(3)

            p.kill()
            driver.delete_all_cookies()
        driver.quit()
        