import requests
import re
import csv

def _sources():
    with open('sources.txt') as fileSources:
        content=fileSources.readlines()
    return content

def _extractIP(source):
    proxy = {"https":"http://proxygin.melinda.local:8080","http":" http://proxygin.melinda.local:8080"}
    req = requests.get(source,proxies=proxy)
    result = req.content
    resultDecoded = result.decode("utf-8")
    finalResult = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", resultDecoded)
    return finalResult

def _extratctUrl(source):
    proxy = {"https":"http://proxygin.melinda.local:8080","http":" http://proxygin.melinda.alocal:8080"}
    req = requests.get(source,proxies=proxy)
    result = req.content
    resultDecoded = result.decode("utf-8")
    finalResult = re.findall('http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', resultDecoded)
    return finalResult

def _extractHash(source):
    proxy = {"https":"http://proxygin.melinda.local:8080","http":" http://proxygin.melinda.local:8080"}
    req = requests.get(source,proxies=proxy)
    result = req.content
    resultDecoded = result.decode("utf-8")
    finalResult= re.findall(r"([a-fA-F\d]{32})", resultDecoded)
    return finalResult

def _merge():
    sources = _sources()
    sourcesWithIocs = {}
    ioc = {}
    for line in sources:
        ioc.update({"hash":_extractHash(line)})
        ioc.update({"ulr":_extratctUrl(line)})
        ioc.update({"ip":_extractIP(line)})
    for line in sources:
        sourcesWithIocs.update({line:ioc})
    return sourcesWithIocs


if __name__ == "__main__":
    ioc = _merge()
    with open('result.csv','w',newline="") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in ioc.items():
            writer.writerow([key,value])

