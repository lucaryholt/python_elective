import sys
import dirhandler as dirH, filehandler as fileH

argv = sys.argv

#Basic arg checking
if len(argv) < 2:
    print('Not enough args')

argTodir = '-todir' in argv
argZip = '-zip' in argv

tempDir = 'tmp'
zipName = 'archive.zip'
workingDir = argv[1]
filesInDir = dirH.filesInDir(workingDir)

if argTodir:
    tempDir = argv[argv.index('-todir') + 1]

#Now makes dir
try:
    dirH.mkdir(tempDir)
except FileExistsError:
    print('INFO: Directory ' + tempDir + ' already exists. Continuing.')

#Copy files
fileH.copyFiles(workingDir, filesInDir, tempDir)

#Now zip if specified
if argZip:
    zipName = argv[argv.index('-zip') + 1]
    fileH.zipPyFiles(workingDir, dirH.filesInDir(tempDir), zipName, tempDir)
