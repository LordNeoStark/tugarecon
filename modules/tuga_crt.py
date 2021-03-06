# TugaRecon - crt module, write by LordNeoStark
# TugaRecon, tribute to Portuguese explorers reminding glorious past of this country
# Bug Bounty Recon, search for subdomains and save in to a file
# Coded By LordNeoStark | https://twitter.com/LordNeoStark | https://github.com/LordNeoStark
# import modules

import time
import requests

from functions import G, W
from modules import tuga_useragents
from functions import write_file
from functions import DeleteDuplicate

class CRT:

    def __init__(self, target, output):

        self.target = target
        self.output = output
        self.module_name = "SSL Certificates"
        self.engine = "crt"

        print(G + f"SSL Certificates: Enumerating subdomains now for {target} \n" + W)

        self.response = self.engine_url()
        self.enumerate(self.response, output, target)
        if self.output is not None and self.subdomainscount != 0:
            DeleteDuplicate(self.engine + '_' + self.output, target)
        else:
            pass

    def engine_url(self):
        try:
            url = f"https://crt.sh/?q={self.target}&output=json"
            response = requests.get(url, headers=tuga_useragents.useragent())
            return response
        except requests.exceptions.Timeout:
            pass


    def enumerate(self, response, output, target):
        subdomains = set()
        self.subdomainscount = 0
        start_time = time.time()

        try:
            while self.subdomainscount < 10000:
                subdomains = response.json()[self.subdomainscount]["name_value"]

                if not subdomains:
                    print(f"[x] Oops! No data found for {self.target} using  SSL Certificates.")
                else:
                    self.subdomainscount = self.subdomainscount + 1
                    if "@" in subdomains:  # filter for emails
                        pass
                    else:
                        print(f"[*] {subdomains}")

                        if self.output is not None:
                            write_file(subdomains, self.engine + '_' + self.output, target)
            if self.output:
                print(f"\nSaving result... {self.engine + '_'+ self.output}")
        except IndexError:
            pass

        #if not subdomains:
            #print(f"[x] Oops! No data found for {self.target} using  SSL Certificates.")
        #else:
            print(
                G + f"\n[**] TugaRecon is complete.  SSL Certificates: {self.subdomainscount} subdomains have been found in %s seconds" % (
                        time.time() - start_time) + W)
