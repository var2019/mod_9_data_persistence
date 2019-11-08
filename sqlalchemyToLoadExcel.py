import pyodbc
import pandas as pd
from sqlalchemy import create_engine

username = "kristensohm"
password = "Gidferd7*"
dbname = "MIS5400"
servername = "gidferd.database.windows.net"

OutputDataSet = pd.read_excel(r"USIncomeAndConsumptionData.xlsx", sheet_name='Personal Income')
eng = create_engine('mssql+pyodbc://kristensohm:Gidferd7*@gidferd.database.windows.net:1433/MIS5400?Driver={ODBC Driver 17 for SQL Server}', echo=True)
OutputDataSet.to_sql('PersonalIncome', eng, index=False)


#connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=' + servername + ',1433;Database=' + dbname + ';Uid=' + username + ';Pwd=' + password + ';'
#conn = pyodbc.connect(connection_string, autocommit=True)
#curs = conn.cursor()