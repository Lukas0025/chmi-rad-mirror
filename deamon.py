import chmirad
import datetime
import time

chmiRadUrl = 'https://www.chmi.cz/files/portal/docs/meteo/rad/data_tr_png_1km/'

def main():
    lastImage = 0

    try:
        with open("last.lock", 'r') as handler:
            lastImage = int(handler.read())
    except:
        print("fail to open lock file")

    lastImage = chmirad.autoImagesDownload(lastImage, chmiRadUrl)

    print("sync done {}".format(datetime.datetime.now()))

    with open("last.lock", 'w') as handler:
        handler.write(str(lastImage))

print("Deamon started")
while True:
    main()
    #sleep 15 minutes
    time.sleep(15 * 60)
print("Deamon ended")