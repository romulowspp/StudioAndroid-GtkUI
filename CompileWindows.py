import os
import urllib
import zipfile
import shutil
import sys

SADir = os.path.abspath(os.path.dirname(sys.argv[0]))
SAFile = os.path.join(SADir, "SAP.py")
Home = os.path.expanduser("~")
PyDir = os.path.join(Home, "PyInstallerTmp")
PyFile = os.path.join(PyDir + 'PyInstaller.zip')
PyInstDir = os.path.join(Home, "PyInstaller")
icon = os.path.join(SADir, "images", "icon.ico")

if not os.path.exists(PyDir):
	os.mkdir(PyDir)
	print("%s made" % PyDir)
else:
	print("%s already exists" % PyDir)


urllib.urlretrieve('https://github.com/pyinstaller/pyinstaller/zipball/develop', PyFile)
zipfile.ZipFile(PyFile).extractall(path=PyDir)
os.remove(PyFile)
DwnDir = os.path.join(PyDir, os.listdir(PyDir)[0])

if not os.path.exists(PyInstDir):
	os.mkdir(PyInstDir)
	print("%s made" % PyInstDir)
else:
	print("%s already exists" % PyInstDir)

for x in os.listdir(DwnDir):
	CopySrc = os.path.join(DwnDir, x)
	CopyDst = os.path.join(PyInstDir, x)
	if not os.path.exists(CopyDst):
		if os.path.isdir(CopySrc):
			shutil.copytree(CopySrc, CopyDst)
		else:
			shutil.copy(CopySrc, CopyDst)

shutil.rmtree(PyDir)
os.chdir(PyInstDir)
print os.getcwd()

os.system("python setup.py")
os.system("python pyinstaller.py -F %s -i %s" %(SAFile, icon))
raw_input("Press enter to exit...")
