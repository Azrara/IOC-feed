
import requests
import csv
import re


def urlhaus() :
    url = "https://urlhaus.abuse.ch/downloads/csv_recent"
    req = requests.get(url)
    result = req.content
    resultDecoded = result.decode("utf-8")
    finalResult = re.findall('http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', resultDecoded)

    with open('urlhausMal.txt', 'w') as fileResult:
        for urlHaus in finalResult:
            fileResult.write("%s\n" % urlHaus)


def c2servers ():
    url = "https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt"
    req = requests.get(url)
    result = req.content
    resultDecoded = result.decode("utf-8")
    finalResult = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", resultDecoded)

    with open('c2servers.txt', 'w') as fileResult:
        for ip in finalResult:
            fileResult.write("%s\n" % ip)


def malwareHash():
    url="https://feodotracker.abuse.ch/downloads/malware_hashes.txt"
    req = requests.get(url)
    result = req.content
    resultDecoded = result.decode("utf-8")
    finalResult= re.findall(r"([a-fA-F\d]{32})", resultDecoded)

    with open('md5Mal.txt', 'w') as fileResult:
        for md5Mal in finalResult:
            fileResult.write("%s\n" % md5Mal)

 

if __name__ == "__main__":
    urlhaus()
    c2servers()
    malwareHash()