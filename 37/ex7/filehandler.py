import os, shutil
from zipfile import ZipFile

def copyFiles(workingDir, files, dst):
    for f in files:
        tmpDst = dst + '/' +  f
        try:
            shutil.copy(workingDir + '/' + f, tmpDst)
        except PermissionError:
            print('Do not have permission to copy: ' + f)

def zipPyFiles(workingDir, files, zipName, tempDir):
    zibObj = ZipFile(zipName, 'w')
    for f in files:
        if f.split('.')[-1] == 'py':
            zibObj.write(workingDir + '/' + f)
    zibObj.close()
