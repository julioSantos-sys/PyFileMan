from core.filesystem.listFiles import *


while True:
    path = input("Digite o diretório:")

    files = getFiles(path)

    for item in files:
        print
