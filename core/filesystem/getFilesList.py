import os


def getFiles(path):
    files = []

    with os.scandir(path) as entries:
        for entry in entries:
            files.append({
                'name': entry.name,
                'path': entry.path,
                'is_dir': entry.is_dir(),
                'is_file': entry.is_file()
            })
    
    return files


