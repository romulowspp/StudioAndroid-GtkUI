import os
import urllib
import zipfile
import shutil
import sys

if "--help" in sys.argv:
	print("\nWelcome!\n"
"This is my home made tool to compile Python Scripts on any OS.\n"
"Usage: python Compile.py [CustomToCompileScript.py [CustomWindowsIcon.ico]]\n"
"Default: CompileScript = SA.py, Icon = images/icon.ico\n")
	exit()

ScriptDir = os.path.abspath(os.path.dirname(sys.argv[0]))
ScriptFile = os.path.join(ScriptDir, "SA.py")
Home = os.path.expanduser("~")
PyDir = os.path.join(Home, "PyInstallerTmp")
PyFile = os.path.join(PyDir + 'PyInstaller.zip')
PyInstDir = os.path.join(Home, "PyInstaller")
icon = "-i %s" % os.path.join(ScriptDir, "images", "icon.ico")

try:
	sys.argv[1]
except IndexError:
	pass
else:
	print("Custom ScriptName: %s" % sys.argv[1])
	ScriptFile = os.path.join(ScriptDir, sys.argv[1])
	icon = ''
	try:
		sys.argv[2]
	except IndexError:
		pass
	else:
		print("Custom Icon: %s" % sys.argv[2])
		icon = "-i %s" % os.path.join(ScriptDir, sys.argv[2])

if not os.path.exists(PyDir):
	os.mkdir(PyDir)
	print("%s made" % PyDir)
else:
	print("%s already exists" % PyDir)


Name = str(os.path.basename(ScriptFile)).replace(".py", "")
compiled = os.path.join(PyInstDir, Name, "dist", Name)


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

os.system("python setup.py")
os.system("python pyinstaller.py -y -F %s %s" %(ScriptFile, icon))
shutil.copy(compiled, os.path.join(ScriptDir, Name + "-Compiled"))
raw_input("Press enter to exit...")
