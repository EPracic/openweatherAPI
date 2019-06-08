import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    return render_template("index.html")


@app.route("/wuppertal", methods=["GET"])
def wuppertal():

    grad = "Wuppertal"

    unit = "metric"

    apikey = "fb5d4f2789aa6013c453b5ff9385bcc1"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("wacken.html", data=data.json())

@app.route("/pula", methods=["GET"])
def pula():

    grad = "Pula"

    unit = "metric"

    apikey = "fb5d4f2789aa6013c453b5ff9385bcc1"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("pula.html", data=data.json())


@app.route("/stockholm", methods=["GET"])
def stockholm():

    grad = "Stockholm"

    unit = "metric"

    apikey = "fb5d4f2789aa6013c453b5ff9385bcc1"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("stockholm.html", data=data.json())

@app.route("/search", methods=["GET"])
def search():

    return render_template("search.html")


@app.route("/searchresult", methods=["POST"])
def searchresult():

    grad = request.form.get("ime")

    unit = "metric"

    apikey = "fb5d4f2789aa6013c453b5ff9385bcc1"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("searchresult.html", data=data.json())


if __name__ == '__main__':
    app.run()