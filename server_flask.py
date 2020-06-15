try:
    from flask import Flask
    from scraper import run as scrape_run
    import sys
    import os

except Exception as e:
    print("Some modules are missing {}".format(e))


app = Flask(__name__)


@app.route("/",methods=['GET'])
def hello_world():
    return "Hello World"


@app.route("/box-ofiice-mojo",methods=['POST'])
def box_office():
    scrape_run()
    return {
        "Status": "Done"
    }
