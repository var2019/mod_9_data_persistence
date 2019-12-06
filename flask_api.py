import sqlalchemy as db
from flask import Flask, abort
import json
import decimal
import datetime

username = "kristensohm"
password = ""
dbname = "MIS5400"
servername = "gidferd.database.windows.net"
driver = "{ODBC Driver 17 for SQL Server}"
engine = db.create_engine(f'mssql+pyodbc://{username}:{password}@{servername}:1433/{dbname}?Driver={driver}', echo=True)
app = Flask(__name__)
app.config.from_object(__name__)

# Establish a database connection before requests
@app.before_request
def before_request():
    try:
        engine.connect()
    except ConnectionError:
        abort("No database connection could be established.", 503)

# Try really hard to dispose of the database connection cleanly
@app.teardown_request
def teardown_request(exception):
    try:
        engine.dispose()
    except AttributeError:
        pass
    finally:
        engine.dispose()

# Default route with no info
@app.route("/", methods=['GET'])
def hello():
    html = "<h3>There be data here</h3>"
    return html.format()

# Gets the data from the income table
@app.route("/api/v1/income", methods=['GET'])
def get_income():
    query = "SELECT * FROM PersonalIncome"
    results = engine.execute(query)
    return json.dumps([dict(r) for r in results], default=alchemyencoder)

# Gets the data from the consumption (expenses) table
@app.route("/api/v1/expenses", methods=['GET'])
def get_expenses():
    query = "SELECT * FROM ['ConsumptionByProduct']"
    results = engine.execute(query)
    return json.dumps([dict(r) for r in results], default=alchemyencoder)

# Used to format decimals and dates properly on conversion from sqlalchemy object to json
def alchemyencoder(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


