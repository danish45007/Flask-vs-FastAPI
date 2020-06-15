try: 
    from fastapi import FastAPI
    from scraper import run as scrape_run
    import os
    import sys

except Exception as e:
    print("Some modules are missing {}".format(e))


app = FastAPI()


@app.get("/")
def hello_world():
    return {
        "Hello": "World",
        "Hi": "Danish"
    }

@app.post("/box-ofiice-mojo")
def box_office():
    scrape_run()
    return {
        "Status": "Done"
    }