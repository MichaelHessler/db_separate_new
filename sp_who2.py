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

cursor.execute("exec sp_who2")
print(cursor.fetchall())
#result = cursor.fetchall()
#for row in result:
#  print row[0]
cursor.commit()
#this works. it runs a proc and prints the results.
#the next step is for write a proc to add file_names where they don't already exist in the table.



