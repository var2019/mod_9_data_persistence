import pyodbc

username = ""
password = ""
dbname = ""
servername = ""
connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=' + servername + ',1433;Database=' + dbname + ';Uid=' + username + ';Pwd=' + password + ';'

conn = pyodbc.connect(connection_string,autocommit=True)
curs = conn.cursor()

curs.execute(
    '''
     create table someDataSet(
     ID int primary key clustered identity(1,1)
     , attribute1 datatype
     , attribute2 datatype 
     )
    '''

     )