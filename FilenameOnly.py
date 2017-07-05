import os


def get_filename_only() -> object:
    """

    :rtype: object
    """
    files = []

    for file in os.scandir('X:\\Zevedtov\\reference\\databases\\AllDBs\\SWN402\\Schema Objects\\Schemas\\dbo\\Tables'):
        # line = ''
        if file.is_file():
            f = file.name.split(".")
            # print(f[0])
            files.append(f[0])

    return files
#KEEP THIS ONE, it is used by others
