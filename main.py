import requests
import argparse
import re
import urlparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="Url that you want to crawl")
    options = parser.parse_args()
    if not options.url:
        parser.error("[!] Please add an url to proceed, --help for more informations.")
    return options

def extract_all_href(url):
    res = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"',res.content)

def crawler(url):
    hrefs = extract_all_href(url)
    for l in hrefs:
        l = urlparse.urljoin(url, l)
        if "#" in l:
            l = l.split("#")[0]
        if target_url in l and l not in target_links:
            target_links.append(l)
            print("[+] Link found ! > " + l)
            crawler(l)

options = get_arguments()
target_url = options.url
target_links = []
crawler(target_url)
