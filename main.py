import os
path='X:\\Zevedtov\\reference\\databases\\AllDBs\\SWN402\\Schema Objects\\Schemas\\dbo\\Tables'
os.getcwd()
for(files) in os.walk(path):
    print(files for files in os.listdir(path) if files.endswith('.sql'))
#this main just a scrap


