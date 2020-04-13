import requests
import csv
import re
from itertools import zip_longest


def getConnection(urlSrc):
    """get data from a specific url"""
    url = urlSrc
    req = requests.get(url)
    result = req.content
    resultDecoded = result.decode("utf-8")
    return resultDecoded

def urlhaus() :
    """get recent malicious url"""
    result = getConnection("https://urlhaus.abuse.ch/downloads/csv_online/")
    re1 = 'http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    re2 = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    finaleResulNotCleaned = re.compile("(%s|%s)" % (re1,re2)).findall(result)
        #Remove repeated URLs
    finaleResulNotCleaned = list(set(finaleResulNotCleaned))
    finaleResulCleaned = []
    for line in finaleResulNotCleaned:
        if line == "https://urlhaus.abuse.ch":
            finaleResulNotCleaned.remove(line)
        else:
            if "http://" in line:
                finaleResulCleaned.append(line.replace("http://",""))
            elif "https://" in line :
                finaleResulCleaned.append(line.replace("https://",""))

    return finaleResulCleaned

def c2servers ():
    """get recent c2 servers"""
    result = getConnection("https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt")
    finalResult = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", result)
    return finalResult

""" def malwareHash():
    """get hashes corresponding to recent malwares"""
    result = getConnection("https://feodotracker.abuse.ch/downloads/malware_hashes.txt")
    finalResult= re.findall(r"([a-fA-F\d]{32})", result)
    return finalResult
 """
 
def ipReputationTalos():
    result = getConnection("http://www.talosintelligence.com/documents/ip-blacklist")
    finalResult = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", result)
    return finalResult


if __name__ == "__main__":
    results = {}
    urls = urlhaus()
    ip = c2servers()
    hashes = malwareHash()

    results.update({"URLs":urls, "IP":ip, "Hashes":hashes})
    transportedData = list(zip_longest(*results.values()))

    with open("results.csv","w",newline="") as finalResult:
        writer = csv.writer(finalResult)
        writer.writerow(["URLs","IP","Hashes"])
        writer.writerows(transportedData)   
