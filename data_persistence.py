import pyodbc

username = ""
password = ""
dbname = ""
servername = ""
connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=' + servername + ',1433;Database=' + dbname + ';Uid=' + username + ';Pwd=' + password + ';'
