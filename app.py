import os

from dotenv import load_dotenv

from base import create_app, db

load_dotenv()

app = create_app(os.getenv("CONFIG_MODE"))

from router import director, movie


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
