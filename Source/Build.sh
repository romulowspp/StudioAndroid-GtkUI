#!/bin/bash
. build/envsetup.sh
brunch $1
make otapackage
