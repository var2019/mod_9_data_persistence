from sqlalchemy import create_engine
from flask import Flask, g, render_template, abort, request
import os
import socket

username = "kristinsohm"
password = ""
dbname = "MIS5400"
servername = "gidferd.database.windows.net"
eng = create_engine('mssql+pyodbc://kristensohm:Gidferd7*@gidferd.database.windows.net:1433/MIS5400?Driver={ODBC Driver 17 for SQL Server}', echo=True)
app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
    try:
        eng.connect()
    except ConnectionError:
        abort("No database connection could be established.", 503)

@app.teardown_request
def teardown_request(exception):
    try:
        g.rdb_conn.close()
    except AttributeError:
        pass


@app.route("/")
def hello():
    html = "<h3>There be data here</h3>"
    return html.format()

@app.route("/getdata")
def get():
    eng.connect()
    return


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)