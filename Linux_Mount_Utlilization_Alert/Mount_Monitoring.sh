#!/bin/bash

rm monitored.html

df -h >> temp1.txt

python mount_monitoring.py

 
echo "Hi Team,">> monitored.html

echo "<h4>Below file systems are found to be utilizing more than <i>60%</i> threshold value on <i><Server-Name></i> server.</h4><br>">> monitored.html

#cat temp4.txt | while read row
#do
##echo "<br> $row </br>">> monitored.html
#echo " $row <br>">> monitored.html
#done
##echo "<div>">> monitored.html
#echo "<br><h3> List of Mount's Usage above 60% :</h3></br><br>" >> monitored.html
#cat temp3.txt | while read row
#do
##echo "<br><font color=white style='BACKGROUND-COLOR:#FF0000; display:block;'> $row <br></font>">> monitored.html
#echo "<font color=white style='BACKGROUND-COLOR:#FF0000;'> $row <br></font>">> monitored.html
#done

 

echo "<center><table border=3><tr BGCOLOR="#EAA429"><th>Mounted On</th><th>Utilization</th></tr></center>">> monitored.html

 

cat temp4.txt | tail -n +2 | while read row
do
fs=`echo $row | cut -d' ' -f6`
echo $fs
usage=`echo $row | cut -d' ' -f5`
echo "<tr><td><center>$fs</center></td><td><center>$usage</center></td></tr>">> monitored.html
done

 

cat temp3.txt | while read row
do
fs=`echo $row | cut -d' ' -f6`
echo $fs
usage=`echo $row | cut -d' ' -f5`
echo "<tr><td><font color=white style='BACKGROUND-COLOR:#FF0000;display:block;'><center>$fs</center></font></td><td><font color=white style='BACKGROUND-COLOR:#FF0000;display:block;'><center>$usage</center></font></td></tr>">> monitored.html
done

 

echo "</table>">> monitored.html
echo "<i><br>For any queries, please contact Helpline.<br><br>************************************************************************************<br><br>This is an auto-generated e-mail. Please do not reply to this message.</i>">> monitored.html

rm temp*
