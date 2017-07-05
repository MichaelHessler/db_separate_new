import pyodbc
server = 'GX700\SQL2012'
database = 'db_separate'
username = 'db_sep_writer'
password = 'write'
driver = '{SQL Server}' # Driver you need to connect to the database
port = '1433'
cnn = pyodbc.connect('DRIVER='+driver+';PORT=port;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+
                 ';PWD='+password)
    #cursor = cnn.cursor()
#not used, junk