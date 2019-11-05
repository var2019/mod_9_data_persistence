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
'''
#Answer the following Questions
**1) Which database will you be using for your final project? (e.g.SQL Server, MongoDB, Other...) (5pts)



** 2) Where will the database you are using be hosted? (e.g.Azure, Locally, Shared MIS Dept.) (5pts)



** 3) Why did you choose the database and hosting option you did? (10 pts)


** Do the Following:

** 1) Setup the data base you will be using

** 2) Connect to the datbase with a python script and upload the script.
*If the script contains sensitive information such as credentials that cannot be shared,
**please take a screen-shot of the connection and blot out sensitive information.(10 pts.)


*3) Describe the schema you will use in your database.If it is a relational database (e.g.SQL Server),
*share your table schema, if it is a document store (e.g.MongoDB) then share a sample JSON file that represents the data you intend to store.(10 pts)
'''



