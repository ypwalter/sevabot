#!/bin/bash
RESULT="`wget -qO- http://www.yerkee.com/api/fortune`"
echo -e $RESULT | sed 's/{"fortune":"//g' | sed 's/"}//g'   
