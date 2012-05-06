MyCommand=${0##*"/"}
CDir=${0%%/"$MyCommand"}
ScriptDir=$(cd $CDir && pwd)
ScriptCommand=SAP.py

Version=0.70

if [ "$OSTYPE" = "cygwin" ]
then
	OPTIONS="cyg"
fi

python --version

if [ "$?" = "1" ] | [ "$?" = "127" ] && [ "$OSTYPE" != "cygwin" ]
then
	sudo apt-get install python
fi

clear

echo """
                         ###     StudioAndroid      ###
                         ###     GTK GUI Build      ###
                                      v$Version

"""

python $ScriptDir/$ScriptCommand $OPTIONS






