#!/bin/bash
BASEDIR=$(dirname $0)
#QACHAT='d45f5b0998b5e501099dc47765ef8a0b'
#SHINGCHAT='0d223d3f39325511e5695cffe6e36b31'

CHATS=(
  'd45f5b0998b5e501099dc47765ef8a0b' 
  '0d223d3f39325511e5695cffe6e36b31'  
  '56fb55db4cfb33e54d43380089df3af8' 
  '54e284888f3bd67017d865c4684465ab' 
  'aef5c4c1e36e41c4df72c57cc1ab3cb2'
  'b90a5b7281c224c0b75b8872f5ef0f91'
  'b48e68dbf51a852ca51211837d8ae9d3'
)

#CHATS=('0d223d3f39325511e5695cffe6e36b31')

#$BASEDIR/send.sh $QACHAT '工作辛苦了，記得訂明天便當 https://dinbendon.net/do/'

for CHAT in ${CHATS[@]} 
do
  $BASEDIR/send.sh $CHAT '.
.
  ▶ ▶ ▶ 工作辛苦了，記得訂明天便當 https://dinbendon.net/do/
.
  '

done

