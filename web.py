from flask import Flask, redirect
import chmirad

app = Flask(__name__,
            static_url_path='/data', 
            static_folder='data')

chmiRadUrl = 'https://www.chmi.cz/files/portal/docs/meteo/rad/data_tr_png_1km/'

@app.route("/")
def main():
    chmiTime  = int(chmirad.getImageTime(chmirad.getLastest(chmirad.getImagesList(chmiRadUrl))).timestamp())
    mirrorTime = 0
    try:
        with open("last.lock", 'r') as handler:
            mirrorTime = int(handler.read())
    except:
        print("fail to open lock file")
        
    return "<h1>Toto je CHMI-RAD zrcadlo</h1><p>Obsahuje kopie radarových snímků z CHMI. K těmto snímkům lze přistupovat přes jednoduché API.</p><h3>Stav zrcadla</h3><p>UPSTREAM: {}</p>".format(chmiRadUrl) + "<p>Zcadlo obsahuje poslední snímek s timestamp {}. CHMI Upstream obsahuje poslední snímek s timestamp {}. Zrcadlo je opožděno o {}s.</p>".format(mirrorTime, chmiTime, chmiTime - mirrorTime) + "<h5>Poslední snímek zrcadla</h5><img style='max-width:100%' src='/last'><h5>Poslední snímek CHMI Upstream</h5><img style='max-width:100%' src='/lastchmi'><h3>API</h3><ul><li>GET /last - poslední snímek na zrcadle</li><li>GET /lastchmi - poslední snímek UPSTREAMU</li><li>GET /lastcode - kód posledního snímku zrcadla</li></ul><p>Historické snímky jsou dostupné v /data pod jmény [timestamp].png kde timstamp jsou v intervalech 15min od /lastcode. Například GET /data/{}.png.</p>".format(mirrorTime)

@app.route("/last")
def last():
    mirrorTime = 0
    try:
        with open("last.lock", 'r') as handler:
            mirrorTime = int(handler.read())
    except:
        print("fail to open lock file")

    return redirect("/data/{}.png".format(mirrorTime), code=302)

@app.route("/lastchmi")
def lastchmi():
    return redirect(chmirad.getLastest(chmirad.getImagesList(chmiRadUrl)), code=302)

@app.route("/lastcode")
def lastcode():
    mirrorTime = 0
    try:
        with open("last.lock", 'r') as handler:
            mirrorTime = int(handler.read())
    except:
        print("fail to open lock file")

    return str(mirrorTime)