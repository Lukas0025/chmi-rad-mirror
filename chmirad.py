import urllib.request
import re
from datetime import datetime

def extractHrefs(html, url):
    links = re.findall("href=[\"'](.*)[\"']", html)
    
    fullLinks = []
    for link in links:
        if link != "../" and link != "..":
            fullLinks.append("{}{}".format(url, link))

    return fullLinks

def getImagesList(url):
    response = urllib.request.urlopen("{}".format(url))
    text = response.read().decode('utf-8')
    return extractHrefs(text, url)

def getImageTime(url):
    name    = url.split("/")[-1]
    strTime = name.replace("pacz23.z_max3d.", "").replace(".0.png", "")

    return datetime.strptime(strTime, '%Y%m%d.%H%M')

def downloadImage(url):
    fileName = "./data/{}.png".format(int(getImageTime(url).timestamp()))

    imgData = urllib.request.urlopen(url).read()

    with open(fileName, 'wb') as handler:
        handler.write(imgData)

def autoImagesDownload(lastImage, url):
    imagesList = getImagesList(url)

    for image in imagesList:
        time = getImageTime(image)

        if (time.timestamp() > lastImage):
            downloadImage(image)

    return int(getImageTime(getLastest(imagesList)).timestamp())

def getLastest(imagesList):
    maxTime   = 0
    lastImage = None
    for image in imagesList:
        time = getImageTime(image)

        if (time.timestamp() > maxTime):
            maxTime   = time.timestamp()
            lastImage = image

    return lastImage
