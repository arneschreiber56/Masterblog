"""Runs the Masterblog app and provides the flask routes and functionality for
the Masterblog web application"""
from flask import Flask

app = Flask(__name__)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)