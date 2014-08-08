from flask import Flask, render_template, request, redirect, url_for
# from werkzeug.utils import secure_filename
import os

# import simplejson as json
# import collections
# import requests
# import psycopg2
# from datetime import datetime
# import random

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("3d.html")

if __name__ == '__main__':
	app.run(debug=True)