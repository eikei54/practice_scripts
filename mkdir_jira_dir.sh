#!/bin/sh

# Copyright (c) 2019 Akihiro Kamimura <Akihiro.Kamimura@wdc.com>
# All rights reserved.

set -ue

usage_msg='usage:
 - copy X_path data to the local
 - extract compressed bz2 format files
 - open local copied directory

     -h             print help message
     -v             print version'

# check the option arguments
#
while getopts hv option
do
    case "$option" in
    h)
        echo "${usage_msg}"
        exit 0
        ;;
    v)
        echo "version 1"
        exit 0
        ;;
    esac
done
shift $(($OPTIND - 1))

WORK_PATH="/d/work/FA"

jira_no="CCB8-"$1
SOURCE_PATH=$2

# check the number of arguments
if [ $# -ne 2 ]; then
    echo "parameter number; $#" 1>&2
    echo "paramter nums to be 2" 1>&2
    exit 1
fi

#
# Get Folder name, like "Error_000_ERR_COMMAND_TIMEOUT"
#

FOLDER_NAME=`echo $SOURCE_PATH | sed -e "s:^\(.*\)/::1"`

#
# Get original path without Folder name
#

JIRA_PATH=`echo $SOURCE_PATH | sed -e "s:^\(.*\)/.*:\1:"`
JIRA_PATH=`echo $JIRA_PATH | sed -e "s:^.*Traces::"`

TARGET_PATH=$WORK_PATH"/"
TARGET_PATH+=$jira_no
TARGET_PATH+=$JIRA_PATH

#
# Get original path to be used in the local foler
#
echo "Copying X_Drive data to ...."
TEXT_TO_CONSOLE="Copied To       : "

#echo $jira_no
echo $TEXT_TO_CONSOLE$TARGET_PATH

if [ ! -e $TARGET_PATH ]; then
    mkdir -p $TARGET_PATH
fi

#
# copy X Drive's data to the Target Path
#

cp -rp $SOURCE_PATH $TARGET_PATH

# move to $TARGET_PATH folder

TARGET_PATH=$TARGET_PATH"/"$FOLDER_NAME
pushd $TARGET_PATH

# open TARGET_PATH folder

echo "Open Local Dir: $TARGET_PATH"
start $TARGET_PATH

# extract "txt.bz2"
find ./ -name "*.txt.bz2" | xargs -i bzip2 -d {}



