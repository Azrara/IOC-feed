
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

def ipReputationTalos():
    url = "https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/087/936/original/ip_filter.blf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIXACIED2SPMSC7GA%2F20191209%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191209T110649Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=7d358841d5307b2d9262fa9f8001e5042d8d090b218e0627240af477aaf1a71b"
    req = requests.get(url)
    result = req.content
    resultDecoded = result.decode("utf-8")
    finalResult = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", resultDecoded)

    with open('ipReputationTalos.txt', 'w') as fileResult:
        for urlHaus in finalResult:
            fileResult.write("%s\n" % urlHaus)

if __name__ == "__main__":
    urlhaus()
    c2servers()
    malwareHash()
    ipReputationTalos()
