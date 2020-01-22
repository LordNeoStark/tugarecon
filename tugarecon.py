#!/usr/bin/python3

# TugaRecon, tribute to Portuguese explorers reminding glorious past of this country
# Bug Bounty Recon, search for subdomains and save in to a file

# import go here :)

import argparse  # parse arguments
import sys

import urllib3

from modules import crtsearch


# Banner, Tuga or portuguese, is the same ;)
def banner():
    print("        \n"
          "             ______                  ____                      \n"
          "            /_  __/_  ______ _____ _/ __ \___  _________  ____ \n"
          "             / / / / / / __ `/ __ `/ /_/ / _ \/ ___/ __ \/ __ \                \n"
          "            / / / /_/ / /_/ / /_/ / _, _/  __/ /__/ /_/ / / / /               \n"
          "           /_/  \__,_/\__, /\__,_/_/ |_|\___/\___/\____/_/ /_/  V: 0.1b               \n"
          "                     /____/                                    \n"
          "\n"
          "                        # Coded By LordNeoStark #\n"
          "    ")


# parser error
def parser_error(errmsg):
    print("Usage: python3 " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg)
    sys.exit()


# parse the arguments
def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -d google.com")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-d', '--domain', type=str, help="Domain name to enumerate it's subdomains", required=True)
    parser.add_argument('-b', '--bruteforce', help='Enable the subbrute bruteforce module', nargs='?', default=False)
    parser.add_argument('-p', '--ports', help='Scan the found subdomains against specified tcp ports')
    parser.add_argument('-v', '--verbose', help='Enable Verbosity and display results in realtime', nargs='?',
                        default=False)
    parser.add_argument('-t', '--threads', help='Number of threads to use for subbrute bruteforce', type=int,
                        default=30)
    parser.add_argument('-e', '--engines', help='Specify a comma-separated list of search engines')
    parser.add_argument('-o', '--output', help='Save the results to text file')
    return parser.parse_args()

def useragent():
	user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
	return user_agent

# parse host from scheme, to use for certificate transparency abuse
def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print('[*] Invalid domain, try again..')
        sys.exit(1)
    return host


# write subdomains to a file
def write_file(subdomains, output_file):
    # saving subdomains results to output file
    with open(output_file, 'a') as fp:
        fp.write(subdomains + '\n')
        fp.close()


def main():
    banner()

    args = parse_args()  # args = parser.parse_args()
    target = parse_url(args.domain)
    output = args.output

    # default search crt.sh
    if target:
        crtsearch.CRTsearch(target, output)

if __name__ == "__main__":
    main()

#####################################################################################################
'''
# the domain to scan for subdomains
domain = "sapo.pt"

# read all subdomains in file
file = open("subdomains.txt")
# read all content
content = file.read()
# split by new lines
subdomains = content.splitlines()

for subdomain in subdomains:
    # construct the url
    url = f"http://{subdomain}.{domain}"
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        # pass
        print("ERROR: ", url)
    else:
        print("[+] Discovered subdomain:", url)
'''
