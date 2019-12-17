# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:58:09 2019

@author: NB25761
"""

from urllib.parse import urljoin
from bs4 import BeautifulSoup
from urllib.request import urlopen

def getAllUrl(url):
    urlList = []
    try:
        page = urlopen( url ).read()
        soup = BeautifulSoup(page,features="lxml")
        soup.prettify()
        for anchor in soup.findAll('a', href=True):
            if not 'http://' in anchor['href']:
                if urljoin(url, anchor['href']) not in urlList:
                    urlList.append(urljoin(url, anchor['href']))
            else:
                if anchor['href'] not in urlList:
                    urlList.append(anchor['href'])
    
        return urlList

    except:
        print("error")
        return []




def getAllUrlsFromSites(sitesUrl,sitesName):
    for i in range(len(sitesUrl)):    
        print("getting urls from: " + sitesName[i])
        urls = getAllUrl(sitesUrl[i])
        
        fullList = []
        
        for x in urls:
            listUrls = list
            listUrls = getAllUrl(x)
            try:
                for j in listUrls:
                    if not j in fullList:
                        fullList.append(j)
            except :
                print ('Woops wrong content passed')

        f = open("files/" + str(sitesName[i]) + ".txt", "x",encoding='utf-8')
        
        for i in fullList:
            f.write(i+ "\n")    
            
        f.close()
        
        
        
sitesUrl = ["https://www.worten.pt/","https://www.pcdiga.com/","https://www.radiopopular.pt/","https://www.fnac.pt/","https://mediamarkt.pt/"]
sitesNames = ["worten","pcdiga","radioPopular","fnac","mediamarkt"]
getAllUrlsFromSites(sitesUrl,sitesNames)
