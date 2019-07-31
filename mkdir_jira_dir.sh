#!/bin/sh

#SOURCE_PATH="/x/fwtest/Traces/L2/p6s/Integrity_CIV-X04/9JA0742A_07-18-19_18-23-51/errors/Error_000_ERR_COMMAND_TIMEOUT"


WORK_PATH="/d/work/FA"

jira_no=$1
SOURCE_PATH=$2

# check the number of arguments
if [ $# -ne 2 ]; then
    echo "parameter number; $#" 1>&2
    echo "paramter nums to be 2" 1>&2
    exit 1
fi


#echo $SOURCE_PATH
JIRA_PATH=`echo $SOURCE_PATH | sed -e "s:^\(.*\)/.*:\1:"`
JIRA_PATH=`echo $JIRA_PATH | sed -e "s:^.*Traces::"`
echo $JIRA_PATH

#echo "/x/fwtest/Traces/L2/p6s/Integrity_CIV-X04/9JA0742A_07-18-19_18-23-51/errors/Error_000_ERR_COMMAND_TIMEOUT" | sed -e "s:^.*Traces::"

TARGET_PATH=$WORK_PATH"/"
TARGET_PATH+=$jira_no
TARGET_PATH+=$JIRA_PATH

#echo $jira_no
echo $TARGET_PATH

if [ ! -e $TARGET_PATH ]; then
    mkdir -p $TARGET_PATH
fi

cp -rp $SOURCE_PATH $TARGET_PATH

