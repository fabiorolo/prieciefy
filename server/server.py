# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:37:16 2019

@author: NB25761
"""


from flask import Flask
from flask import request
from os import walk

app = Flask(__name__)

@app.route("/url")
def getUrls():    
    siteName = request.args.get('siteName')  
    urls = ''
    for line in open("files/" + siteName.strip(" ") + '.txt'):
        urls += (line.replace("\n",'')) + ","
    
    return urls[0:-1]

@app.route("/stores")
def getAvailableStores():
    f = []
    strToReturn = ""

    for (dirpath, dirnames, filenames) in walk("../files"):
        f.extend(filenames)
        break
    
    for i in f:
        strToReturn +=i[0:-4] + ","
        
    
    return strToReturn[0:-1]
    
    
if __name__ == "__main__":
    app.run()
    



