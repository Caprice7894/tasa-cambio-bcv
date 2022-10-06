#! /bin/bash
curl http://www.bcv.org.ve | grep centrado\" | awk -F" " ' {print $5} '
#echo -e "1,0\n2,0\n3,0\n4,0\n5,0"
