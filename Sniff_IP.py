import subprocess
import sys
import time



class Sniff():

    def __init__(self):

        self.IP_addres = "192.168.1.116"
        self.stdout = None
        self.stderr = None
        self.home = False


    def sniff(self):

        while True:
            print("In while True")
            self.resp = subprocess.Popen([f"ping -c 20 {self.IP_addres}"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.stdout, self.stderr = self.resp.communicate()
            self.stdout = self.stdout.decode("utf-8")


            if("Request timeout for icmp_seq" in self.stdout and not "icmp_seq=" in self.stdout and not "ttl=" in self.stdout):
                print("Nothing found")
                time.sleep(20)

            elif("ttl=" in self.stdout and "time=" in self.stdout and "bytes from" in self.stdout):
                print("Siki is arrived at home")
                self.home = True
                break
            else:
                time.sleep(20)
                print("Nothing recv")
