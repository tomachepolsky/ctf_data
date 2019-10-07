#!/bin/bash
PID=$$
RUNMETHOD=$(cat /proc/$PID/cmdline | sed 's|/bin/bash\x0||')

if [ "${RUNMETHOD:0:1}" == "/" ]; then echo "absolute";
elif [ "${RUNMETHOD:0:2}" == "./" ]; then echo "relative";
else echo "something went wrong"; fi
echo -e "\nYour program was run from $0" 
#echo $PWD
#echo $0

cat /proc/$PID/cmdline
echo -e "\n$RUNMETHOD \n"
#env
