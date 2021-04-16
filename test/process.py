import subprocess
from subprocess import PIPE
import time

p = subprocess.Popen(['tcpdump','-w', 'cap.pcap'], stdout=subprocess.PIPE)

time.sleep(10)
p.kill()