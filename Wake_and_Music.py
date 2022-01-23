import subprocess
import time
import wakeonlan
import keyboard
import Sniff_IP
import socket
import sys



class Wake():

    def __init__(self):

        self.sniff = Sniff_IP.Sniff()
        self.IP_addres = "192.168.1.255"
        self.MAC_addres = "80:4a:14:5e:c6:3c"
        self.MAC_addres_book = "1c:91:80:d5:a0:55"
        self.url = "https://www.youtube.com/watch?v=UceaB4D0jpo&list=RDMM&index=15"


    def wake_pc(self):

        print("Start")
        #self.sniff.sniff()
        #if(self.sniff.home == True):

        """
        mac = sys.argv[2]
        data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(bytes(data.encode("utf-8")), (sys.argv[1], 9))
        """

        time.sleep(70)
        keyboard.press_and_release("enter")



        #else:
            #sys.exit(4)






if __name__ == "__main__":
    wake = Wake()
    wake.wake_pc()