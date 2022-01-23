import subprocess
import time
import wakeonlan
import keyboard
import Sniff_IP
import sys
import socket




class Wake():

    def __init__(self):

        self.sniff = Sniff_IP.Sniff()
        self.IP_addres = "192.168.1.255"
        self.MAC_addres = "80:4a:14:5e:c6:3c"
        self.url = "https://www.youtube.com/watch?v=UceaB4D0jpo&list=RDMM&index=15"


    def wake_pc(self):

        print("Start")
        #self.sniff.sniff()
        #if(self.sniff.home == True):
        #wakeonlan.send_magic_packet(self.MAC_addres, ip_address=self.IP_addres)
        #else:
        #    sys.exit(4)

        """
        mac = sys.argv[2]
        data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(bytes(data.encode("utf-8")), (sys.argv[1], 9))
        """

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(b'\xff' * 6 + b'\x80\x4a\x14\x5e\xc6\x3c' * 16, ('192.168.1.255', 9))



        print("Finish")






if __name__ == "__main__":
    wake = Wake()
    wake.wake_pc()