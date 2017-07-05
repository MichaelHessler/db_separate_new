import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=GX700\SQL2012;'
                                'Database=db_separate;'
                                'uid=db_sep_writer;pwd=write')
cursor = connection.cursor()
SQLCommand = ("SELECT count(table_id) FROM tbl_tables")
cursor.execute(SQLCommand)
results = cursor.fetchone()
connection.close()

#note that this runs to this point but doesn't print a return value
#print(str(results[0]) + " " + results[1])
