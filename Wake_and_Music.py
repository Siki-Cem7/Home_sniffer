import subprocess
import time
import sys
import wakeonlan
import keyboard
import Sniff_IP




class Wake():

    def __init__(self):

        self.sniff = Sniff_IP.Sniff()
        self.IP_addres = "192.168.1.255"
        self.MAC_addres = "80:4a:14:5e:c6:3c"
        self.url = "https://www.youtube.com/watch?v=UceaB4D0jpo&list=RDMM&index=15"


    def wake_pc(self):

        print("Start")
        self.sniff.sniff()
        if(self.sniff.home == True):
            wakeonlan.send_magic_packet(self.MAC_addres, ip_address=self.IP_addres)
        else:
            sys.exit(4)






if __name__ == "__main__":
    wake = Wake()
    wake.wake_pc()