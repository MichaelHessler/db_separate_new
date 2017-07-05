import pypyodbc
import FilenameOnly
TableNames = FilenameOnly.get_filename_only()
print(type(TableNames))
# print(str(TableNames.__len__()))
connection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=GX700\SQL2012;'
                                'Database=db_separate;'
                                'uid=db_sep_writer;pwd=write')
cursor = connection.cursor()
#cursor.executemany("INSERT INTO tbl_tables (1,2) VALUES (,?)" ,FilenameOnly.get_filename_only())
cursor.execute("INSERT INTO tbl_tables (table_name) VALUES ('AccountUpdate')")
#cursor.execute("INSERT INTO tbl_tables  (1,2) VALUES (,?)", TableNames, many_mode = 'false')
cursor.commit()


#var_string = ', '.join('?' * len(TableNames))
#query_string = 'INSERT INTO tbl_tables (table_name) VALUES (%s);' % var_string
#cursor.execute(query_string, TableNames)


SQLCommand = ("SELECT count(table_id) FROM tbl_tables")
cursor.execute(SQLCommand)
results = cursor.fetchone()
connection.close()
# This worked