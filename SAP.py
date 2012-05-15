

# IMPORTS
from __future__ import division
import os
import fnmatch
import webbrowser
import urllib
import sys
import random
import pygtk
pygtk.require('2.0')
import gtk
import gobject
import shutil
import signal
import zipfile


Opt5="EMPTY"
Web = webbrowser.get()
if sys.platform == 'linux2':
	OS = 'Lin'
elif sys.platform == 'win32':
	OS = 'Win'
else:
	print("Your OS is not Windows32 and not Linux2, could you PM me the next output?\n\n\n" + sys.platform)

def delete_event(self, widget, event, data=None):
	gtk.main_quit()
	return False


def main(self):
	gtk.main()

def destroy(self, widget, data=None):
	gtk.main_quit()

def callback(widget, option):
	if option == '1':
		Utils()
	elif option == '2':
		CopyFrom()
	elif option == '3':
		Resize()
	elif option == '4':
		Theme()
	elif option == '6':
		PrepareBuilding()
	elif option == 'change':
		Changelog()
	elif option == 'help':
		Help()
	elif option == 'upd':
		Update()
	else :
		if OS == 'Lin':
			print('"' + option + '"' + " is the command...")
			Run = raw_input("Do you want to run the command in the terminal with normal usage?  [Y/n]")
			if not Run == 'n' :
				os.system("./Script " + option)
		else :
			print("This option is not defined yet, SORRY!")

def NewDialog(Title, Text):
	dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_OK)
	dialog.set_markup("<b>%s</b>" % Title)
	dialog.format_secondary_markup("%s" % Text)
	dialog.run()
	dialog.destroy()

def Restart(cmd):
	python = sys.executable
	os.execl(python, python, * sys.argv)

def KillPage(cmd):
	notebook = MainApp.notebook
	page = notebook.get_current_page()
        notebook.remove_page(page)
        notebook.queue_draw_area(0,0,-1,-1)


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

def ExZip():
	zipfile.ZipFile(ScriptDir + "/Utils.zip").extractall()
	os.system("chmod 755 " + ScriptDir + "/Utils/*")


window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.set_title("StudioAndroid")
window.connect("delete_event", delete_event, 0)
window.set_border_width(15)
window.set_size_request(750,500)
#window.set_resizable(False)
window.set_position(gtk.WIN_POS_CENTER)

vbox = gtk.VBox(False, 5)
hbox = gtk.HBox(False, 5)

ScriptDir=os.path.dirname(sys.argv[0])
Home=os.path.expanduser('~')

print("OS = " + OS)
print("ScriptDir = " + ScriptDir)
print("Home = " + Home)

StatusTable = gtk.Table(1, 3, True)
MainAppButton = gtk.Button("Main App")
MainAppButton.connect("clicked", Restart)
StatusTable.attach(MainAppButton, 0, 1, 0, 1, yoptions=gtk.EXPAND)



class MainApp():
	if OS == 'Win':
		Icon = "\images\icon.png"
	else:
		Icon = "/images/icon.png"

	placeIcon = gtk.gdk.pixbuf_new_from_file(ScriptDir + Icon)
	window.set_icon(placeIcon)

	#
	# MAIN TABLE
	#



	table = gtk.Table(3, 3, False)
	table.set_col_spacings(0)
	table.set_row_spacings(0)

	notebook = gtk.Notebook()
	notebook.set_tab_pos(gtk.POS_TOP)
	table.attach(notebook, 0, 3, 0, 3)

        notebook.show()

	# UTIL TABLE
	UtilVBox = gtk.VBox()

	UtilLabel = gtk.Label("Utilities")

	image = gtk.Image()
	image.set_from_file("images/Utils.png")
	image.show()
	UtilVBox.pack_start(image)

	MainOptCl = gtk.Button("Clean Workspace")
	MainOptCl.connect("clicked", callback, "Cl")
	UtilVBox.pack_start(MainOptCl, False, False, 10)

	MainOpt1 = gtk.Button("Install Utilities")
	MainOpt1.connect("clicked", callback, "1")
	UtilVBox.pack_start(MainOpt1, False, False, 10)

	MainOpt2 = gtk.Button("CopieFrom")
	MainOpt2.connect("clicked", callback, "2")
	UtilVBox.pack_start(MainOpt2, False, False, 10)

	MainOpt3 = gtk.Button("Resize")
	MainOpt3.connect("clicked", callback, "3")
	UtilVBox.pack_start(MainOpt3, False, False, 10)

	MainOpt4 = gtk.Button("Batch Theme")
	MainOpt4.connect("clicked", callback, "4")
	UtilVBox.pack_start(MainOpt4, False, False, 10)

	MainOpt5 = gtk.Button("Optimize Images")
	MainOpt5.connect("clicked", callback, "5")
	UtilVBox.pack_start(MainOpt5, False, False, 10)

	notebook.insert_page(UtilVBox, UtilLabel, 1)

	# DEVELOP TABLE

	DevelopTable = gtk.Table(8, 1, False)
	DevelopLabel = gtk.Label("Development")
	DevelopVBox = gtk.VBox()

	image = gtk.Image()
	image.set_from_file("images/Develop.png")
	image.show()
	DevelopVBox.pack_start(image)

	MainOpt6 = gtk.Button("Prepare Building")
	MainOpt6.connect("clicked", callback, "6")
	DevelopVBox.pack_start(MainOpt6, False, False, 10)

	MainOpt7 = gtk.Button("Build from Source")
	MainOpt7.connect("clicked", callback, "7")
	DevelopVBox.pack_start(MainOpt7, False, False, 10)

	MainOpt8 = gtk.Button("Build Kernel")
	MainOpt8.connect("clicked", callback, "8")
	DevelopVBox.pack_start(MainOpt8, False, False, 10)

	MainOpt9 = gtk.Button("Add Governor")
	#MainOpt9.connect("clicked", self.callback, "Build Kernel")
	DevelopVBox.pack_start(MainOpt9, False, False, 10)

	MainOpt10 = gtk.Button("Switch Build-Mode")
	MainOpt10.connect("clicked", callback, "10")
	DevelopVBox.pack_start(MainOpt10, False, False, 10)

	MainOpt11 = gtk.Button("Install Android-SDK")
	MainOpt11.connect("clicked", callback, "11")
	DevelopVBox.pack_start(MainOpt11, False, False, 10)

	MainOpt12 = gtk.Button("Install Java JDK")
	MainOpt12.connect("clicked", callback, "12")
	DevelopVBox.pack_start(MainOpt12, False, False, 10)

	notebook.insert_page(DevelopVBox, DevelopLabel, 2)

	# APK TABLE

	ApkLabel = gtk.Label("APK")
	APKVBox = gtk.VBox()

	image = gtk.Image()
	image.set_from_file("images/APK.png")
	image.show()
	APKVBox.pack_start(image, False, False, 10)

	MainOpt13 = gtk.Button("(De)Compile")
	MainOpt13.connect("clicked", callback, "13")
	APKVBox.pack_start(MainOpt13, False, False, 10)

	MainOpt14 = gtk.Button("Extract/Repackage")
	MainOpt14.connect("clicked", callback, "14")
	APKVBox.pack_start(MainOpt14, False, False, 10)

	MainOpt15 = gtk.Button("Sign APK")
	MainOpt15.connect("clicked", callback, "15")
	APKVBox.pack_start(MainOpt15, False, False, 10)

	MainOpt16 = gtk.Button("Zipalign APK")
	MainOpt16.connect("clicked", callback, "16")
	APKVBox.pack_start(MainOpt16, False, False, 10)

	MainOpt17 = gtk.Button("Compile, Zip, Sign")
	MainOpt17.connect("clicked", callback, "17")
	APKVBox.pack_start(MainOpt17, False, False, 10)

	MainOpt18 = gtk.Button("Install APK")
	MainOpt18.connect("clicked", callback, "18")
	APKVBox.pack_start(MainOpt18, False, False, 10)

	notebook.insert_page(APKVBox, ApkLabel, 3)

	# ADVANCE TABLE

	AdvanceVBox = gtk.VBox()
	AdvanceLabel = gtk.Label("Advanced")

	image = gtk.Image()
	image.set_from_file("images/Advanced.png")
	image.show()
	AdvanceVBox.pack_start(image)

	MainOpt19 = gtk.Button("Smali")
	MainOpt19.connect("clicked", callback, "19")
	AdvanceVBox.pack_start(MainOpt19, False, False, 10)

	MainOpt20 = gtk.Button("BakSmali")
	MainOpt20.connect("clicked", callback, "20")
	AdvanceVBox.pack_start(MainOpt20, False, False, 10)

	MainOpt21 = gtk.Button("ODEX")
	#MainOpt21.connect("clicked", callback, "ODEX")
	AdvanceVBox.pack_start(MainOpt21, False, False, 10)

	MainOpt22 = gtk.Button("DE-ODEX")
	MainOpt22.connect("clicked", callback, "22")
	AdvanceVBox.pack_start(MainOpt22, False, False, 10)

	MainOpt23 = gtk.Button("Aroma Menu")
	MainOpt23.connect("clicked", callback, "23")
	AdvanceVBox.pack_start(MainOpt23, False, False, 10)

	notebook.insert_page(AdvanceVBox, AdvanceLabel, 4)

	# EMPTY TABLE

	#button5 = gtk.Button(Opt5)
        #button5.connect("clicked", callback, Opt5)
	MainAppButton = gtk.Button("Restart")
	MainAppButton.connect("clicked", Restart)
	table.attach(MainAppButton, 1, 2, 1, 2, yoptions=gtk.EXPAND)

	# OPTIONS TABLE

	OptionsTable = gtk.Table(8, 1, False)
	OptionsLabel = gtk.Label("Options")

	image = gtk.Image()
	image.set_from_file("images/Options.png")
	image.show()
	OptionsTable.attach(image, 0, 1, 0, 1, yoptions=gtk.EXPAND)
	
	MainOptl = gtk.Button("Check the log")
	MainOptl.connect("clicked", callback, "Check the log")
	OptionsTable.attach(MainOptl, 0, 1, 1, 2, yoptions=gtk.EXPAND)

	MainOptc = gtk.Button("Changelog")
	MainOptc.connect("clicked", callback, "change")
	OptionsTable.attach(MainOptc, 0, 1, 2, 3, yoptions=gtk.EXPAND)

	MainOpth = gtk.Button("Help! What do I do?")
	MainOpth.connect("clicked", callback, "help")
	OptionsTable.attach(MainOpth, 0, 1, 3, 4, yoptions=gtk.EXPAND)

	MainOptu = gtk.Button("Update StudioAndroid")
	MainOptu.connect("clicked", callback, "upd")
	OptionsTable.attach(MainOptu, 0, 1, 4, 5, yoptions=gtk.EXPAND)

	#table.attach(OptionsTable, 2, 3, 1, 2)
	notebook.insert_page(OptionsTable, OptionsLabel, 5)
	OptionsTable.show()

	# END, show main table	
	table.show()
        #self.box2.pack_start(table, False, True, 0)
	window.add(table)

	
        window.show_all()



def Utils():
	def SetAll(cmd):
		button1.set_active(True)
		button2.set_active(True)
		button3.set_active(True)
		button4.set_active(True)
		button5.set_active(True)
		button6.set_active(True)
		button7.set_active(True)
		button8.set_active(True)
		button10.set_active(True)
	
	def Install(cmd):
		if OS == 'Lin':
			os.system("mkdir -p " + Home + "/bin")
			if button1.get_active():
				shutil.copy(ScriptDir + "/Utils/adb", Home + "/bin/")
			if button2.get_active():
				shutil.copy(ScriptDir + "/Utils/aapt", Home + "/bin")
			if button3.get_active():
				shutil.copy(ScriptDir + "/Utils/7za", Home + "/bin")
			if button4.get_active(): 
				os.system("mkdir -p " + Home + "/bin/other")
				shutil.copy(ScriptDir + "/Utils/Script.sh", Home + "/bin")
				shutil.copy(ScriptDir + "/Utils/apktool.jar", Home + "/bin/other")
				shutil.copy(ScriptDir + "/Utils/apktool", Home + "/bin/other")
				shutil.copy(ScriptDir + "/Utils/signapk.jar", Home + "/bin/other")
				shutil.copy(ScriptDir + "/Utils/testkey.pk8", Home + "/bin/other")
				shutil.copy(ScriptDir + "/Utils/testkey.x509.pem", Home + "/bin/other")
				shutil.copy(ScriptDir + "/Utils/7za", Home + "/bin/other")
				shutil.copy(ScriptDir + "/Utils/aapt", Home + "/bin/other")
				shutil.copy(ScriptDir + "/Utils/optipng", Home + "/bin/other")
			if button5.get_active():
				shutil.copy(ScriptDir + "/Utils/optipng", Home + "/bin")
			if button6.get_active():
				shutil.copy(ScriptDir + "/Utils/signapk.jar", Home + "/bin/")
				shutil.copy(ScriptDir + "/Utils/testkey.pk8", Home + "/bin/")
				shutil.copy(ScriptDir + "/Utils/testkey.x509.pem", Home + "/bin/")
			if button7.get_active():
				shutil.copy(ScriptDir + "/Utils/smali-1.3.2.jar", Home + "/bin")
			if button8.get_active():
				shutil.copy(ScriptDir + "/Utils/baksmali-1.3.2.jar", Home + "/bin")
			if button10.get_active():
				os.system("sudo apt-get install imagemagick")
		if OS == 'Win':
			print("Sorry, windows does not support $PATH modifications from cmd...\nInstead, I will open up a site for you")
			print("That site contains a HOWTO on adding a directory to the PATH.")
			print("Add this directory: " + ScriptDir)
			if button10.get_active():
				ImageMagick = '[2] Open link and install imagemagick'
			else:
				ImageMagick = ''
			print("\n Options: [n] NVM  [1] Open link" + ImageMagick + "\n")
			q = raw_input("Choose an option :  ")
			if not q == 'n':
				Web.open("http://www.computerhope.com/issues/ch000549.htm")
			if q == '2':
				Web.open("ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-6.7.6-9-Q16-windows-dll.exe")
		KillPage(cmd)

	notebook = MainApp.notebook
	ExZip()
	UtilsLabel = gtk.Label("Install Utilities")
	InstUtilsTable = gtk.Table(1, 1, False)
	vbox = gtk.VBox()
	InstUtilsTable.attach(vbox, 0, 1, 0, 1)

	OptionsTable = gtk.Table(1, 3, True)
	UtilsTable = gtk.Table(11, 2, True)

        label = gtk.Label("Hey there!\n Please select the tools you want to install.\nImageMagick is needed for all image tools I included!")
	label.set_justify(gtk.JUSTIFY_CENTER)
	vbox.pack_start(label, False, False, 0)

	button1 = gtk.CheckButton("ADB")
	UtilsTable.attach(button1, 0, 1, 0, 1)

	button2 = gtk.CheckButton("AAPT")
	UtilsTable.attach(button2, 0, 1, 1, 2)
	
	button3 = gtk.CheckButton("7z")
	UtilsTable.attach(button3, 0, 1, 2, 3)
	
	button4 = gtk.CheckButton("APK Manager")
	UtilsTable.attach(button4, 0, 1, 3, 4)
	
	button5 = gtk.CheckButton("Optipng")
	UtilsTable.attach(button5, 0, 1, 4, 5)
	
	button6 = gtk.CheckButton("SignAPK")
	UtilsTable.attach(button6, 0, 1, 5, 6)
	
	button7 = gtk.CheckButton("Smali")
	UtilsTable.attach(button7, 0, 1, 6, 7)
	
	button8 = gtk.CheckButton("BakSmali")
	UtilsTable.attach(button8, 0, 1, 7, 8)

	button9 = gtk.CheckButton("ALL!")
	button9.connect("toggled", SetAll)
	UtilsTable.attach(button9, 0, 1, 9, 10)

	button10 = gtk.CheckButton("ImageMagick")
	UtilsTable.attach(button10, 1, 2, 0, 1)

	buttonInstall = gtk.Button("Install")
	buttonInstall.connect("clicked", Install)
	UtilsTable.attach(buttonInstall, 0, 2, 10, 11)
	
	
	vbox.pack_start(UtilsTable, False, False, 0)
	vbox.show_all()

	box = gtk.HBox()
	closebtn = gtk.Button()
	image = gtk.Image()
	image.set_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
	closebtn.connect("clicked", KillPage)
	closebtn.set_image(image)
	closebtn.set_relief(gtk.RELIEF_NONE)
	box.pack_start(UtilsLabel, True, True)
	box.pack_end(closebtn, False, False)
	UtilsLabel = box
	UtilsLabel.show_all()

	notebook.insert_page(InstUtilsTable, UtilsLabel, 5)
	window.show_all()
	notebook.set_current_page(5)


	

def CopyFrom():
	def Start(cmd):
		FromDir2 = FromDir.get_text()
		if not FromDir2.endswith("/"):
			FromDir3 = FromDir2 + "/"
		else :
			FromDir3 = FromDir2
		ToDir2 = ToDir.get_text()
		if not ToDir2.endswith("/"):
			ToDir3 = ToDir2 + "/"
		else :
			ToDir3 = ToDir2
		Ext2 = Ext.get_text()
		print("Copying files FROM " + FromDir3 + " to " + ToDir3 + " With extension " + Ext2)
		for ToFile in find_files(ToDir3, "*" + Ext2):
			filename = ToFile.replace(ToDir3, '')
			for FromFile in find_files(FromDir3, filename):
				print("Copy " + FromFile + " to " + ToFile)
				shutil.copy(FromFile, ToFile)
		KillPage(cmd)

	CopyFromWindow = window
	CopyFromLabel = gtk.Label("CopyFrom")

	vbox = gtk.VBox()
	notebook = MainApp.notebook

	label = gtk.Label("""This tool copies files existing in a directory FROM an other directory.
			Can be handy for porting themes and such\n\nMake sure both directories have the same structure!\n\n\n""")

	CopyFromTable = gtk.Table(4, 2, True)
	CopyFromTable.set_row_spacings(10)

	vbox.pack_start(label, False, False, 0)
	vbox.pack_start(CopyFromTable, False, False, 0)

	ToDir = gtk.Entry()
	ToDir.set_text(Home + "/")
	ToDir.set_size_request(30, 25)
	ToDirLabel = gtk.Label("Enter the directory you want to copy the files TO")

	CopyFromTable.attach(ToDir, 0, 1, 0, 1, yoptions=gtk.EXPAND)
	CopyFromTable.attach(ToDirLabel, 1, 2, 0, 1)

	FromDir = gtk.Entry()
	FromDir.set_text(Home + "/")
	FromDir.set_size_request(30, 25)
	FromDirLabel = gtk.Label("Enter the directory you want to copy the files FROM")

	CopyFromTable.attach(FromDir, 0, 1, 1, 2, yoptions=gtk.EXPAND)
	CopyFromTable.attach(FromDirLabel, 1, 2, 1, 2)

	Ext = gtk.Entry()
	Ext.set_size_request(30, 25)
	Ext.set_text(".")
	ExtLabel = gtk.Label("Enter the extension of the files you want to copy")

	CopyFromTable.attach(Ext, 0, 1, 2, 3, yoptions=gtk.EXPAND)
	CopyFromTable.attach(ExtLabel, 1, 2, 2, 3)

	StartButton = gtk.Button("CopyFrom!")
	StartButton.connect("clicked", Start)
	CopyFromTable.attach(StartButton, 0, 2, 3, 4)
	
	vbox.pack_end(StatusTable, False, False, 0)

	box = gtk.HBox()
	closebtn = gtk.Button()
	image = gtk.Image()
	image.set_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
	closebtn.connect("clicked", KillPage)
	closebtn.set_image(image)
	closebtn.set_relief(gtk.RELIEF_NONE)
	box.pack_start(CopyFromLabel, True, True)
	box.pack_end(closebtn, False, False)
	CopyFromLabel = box
	CopyFromLabel.show_all()
	
	notebook.insert_page(vbox, CopyFromLabel, 5)
	CopyFromWindow.show_all()
	notebook.set_current_page(5)

def Resize():
	def StartResize(cmd):
		DstDir = ScriptDir + "/Resized/"
		if NormalResize.get_active():
			Perc = ResizePercentageBox.get_text()
			#Perc = int(Perc)
			if not Perc.endswith("%"):
				Perc = Perc + "%"
			InDir = ResizeDirBox.get_text()
		if EasyResize.get_active():
			InDPI = InDPIBox.get_text()
			OutDPI = OutDPIBox.get_text()
			if InDPI == 'XHDPI':
				InRes = 720
			elif InDPI == 'HDPI':
				InRes = 480
			elif InDPI == 'MDPI':
				InRes = 320
			elif InDPI == 'LDPI':
				InRes = 240
			else:
				InRes = InDPI
			if OutDPI == 'XHDPI':
				OutRes = 720
			elif OutDPI == 'HDPI':
				OutRes = 480
			elif OutDPI == 'MDPI':
				OutRes = 320
			elif OutDPI == 'LDPI':
				OutRes = 240
			else:
				ResDPI = OutDPI
			InDir = EasyResizeDirBox.get_text()

		if ApkResize.get_active():
			InDPI = ApkInDPIBox.get_text()
			OutDPI = ApkOutDPIBox.get_text()
			if InDPI == 'XHDPI':
				InRes = 720
				InDir1 = 'xhdpi'
			elif InDPI == 'HDPI':
				InRes = 480
				InDir1 = 'hdpi'
			elif InDPI == 'MDPI':
				InRes = 320
				InDir1 = 'mdpi'
			elif InDPI == 'LDPI':
				InRes = 240
				InDir1 = 'ldpi'
			else:
				InRes = InDPI
			if OutDPI == 'XHDPI':
				OutRes = 720
				OutDir1 = 'xhdpi'
			elif OutDPI == 'HDPI':
				OutRes = 480
				OutDir1 = 'hdpi'
			elif OutDPI == 'MDPI':
				OutRes = 320
				OutDir1 = 'mdpi'
			elif OutDPI == 'LDPI':
				OutRes = 240
				OutDir1 = 'ldpi'
			else:
				OutRes = OutDPI
			InApk = ApkResizeDirBox.get_text()
			ResizeApk = ApkResizeDirBox.get_text()
			FullZipDir = ScriptDir + "/Resizing"
			zipfile.ZipFile(ResizeApk).extractall(path=FullZipDir)
			InDir = ScriptDir + "/Resizing/res/drawable-" + InDir1
			DstDir = ScriptDir + "/Resizing/res/drawable-" + OutDir1 + "/"

		if ApkResize.get_active() or EasyResize.get_active():
			Perc = OutRes * 100 / InRes


		print "Resize percentage is",
		print Perc

		os.system("rm -r " + DstDir)
		os.system("mkdir -p " + DstDir)
		if not InDir.endswith("/"):
			SrcDir = InDir + "/"
		else:
			SrcDir = InDir

		print("SrcDir = " + SrcDir + "\nDstDir = " + DstDir)

		for Image in find_files(SrcDir, "*.png"):
			DstFile = Image.replace(SrcDir, DstDir)
			Name = os.path.basename(Image)
			Sub = Image.replace(SrcDir, '')
			SubD = Sub.replace(Name, '')
			SubDir = SubD
			if not SubDir == '' or SubDir == '/':
				os.system("mkdir -p " + DstDir + SubDir)
			print(Image + " -> " + DstFile + "\n")
			os.system("convert %s -resize %s %s" % (Image, Perc, DstFile))
		message = "You can find the resized images in Resized"
		NewDialog("Resized", "You can find the resized images in Resized")
		KillPage(cmd)
		
		
	ResizeWindow = window
	ResizeLabel = gtk.Label("Resize")
	vbox = gtk.VBox()
	sw = gtk.ScrolledWindow()
	notebook = MainApp.notebook
	

	label = gtk.Label("This tool can be used to resize images, but also APK's :D\n\nChoose an option:\n\n")
	vbox.pack_start(label, False, False, 20)
	sw.add_with_viewport(vbox)

	NormalResize = gtk.RadioButton(None, "Normal resizing using resize percentage")
	vbox.pack_start(NormalResize, False, False, 2)

	NormalResizeTable = gtk.Table(2, 2, True)
	NormalResizeTable.set_col_spacings(2)
	NormalResizeTable.set_row_spacings(2)

	ResizePercentageBox = gtk.Entry()
	ResizePercentageBox.set_text("%")
	ResizePercentageBox.set_size_request(0, 30)

	ResizePercentageLabel = gtk.Label("Enter the resize percentage 0-100 %")

	ResizeDirBox = gtk.Entry()
	ResizeDirBox.set_text(ScriptDir + "/")
	ResizeDirBox.set_size_request(0, 30)

	ResizeDirLabel = gtk.Label("Enter the directory containing the images you want to resize")

	NormalResizeTable.attach(ResizePercentageBox, 0, 1, 0, 1, xpadding=20)
	NormalResizeTable.attach(ResizePercentageLabel, 1, 2, 0, 1)
	NormalResizeTable.attach(ResizeDirBox, 0, 1, 1, 2, xpadding=20)
	NormalResizeTable.attach(ResizeDirLabel, 1, 2, 1, 2)
	vbox.pack_start(NormalResizeTable, False, False, 0)

	EasyResize = gtk.RadioButton(NormalResize, "Easy resizing using ..DPI values")
	vbox.pack_start(EasyResize, False, False, 2)

	EasyResizeTable = gtk.Table(2, 2, True)
	
	InDPIBox = gtk.Entry()
	InDPIBox.set_text("..DPI")
	EasyResizeTable.attach(InDPIBox, 0, 1, 0, 1, xpadding=20)
	InDPILabel = gtk.Label("Give the DPI of the images you want to resize")
	EasyResizeTable.attach(InDPILabel, 1, 2, 0, 1)

	OutDPIBox = gtk.Entry()
	OutDPIBox.set_text("..DPI")
	EasyResizeTable.attach(OutDPIBox, 0, 1, 1, 2, xpadding=20)
	OutDPILabel = gtk.Label("Give the DPI of the resolution you want to resize to")
	EasyResizeTable.attach(OutDPILabel, 1, 2, 1, 2)

	EasyResizeDirBox = gtk.Entry()
	EasyResizeDirBox.set_text(ScriptDir + "/")
	EasyResizeDirBox.set_size_request(0, 30)
	EasyResizeTable.attach(EasyResizeDirBox, 0, 1, 2, 3, xpadding=20)
	ResizeDirLabel = gtk.Label("Enter the directory containing the images you want to resize")
	EasyResizeTable.attach(ResizeDirLabel, 1, 2, 2, 3)

	vbox.pack_start(EasyResizeTable, False, False, 0)

	ApkResize = gtk.RadioButton(NormalResize, "Resize an APK using DPI values")
	vbox.pack_start(ApkResize, False, False, 10)

	APKResizeTable = gtk.Table(3, 2, True)
	
	ApkInDPIBox = gtk.Entry()
	ApkInDPIBox.set_text("..DPI")
	APKResizeTable.attach(ApkInDPIBox, 0, 1, 0, 1, xpadding=20)
	ApkInDPILabel = gtk.Label("Give the DPI of the images you want to resize")
	APKResizeTable.attach(ApkInDPILabel, 1, 2, 0, 1)

	ApkOutDPIBox = gtk.Entry()
	ApkOutDPIBox.set_text("..DPI")
	APKResizeTable.attach(ApkOutDPIBox, 0, 1, 1, 2, xpadding=20)
	ApkOutDPILabel = gtk.Label("Give the DPI of the resolution you want to resize to")
	APKResizeTable.attach(ApkOutDPILabel, 1, 2, 1, 2)

	ApkResizeDirBox = gtk.Entry()
	ApkResizeDirBox.set_text(ScriptDir + "/")
	ApkResizeDirBox.set_size_request(0, 30)
	APKResizeTable.attach(ApkResizeDirBox, 0, 1, 2, 3, xpadding=20)
	ResizeDirLabel = gtk.Label("Enter the directory containing the APK")
	APKResizeTable.attach(ResizeDirLabel, 1, 2, 2, 3)

	vbox.pack_start(APKResizeTable, False, False, 0)

	ExtensionBox = gtk.Entry()
	ExtensionBox.set_size_request(0, 30)
	ExtensionBox.set_text(".png")
	APKResizeTable.attach(ExtensionBox, 0, 1, 3, 4, xpadding=10)

	ResizeStartButton = gtk.Button("Start resizing")
	ResizeStartButton.connect("clicked", StartResize)
	vbox.pack_start(ResizeStartButton, False, False, 15)

	box = gtk.HBox()
	closebtn = gtk.Button()
	image = gtk.Image()
	image.set_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
	closebtn.connect("clicked", KillPage)
	closebtn.set_image(image)
	closebtn.set_relief(gtk.RELIEF_NONE)
	box.pack_start(ResizeLabel, True, True)
	box.pack_end(closebtn, False, False)
	ResizeLabel = box
	ResizeLabel.show_all()

	notebook.insert_page(sw, ResizeLabel, 5)

	ResizeWindow.show_all()
	notebook.set_current_page(5)

def Theme():
	def ShowColor(cmd):
		Red1 = RedBox.get_text()
		Red2 = int(Red1) * 65535 / 100
		Red3 = int(Red2)
		Green1 = GreenBox.get_text()
		Green2 = int(Green1) * 65535 / 100
		Green3 = int(Green2)
		Blue1 = BlueBox.get_text()
		Blue2 = int(Blue1) * 65535 / 100
		Blue3 = int(Blue2)
		Red = int(Red3)
		Green = int(Green3)
		Blue = int(Blue3)
		print("R %s G %s B %s") % (Red, Green, Blue)
		color = gtk.gdk.Color(red=Red, green=Green, blue=Blue)
		Draw.modify_bg(gtk.STATE_NORMAL, color)
	def StartTheming(cmd):
		Red = str(RedBox.get_text())
		Green = str(GreenBox.get_text())
		Blue = str(BlueBox.get_text())
		ExZip()
		SrcDir = ScriptDir + "/Theme"
		os.system("mkdir -p " + SrcDir)
		for Image in find_files(SrcDir, "*.png"):
			Image1 = str(Image)
			os.system("mogrify -colorize " + Red + "," + Green + "," + Blue + " " + Image1)
	ThemeWindow = window	
	ThemeLabel = gtk.Label("Place the images you want to theme inside " + ScriptDir + "/Theme/")
	notebook = MainApp.notebook

	SrcDir = ScriptDir + "/Theme"
	os.system("mkdir -p " + SrcDir)

	vbox = gtk.VBox()
	vbox.pack_start(ThemeLabel, False, False, 10)

	ColorTable = gtk.Table(3, 2, True)
	vbox.pack_start(ColorTable, False, False, 0)

	RedBox = gtk.Entry()
	RedBox.set_text("22")
	RedLabel = gtk.Label("Enter the RED value (0-100)")
	ColorTable.attach(RedBox, 0, 1, 0, 1)
	ColorTable.attach(RedLabel, 1, 2, 0, 1)

	GreenBox = gtk.Entry()
	GreenBox.set_text("66")
	GreenLabel = gtk.Label("Enter the GREEN value (0-100)")
	ColorTable.attach(GreenBox, 0, 1, 1, 2)
	ColorTable.attach(GreenLabel, 1, 2, 1, 2)

	BlueBox = gtk.Entry()
	BlueBox.set_text("77")
	BlueLabel = gtk.Label("Enter the BLUE value (0-100)")
	ColorTable.attach(BlueBox, 0, 1, 2, 3)
	ColorTable.attach(BlueLabel, 1, 2, 2, 3)
	


	ColorButton = gtk.Button("Show Color")
	ColorButton.connect("clicked", ShowColor)

	vbox.pack_start(ColorButton, False, False, 15)

	Draw = gtk.DrawingArea()
	Color = Draw.get_colormap().alloc_color(0, 65535, 0)
	Draw.set_size_request(100, 50)
	Draw.show()
	vbox.pack_start(Draw, False, False, 0)

	StartButton = gtk.Button("Start theming!")
	StartButton.connect("clicked", StartTheming)
	vbox.pack_start(StartButton, False, False, 15)

	box = gtk.HBox()
	label = gtk.Label("Theme")
	closebtn = gtk.Button()
	image = gtk.Image()
	image.set_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
	closebtn.connect("clicked", KillPage)
	closebtn.set_image(image)
	closebtn.set_relief(gtk.RELIEF_NONE)
	box.pack_start(label, True, True)
	box.pack_end(closebtn, False, False)
	ThemeLabel = box
	ThemeLabel.show_all()

	notebook.insert_page(vbox, ThemeLabel, 5)

	ThemeWindow.show_all()
	notebook.set_current_page(5)
	

def PrepareBuilding():
	def Prepare(cmd):
		MessageLabel = gtk.Label("Please check the terminal for further progress...")
		box.pack_start(MessageLabel, False, False, 40)
		PrepareWindow.show_all()
		os.system("""sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python2.5
sudo add-apt-repository "deb http://archive.canonical.com/ lucid partner"
sudo add-apt-repository "deb-src http://archive.canonical.com/ubuntu lucid partner"
sudo apt-get update
sudo apt-get install sun-java6-jdk
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git-core
sudo apt-get install valgrind
sudo apt-get install git-core gnupg flex bison gperf build-essential \
zip curl zlib1g-dev libc6-dev lib64ncurses5-dev \
x11proto-core-dev libx11-dev lib64readline-gplv2-dev lib64z1-dev \
libgl1-mesa-dev g++-multilib tofrodos
mkdir -p ~/bin
mkdir -p ~/android/system
curl https://dl-ssl.google.com/dl/googlesource/git-repo/repo > ~/bin/repo
chmod a+x ~/bin/repo
sudo echo '#Acer
SUBSYSTEM==usb, SYSFS{idVendor}==0502, MODE=0666

#ASUS
SUBSYSTEM==usb, SYSFS{idVendor}==0b05, MODE=0666

#Dell
SUBSYSTEM==usb, SYSFS{idVendor}==413c, MODE=0666

#Foxconn
SUBSYSTEM==usb, SYSFS{idVendor}==0489, MODE=0666

#Garmin-Asus
SUBSYSTEM==usb, SYSFS{idVendor}==091E, MODE=0666

#Google
SUBSYSTEM==usb, SYSFS{idVendor}==18d1, MODE=0666

#HTC
SUBSYSTEM=="usb", SYSFS{idVendor}=="0bb4", MODE="0666"

#Huawei
SUBSYSTEM==usb, SYSFS{idVendor}==12d1, MODE=0666

#K-Touch
SUBSYSTEM==usb, SYSFS{idVendor}==24e3, MODE=0666

#KT Tech
SUBSYSTEM==usb, SYSFS{idVendor}==2116, MODE=0666

#Kyocera
SUBSYSTEM==usb, SYSFS{idVendor}==0482, MODE=0666

#Lenevo
SUBSYSTEM==usb, SYSFS{idVendor}==17EF, MODE=0666

#LG
SUBSYSTEM==usb, SYSFS{idVendor}==1004, MODE=0666

#Motorola
SUBSYSTEM==usb, SYSFS{idVendor}==22b8, MODE=0666

#NEC
SUBSYSTEM==usb, SYSFS{idVendor}==0409, MODE=0666

#Nook
SUBSYSTEM==usb, SYSFS{idVendor}==2080, MODE=0666

#Nvidia
SUBSYSTEM==usb, SYSFS{idVendor}==0955, MODE=0666

#OTGV
SUBSYSTEM==usb, SYSFS{idVendor}==2257, MODE=0666

#Pantech
SUBSYSTEM==usb, SYSFS{idVendor}==10A9, MODE=0666

#Philips
SUBSYSTEM==usb, SYSFS{idVendor}==0471, MODE=0666

#PMC-Sierra
SUBSYSTEM==usb, SYSFS{idVendor}==04da, MODE=0666

#Qualcomm
SUBSYSTEM==usb, SYSFS{idVendor}==05c6, MODE=0666

#SK Telesys
SUBSYSTEM==usb, SYSFS{idVendor}==1f53, MODE=0666

#Samsung
SUBSYSTEM==usb, SYSFS{idVendor}==04e8, MODE=0666

#Sharp
SUBSYSTEM==usb, SYSFS{idVendor}==04dd, MODE=0666

#Sony Ericsson
SUBSYSTEM==usb, SYSFS{idVendor}==0fce, MODE=0666

#Toshiba
SUBSYSTEM==usb, SYSFS{idVendor}==0930, MODE=0666

#ZTE
SUBSYSTEM==usb, SYSFS{idVendor}==19D2, MODE=0666' > /etc/udev/rules.d/51-android.rules
sudo chmod a+r /etc/udev/rules.d/51-android.rules

echo '-----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: GnuPG v1.4.2.2 (GNU/Linux)  
    mQGiBEnnWD4RBACt9/h4v9xnnGDou13y3dvOx6/t43LPPIxeJ8eX9WB+8LLuROSV
    lFhpHawsVAcFlmi7f7jdSRF+OvtZL9ShPKdLfwBJMNkU66/TZmPewS4m782ndtw7
    8tR1cXb197Ob8kOfQB3A9yk2XZ4ei4ZC3i6wVdqHLRxABdncwu5hOF9KXwCgkxMD
    u4PVgChaAJzTYJ1EG+UYBIUEAJmfearb0qRAN7dEoff0FeXsEaUA6U90sEoVks0Z
    wNj96SA8BL+a1OoEUUfpMhiHyLuQSftxisJxTh+2QclzDviDyaTrkANjdYY7p2cq
    /HMdOY7LJlHaqtXmZxXjjtw5Uc2QG8UY8aziU3IE9nTjSwCXeJnuyvoizl9/I1S5
    jU5SA/9WwIps4SC84ielIXiGWEqq6i6/sk4I9q1YemZF2XVVKnmI1F4iCMtNKsR4
    MGSa1gA8s4iQbsKNWPgp7M3a51JCVCu6l/8zTpA+uUGapw4tWCp4o0dpIvDPBEa9
    b/aF/ygcR8mh5hgUfpF9IpXdknOsbKCvM9lSSfRciETykZc4wrRCVGhlIEFuZHJv
    aWQgT3BlbiBTb3VyY2UgUHJvamVjdCA8aW5pdGlhbC1jb250cmlidXRpb25AYW5k
    cm9pZC5jb20+iGAEExECACAFAknnWD4CGwMGCwkIBwMCBBUCCAMEFgIDAQIeAQIX
    gAAKCRDorT+BmrEOeNr+AJ42Xy6tEW7r3KzrJxnRX8mij9z8tgCdFfQYiHpYngkI
    2t09Ed+9Bm4gmEO5Ag0ESedYRBAIAKVW1JcMBWvV/0Bo9WiByJ9WJ5swMN36/vAl
    QN4mWRhfzDOk/Rosdb0csAO/l8Kz0gKQPOfObtyYjvI8JMC3rmi+LIvSUT9806Up
    hisyEmmHv6U8gUb/xHLIanXGxwhYzjgeuAXVCsv+EvoPIHbY4L/KvP5x+oCJIDbk
    C2b1TvVk9PryzmE4BPIQL/NtgR1oLWm/uWR9zRUFtBnE411aMAN3qnAHBBMZzKMX
    LWBGWE0znfRrnczI5p49i2YZJAjyX1P2WzmScK49CV82dzLo71MnrF6fj+Udtb5+
    OgTg7Cow+8PRaTkJEW5Y2JIZpnRUq0CYxAmHYX79EMKHDSThf/8AAwUIAJPWsB/M
    pK+KMs/s3r6nJrnYLTfdZhtmQXimpoDMJg1zxmL8UfNUKiQZ6esoAWtDgpqt7Y7s
    KZ8laHRARonte394hidZzM5nb6hQvpPjt2OlPRsyqVxw4c/KsjADtAuKW9/d8phb
    N8bTyOJo856qg4oOEzKG9eeF7oaZTYBy33BTL0408sEBxiMior6b8LrZrAhkqDjA
    vUXRwm/fFKgpsOysxC6xi553CxBUCH2omNV6Ka1LNMwzSp9ILz8jEGqmUtkBszwo
    G1S8fXgE0Lq3cdDM/GJ4QXP/p6LiwNF99faDMTV3+2SAOGvytOX6KjKVzKOSsfJQ
    hN0DlsIw8hqJc0WISQQYEQIACQUCSedYRAIbDAAKCRDorT+BmrEOeCUOAJ9qmR0l
    EXzeoxcdoafxqf6gZlJZlACgkWF7wi2YLW3Oa+jv2QSTlrx4KLM=
    =Wi5D 
    -----END PGP PUBLIC KEY BLOCK-----' > ~/gpgimport
gpg --import ~/gpgimport
rm ~/gpgimport""")
		os.system("""sudo apt-get install git-core gnupg flex bison gperf build-essential \
zip curl zlib1g-dev libc6-dev tofrodos python-markdown \
libxml2-utils xsltproc x11proto-core-dev libgl1-mesa-dev libx11-dev""")
		if Button64.get_active():
			os.system("""sudo apt-get install lib32ncurses5-dev ia32-libs lib32readline5-dev lib32z-dev g++-multilib mingw32""")
		if Button32.get_active():
			os.system("sudo apt-get install libncurses5-dev libreadline6-dev")
		if Button1010.get_active():
			os.system("sudo ln -s /usr/lib32/mesa/libGL.so.1 /usr/lib32/mesa/libGL.so")
		if Button1110.get_active():
			os.system("sudo apt-get install libx11-dev:i386")
		if Button1204.get_active():
			os.system("""sudo apt-get install libncurses5-dev:i386 libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-dev:i386 \
g++-multilib mingw32 openjdk-6-jdk tofrodos libxml2-utils xsltproc zlib1g-dev:i386""")

	PrepareWindow = window
	PrepareLabel = gtk.Label("Prepare")
	notebook = MainApp.notebook

	box = gtk.VBox()
	notebook.insert_page(box, PrepareLabel, 5)
	

	label=gtk.Label("You need this option before you can build.\nPlease select your OS...")
	box.pack_start(label, False, False, 10)

	Button1004 = gtk.RadioButton(None, "Ubuntu 10.04")
	box.pack_start(Button1004, False, False, 10)
	Button1010 = gtk.RadioButton(Button1004, "Ubuntu 10.10")
	box.pack_start(Button1010, False, False, 10)
	Button1110 = gtk.RadioButton(Button1004, "Ubuntu 11.10")
	box.pack_start(Button1110, False, False, 10)
	Button1204 = gtk.RadioButton(Button1004, "Ubuntu 12.04")
	box.pack_start(Button1204, False, False, 10)
	separator = gtk.HSeparator()
	box.pack_start(separator, False, True, 0)
	Button32 = gtk.RadioButton(None, "32-bits")
	box.pack_start(Button32, False, False, 10)
	Button64 = gtk.RadioButton(Button32, "64-bits")	
	Button64.set_active(True)
	def SetButton64(cmd):
		Button64.set_active(True)
	Button1204.connect("toggled", SetButton64)
	box.pack_start(Button64, False, False, 10)
	ButtonPrepare = gtk.Button("Prepare to Build")
	ButtonPrepare.connect("clicked", Prepare)
	box.pack_start(ButtonPrepare, False, False, 20)
	PrepareWindow.show_all()

def Changelog():
	ChangeWindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
	ChangeWindow.set_size_request(700, 600)
	ChangeWindow.set_title("StudioAndroid - Changelog")
	sw = gtk.ScrolledWindow()
	ChangeWindow.add(sw)

	changelog = open(ScriptDir + "/changelog", "r")
	Text = changelog.read()
	Label = gtk.Label(Text)

	sw.add_with_viewport(Label)
	ChangeWindow.show_all()

def Help():
	Web.open("http://forum.xda-developers.com/showpost.php?p=23546408&postcount=9")

def Update():
	Web.open("http://forum.xda-developers.com/showthread.php?t=1491689")




gtk.main()



