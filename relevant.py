import os
relevant_path = 'X:/Zevedtov/reference/databases/AllDBs/SWN402/Schema Objects/Schemas/dbo/Tables'
print(x for x in os.listdir(relevant_path) if x.endswith('.sql'))