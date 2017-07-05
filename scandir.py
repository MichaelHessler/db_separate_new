import os
for file in os.scandir('X:\\Zevedtov\\reference\\databases\\AllDBs\\SWN402\\Schema Objects\\Schemas\\dbo\\Tables'):
    line = ''
    if file.is_file():
        line += 'f'
    elif file.is_dir():
        line += 'd'
    elif file.is_symlink():
        line += 'l'
    line += '\t'
    print("{}{}".format(line, file.name))
#this was borrowed from what I found online