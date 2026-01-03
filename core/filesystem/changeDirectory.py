import os

def goBack(path):

    path = os.path.dirname(path)
    
    return path

def goForward(path, itemPos, files):

    file = files[itemPos]

    if file['type'] == 0:

        path = os.path.join(path, file['name'])

        return path

    return 0
