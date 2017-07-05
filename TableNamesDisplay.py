import pypyodbc
import FilenameOnly

TableNames = FilenameOnly.get_filename_only()
connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=GX700\SQL2012;'
                              'Database=db_separate;'
                              'uid=db_sep_writer;pwd=write')
cursor = connection.cursor()
for index in range(len(TableNames)):
    #print(TableNames[index])
    ReadCommand = (
        "SELECT CAST(CASE  WHEN EXISTS(SELECT * FROM tbl_tables where table_name = '"
        + TableNames[index] +
        "') THEN 1 ELSE 0 END AS BIT)")
    #print(ReadCommand)
    cursor.execute(ReadCommand)
    #assert isinstance(cursor, object)
    results = cursor.fetchone()
    if results:
        print("{0} results={1}".format(str(TableNames[index]), str(results)))
    else:
        print("{0}resultsNOT={1}".format(str(TableNames[index]), str(results)))
    # cursor.commit()
connection.close()

    # TableNames[index]
    # str(index))

    # cursor.execute("INSERT INTO tbl_tables (table_name) VALUES (?)", TableNames[index])

    # cursor.commit()
