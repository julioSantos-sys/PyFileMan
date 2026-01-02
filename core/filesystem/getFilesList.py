import os

def is_binary(path, chunk_size=512):
    try:
        with open(path, 'rb') as f:
            chunk = f.read(chunk_size)
            return b'\x00' in chunk
    except Exception:
        return True


def getFiles(path):
    files = []

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                fileType = 0
            elif is_binary(entry.path):
                fileType = 1
            else:
                fileType = 2
            files.append({
                'name': entry.name,
                'path': entry.path,
                'type': fileType
            })
    
    files.sort(key=lambda f: (f['type'], f['name'].lower()))

    return files


