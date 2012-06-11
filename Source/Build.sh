#!/bin/bash

MyCommand=${0##*"/"}
if [ "$1" = "sync" ]
then
	repocmd=$(cat ${0%%$MyCommand}/repocmd)
	switches=$(cat ${0%%$MyCommand}/syncswitches)
	$repocmd
	repo sync $switches
fi
if [ "$1" = "make" ]
then
	switches=$(cat ${0%%$MyCommand}/makeswitches)
	. build/envsetup.sh
	brunch $2
	make otapackage
fi
