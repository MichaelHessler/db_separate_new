import os
for file in os.scandir('X:\\Zevedtov\\reference\\databases\\AllDBs\\SWN402\\Schema Objects\\Schemas\\dbo\\Tables'):
    # line = ''
    if file.is_file():
        f = file.name.split(".")
        print(f[0])
        #this works and lists each of the filenames