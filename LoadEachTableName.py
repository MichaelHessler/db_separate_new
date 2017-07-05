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
for index in range(len(TableNames)):
    parameter = TableNames[index]
    print(TableNames[index])
    SQLCommand = ("exec  db_separate.dbo.uspAddNewTable_name  '?' ")
    print(SQLCommand)
    cursor.execute(SQLCommand, parameter)
    # assert isinstance(cursor, object)
    # results = cursor.fetchall()
    print(cursor.fetchall())
    cursor.commit()
connection.close()



# cursor.execute("exec  dbo.uspAddNewTable_name  @_new_table_name")
